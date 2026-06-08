from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://automationexercise.com")
print("Homepage is sucessfully visible")
driver.find_element(By.XPATH,("//a[normalize-space()='Signup / Login']")).click()
print("New User Signup is visible")
driver.find_element(By.XPATH,("//input[@placeholder='Name']")).send_keys("admin")
driver.find_element(By.XPATH,("//input[@data-qa='signup-email']")).send_keys("admin123@gmail.com")
driver.find_element(By.XPATH,("//button[normalize-space()='Signup']")).click()
print("Error message: Email Address already exist!")
driver.close()