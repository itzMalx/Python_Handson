from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://automationexercise.com")
print(driver.title)
print("Homepage is successfuly visible")
driver.find_element(By.XPATH,("//a[normalize-space()='Signup / Login']")).click()
print("Login to your account")
driver.find_element(By.XPATH,("//input[@data-qa='login-email']")).send_keys("mala123@gmail.com")
driver.find_element(By.XPATH,("//input[@placeholder='Password']")).send_keys("098764")
driver.find_element(By.XPATH,("//button[normalize-space()='Login']")).click()
print("Your email or password is incorrect!")
driver.close()
