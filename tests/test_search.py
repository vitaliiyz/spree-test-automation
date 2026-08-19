import pytest
from playwright.sync_api import Page

from pages.search_page import SearchPage


@pytest.fixture
def search_page(page: Page) -> SearchPage:
    """Fixture providing an initialized SearchPage instance."""
    page_obj = SearchPage(page)
    page_obj.navigate()
    return page_obj


def test_search_returns_matching_products(search_page: SearchPage) -> None:
    """Verify that searching for a valid keyword displays product results."""
    search_page.search_for("mug")
    search_page.verify_results_displayed()


def test_search_with_invalid_query_shows_empty_state(search_page: SearchPage) -> None:
    """Verify that an appropriate empty state appears when no matches are found."""
    search_page.search_for("non_existing_product_xyz_123")
    search_page.verify_empty_state_displayed()
