import math

from playwright.sync_api import expect

from pages.products_page import ProductsPage

PRODUCTS_PER_BATCH = 12


def test_product_cards_display_required_details(opened_products_page: ProductsPage) -> None:
    expect(opened_products_page.product_cards).to_be_visible()

    product_count_in_span = opened_products_page.get_product_count_in_span()
    batches_count = math.ceil(product_count_in_span / PRODUCTS_PER_BATCH)

    for i in range(1, batches_count + 1):
        if i != batches_count:
            expect(opened_products_page.product).to_have_count(i * PRODUCTS_PER_BATCH)
            opened_products_page.product.last.scroll_into_view_if_needed()
        else:
            expect(opened_products_page.product).to_have_count(product_count_in_span)
            expect(opened_products_page.no_more_products_text).to_be_visible()
