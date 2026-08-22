from playwright.sync_api import Locator, Page

from pages.base_page import BasePage


class LoginPage(BasePage):
    """Login page object for handling login operations."""

    def __init__(self, page: Page) -> None:
        """Initialize the login page."""
        super().__init__(page)
        self._path = "/account"

        self.card_title: Locator = self._page.locator('[data-slot="card-title"]')
        self.email: Locator = self._page.locator("#email")
        self.password: Locator = self._page.locator("#password")
        self.login_button: Locator = self._page.get_by_role("button", name="Sign In")

    def login(self, email: str, password: str) -> None:
        """Perform login action."""
        self.email.fill(email)
        self.password.fill(password)
        self.login_button.click()
