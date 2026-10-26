from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Configure Chrome for GitHub Actions
options = webdriver.ChromeOptions()
options.add_argument("--headless=new")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--disable-gpu")
options.add_argument("--window-size=1920,1080")

# Start Chrome
driver = webdriver.Chrome(options=options)

try:
    # Open login page
    driver.get("http://127.0.0.1:5000/")

    wait = WebDriverWait(driver, 15)

    print("Student Login Page Opened")

    # Test 1: Correct username and password
    username = driver.find_element(By.ID, "username")
    password = driver.find_element(By.ID, "password")

    username.send_keys("student")
    password.send_keys("student123")

    driver.find_element(By.ID, "loginButton").click()

    result = wait.until(
        EC.visibility_of_element_located((By.ID, "message"))
    )

    assert result.text == "Login successful!"

    print("TEST 1 PASSED: Valid login successful")

    # Test 2: Incorrect password
    username.clear()
    password.clear()

    username.send_keys("student")
    password.send_keys("wrong123")

    driver.find_element(By.ID, "loginButton").click()

    result = wait.until(
        EC.text_to_be_present_in_element(
            (By.ID, "message"),
            "Invalid username or password!"
        )
    )

    assert result

    print("TEST 2 PASSED: Invalid login rejected")

    print("ALL SELENIUM TESTS PASSED!")

finally:
    driver.quit()