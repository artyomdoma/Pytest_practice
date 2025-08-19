from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

current_dir = os.path.abspath(os.path.dirname(__file__))
try:
    link = "https://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    input = browser.find_element(By.CSS_SELECTOR, "input.form-control[name='firstname']")
    input.send_keys("Ivan")
    input = browser.find_element(By.CSS_SELECTOR, "input.form-control[name='lastname']")
    input.send_keys("Petrov")
    input = browser.find_element(By.CSS_SELECTOR, "input.form-control[name='email']")
    input.send_keys("Petrov@mail.ru")
    element = browser.find_element(By.CSS_SELECTOR, "input#file")
    file_path = os.path.join(current_dir, 'file.txt')
    element.send_keys(file_path)
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()