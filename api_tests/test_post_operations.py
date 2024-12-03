# api_tests/test_create_post.py
import requests
from config.config import logger, pytest_configure


def test_create_post():
    url = "https://jsonplaceholder.typicode.com/posts"

    new_post = {
        "title": "Test Post",
        "body": "This is a test post.",
        "userId": 1
    }

    logger.info(f"Sending POST request to {url} with data: {new_post}")
    response = requests.post(url, json=new_post)

    # Log the status code and response body
    logger.info(f"Response Status Code: {response.status_code}")
    logger.info(f"Response Body: {response.json()}")

    assert response.status_code == 201
    assert response.json()['title'] == new_post['title']
    assert response.json()['body'] == new_post['body']

def test_create_post_with_missing_data():
    url = "https://jsonplaceholder.typicode.com/posts"

    new_post = {
        "title": "Test Post"
    }

    logger.info(f"Sending POST request to {url} with data: {new_post}")
    response = requests.post(url, json=new_post)

    logger.info(f"Response Status Code: {response.status_code}")
    logger.info(f"Response Body: {response.json()}")

    assert response.status_code == 201

def test_update_post():
    url = "https://jsonplaceholder.typicode.com/posts/1"

    updated_post = {
        "id": 1,
        "title": "Updated Post",
        "body": "This is an updated test post.",
        "userId": 1
    }

    logger.info(f"Sending PUT request to {url} with data: {updated_post}")
    response = requests.put(url, json=updated_post)

    logger.info(f"Response Status Code: {response.status_code}")
    logger.info(f"Response Body: {response.json()}")

    assert response.status_code == 200

    assert response.json()['title'] == updated_post['title']
    assert response.json()['body'] == updated_post['body']
