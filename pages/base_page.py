from playwright.sync_api import Page

from config import BASE_URL


class BasePage:
    """Base page object for common page operations."""

    def __init__(self, page: Page) -> None:
        """Initialize the base page."""
        self.page = page
        self._path = ""

    def open(self) -> None:
        """Open the page in the browser."""
        self.page.goto(f"{BASE_URL}{self._path}")
