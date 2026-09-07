import pytest
from playwright.sync_api import Page

from config import LOGIN_EMAIL, PASSWORD
from pages.account_page import AccountPage
from pages.login_page import LoginPage


@pytest.fixture
def login_page(page: Page) -> LoginPage:
    """Fixture to initialize and return the Login Page."""
    return LoginPage(page)


@pytest.fixture
def opened_login_page(login_page: LoginPage) -> LoginPage:
    """Fixture to open and return the Login Page."""
    login_page.open()

    return login_page


@pytest.fixture
def account_page(page: Page) -> AccountPage:
    """Fixture to initialize the Account Page."""
    return AccountPage(page)


@pytest.fixture
def logged_in_account_page(opened_login_page: LoginPage, account_page: AccountPage) -> AccountPage:
    """Fixture to log in and return the Account Page."""
    opened_login_page.login(email=LOGIN_EMAIL, password=PASSWORD)

    return account_page
