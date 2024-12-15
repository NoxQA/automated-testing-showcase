# Automation Testing Showcase (Selenium, Appium, API Testing)

This repository demonstrates my proficiency in writing end-to-end automated tests using Selenium, Appium, Pytest, and Python. These tests cover real-world scenarios typically encountered in both web and mobile applications. The repository includes tests for UI automation (using Selenium and Appium) and API testing (using Requests).

The project is integrated with GitHub Actions for Continuous Integration (CI). Every time changes are made to the test scripts, the CI pipeline automatically triggers and runs the tests, ensuring that the automated test scenarios are always up-to-date and functioning correctly.

## Features

- Tests multiple scenarios on the [the-internet.herokuapp.com](https://the-internet.herokuapp.com/) such as A/B Testing, Checkboxes, Dropdowns, Basic Authentication, and more.
- Appium Tests: Automated testing for Appium's sample mobile applications [https://github.com/appium/sample-apps] on (Android and iOS) for UI functionality and interactions.
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

### Apium Test Scenarios
The following test scenarios have been automated using **Appium**:
- Accessibility Tests - Node Provider, Node Query, Accesibility Service, Custom View
- Animation Tests - Bouncing Balls, Cloning, Custom Evaluator, Layout Animations, Hide-Show Animations, Multiple Properties, Reversing, Seeking, View-Flip
- App - Action Bar Tabs, Usage
- Incoming tests in the future - Content, Graphics, Media, NFC, OS, Preference, Text, Views

### API Test Scenarios

The following **API test scenarios** have been automated using **Requests** and **Pytest**:

- **GET**: Test fetching posts, single posts, and non-existent posts from a mock API.
- **POST**: Test creating new posts with valid and missing data.
- **PUT**: Test updating existing posts.
- **PATCH**: Test partially updating a post.
- **DELETE**: Test deleting posts and non-existent posts.

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
- **Appium and Android SDK** - setup (for mobile testing)

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
   cd automation-testing-showcase
3. Set up a virtual environment (optional but recommended):
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate   # For Linux/macOS
   .venv\Scripts\activate      # For Windows
4. Install the dependencies:
   ```bash
   pip install -r requirements.txt

5. For Selenium tests:

- Make sure you have **Google Chrome** and **ChromeDriver** installed.
- Download **ChromeDriver** that matches your Chrome version from [here](https://sites.google.com/a/chromium.org/chromedriver/).

6. For API tests:

- This project uses the Requests library to perform HTTP requests for API testing. It does not require additional setup besides installing the dependencies.

7. For Appium tests - 

- Make sure Appium is installed. You can install it globally using npm:
   ```bash
      npm install -g appium

- Set up the Android SDK and AVD (Android Emulator) or connect a physical device.
- Configure desired capabilities in the Appium test scripts to match the device/emulator setup (refer to appium_config.py).

#### Running Tests

1. Run Selenium tests (Web Automation):
      ```bash
   pytest selenium_tests/

2. Run API tests:
    ```bash
   pytest api_tests

3. Run Appium Tests (Mobile UI Automation):

- Ensure that the Appium server is running, then execute the Appium tests:
  ```bash
      appium
      
      pytest appium_tests/

3. Run all tests:
   ```bash
   pytest --maxfail=0 --disable-warnings -v

### CI with GitHub Actions

This repository is integrated with GitHub Actions for Continuous Integration (CI), which automates the process of running tests whenever code is pushed or a pull request is created.

   What happens during the CI pipeline:
        - The workflow runs automated tests, including Selenium, Appium, and API tests.
        - After each test run, Allure Reports are automatically generated and stored as artifacts in the CI pipeline.

   Accessing Allure Reports:
        - Once the tests are executed, you can view the Allure Test Report directly from the GitHub Actions page in the repository.
        - Navigate to the Actions tab in the repository to find the latest workflow runs. Select a workflow run, and under Artifacts, you will find the generated Allure Reports.
        - Download the Allure Report zip file and extract it to view the detailed test execution results (i.e., passed, failed, skipped tests, trends, logs, and more).

   How it works:
        The CI workflow, defined in the .github/workflows/ci.yml file, executes the tests and generates the Allure results using the following steps:
            - Test execution: Selenium, Appium, and API tests are executed.
            - Report generation: Allure is configured to generate detailed, interactive test reports.
            - Artifact storage: Allure reports are stored as an artifact in the CI pipeline.

### Conlusion
This repository showcases my ability to automate web and mobile applications using Selenium, Appium and API testing with Requests. It includes a variety of test scenarios that simulate real-world use cases for web applications, demonstrating my knowledge of test automation in both the UI and API layers.
