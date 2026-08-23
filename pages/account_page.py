from playwright.sync_api import Locator, Page

from pages.base_page import BasePage


class AccountPage(BasePage):
    """Account page object for handling account operations."""

    def __init__(self, page: Page) -> None:
        """Initialize the account page."""
        super().__init__(page)
        self._path = "/account"

        self.account_title: Locator = self._page.get_by_role(
            "heading",
            name="Account Overview",
            exact=True,
        )
        self.sidebar: Locator = self._page.get_by_role("complementary")
        self.sign_out_button: Locator = self.sidebar.get_by_role("button", name="Sign Out")

    def sign_out(self) -> None:
        """Perform sign out action."""
        self.sign_out_button.click()
