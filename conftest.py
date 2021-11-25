import logging

import pytest

def pytest_addoption(parser) -> None:
    parser.addoption(
        "--hello",
        action="store_true",
        help="Print Hello before executing tests.")

    parser.addoption(
        "--bye",
        action="store_true",
        help="Print Bye at exiting framework.")

def pytest_sessionstart(session: pytest.FixtureRequest.session) -> None:
    logging.info("------------------ START ------------------")
    f_hello = session.config.getoption('--hello')
    if f_hello:
        print("Hello")

def pytest_sessionfinish(session: pytest.FixtureRequest.session):
    cleanup = session.config.getoption("--bye")
    if cleanup:
        print("\nBye")
    logging.info("------------------ STOP ------------------")
