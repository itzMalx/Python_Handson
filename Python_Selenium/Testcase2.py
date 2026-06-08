from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://automationexercise.com")
print(driver.title)
print("Homepage is successfully visible")
driver.find_element(By.XPATH,"//a[normalize-space()='Signup / Login']").click()
print("Signup/Login page is visible")
driver.find_element( By.XPATH, "//input[@data-qa='login-email']").send_keys("zxcv12@gmail.com")
driver.find_element( By.XPATH,"//input[@placeholder='Password']").send_keys("mala123")
driver.find_element( By.XPATH,"//button[normalize-space()='Login']").click()
loggedin = driver.find_element( By.XPATH, "//a[contains(text(),'Logged in as')]")
print(loggedin.text)
driver.find_element(By.XPATH,"//a[normalize-space()='Delete Account']").click()
print("Account Deleted page is visible")
driver.quit()