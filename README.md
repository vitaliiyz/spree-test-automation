# Spree Test Automation

Test automation framework for Spree Commerce.

The project currently covers UI authentication testing using Python, Pytest, and Playwright.
API testing with Requests is planned.

## Tech Stack

- **Python 3.13** — python runtime.
- **Pytest 9.1.1** — testing framework.
- **Playwright 1.62.0** — browser automation library.
- **Requests 2.34.2** — HTTP library for API testing.
- **Ruff 0.16.3** — linting tool.
- **Black 26.5.1** — code formatter.
- **Docker Compose** — containerized CI services and Playwright test runner.
- **GitHub Actions** — automated checks and end-to-end test execution.

Minimum dependency versions are specified in `pyproject.toml`; exact resolved versions are recorded in `uv.lock` for reproducible installations.

## Planned test coverage

- [x] Customer authentication: successful login, invalid password, unknown email, and logout.
- [ ] Customer registration.
- [ ] Product catalog, search, and filtering.
- [ ] Cart management.
- [ ] Checkout and order creation.
- [ ] API tests for customers, products, carts, and orders.
- [ ] Additional negative scenarios and validation errors.

## Project structure

```
.
├── .github
│   └── workflows
│       └── tests.yml
├── .env.example
├── .gitignore
├── .python-version
├── AGENTS.md
├── README.md
├── compose.ci.yml
├── config.py
├── pages
│   ├── account_page.py
│   ├── base_page.py
│   └── login_page.py
├── pyproject.toml
├── tests
│   └── ui
│       ├── conftest.py
│       └── test_auth.py
└── uv.lock
```

## Prerequisites

- [uv](https://docs.astral.sh/uv/getting-started/installation/) installed.
- Spree Commerce storefront running and available at the URL configured in `BASE_URL` (for example, `http://localhost:3001`).

## Setup and execution

Clone the repository and enter its directory:

```bash
git clone https://github.com/vitaliiyz/spree-test-automation.git
cd spree-test-automation
```

Install the dependencies:

```bash
uv sync --locked
```

Create a local environment file:

```bash
cp .env.example .env
```

Open `.env` and provide the storefront URL and valid customer credentials:

```dotenv
LOGIN_EMAIL=your_login_email
PASSWORD=your_login_password
BASE_URL=http://localhost:3001/us/en
```

The `.env` file contains local credentials and must not be committed.

For local execution, install the Chromium browser used by the UI tests. CI uses the pinned
Playwright Docker image instead:

```bash
uv run playwright install chromium
```

Run the complete suite from the repository root:

```bash
uv run pytest
```

## Continuous integration

The GitHub Actions workflow runs for pull requests targeting `main`, pushes to `main`, and manual
workflow dispatches.

The workflow checks out the pinned Spree storefront revision, validates the Python code, starts
PostgreSQL, Redis, and Spree through Docker Compose, seeds the database, creates a test customer,
and starts the storefront through `pnpm`. Pytest then runs inside a version- and digest-pinned
Playwright Python container. Docker resources are removed after the run, including after failures.
