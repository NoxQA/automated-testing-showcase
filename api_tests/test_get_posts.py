import requests
from config.config import logger, pytest_configure


def test_get_posts():
    url = "https://jsonplaceholder.typicode.com/posts"
    logger.info(f"Sending GET request to {url}")
    response = requests.get(url)

    logger.info(f"Response Status Code: {response.status_code}")
    logger.info(f"Response Body: {response.json()}")

    assert response.status_code == 200
    assert len(response.json()) > 0


def test_get_single_post():
    url = "https://jsonplaceholder.typicode.com/posts/1"
    logger.info(f"Sending GET request to {url}")
    response = requests.get(url)

    logger.info(f"Response Status Code: {response.status_code}")
    logger.info(f"Response Body: {response.json()}")

    assert response.status_code == 200
    assert response.json()['id'] == 1


def test_get_non_existent_post():
    url = "https://jsonplaceholder.typicode.com/posts/99999"
    logger.info(f"Sending GET request to {url}")
    response = requests.get(url)

    logger.info(f"Response Status Code: {response.status_code}")
    logger.info(f"Response Body: {response.json()}")

    assert response.status_code == 404
