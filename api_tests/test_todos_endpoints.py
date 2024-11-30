# api_tests/test_update_todo.py
import requests
from config.config import logger


def test_update_todo():
    url = "https://jsonplaceholder.typicode.com/todos/1"

    updated_todo = {
        "userId": 1,
        "id": 1,
        "title": "Updated Todo",
        "completed": True
    }

    logger.info(f"Sending PUT request to {url} with data: {updated_todo}")
    response = requests.put(url, json=updated_todo)

    # Log the status code and response body
    logger.info(f"Response Status Code: {response.status_code}")
    logger.info(f"Response Body: {response.json()}")

    # Check if the response status code is 200
    assert response.status_code == 200

    # Validate the updated data
    assert response.json()['title'] == updated_todo['title']
    assert response.json()['completed'] == updated_todo['completed']


def test_patch_todo():
    url = "https://jsonplaceholder.typicode.com/todos/1"

    patch_data = {
        "completed": False  # Only updating the 'completed' field
    }

    logger.info(f"Sending PATCH request to {url} with data: {patch_data}")
    response = requests.patch(url, json=patch_data)

    # Log the status code and response body
    logger.info(f"Response Status Code: {response.status_code}")
    logger.info(f"Response Body: {response.json()}")

    # Check if the response status code is 200
    assert response.status_code == 200

    # Validate that the 'completed' field is updated
    assert response.json()['completed'] == patch_data['completed']


def test_delete_todo():
    url = "https://jsonplaceholder.typicode.com/todos/1"

    # First, delete the todo
    logger.info(f"Sending DELETE request to {url}")
    response = requests.delete(url)

    # Log the status code and response body
    logger.info(f"Response Status Code: {response.status_code}")
    logger.info(f"Response Body: {response.json()}")

    # Check if the response status code is 200, as this is how the mock API behaves
    assert response.status_code == 200

    # Verify that the todo was deleted by attempting to get it
    response = requests.get(url)

    # Expecting 200 as the mock API may not fully remove the resource
    assert response.status_code == 200


def test_delete_non_existent_todo():
    url = "https://jsonplaceholder.typicode.com/todos/999999"

    logger.info(f"Sending DELETE request to {url}")
    response = requests.delete(url)

    # Log the status code and response body
    logger.info(f"Response Status Code: {response.status_code}")
    logger.info(f"Response Body: {response.json()}")

    # Deleting a non-existent resource should return 200 as per mock API behavior
    assert response.status_code == 200