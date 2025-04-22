import os
import pytest

@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    results_dir = config.getoption("--alluredir")
    if results_dir and not os.path.exists(results_dir):
        os.makedirs(results_dir)