import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.safari.service import Service
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Fetch email and password from environment variables
email = os.getenv('EMAIL')
password = os.getenv('PASSWORD')

if not email or not password:
    raise ValueError("EMAIL and PASSWORD environment variables are not set")

# Initialize the Safari driver
safari_service = Service('/usr/bin/safaridriver')
driver = webdriver.Safari(service=safari_service)

wait = WebDriverWait(driver, 10) # Wait for up to 10 seconds

try:
    # Open the webpage
    driver.get("https://moodle.tuni.fi/course/view.php?id=37071")

    # Wait and click the login button
    print("clicking login button")
    try:
        login_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".additional-login")))
        login_button.click()
    except TimeoutException:
        print("Login button not found")

    print("inputting email")
    try:
        email_input = wait.until(EC.presence_of_element_located((By.ID, "i0116")))
        email_input.send_keys(email)
    except TimeoutException:
        print("Email input field not found")

    # Click the Next button
    try:
        next_button = wait.until(EC.element_to_be_clickable((By.ID, "idSIButton9")))
        next_button.click()
    except TimeoutException:
        print("Next button not found")

    # Wait for the password input field and input the password
    print("inputting password")
    try:
        password_input = wait.until(EC.presence_of_element_located((By.ID, "i0118")))
        password_input.send_keys(password)
    except TimeoutException:
        print("Password input field not found")

    time.sleep(1)
    # Click the Sign-in button
    print("clicking sign-in button")
    try:
        signin_button = wait.until(EC.element_to_be_clickable((By.ID, "idSIButton9")))
        signin_button.click()
    except TimeoutException:
        print("Sign-in button not found")

    time.sleep(10)

    # Click the Yes button
    print("clicking yes button")
    try:
        yes_button = wait.until(EC.element_to_be_clickable((By.ID, "idSIButton9")))
        yes_button.click()
    except TimeoutException:
        print("Yes button not found")

    time.sleep(2)
    # Click the sectionlink-4 link
    print("clicking sectionlink-4 link")
    try:
        sectionlink_4_link = wait.until(EC.element_to_be_clickable((By.ID, "tile-4")))
        sectionlink_4_link.click()
    except TimeoutException:
        print("sectionlink-4 link not found")

    time.sleep(5)
    # Click module-2494203 link
    print("clicking module-2494203 link")
    try:
        module_2494203_link = wait.until(EC.element_to_be_clickable((By.ID, "module-2494203")))
        module_2494203_link.click()
    except TimeoutException:
        print("module-2494203 link not found")

    time.sleep(5)
    print("clicking Start button")
    try:
      iframe = driver.find_element(By.ID, "h5p-iframe-35645")
      driver.switch_to.frame(iframe)
      a_elements = driver.find_elements(By.TAG_NAME, 'a')
      for element in a_elements:
          trimmed_text = element.text.strip()
          print(trimmed_text)
          if trimmed_text == "Start":
              print("found start button")
              element.click()
              break
      print("element not found")
    except TimeoutException:
      print("element not found")
    
    driver.switch_to.default_content()

    time.sleep(2)

    try: 
      iframe = driver.find_element(By.ID, "h5p-iframe-35645")
      driver.switch_to.frame(iframe)

      for i in range(0, 10):
        # Find the question element and extract its text
        question_element = driver.find_element(By.ID, f"h5p-mcq{i}")
        question = question_element.text.strip()
        print("Question:", question)

        # Find the choice elements and extract their texts
        choice_elements = driver.find_elements(By.CLASS_NAME, "h5p-answer")
        choices = [choice.text.strip() for choice in choice_elements]

        if question == 'Business model describes how an organization…':
          print("found question 1")
          time.sleep(1)
          for choice in choice_elements:
            if choice.text.strip() == 'can evolve against upcoming risks and changes':
              print('Click choice:', choice.text.strip())
              choice.click()
              time.sleep(1)  # Wait for any potential animations or updates
            if choice.text.strip() == 'can capture value from the market':
              print('Click choice:', choice.text.strip())
              choice.click()
              time.sleep(1)  # Wait for any potential animations or updates
            if choice.text.strip() == 'can create value':
              print('Click choice:', choice.text.strip())
              choice.click()
              time.sleep(1)
          time.sleep(1)  # Wait for any potential animations or updates
          # Find all 'Check the answers' buttons
          check_answers_buttons = driver.find_elements(By.CLASS_NAME, "h5p-question-check-answer")

          # Iterate over each 'Check the answers' button and click if it is visible
          for button in check_answers_buttons:
              try:
                  if button.is_displayed():
                      button.click()
                      time.sleep(1)  # Wait for any potential animations or updates
                      break
              except Exception as e:
                  print(f"Error clicking a 'Check the answers' button: {e}")

          # Find all 'Next question' buttons
          next_question_buttons = driver.find_elements(By.CLASS_NAME, "h5p-question-next")

          # Iterate over each 'Next question' button and click if it is visible
          for button in next_question_buttons:
              try:
                  if button.is_displayed():
                      button.click()
                      time.sleep(1)  # Wait for the next question to load
                      break
              except Exception as e:
                  print(f"Error clicking a 'Next question' button: {e}")

        elif question == 'Software licenses…':
          print("found question 2")
          time.sleep(1)
          for choice in choice_elements:
            if choice.text.strip() == 'govern the use and distribution of software':
              print('Click choice:', choice.text.strip())
              choice.click()
              time.sleep(1)  # Wait for any potential animations or updates
            if choice.text.strip() == 'are often combined with other services (e.g., training and maintenance)':
              print('Click choice:', choice.text.strip())
              choice.click()
              time.sleep(1)  # Wait for any potential animations or updates
          time.sleep(1)  # Wait for any potential animations or updates

          # Find all 'Check the answers' buttons
          check_answers_buttons = driver.find_elements(By.CLASS_NAME, "h5p-question-check-answer")

          # Iterate over each 'Check the answers' button and click if it is visible
          for button in check_answers_buttons:
              try:
                  if button.is_displayed():
                      button.click()
                      time.sleep(1)  # Wait for any potential animations or updates
                      break
              except Exception as e:
                  print(f"Error clicking a 'Check the answers' button: {e}")

          # Find all 'Next question' buttons
          next_question_buttons = driver.find_elements(By.CLASS_NAME, "h5p-question-next")

          # Iterate over each 'Next question' button and click if it is visible
          for button in next_question_buttons:
              try:
                  if button.is_displayed():
                      button.click()
                      time.sleep(1)  # Wait for the next question to load
                      break
              except Exception as e:
                  print(f"Error clicking a 'Next question' button: {e}")

        elif question == 'Product bundling is good when…':
          print("found question 3")
          time.sleep(1)
          for choice in choice_elements:
            if choice.text.strip() == 'it helps developing software further that would not be sustained otherwise':
              print('Click choice:', choice.text.strip())
              choice.click()
              time.sleep(1)  # Wait for any potential animations or updates
            if choice.text.strip() == 'it helps gain competitive advantage':
              print('Click choice:', choice.text.strip())
              choice.click()
              time.sleep(1)  # Wait for any potential animations or updates
            if choice.text.strip() == 'it helps sell products that wouldn’t be sold otherwise':
              print('Click choice:', choice.text.strip())
              choice.click()
              time.sleep(1)
          time.sleep(1)  # Wait for any potential animations or updates
          # Find all 'Check the answers' buttons
          check_answers_buttons = driver.find_elements(By.CLASS_NAME, "h5p-question-check-answer")

          # Iterate over each 'Check the answers' button and click if it is visible
          for button in check_answers_buttons:
              try:
                  if button.is_displayed():
                      button.click()
                      time.sleep(1)  # Wait for any potential animations or updates
                      break
              except Exception as e:
                  print(f"Error clicking a 'Check the answers' button: {e}")

          # Find all 'Next question' buttons
          next_question_buttons = driver.find_elements(By.CLASS_NAME, "h5p-question-next")

          # Iterate over each 'Next question' button and click if it is visible
          for button in next_question_buttons:
              try:
                  if button.is_displayed():
                      button.click()
                      time.sleep(1)  # Wait for the next question to load
                      break
              except Exception as e:
                  print(f"Error clicking a 'Next question' button: {e}")

        elif question == 'Freemium…':
          print("found question 4")
          time.sleep(1)
          for choice in choice_elements:
            if choice.text.strip() == 'is good for luring in customers':
              print('Click choice:', choice.text.strip())
              choice.click()
              time.sleep(1)  # Wait for any potential animations or updates
            if choice.text.strip() == 'has a risk if the premium option isn’t attractive or clear to the customer':
              print('Click choice:', choice.text.strip())
              choice.click()
              time.sleep(1)  # Wait for any potential animations or updates
            if choice.text.strip() == 'charges for premium':
              print('Click choice:', choice.text.strip())
              choice.click()
              time.sleep(1)
          time.sleep(1)  # Wait for any potential animations or updates
          check_answers_buttons = driver.find_elements(By.CLASS_NAME, "h5p-question-check-answer")

          # Iterate over each 'Check the answers' button and click if it is visible
          for button in check_answers_buttons:
              try:
                  if button.is_displayed():
                      button.click()
                      time.sleep(1)  # Wait for any potential animations or updates
                      break
              except Exception as e:
                  print(f"Error clicking a 'Check the answers' button: {e}")

          # Find all 'Next question' buttons
          next_question_buttons = driver.find_elements(By.CLASS_NAME, "h5p-question-next")

          # Iterate over each 'Next question' button and click if it is visible
          for button in next_question_buttons:
              try:
                  if button.is_displayed():
                      button.click()
                      time.sleep(1)  # Wait for the next question to load
                      break
              except Exception as e:
                  print(f"Error clicking a 'Next question' button: {e}")

        elif question == 'SaaS…':
          print("found question 5")
          time.sleep(1)
          for choice in choice_elements:
            if choice.text.strip() == 'has often a subscription-based revenue model':
              print('Click choice:', choice.text.strip())
              choice.click()
              time.sleep(1)  # Wait for any potential animations or updates
          time.sleep(1)  # Wait for any potential animations or updates
          check_answers_buttons = driver.find_elements(By.CLASS_NAME, "h5p-question-check-answer")

          # Iterate over each 'Check the answers' button and click if it is visible
          for button in check_answers_buttons:
              try:
                  if button.is_displayed():
                      button.click()
                      time.sleep(1)  # Wait for any potential animations or updates
                      break
              except Exception as e:
                  print(f"Error clicking a 'Check the answers' button: {e}")

          # Find all 'Next question' buttons
          next_question_buttons = driver.find_elements(By.CLASS_NAME, "h5p-question-next")

          # Iterate over each 'Next question' button and click if it is visible
          for button in next_question_buttons:
              try:
                  if button.is_displayed():
                      button.click()
                      time.sleep(1)  # Wait for the next question to load
                      break
              except Exception as e:
                  print(f"Error clicking a 'Next question' button: {e}")

        elif question == 'Affiliate model…':
          print("found question 6")
          time.sleep(1)
          for choice in choice_elements:
            if choice.text.strip() == 'is about cooperation with other companies':
              print('Click choice:', choice.text.strip())
              choice.click()
              time.sleep(1)  # Wait for any potential animations or updates
            if choice.text.strip() == 'is typically about collection of commission for sales':
              print('Click choice:', choice.text.strip())
              choice.click()
              time.sleep(1)  # Wait for any potential animations or updates
            if choice.text.strip() == 'refers to broker-business':
              print('Click choice:', choice.text.strip())
              choice.click()
              time.sleep(1)
          time.sleep(1)  # Wait for any potential animations or updates
          check_answers_buttons = driver.find_elements(By.CLASS_NAME, "h5p-question-check-answer")

          # Iterate over each 'Check the answers' button and click if it is visible
          for button in check_answers_buttons:
              try:
                  if button.is_displayed():
                      button.click()
                      time.sleep(1)  # Wait for any potential animations or updates
                      break
              except Exception as e:
                  print(f"Error clicking a 'Check the answers' button: {e}")

          # Find all 'Next question' buttons
          next_question_buttons = driver.find_elements(By.CLASS_NAME, "h5p-question-next")

          # Iterate over each 'Next question' button and click if it is visible
          for button in next_question_buttons:
              try:
                  if button.is_displayed():
                      button.click()
                      time.sleep(1)  # Wait for the next question to load
                      break
              except Exception as e:
                  print(f"Error clicking a 'Next question' button: {e}")

        elif question == 'In direct data monetization approach…':
          print("found question 7")
          time.sleep(1)
          for choice in choice_elements:
            if choice.text.strip() == 'you sell the data':
              print('Click choice:', choice.text.strip())
              choice.click()
              time.sleep(1)  # Wait for any potential animations or updates
            if choice.text.strip() == 'you can productize data':
              print('Click choice:', choice.text.strip())
              choice.click()
              time.sleep(1)  # Wait for any potential animations or updates
            if choice.text.strip() == 'you can package and even bundle data':
              print('Click choice:', choice.text.strip())
              choice.click()
              time.sleep(1)
          time.sleep(1)  # Wait for any potential animations or updates
          check_answers_buttons = driver.find_elements(By.CLASS_NAME, "h5p-question-check-answer")

          # Iterate over each 'Check the answers' button and click if it is visible
          for button in check_answers_buttons:
              try:
                  if button.is_displayed():
                      button.click()
                      time.sleep(1)  # Wait for any potential animations or updates
                      break
              except Exception as e:
                  print(f"Error clicking a 'Check the answers' button: {e}")

          # Find all 'Next question' buttons
          next_question_buttons = driver.find_elements(By.CLASS_NAME, "h5p-question-next")

          # Iterate over each 'Next question' button and click if it is visible
          for button in next_question_buttons:
              try:
                  if button.is_displayed():
                      button.click()
                      time.sleep(1)  # Wait for the next question to load
                      break
              except Exception as e:
                  print(f"Error clicking a 'Next question' button: {e}")

        elif question == 'In data brokering…':
          print("found question 8")
          time.sleep(1)
          for choice in choice_elements:
            if choice.text.strip() == 'you can create revenues by selling licenses to data':
              print('Click choice:', choice.text.strip())
              choice.click()
              time.sleep(1)  # Wait for any potential animations or updates
            if choice.text.strip() == 'you aggregate data':
              print('Click choice:', choice.text.strip())
              choice.click()
              time.sleep(1)  # Wait for any potential animations or updates
            if choice.text.strip() == 'you can use APIs to collect data':
              print('Click choice:', choice.text.strip())
              choice.click()
              time.sleep(1)
          time.sleep(1)  # Wait for any potential animations or updates
          check_answers_buttons = driver.find_elements(By.CLASS_NAME, "h5p-question-check-answer")

          # Iterate over each 'Check the answers' button and click if it is visible
          for button in check_answers_buttons:
              try:
                  if button.is_displayed():
                      button.click()
                      time.sleep(1)  # Wait for any potential animations or updates
                      break
              except Exception as e:
                  print(f"Error clicking a 'Check the answers' button: {e}")

          # Find all 'Next question' buttons
          next_question_buttons = driver.find_elements(By.CLASS_NAME, "h5p-question-next")

          # Iterate over each 'Next question' button and click if it is visible
          for button in next_question_buttons:
              try:
                  if button.is_displayed():
                      button.click()
                      time.sleep(1)  # Wait for the next question to load
                      break
              except Exception as e:
                  print(f"Error clicking a 'Next question' button: {e}")

        elif question == 'In indirect monetization with data…':
          print("found question 9")
          time.sleep(1)
          for choice in choice_elements:
            if choice.text.strip() == 'Customers may pay for insights based on their own data':
              print('Click choice:', choice.text.strip())
              choice.click()
              time.sleep(1)  # Wait for any potential animations or updates
            if choice.text.strip() == 'you can make use of consulting approach based on data that you have collected and analyzed':
              print('Click choice:', choice.text.strip())
              choice.click()
              time.sleep(1)  # Wait for any potential animations or updates
            if choice.text.strip() == 'information-based services is a good approach':
              print('Click choice:', choice.text.strip())
              choice.click()
          time.sleep(1)  # Wait for any potential animations or updates
          check_answers_buttons = driver.find_elements(By.CLASS_NAME, "h5p-question-check-answer")

          # Iterate over each 'Check the answers' button and click if it is visible
          for button in check_answers_buttons:
              try:
                  if button.is_displayed():
                      button.click()
                      time.sleep(1)  # Wait for any potential animations or updates
                      break
              except Exception as e:
                  print(f"Error clicking a 'Check the answers' button: {e}")

          # Find all 'Next question' buttons
          next_question_buttons = driver.find_elements(By.CLASS_NAME, "h5p-question-next")

          # Iterate over each 'Next question' button and click if it is visible
          for button in next_question_buttons:
              try:
                  if button.is_displayed():
                      button.click()
                      time.sleep(1)  # Wait for the next question to load
                      break
              except Exception as e:
                  print(f"Error clicking a 'Next question' button: {e}")

        elif question == 'The following are well-known software pricing methods':
          print("found question 10")
          time.sleep(1)
          for choice in choice_elements:
            if choice.text.strip() == 'demand-driven pricing':
              print('Click choice:', choice.text.strip())
              choice.click()
              time.sleep(1)  # Wait for any potential animations or updates
            if choice.text.strip() == 'competition-based pricing':
              print('Click choice:', choice.text.strip())
              choice.click()
              time.sleep(1)  # Wait for any potential animations or updates
            if choice.text.strip() == 'Pay-per-use':
              print('Click choice:', choice.text.strip())
              choice.click()
              time.sleep(1)
          time.sleep(1)  # Wait for any potential animations or updates
          check_answers_buttons = driver.find_elements(By.CLASS_NAME, "h5p-question-check-answer")

          # Iterate over each 'Check the answers' button and click if it is visible
          for button in check_answers_buttons:
              try:
                  if button.is_displayed():
                      button.click()
                      time.sleep(1)  # Wait for any potential animations or updates
                      break
              except Exception as e:
                  print(f"Error clicking a 'Check the answers' button: {e}")

          # Find all 'Next question' buttons
          next_question_buttons = driver.find_elements(By.CLASS_NAME, "h5p-question-next")

          # Click the 'finish question' button
          next_question_button = driver.find_element(By.CLASS_NAME, "h5p-question-finish")
          next_question_button.click()
          time.sleep(1)  # Wait for the next question to load
        else:
           print("question not found")
           print(question)
            

      # Switch back to the default content
      driver.switch_to.default_content()

    except NoSuchElementException:
      print("Element not found")
      # Switch back to the default content in case of an exception
      driver.switch_to.default_content()
    time.sleep(10)
finally:
    # Close the browser
    driver.quit()
