import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

service = Service(executable_path=ChromeDriverManager().install())
options = webdriver.ChromeOptions()

driver = webdriver.Chrome(service=service, options=options)
# Open the main URL
main_url = 'http://124608.sahakari.patanjaliayurved.org/#/login;logout=logout'  # Replace with the actual main URL
driver.get(main_url)
wait = WebDriverWait(driver, 50)
driver.implicitly_wait(40)

username_input = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, 'inputEmail3')))
password_input = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, 'inputPassword3')))
login_button = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CLASS_NAME, 'submit')))

username_input.send_keys('admin')
password_input.send_keys('654321')
login_button.click()
print("*** Auth Successful *******")

time.sleep(2)

try:
    sales_invoice_link = WebDriverWait(driver, 20).until(EC.element_to_be_clickable(
        (By.XPATH, '/html/body/app/main/pages/div/div[2]/div/dashboard/div/div/div[2]/div[1]/div[6]/a')))
    sales_invoice_link.click()
    time.sleep(2)
    print('Clicked on Sales Invoice link')
    action = ActionChains(driver)

    action.key_down(Keys.CONTROL).perform()
    time.sleep(2)

    from_so_btn = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH,
                                                                              '/html/body/app/main/pages/div/div['
                                                                              '2]/div/sales/addsales-invoice/div['
                                                                              '1]/div['
                                                                              '3]/voucher-master-action/button[2]')))

    from_so_btn.click()
    time.sleep(2)

    action.key_up(Keys.CONTROL).perform()
except Exception as e:
    print(f'Sales Invoice link is not clickable or not found {e}')

# -----------------------------------------------------------------------------------------------------
