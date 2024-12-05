# api_tests/test_update_todo.py
import requests
from config.config import logger, pytest_configure


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

    logger.info(f"Response Status Code: {response.status_code}")
    logger.info(f"Response Body: {response.json()}")

    assert response.status_code == 200
    assert response.json()['title'] == updated_todo['title']
    assert response.json()['completed'] == updated_todo['completed']


def test_patch_todo():
    url = "https://jsonplaceholder.typicode.com/todos/1"

    patch_data = {
        "completed": False
    }

    logger.info(f"Sending PATCH request to {url} with data: {patch_data}")
    response = requests.patch(url, json=patch_data)

    logger.info(f"Response Status Code: {response.status_code}")
    logger.info(f"Response Body: {response.json()}")

    assert response.status_code == 200
    assert response.json()['completed'] == patch_data['completed']

def test_delete_todo():
    url = "https://jsonplaceholder.typicode.com/todos/1"

    logger.info(f"Sending DELETE request to {url}")
    response = requests.delete(url)

    logger.info(f"Response Status Code: {response.status_code}")
    logger.info(f"Response Body: {response.json()}")

    assert response.status_code == 200
    response = requests.get(url)
    assert response.status_code == 200

def test_delete_non_existent_todo():
    url = "https://jsonplaceholder.typicode.com/todos/999999"

    logger.info(f"Sending DELETE request to {url}")
    response = requests.delete(url)

    logger.info(f"Response Status Code: {response.status_code}")
    logger.info(f"Response Body: {response.json()}")

    assert response.status_code == 200