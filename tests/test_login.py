from playwright.sync_api import Page, expect


def test_main_page(page: Page):
    page.goto('http://localhost:3001')
    expect(page.get_by_text('Spree Store Storefront')).to_be_visible()


def test_login(page: Page):
    page.goto('http://localhost:3001')
    page.locator('//a[@aria-label="Account"]').click()
    expect(page.locator('[data-slot="card-title"]'), 'No element found').to_have_text('My Account')
