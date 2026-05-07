import pytest
from selenium import webdriver


@pytest.fixture
def conf():
    driver = webdriver.Chrome()
    return driver
