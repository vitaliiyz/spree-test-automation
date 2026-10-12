from playwright.sync_api import expect

from config import FIRST_NAME, LAST_NAME, PASSWORD
from pages.account_page import AccountPage
from pages.login_page import LoginPage
from pages.register_page import RegisterPage


def test_successful_registration(
    opened_register_page: RegisterPage, account_page: AccountPage, registration_email, remove_user
) -> None:
    """Test to verify that user can create an account successfully with valid data."""

    try:
        opened_register_page.register(
            first_name=FIRST_NAME,
            last_name=LAST_NAME,
            email=registration_email,
            password=PASSWORD,
        )

        expect(account_page.account_title).to_be_visible()
        expect(account_page.sidebar.get_by_text(registration_email, exact=True)).to_be_visible()

    finally:
        remove_user(registration_email)


def test_registered_user_can_login_again(
    opened_register_page: RegisterPage,
    account_page: AccountPage,
    login_page: LoginPage,
    registration_email,
    remove_user,
) -> None:
    """Test to verify that user can create an account successfully with valid data and login again."""

    try:
        opened_register_page.register(
            first_name=FIRST_NAME,
            last_name=LAST_NAME,
            email=registration_email,
            password=PASSWORD,
        )

        account_page.sign_out()

        login_page.login(registration_email, PASSWORD)
        expect(account_page.account_title).to_be_visible()
        expect(account_page.sidebar.get_by_text(registration_email, exact=True)).to_be_visible()

    finally:
        remove_user(registration_email)


def test_registration_email_exists(
    opened_register_page: RegisterPage, registration_email, registered_user
) -> None:
    """Test to verify that user cannot create an account with an existing email."""

    opened_register_page.register(
        first_name=FIRST_NAME,
        last_name=LAST_NAME,
        email=registration_email,
        password=PASSWORD,
    )

    expect(opened_register_page.alert).to_have_text("Email has already been taken")


def test_registration_without_policies_agree(
    opened_register_page: RegisterPage, registration_email, remove_user
) -> None:
    """Test to verify that user cannot create an account without an agreed policy checkbox."""

    try:
        opened_register_page.register(
            first_name=FIRST_NAME,
            last_name=LAST_NAME,
            email=registration_email,
            password=PASSWORD,
            click_policy_checkbox=False,
        )

        expect(opened_register_page.alert).to_have_text(
            "You must agree to the store policies to create an account"
        )
        expect(opened_register_page.privacy_policy_label).to_contain_class("text-red-500")

    finally:
        remove_user(registration_email)


def test_registration_passwords_not_match(
    opened_register_page: RegisterPage, registration_email, remove_user
) -> None:
    """Test to verify that user cannot create an account with different values in password and confirm password fields."""

    try:
        opened_register_page.register(
            first_name=FIRST_NAME,
            last_name=LAST_NAME,
            email=registration_email,
            password=PASSWORD,
            confirm_password=f"{PASSWORD}1",
        )

        expect(opened_register_page.alert).to_have_text("Passwords do not match")

    finally:
        remove_user(registration_email)


def test_privacy_policy_link_works(opened_register_page: RegisterPage) -> None:

    with opened_register_page.page.expect_popup() as popup:
        opened_register_page.privacy_policy_link.click()

    privacy_page = popup.value

    expect(privacy_page.get_by_role("heading", name="Privacy Policy", exact=True)).to_have_text(
        "Privacy Policy"
    )


def test_terms_of_service_link_works(opened_register_page: RegisterPage) -> None:

    with opened_register_page.page.expect_popup() as popup:
        opened_register_page.terms_of_service_link.click()

    terms_page = popup.value

    expect(terms_page.get_by_role("heading", name="Terms of Service", exact=True)).to_have_text(
        "Terms of Service"
    )
