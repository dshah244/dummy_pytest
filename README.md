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

2. Run tests and create code-coverage
    * code-coverage using pytest-cov
    
        ```bash
        pytest test_dummy.py --cov=conftest --cov-report=html:cov_report
        ```

    * Code-coverage using coverage
        
        ```bash
        rm -rf .coverage cov_report
        coverage --include=conftest.py run -m pytest test_dummy.py
        coverage html -d cov_report
        ```