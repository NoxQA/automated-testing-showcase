from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest
from config.config import logger, driver
from time import sleep


def verify_sorting(driver, table_id):
    try:
        # Define the locator for table headers
        headers = WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.XPATH, f"//table[@id='{table_id}']//th/span"))
        )

        for header in headers:
            header_text = header.text.strip()
            logger.info(f"Testing sorting for column: '{header_text}'")

            # Find the column index dynamically (1-based for XPath)
            column_index = headers.index(header) + 1
            logger.info(f"Column index for '{header_text}': {column_index}")

            # Wait for rows to be present
            rows = WebDriverWait(driver, 10).until(
                lambda d: d.find_elements(By.XPATH, f"//table[@id='{table_id}']/tbody/tr")
            )
            logger.info(f"Found {len(rows)} rows in the table.")

            # Capture initial values in the column for comparison
            initial_values = [
                row.find_element(By.XPATH, f"./td[{column_index}]").text.strip()
                for row in rows
            ]
            logger.info(f"Initial values for '{header_text}': {initial_values}")

            if not initial_values:
                raise AssertionError(f"No values captured for column '{header_text}'.")

            # Step 1: Click to sort the column (ascending)
            header.click()

            # Step 2: Wait until the rows are reordered (wait for values to change)
            WebDriverWait(driver, 10).until(
                lambda d: [
                              row.find_element(By.XPATH, f"./td[{column_index}]").text.strip()
                              for row in d.find_elements(By.XPATH, f"//table[@id='{table_id}']/tbody/tr")
                          ] != initial_values
            )

            # Step 3: Capture the sorted values after clicking the header
            sorted_values = [
                row.find_element(By.XPATH, f"./td[{column_index}]").text.strip()
                for row in driver.find_elements(By.XPATH, f"//table[@id='{table_id}']/tbody/tr")
            ]
            logger.info(f"Sorted values for '{header_text}': {sorted_values}")

            # Step 4: Check that the sorting was successful (ascending)
            assert initial_values != sorted_values, f"Values did not change after sorting column '{header_text}'."

            # Optionally: Check if it's sorted in ascending order (numeric or lexicographic)
            if header_text.lower() == "due":  # Handle currency column with special sorting
                # Convert the 'Due' column values to floats for correct numeric sorting
                initial_values_float = [float(value.replace('$', '').replace(',', '').strip()) for value in initial_values]
                sorted_values_float = [float(value.replace('$', '').replace(',', '').strip()) for value in sorted_values]

                assert sorted_values_float == sorted(initial_values_float), f"Column '{header_text}' is not sorted correctly in ascending order."
            else:
                # For other columns (e.g., names or emails), default lexicographical sorting
                if header_text.lower() == "name":  # Example: if we are sorting by name
                    assert sorted_values == sorted(initial_values), f"Column '{header_text}' is not sorted correctly in ascending order."

            # Step 5: Test descending sorting by clicking the header again
            header.click()

            # Wait for rows to reorder again
            WebDriverWait(driver, 10).until(
                lambda d: [
                              row.find_element(By.XPATH, f"./td[{column_index}]").text.strip()
                              for row in d.find_elements(By.XPATH, f"//table[@id='{table_id}']/tbody/tr")
                          ] != sorted_values
            )

            # Capture the descending sorted values
            descending_values = [
                row.find_element(By.XPATH, f"./td[{column_index}]").text.strip()
                for row in driver.find_elements(By.XPATH, f"//table[@id='{table_id}']/tbody/tr")
            ]
            logger.info(f"Descending sorted values for '{header_text}': {descending_values}")

            # Check if the values are sorted correctly in descending order
            if header_text.lower() == "due":
                descending_values_float = [float(value.replace('$', '').replace(',', '').strip()) for value in descending_values]
                assert descending_values_float == sorted(sorted_values_float, reverse=True), f"Column '{header_text}' is not sorted correctly in descending order."
            else:
                assert descending_values == sorted(sorted_values, reverse=True), f"Column '{header_text}' is not sorted correctly in descending order."

    except Exception as e:
        logger.error(f"Error occurred while verifying sorting: {e}")
        raise  # Re-raise the exception to ensure the test fails in case of issues

@pytest.mark.usefixtures("driver")
def test_data_tables(driver):
    # Step 1: Navigate to the Data Tables page
    logger.info("Navigating to the Data Tables page.")
    driver.get("https://the-internet.herokuapp.com/tables")

    # Step 2: Verify that the title "Data Tables" is present
    title_element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.TAG_NAME, "h3"))
    )
    assert title_element.text == "Data Tables", "Title 'Data Tables' not found."

    # Step 3: Verify the first table (Example 1) contains expected data
    table1_row_data = [
        ("Smith", "John", "jsmith@gmail.com", "$50.00", "http://www.jsmith.com"),
        ("Bach", "Frank", "fbach@yahoo.com", "$51.00", "http://www.frank.com"),
        ("Doe", "Jason", "jdoe@hotmail.com", "$100.00", "http://www.jdoe.com"),
        ("Conway", "Tim", "tconway@earthlink.net", "$50.00", "http://www.timconway.com")
    ]

    # Wait for rows in table 1 to be present
    table1_rows = WebDriverWait(driver, 10).until(
        lambda d: d.find_elements(By.XPATH, "//table[@id='table1']/tbody/tr")
    )
    logger.info(f"Found {len(table1_rows)} rows in table1.")

    for index, row_data in enumerate(table1_row_data, start=1):
        row = table1_rows[index - 1]  # Use the row index directly
        row_texts = [cell.text for cell in
                     row.find_elements(By.TAG_NAME, "td")[:-1]]  # Exclude the last column (Action)
        assert row_texts == list(row_data), f"Row {index} data is incorrect. Expected {row_data}, but got {row_texts}."

    # Step 4: Verify the second table (Example 2) contains expected data
    # Skip the sorting verification for the second table (table2)
    table2_row_data = [
        ("Smith", "John", "jsmith@gmail.com", "$50.00", "http://www.jsmith.com"),
        ("Bach", "Frank", "fbach@yahoo.com", "$51.00", "http://www.frank.com"),
        ("Doe", "Jason", "jdoe@hotmail.com", "$100.00", "http://www.jdoe.com"),
        ("Conway", "Tim", "tconway@earthlink.net", "$50.00", "http://www.timconway.com")
    ]

    # Wait for rows in table 2 to be present
    table2_rows = WebDriverWait(driver, 10).until(
        lambda d: d.find_elements(By.XPATH, "//table[@id='table2']/tbody/tr")
    )
    logger.info(f"Found {len(table2_rows)} rows in table2.")

    for index, row_data in enumerate(table2_row_data, start=1):
        row = table2_rows[index - 1]
        row_texts = [cell.text for cell in
                     row.find_elements(By.TAG_NAME, "td")[:-1]]  # Exclude the last column (Action)
        assert row_texts == list(row_data), f"Row {index} data is incorrect. Expected {row_data}, but got {row_texts}."
