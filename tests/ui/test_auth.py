from playwright.sync_api import expect

from config import INVALID_PASSWORD, LOGIN_EMAIL, PASSWORD, UNKNOWN_EMAIL
from pages.account_page import AccountPage
from pages.login_page import LoginPage


def test_successful_login(opened_login_page: LoginPage, account_page: AccountPage) -> None:
    """
    Test to verify that a user can successfully log in with valid credentials.
    """
    opened_login_page.login(email=LOGIN_EMAIL, password=PASSWORD)

    expect(account_page.account_title).to_be_visible()
    expect(account_page.sidebar.get_by_text(LOGIN_EMAIL, exact=True)).to_be_visible()


def test_login_with_invalid_password(opened_login_page: LoginPage) -> None:
    """
    Test to verify that a user with an invalid password_field sees an error.
    """
    opened_login_page.login(email=LOGIN_EMAIL, password=INVALID_PASSWORD)

    expect(opened_login_page.invalid_credentials_error).to_be_visible()


def test_login_with_unknown_email(opened_login_page: LoginPage) -> None:
    """
    Test to verify that a user with an unknown email sees an error.
    """
    opened_login_page.login(email=UNKNOWN_EMAIL, password=PASSWORD)

    expect(opened_login_page.invalid_credentials_error).to_be_visible()


def test_logout(logged_in_account_page: AccountPage, login_page: LoginPage) -> None:
    """
    Test to verify that a user can successfully log out.
    """
    logged_in_account_page.sign_out()

    expect(logged_in_account_page.account_title).not_to_be_visible()
    expect(login_page.login_form).to_be_visible()
