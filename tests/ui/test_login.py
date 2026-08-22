from playwright.sync_api import expect

from config import LOGIN_EMAIL, PASSWORD
from pages.account_page import AccountPage
from pages.login_page import LoginPage


def test_login_form_is_displayed(opened_login_page: LoginPage) -> None:
    """
    Test to verify that the login page is open and displays the expected content.
    """
    expect(opened_login_page.card_title).to_have_text("My Account")
    expect(opened_login_page.email).to_be_visible()
    expect(opened_login_page.password).to_be_visible()
    expect(opened_login_page.login_button).to_be_visible()


def test_successful_login(opened_login_page: LoginPage, account_page: AccountPage) -> None:
    """
    Test to verify that a user can successfully log in with valid credentials.
    """
    opened_login_page.login(email=LOGIN_EMAIL, password=PASSWORD)
    expect(account_page.account_title).to_be_visible()
