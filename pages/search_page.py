# pages/search_page.py
from playwright.sync_api import Locator, Page, expect


class SearchPage:
    """Page Object representing catalog search functionality."""

    def __init__(self, page: Page) -> None:
        self.page = page

    @property
    def search_input(self) -> Locator:
        # Tries accessible placeholders first, falling back to id/name selectors
        return self.page.get_by_placeholder("Search", exact=False).or_(
            self.page.locator('input[name="keywords"], #keywords, input[type="search"]')
        ).first

    @property
    def product_cards(self) -> Locator:
        return self.page.locator(
            ".product-component, .product-card, [data-hook='products_list_item']"
        )

    @property
    def empty_results_message(self) -> Locator:
        return self.page.locator(".no-results, :text('No products found')").first

    def navigate(self, path: str = "/") -> None:
        """Navigates to the specified target path."""
        self.page.goto(path)

    def search_for(self, query: str) -> None:
        """Fills the search field and submits the query."""
        self.search_input.fill(query)
        self.search_input.press("Enter")

    def verify_results_displayed(self) -> None:
        """Asserts that at least one product card is visible."""
        expect(self.product_cards.first).to_be_visible()

    def verify_empty_state_displayed(self) -> None:
        """Asserts that the no-results indicator is visible."""
        expect(self.empty_results_message).to_be_visible()