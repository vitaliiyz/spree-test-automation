from playwright.sync_api import Locator, Page

from pages.base_page import BasePage


class LoginPage(BasePage):
    """Login page object for handling login operations."""

    def __init__(self, page: Page) -> None:
        """Initialize the login page."""
        super().__init__(page)
        self._path = "/account"

        self.login_form: Locator = self._page.locator('[data-slot="card"]')
        self.login_form_title: Locator = self.login_form.locator('[data-slot="card-title"]')
        self.email_field: Locator = self.login_form.get_by_role("textbox", name="Email", exact=True)
        self.password_field: Locator = self.login_form.get_by_role(
            "textbox", name="Password", exact=True
        )
        self.login_button: Locator = self.login_form.get_by_role("button", name="Sign In")
        self.invalid_credentials_error: Locator = self.login_form.get_by_text(
            "Invalid email or password", exact=True
        )

    def login(self, email: str, password: str) -> None:
        """Perform login action."""
        self.email_field.fill(email)
        self.password_field.fill(password)
        self.login_button.click()
