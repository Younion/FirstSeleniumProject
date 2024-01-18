from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
import time

class TestPositiveScenarios:
    @pytest.mark.login
    def test_positive_login(self, driver):
        #open page
        driver.get("https:ionme.dev")

        #click login
        login_locator = driver.find_element(By.XPATH, "//a[@href='/login/']")
        login_locator.click()
        time.sleep(2)

        # Type email into email field
        email_locator = driver.find_element(By.XPATH, "//input[@id='id_username']")
        email_locator.send_keys("younion@gmail.com")
     
        # Type password into Password field
        password_locator = driver.find_element(By.XPATH, "//input[@id='id_password']")
        password_locator.send_keys("WTFzeldaforever!")

        # Push Login button
        submit_locator = driver.find_element(By.XPATH, "//section[@id='login']//form[@method='POST']/button[@type='submit']")
        submit_locator.click()
        time.sleep(2)

        # Verify new page URL contains ionme.dev/logged-in-successfully/
        url_locator = driver.current_url
        assert url_locator == "https://ionme.dev/"
        print("Your URL is: " + str(url_locator))

        # Verify new page contains expected text ('Congratulations' or 'successfully logged in')
        text_locator = driver.find_element(By.XPATH, "//div[@id='navbarToggleExternalContent']/ul//a[@href='/logout/']")
        actual_text = text_locator.text
        assert actual_text == "Logout"
        print(actual_text)

        # Verify button Log out is displayed on the new page
        logout_locator = driver.find_element(By.LINK_TEXT, "Logout")
        assert logout_locator.is_displayed()
    
    @pytest.mark.login
    def test_negative_login(self, driver):    
        #open page
        driver.get("https:ionme.dev")

        #click login
        login_locator = driver.find_element(By.XPATH, "//a[@href='/login/']")
        login_locator.click()
        time.sleep(2)

        # Type email into email field
        email_locator = driver.find_element(By.XPATH, "//input[@id='id_username']")
        email_locator.send_keys("younion@outlook.com")
     
        # Type password into Password field
        password_locator = driver.find_element(By.XPATH, "//input[@id='id_password']")
        password_locator.send_keys("wrongpassword!")

        # Push Login button
        submit_locator = driver.find_element(By.XPATH, "//section[@id='login']//form[@method='POST']/button[@type='submit']")
        submit_locator.click()
        time.sleep(2)

        # Verify new page URL contains ionme.dev/
        url_locator = driver.current_url
        assert url_locator == "https://ionme.dev/login/"
        print("Your URL is: " + str(url_locator))

        # Verify new page contains expected text
        text_locator = driver.find_element(By.XPATH, "//section[@id='login']//form[@method='POST']//ul[@class='m-0']/li")
        actual_text = text_locator.text
        assert actual_text == "Please enter a correct email address and password. Note that both fields may be case-sensitive."
        print(actual_text)