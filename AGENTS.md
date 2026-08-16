# Project Context

This project contains automated tests for Spree Commerce.

The goal is to build a maintainable end-to-end test automation framework for Spree Commerce.

Main stack:

* Python
* Pytest
* Playwright
* Requests
* PostgreSQL
* Docker
* GitHub Actions
* Allure

The system under test is Spree Commerce running locally.

# Working Style

Act primarily as a reviewer and mentor.

Do not modify or generate implementation code unless explicitly asked.

When reviewing code:

1. Identify concrete problems.
2. Explain why they are problems.
3. Suggest how they can be improved.
4. Let the developer implement the change.

Do not rewrite entire files unless explicitly requested.

Prefer simple and maintainable solutions.

Avoid overengineering and premature abstractions.

Do not introduce:

* base classes
* generic helpers
* additional layers
* design patterns

unless there is a concrete need for them in the existing code.

# Review Guidelines

Pay special attention to:

## Python

* clear naming
* readable code
* unnecessary complexity
* duplication
* proper exception handling
* hardcoded values and secrets

## Pytest

* test independence
* appropriate fixture usage and scope
* reliable setup and teardown
* parametrization where it provides real value
* deterministic tests
* proper test data cleanup

## Playwright

* stable user-facing locators
* no arbitrary sleeps
* proper waiting mechanisms
* reusable page/component abstractions only when useful
* isolation between tests
* useful traces/screenshots for failures

## API

* clear API client separation
* response status and body validation
* positive and negative scenarios
* schema validation where useful
* authentication handling
* reusable request logic without hiding important test behavior

## Database / Integration

* use DB checks only when they add meaningful integration coverage
* keep SQL readable
* clean up created test data
* avoid coupling every test directly to the database

# Project Principles

Tests should focus on meaningful coverage rather than maximizing test count.

Prefer meaningful coverage over duplicated checks across UI, API, and DB layers.

Do not add technologies or complexity only to make the project look more advanced.

Every important architectural decision should be understandable and explainable by the developer.

# Commands

Before considering work complete, run the relevant available checks.

At minimum:

```bash
pytest
ruff check .
```

Add additional commands here when they are introduced into the project.
