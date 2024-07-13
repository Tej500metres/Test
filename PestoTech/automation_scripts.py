# Import necessary libraries
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Initialize the WebDriver
driver = webdriver.Chrome(executable_path="/path/to/chromedriver")


# Test Case 1: User Registration
def test_user_registration():
    driver.get("http://ecommerce-website.com/register")
    driver.find_element(By.ID, "username").send_keys("testuser")
    driver.find_element(By.ID, "email").send_keys("testuser@example.com")
    driver.find_element(By.ID, "password").send_keys("password123")
    driver.find_element(By.ID, "confirm_password").send_keys("password123")
    driver.find_element(By.ID, "register").click()
    assert "Registration successful" in driver.page_source


# Test Case 2: Product Search
def test_product_search():
    driver.get("http://ecommerce-website.com")
    search_box = driver.find_element(By.NAME, "q")
    search_box.send_keys("laptop")
    search_box.send_keys(Keys.RETURN)
    assert "Search results for 'laptop'" in driver.page_source


# Test Case 3: Add Item to Cart
def test_add_to_cart():
    driver.get("http://ecommerce-website.com/product/1")
    driver.find_element(By.ID, "add_to_cart").click()
    driver.find_element(By.ID, "cart").click()
    assert "Product 1" in driver.page_source


# Execute the tests
test_user_registration()
test_product_search()
test_add_to_cart()

# Close the WebDriver
driver.quit()
