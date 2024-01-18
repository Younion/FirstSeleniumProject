from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest


@pytest.fixture
def driver():
    print("creating chrome driver")
    my_driver = webdriver.Chrome()
    yield my_driver
    print("closing chrome driver")
    my_driver.close()