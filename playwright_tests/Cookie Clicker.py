from playwright.sync_api import sync_playwright
import re
import time

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False, args=["--start-maximized"])
    context = browser.new_context()
    page = browser.new_page()
    page.goto("https://orteil.dashnet.org/cookieclicker/")

    lang_button = page.locator('#langSelect-EN')
    lang_button.wait_for(state="visible", timeout=60000)

    if lang_button.count() > 0:
        lang_button.click()
    else:
        print("Language selection didn't appear.")

    page.wait_for_timeout(5000)

    end_time = time.time() + 60
    cookie_button = page.locator('#bigCookie')

    total_cookie_clicks = 0
    total_purchases = 0

    last_product_check_time = time.time()
    last_cookie_amount = 0
    while time.time() < end_time:
        cookie_button.click()
        total_cookie_clicks += 1

        total_cookie_amount_locator = page.locator('#cookies')
        cookie_amount = total_cookie_amount_locator.inner_text()

        match = re.search(r"(\d+)", cookie_amount)
        if match:
            cookie_amount = int(match.group(1))
        else:
            print("Could not extract cookie amount.")

        if time.time() - last_product_check_time > 5:
            print("Checking for available products...")

            product_enabled = page.locator('.product.unlocked.enabled')
            product_count = product_enabled.count()

            for i in range(product_count):
                product_locator = product_enabled.nth(i)
                product_price_locator = product_locator.locator('.price')

                product_price_locator.wait_for(state="visible", timeout=5000)

                if product_price_locator.count() > 0:
                    product_price_text = product_price_locator.inner_text()
                    product_price = int(re.search(r"(\d+)", product_price_text).group(1))

                    if cookie_amount >= product_price:
                        print(f"Clicking on product {i} with price {product_price} cookies...")
                        product_locator.click()
                        total_purchases += 1
                else:
                    print(f"Product {i} does not have a visible price.")

            last_product_check_time = time.time()

        golden_cookie_locator = page.locator('.goldenCookie')
        if golden_cookie_locator.is_visible():
            print("Golden cookie detected, clicking...")
            golden_cookie_locator.click()

        last_cookie_amount = cookie_amount

        time.sleep(0.1)

    print(f"Test Finished\nTotal cookies clicked: {total_cookie_clicks}")
    print(f"Total products purchased: {total_purchases}")
    print(f"Final cookie amount: {last_cookie_amount}")
