from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.maximize_window()
driver.get("http://automationexercise.com")
print("Homepage is visbile successfully")
driver.find_element(By.XPATH,("//a[normalize-space()='Contact us']")).click()
print("GET IN TOUCH is visible")
driver.find_element(By.XPATH,("//input[@placeholder='Name']")).send_keys("Malavicka")
driver.find_element(By.XPATH,("//input[@placeholder='Email']")).send_keys("mala123@gmail.com")
driver.find_element(By.XPATH,("//input[@placeholder='Subject']")).send_keys("Adding a new file")
driver.find_element(By.XPATH,("//textarea[@id='message']")).send_keys("Uploaded a new file")
driver.find_element(By.XPATH,("//input[@name='upload_file']")).send_keys(r"C:\Users\Prade\python.txt")
driver.find_element(By.XPATH,("//input[@name='submit']")).click()
alert=driver.switch_to.alert
alert.accept()
print("Success! Your details have been submitted successfully")
driver.find_element(By.XPATH,("//a[normalize-space()='Home']")).click()
print("Landed to home page successfully")
