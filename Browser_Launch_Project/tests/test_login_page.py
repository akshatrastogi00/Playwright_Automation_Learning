import pytest
from config.constants import BASE_URL, VALID_PASSWORD, VALID_USERNAME
from pages.login_page import LoginPage


def test_launch_login_page(browser_context):
    page = browser_context
    login_page = LoginPage(page)
    login_page.open_login_page(BASE_URL)

    assert login_page.is_login_form_visible() is True
    assert login_page.is_logo_visible() is True

    login_page.take_screenshot("launch_page")


@pytest.mark.parametrize(
    "username,password,expected_message",
    [
        ("", "admin123", "Required"),
        ("Admin", "", "Required"),
        ("invalid", "invalid", "Invalid credentials"),
    ],
)
def test_login_negative_cases(browser_context, username, password, expected_message):
    page = browser_context
    login_page = LoginPage(page)
    login_page.open_login_page(BASE_URL)
    login_page.login(username, password)

    login_page.take_screenshot(f"negative_{username or 'blank'}")

    assert "/auth/login" in page.url.lower()
    assert login_page.is_login_form_visible() is True


def test_login_success(browser_context):
    page = browser_context
    login_page = LoginPage(page)
    login_page.open_login_page(BASE_URL)
    login_page.login(VALID_USERNAME, VALID_PASSWORD)

    try:
        page.wait_for_url("**/*", timeout=15000)
    except Exception:
        pass

    login_page.take_screenshot("successful_login")

    assert page.url != BASE_URL
