# OrangeHRM Playwright Python Automation Project

## Overview
This project uses Python with Playwright and the Page Object Model (POM) to automate the OrangeHRM login page.

## Folder Structure
- pages/: page object classes
- tests/: test cases
- screenshots/: captured screenshots
- reports/: HTML test reports

## Setup
1. Create a virtual environment:
   python -m venv .venv
2. Activate it:
   .venv\Scripts\activate
3. Install dependencies:
   pip install -r requirements.txt
4. Install Playwright browsers:
   playwright install

## Run Tests
pytest

## Covered Scenarios
- Launch the login page
- Verify login form visibility
- Validate login with valid credentials
- Validate negative login attempts
- Capture screenshots for key steps

## Suggested Future Enhancements
- Add data-driven tests with Excel/CSV inputs
- Integrate with Jenkins or GitHub Actions
- Add all-pure POM for dashboard and employee modules
- Add logging and reporting improvements
- Introduce CI/CD and test retries
