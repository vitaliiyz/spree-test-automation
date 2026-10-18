import pytest
from playwright.sync_api import Page

from config import FIRST_NAME, LAST_NAME, LOGIN_EMAIL, PASSWORD
from pages.account_page import AccountPage
from pages.login_page import LoginPage
from pages.register_page import RegisterPage
from utils.email_generator import generate_email
from utils.postgres_helper import (
    create_user_data,
    get_spree_refresh_tokens_by_id,
    get_user_by_email,
    remove_created_user_data_by_id,
)


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


@pytest.fixture
def opened_register_page(page: Page) -> RegisterPage:
    """Fixture to initialize the Register Page."""
    register_page = RegisterPage(page)
    register_page.open()

    return register_page


@pytest.fixture
def registration_email():
    """Fixture to generate an email address and remove created user data from database after testing."""
    return generate_email()


@pytest.fixture
def registered_user_email(registration_email, remove_user):
    """Fixture to generate an email and remove created user data from database after testing."""
    yield registration_email
    remove_user(registration_email)


@pytest.fixture
def remove_user():
    """Fixture to remove created user data from database after testing."""

    def remove_created_user_data_by_email(email: str) -> None:
        user = get_user_by_email(email)

        if user:
            user_id = user["id"]
            remove_created_user_data_by_id(user_id)

            assert get_user_by_email(email) is None
            assert not get_spree_refresh_tokens_by_id(user_id)

    return remove_created_user_data_by_email


@pytest.fixture
def registered_user(registered_user_email, remove_user):
    """Fixture to register user data from database after testing."""
    create_user_data(registered_user_email, FIRST_NAME, LAST_NAME)
    return registered_user_email
