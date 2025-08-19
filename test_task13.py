from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math
import time

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

link = "http://suninjuly.github.io/redirect_accept.html"
browser = webdriver.Chrome()

try:
    browser.get(link)

    browser.find_element(By.CSS_SELECTOR, "button.trollface").click()
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)
    x = WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "span#input_value"))
    ).text
    y = calc(x)
    answer_input = browser.find_element(By.CSS_SELECTOR, "input#answer")
    answer_input.send_keys(y)
    submit_btn = browser.find_element(By.CSS_SELECTOR, "button.btn")
    submit_btn.click()

finally:
    time.sleep(10)
    browser.quit()
