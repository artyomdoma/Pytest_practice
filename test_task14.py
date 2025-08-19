from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math

# функция для расчета формулы
def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

link = "http://suninjuly.github.io/explicit_wait2.html"
browser = webdriver.Chrome()

try:
    browser.get(link)
    price = WebDriverWait(browser, 10).until(
            EC.text_to_be_present_in_element((By.ID, "price"), '100'))
    message = browser.find_element(By.ID, "price")
    submit_btn = browser.find_element(By.ID, "book")
    submit_btn.click()
    x = WebDriverWait(browser, 1).until(
        EC.visibility_of_element_located((By.ID, "input_value"))
    ).text
    y = calc(x)
    answer_input = browser.find_element(By.CSS_SELECTOR, "input#answer")
    answer_input.send_keys(y)
    submit_btn = browser.find_element(By.ID, "solve")
    submit_btn.click()

finally:
    time.sleep(10)
    browser.quit()