
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

URL = "http://127.0.0.1:8000"

# Step 1: Open Chrome
driver = webdriver.Chrome()

try:
    # Step 2: Maximize the browser window
    driver.maximize_window()

    # Step 3: Open the login page
    driver.get(URL)

    wait = WebDriverWait(driver, 10)

    # Step 4: Enter username
    username = wait.until(
        EC.visibility_of_element_located((By.ID, "username"))
    )
    username.send_keys("student")

    # Step 5: Enter password
    password = driver.find_element(By.ID, "password")
    password.send_keys("student123")

    # Step 6: Click the Login button
    login_button = driver.find_element(By.ID, "loginButton")
    login_button.click()

    # Step 7: Verify the success message
    message = wait.until(
        EC.visibility_of_element_located((By.ID, "message"))
    )

    assert message.text == "Login successful!", (
        f"Unexpected message: {message.text}"
    )

    print("TEST PASSED: Login successful!")
    print("Username: student")
    print("Expected message verified.")

    # Step 8: Keep Chrome open until you press Enter
    input("Press Enter to close the browser...")

except Exception as error:
    print("TEST FAILED:", error)
    input("Press Enter to close the browser...")

finally:
    # Step 9: Close Chrome
    driver.quit()
