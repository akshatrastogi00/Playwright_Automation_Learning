import os

import pytest
from playwright.sync_api import sync_playwright


@pytest.fixture(scope="function")
def browser_context():
    headless = os.getenv("PLAYWRIGHT_HEADLESS", "true").lower() == "true"

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=headless)
        context = browser.new_context(viewport={"width": 1440, "height": 900})
        page = context.new_page()
        page.set_default_timeout(30000)
        page.set_default_navigation_timeout(30000)
        yield page
        context.close()
        browser.close()
