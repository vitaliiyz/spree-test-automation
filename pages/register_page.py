from playwright.sync_api import Locator, Page

from pages.base_page import BasePage


class RegisterPage(BasePage):
    """Login page object for handling register operations."""

    def __init__(self, page: Page) -> None:
        """Initialize the register page."""
        super().__init__(page)
        self._path = "/account/register"

        self.register_form: Locator = self.page.locator('[data-slot="card"]')
        self.register_form_title: Locator = self.register_form.locator('[data-slot="card-title"]')
        self.register_form_description: Locator = self.register_form.locator(
            '[data-slot="card-description"]'
        )
        self.first_name_field: Locator = self.register_form.get_by_role(
            "textbox", name="First name", exact=True
        )
        self.last_name_field: Locator = self.register_form.get_by_role(
            "textbox", name="Last name", exact=True
        )
        self.email_field: Locator = self.register_form.get_by_role(
            "textbox", name="Email", exact=True
        )
        self.password_field: Locator = self.register_form.get_by_role(
            "textbox", name="Password", exact=True
        )
        self.password_visibility_button: Locator = self.register_form.locator(
            "#password + div button"
        )
        self.confirm_password_field: Locator = self.register_form.get_by_role(
            "textbox", name="Confirm Password", exact=True
        )
        self.confirm_password_visibility_button: Locator = self.register_form.locator(
            "#passwordConfirmation + div button"
        )
        self.policy_consent_checkbox: Locator = self.register_form.get_by_role(
            "checkbox",
            name="I agree to the Privacy Policy and Terms of Service",
            exact=True,
        )
        self.privacy_policy_link: Locator = self.register_form.get_by_role(
            "link", name="Privacy Policy", exact=True
        )
        self.terms_of_service_link: Locator = self.register_form.get_by_role(
            "link", name="Terms of Service", exact=True
        )
        self.privacy_policy_label: Locator = self.privacy_policy_link.locator(
            "xpath=ancestor::label[1]"
        )
        self.create_account_button: Locator = self.register_form.get_by_role(
            "button", name="Create Account", exact=True
        )
        self.sign_in_link: Locator = self.register_form.get_by_role(
            "link", name="Sign in", exact=True
        )
        self.alert: Locator = self.register_form.get_by_role("alert")

    def register(
        self,
        first_name: str,
        last_name: str,
        email: str,
        password: str,
        confirm_password: str | None = None,
        click_policy_checkbox: bool = True,
    ) -> None:
        self.first_name_field.fill(first_name)
        self.last_name_field.fill(last_name)
        self.email_field.fill(email)
        self.password_field.fill(password)

        self.confirm_password_field.fill(
            confirm_password if confirm_password is not None else password
        )

        if click_policy_checkbox:
            self.policy_consent_checkbox.click()

        self.create_account_button.click()
