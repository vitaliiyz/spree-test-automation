# Spree Test Automation

Test automation framework for Spree Commerce.

The project currently covers UI testing using Python, Pytest, and Playwright.
API testing with Requests is planned.

## Tech Stack

- **Python 3.13** — python runtime.
- **Pytest 9.1.1** — testing framework.
- **Playwright 1.62.0** — browser automation library.
- **Requests 2.34.2** — HTTP library for API testing.
- **Ruff 0.16.3** — linting tool.
- **Black 26.5.1** — code formatter.

Minimum dependency versions are specified in `pyproject.toml`; exact resolved versions are recorded in `uv.lock` for reproducible installations.

## Planned test coverage

- [ ] Customer registration and authentication.
- [ ] Product catalog, search, and filtering.
- [ ] Cart management.
- [ ] Checkout and order creation.
- [ ] API tests for customers, products, carts, and orders.
- [ ] Negative scenarios and validation errors.

## Project structure

```
.
├── .gitignore
├── .python-version
├── AGENTS.md
├── README.md
├── pyproject.toml
├── tests
│   └── test_login.py
└── uv.lock
```

## Prerequisites

- [uv](https://docs.astral.sh/uv/getting-started/installation/) installed.
- Spree Commerce storefront running and available at `http://localhost:3001`.

## Setup and execution

Clone the repository and enter its directory:

```bash
git clone https://github.com/vitaliiyz/spree-test-automation.git
cd spree-test-automation
```

Install the dependencies:

```bash
uv sync
```

Install the Chromium browser used by the UI tests:

```bash
uv run playwright install chromium
```

Run the complete suite from the repository root:

```bash
uv run pytest
```
