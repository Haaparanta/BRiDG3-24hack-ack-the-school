import os
import time
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

# Load environment variables from .env file
load_dotenv()

# Fetch email and password from environment variables
email = os.getenv('EMAIL')
password = os.getenv('PASSWORD')

if not email or not password:
    raise ValueError("EMAIL and PASSWORD environment variables are not set")

# Initialize the Safari driver
driver = webdriver.Safari()

try:
    # Open the webpage
    driver.get("https://moodle.tuni.fi/course/view.php?id=37071")
    time.sleep(3)

    # Click the login button
    try:
        login_button = driver.find_element(By.CSS_SELECTOR, ".additional-login")
        login_button.click()
    except NoSuchElementException:
        print("Login button not found")
    time.sleep(3)

    # Wait for the email input field and input the email
    try:
        email_input = driver.find_element(By.ID, "i0116")
        email_input.send_keys(email)
    except NoSuchElementException:
        print("Email input field not found")
    time.sleep(3)

    # Click the Next button
    try:
        next_button = driver.find_element(By.ID, "idSIButton9")
        next_button.click()
    except NoSuchElementException:
        print("Next button not found")
    time.sleep(3)

    # Wait for the password input field and input the password
    try:
        password_input = driver.find_element(By.ID, "i0118")
        password_input.send_keys(password)
    except NoSuchElementException:
        print("Password input field not found")
    time.sleep(3)

    # Click the Sign-in button
    try:
        signin_button = driver.find_element(By.ID, "idSIButton9")
        signin_button.click()
    except NoSuchElementException:
        print("Sign-in button not found")
    time.sleep(30)

    # Click the Yes button
    try:
        yes_button = driver.find_element(By.ID, "idSIButton9")
        yes_button.click()
    except NoSuchElementException:
        print("Yes button not found")
    time.sleep(3)


    # Click the sectionlink-4 link

    try:
        sectionlink_4_link = driver.find_element(By.ID, "section-4")
        sectionlink_4_link.click()
    except NoSuchElementException:
        print("sectionlink-4 link not found")







    time.sleep(60)



finally:
    # Close the browser
    driver.quit()
