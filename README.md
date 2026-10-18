# Spree Test Automation

Test automation framework for Spree Commerce.

The project currently covers UI authentication testing using Python, Pytest, and Playwright.
API testing with Requests is planned.

## Tech Stack

- **Python 3.13** — python runtime.
- **Pytest 9.1.1** — testing framework.
- **Playwright 1.62.0** — browser automation library.
- **Requests 2.34.2** — HTTP library for API testing.
- **Psycopg 3.3.5** — PostgreSQL driver for registration test data setup and cleanup.
- **Ruff 0.16.3** — linting tool.
- **Black 26.5.1** — code formatter.
- **Docker Compose** — containerized CI services and Playwright test runner.
- **GitHub Actions** — automated checks and end-to-end test execution.

Minimum dependency versions are specified in `pyproject.toml`; exact resolved versions are recorded in `uv.lock` for reproducible installations.

## Planned test coverage

- [x] Customer authentication: successful login, invalid password, unknown email, and logout.
- [x] Customer registration.
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
│   ├── login_page.py
│   └── register_page.py
├── pyproject.toml
├── tests
│   └── ui
│       ├── conftest.py
│       ├── test_login.py
│       └── test_register.py
├── utils
│   ├── email_generator.py
│   └── postgres_helper.py
└── uv.lock
```

## Prerequisites

- [uv](https://docs.astral.sh/uv/getting-started/installation/) installed.
- Spree Commerce storefront running and available at the URL configured in `BASE_URL` (for example, `http://localhost:3001`).
- Access to the PostgreSQL database used by the same Spree instance, with
  permissions to read, insert, and delete test data. Configure the connection
  using `DATABASE_URL` in `.env`.

## Local Spree startup

Replace `<path-to-spree-local>` with the path to your local Spree project.

### Start Spree services

```bash
cd <path-to-spree-local>
docker compose up -d
docker compose ps
```

### Start the storefront

Run the following commands in a separate terminal and keep it open:

```bash
cd <path-to-spree-local>/apps/storefront
npm run dev
```

### Enable database access

Registration tests need access to the Spree PostgreSQL database from the host.
Create a proxy container once to expose PostgreSQL at `127.0.0.1:5433`:

```bash
docker run -d \
  --name spree-db-access \
  --restart unless-stopped \
  --network spree-local_default \
  -p 127.0.0.1:5433:5432 \
  alpine/socat \
  TCP-LISTEN:5432,fork,reuseaddr \
  TCP:spree-local-postgres-1:5432
```

This command assumes that the Docker network is named `spree-local_default`
and the PostgreSQL container is named `spree-local-postgres-1`.
Replace these names if your local environment uses different ones.

If the proxy container already exists but is stopped, start it instead:

```bash
docker start spree-db-access
```

Configure `DATABASE_URL` in `.env` using `127.0.0.1`, port `5433`,
and the database name and credentials of your local Spree instance.

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

Open `.env` and fill in all variables from `.env.example`.

Registration tests require access to the Spree PostgreSQL database and create
and delete test data there.

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

## Stop the local environment

Stop the storefront by pressing `Ctrl+C` in the terminal running `npm run dev`.

Stop the database access proxy:

```bash
docker stop spree-db-access
```

Stop Spree services:

```bash
cd <path-to-spree-local>
docker compose stop
```

The containers and database data are preserved.
To start the environment again, follow the **Local Spree startup** instructions.
For database access, use `docker start spree-db-access` because the proxy container already exists.

## Continuous integration

The GitHub Actions workflow runs for pull requests targeting `main`, pushes to `main`, and manual
workflow dispatches.

The workflow checks out the pinned Spree storefront revision, validates the Python code, starts
PostgreSQL, Redis, and Spree through Docker Compose, seeds the database, creates a test customer,
and starts the storefront through `pnpm`. Pytest then runs inside a version- and digest-pinned
Playwright Python container. Docker resources are removed after the run, including after failures.
