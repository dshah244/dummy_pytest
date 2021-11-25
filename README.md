# Introduction

This is a dummy project meant to run irrelevant tests.
The focus of this project is to provide a reference to a potential
`pytest-cov` bug.

## Bug

`pytest-cov` does not seem to consider code being executed within `pytest_sessionfinish` for coverage.

Such behaviour can be seen within the [coverage report](./cov_report/index.html).

# Run tests

1. Setup python3.10 environment
    ```bash
    python3 -m venv env_dummy
    . env_dummy/bin/activate
    pip install -U pip setuptools && pip install -r req_dev.txt
    ```

2. Run tests + coverage
    
    Pytest related settings are already present within pyproject.toml
    ```bash
    pytest test_dummy.py
    ```
