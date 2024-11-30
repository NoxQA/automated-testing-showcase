# Selenium Automation and API Testing Showcase

This repository demonstrates my proficiency in writing end-to-end automated tests using **Selenium**, **Pytest**, and **Python**. These tests cover various real-world scenarios typically encountered in web applications. In addition, the repository now includes **API testing** using **Requests** and **Pytest**, covering various REST API endpoints.

## Features

- Tests multiple scenarios on the [the-internet.herokuapp.com](https://the-internet.herokuapp.com/) such as A/B Testing, Checkboxes, Dropdowns, Basic Authentication, and more.
- **API tests** for endpoints such as `GET`, `POST`, `PUT`, `PATCH`, and `DELETE` on mock APIs like [jsonplaceholder.typicode.com](https://jsonplaceholder.typicode.com).
- Each test is structured to automate real-world scenarios commonly found in web applications.

## Test Scenarios

### Selenium Test Scenarios

The following test scenarios have been automated using **Selenium**:

- A/B Testing
- Add/Remove Elements
- Basic Auth (user and pass: admin)
- Broken Images
- Challenging DOM
- Checkboxes
- Context Menu
- Digest Authentication (user and pass: admin)
- Disappearing Elements
- Drag and Drop
- Dropdown
- Dynamic Content
- Dynamic Controls
- Dynamic Loading
- Entry Ad
- Exit Intent
- File Download
- File Upload
- Floating Menu
- Forgot Password
- Form Authentication
- Frames
- Geolocation
- Horizontal Slider
- Hovers
- Infinite Scroll
- Inputs
- JQuery UI Menus
- JavaScript Alerts
- JavaScript onload event error
- Key Presses
- Large & Deep DOM
- Multiple Windows
- Nested Frames
- Notification Messages
- Redirect Link
- Secure File Download
- Shadow DOM
- Shifting Content
- Slow Resources
- Sortable Data Tables
- Status Codes
- Typos
- WYSIWYG Editor

### API Test Scenarios

The following **API test scenarios** have been automated using **Requests** and **Pytest**:

- **GET**: Test fetching posts, single posts, and non-existent posts from a mock API.
- **POST**: Test creating new posts with valid and missing data.
- **PUT**: Test updating existing posts.
- **PATCH**: Test partially updating a post.
- **DELETE**: Test deleting posts and non-existent posts.

## Technologies Used

- **Python**: The programming language used.
- **Selenium**: Web automation library for browser-based tests.
- **Pytest**: Testing framework used for structuring and running tests.
- **Requests**: HTTP library for making API requests and testing API endpoints.
- **ChromeDriver**: WebDriver for Chrome browser.

## Setup

### Prerequisites

- **Python 3.x**
- **pip** (Python package installer)

## Part 2: Installation, Setup, Running Tests, and Conclusion (Post-Installation)

### Technologies Used

- **Python**: The programming language used.
- **Selenium**: Web automation library for browser-based tests.
- **Pytest**: Testing framework used for structuring and running tests.
- **Requests**: HTTP library for making API requests and testing API endpoints.
- **ChromeDriver**: WebDriver for Chrome browser.

### Setup

#### Prerequisites

- **Python 3.x**
- **pip** (Python package installer)

#### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/NoxQA/selenium-automation-showcase.git
2. Navigate to the project directory:
   ```bash
   cd selenium-automation-showcase
3. Set up a virtual environment (optional but recommended):
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate   # For Linux/macOS
   .venv\Scripts\activate      # For Windows
4.Install the dependencies:
      ```bash
      pip install -r requirements.txt

5.For Selenium tests:

- Make sure you have **Google Chrome** and **ChromeDriver** installed.
- Download **ChromeDriver** that matches your Chrome version from [here](https://sites.google.com/a/chromium.org/chromedriver/).

6. For API tests:

- This project uses the Requests library to perform HTTP requests for API testing. It does not require additional setup besides installing the dependencies.

#### Running Tests

1. Run Selenium tests (Web Automation):
      ```bash
   pytest tests/

2. Run API tests:
    ```bash
   pytest api_tests

3. Run all tests:
   ```bash
   pytest --maxfail=1 --disable-warnings -v

### Conlusion
This repository showcases my ability to automate web applications using Selenium and API testing with Requests. It includes a variety of test scenarios that simulate real-world use cases for web applications, demonstrating my knowledge of test automation in both the UI and API layers.










   
