import pytest
from playwright.sync_api import Page

from pages.account_page import AccountPage
from pages.login_page import LoginPage


@pytest.fixture
def opened_login_page(page: Page) -> LoginPage:
    """Fixture to initialize the Login Page."""
    login_page = LoginPage(page)
    login_page.open()
    return login_page


@pytest.fixture
def account_page(page: Page) -> AccountPage:
    return AccountPage(page)
