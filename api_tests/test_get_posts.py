# api_tests/test_get_posts.py
import requests
from config.config import logger


def test_get_posts():
    url = "https://jsonplaceholder.typicode.com/posts"
    logger.info(f"Sending GET request to {url}")
    response = requests.get(url)

    # Log the status code and response body
    logger.info(f"Response Status Code: {response.status_code}")
    logger.info(f"Response Body: {response.json()}")

    # Check if the response status code is 200
    assert response.status_code == 200

    # Check if the response contains data
    assert len(response.json()) > 0


def test_get_single_post():
    url = "https://jsonplaceholder.typicode.com/posts/1"
    logger.info(f"Sending GET request to {url}")
    response = requests.get(url)

    # Log the status code and response body
    logger.info(f"Response Status Code: {response.status_code}")
    logger.info(f"Response Body: {response.json()}")

    # Check if the response status code is 200
    assert response.status_code == 200

    # Validate that the post has the expected ID
    assert response.json()['id'] == 1


def test_get_non_existent_post():
    url = "https://jsonplaceholder.typicode.com/posts/99999"
    logger.info(f"Sending GET request to {url}")
    response = requests.get(url)

    # Log the status code and response body
    logger.info(f"Response Status Code: {response.status_code}")
    logger.info(f"Response Body: {response.json()}")

    # Check if the response status code is 404 (Not Found)
    assert response.status_code == 404
