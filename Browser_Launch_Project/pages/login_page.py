from pages.base_page import BasePage


class LoginPage(BasePage):
    username_input = 'input[name="username"]'
    password_input = 'input[name="password"]'
    login_button = 'button[type="submit"]'
    error_message = '.oxd-alert-content'
    login_logo = '.orangehrm-login-branding'

    def open_login_page(self, url: str):
        self.open(url)

    def is_login_form_visible(self) -> bool:
        return self.is_visible(self.username_input) and self.is_visible(self.password_input)

    def login(self, username: str, password: str):
        self.fill(self.username_input, username)
        self.fill(self.password_input, password)
        self.click(self.login_button)

    def get_error_message(self) -> str:
        try:
            self.wait_for_visible(self.error_message, timeout=8000)
            return self.get_text(self.error_message)
        except Exception:
            return self.page.locator("body").inner_text()

    def is_logo_visible(self) -> bool:
        return self.is_visible(self.login_logo)
