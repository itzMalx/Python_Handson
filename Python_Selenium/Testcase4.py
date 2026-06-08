from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://automationexercise.com")
print(driver.title)
print("Homepage is sucessfully displayed")
driver.find_element(By.XPATH,("//a[normalize-space()='Signup / Login']")).click()
driver.find_element(By.XPATH,("//input[@data-qa='login-email']")).send_keys("zxcv12@gmail.com")
driver.find_element(By.XPATH,("//input[@placeholder='Password']")).send_keys("mala123")
driver.find_element(By.XPATH,("//button[normalize-space()='Login']")).click()
print("Logged in as username is visible")
driver.find_element(By.XPATH,("//a[normalize-space()='Logout']")).click()
print("User is navigated to homepage")
driver.close()