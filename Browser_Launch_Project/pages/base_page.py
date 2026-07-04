from pathlib import Path

from utils.helpers import ensure_directory


class BasePage:
    def __init__(self, page):
        self.page = page

    def wait_for_page_ready(self):
        try:
            self.page.wait_for_load_state("networkidle", timeout=10000)
        except Exception:
            self.page.wait_for_load_state("domcontentloaded", timeout=10000)
        self.page.locator("body").first.wait_for(state="visible", timeout=10000)
        self.page.wait_for_timeout(500)

    def open(self, url: str):
        self.page.goto(url, wait_until="domcontentloaded", timeout=30000)
        self.wait_for_page_ready()

    def wait_for_visible(self, selector: str, timeout: int = 10000):
        self.page.locator(selector).first.wait_for(state="visible", timeout=timeout)

    def click(self, selector: str):
        self.wait_for_visible(selector)
        self.page.locator(selector).first.click()

    def fill(self, selector: str, value: str):
        self.wait_for_visible(selector)
        self.page.locator(selector).first.fill(value)

    def get_text(self, selector: str) -> str:
        self.wait_for_visible(selector)
        return self.page.locator(selector).first.inner_text()

    def is_visible(self, selector: str) -> bool:
        try:
            self.page.locator(selector).first.wait_for(state="visible", timeout=5000)
            return True
        except Exception:
            return False

    def take_screenshot(self, name: str):
        self.wait_for_page_ready()
        screenshot_dir = Path("screenshots")
        ensure_directory(str(screenshot_dir))
        screenshot_path = screenshot_dir / f"{name}.png"
        self.page.screenshot(path=str(screenshot_path), full_page=True, animations="disabled")
        return screenshot_path
