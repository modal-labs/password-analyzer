# Password Analyzer

Sample repo for test case generation example (coming soon)!

## Requirements

- Install [Poetry](https://python-poetry.org/docs/#installation)
- Create a virtualenv `python -m venv .venv && source .venv/bin/activate`
- Install dependencies `poetry install --no-root`
- Run tests `poetry run pytest`
- For viewing test results in Allure, install [Allure](https://allurereport.org/docs/pytest/) and run
  - `poetry run pytest --alluredir allure-results`
  - `allure serve allure-results`
