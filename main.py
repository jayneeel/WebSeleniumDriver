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


def open_from_so():
    action.key_down(Keys.CONTROL).perform()
    time.sleep(1)
    from_so_btn = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH,
                                                                              '/html/body/app/main/pages/div/div['
                                                                              '2]/div/sales/addsales-invoice/div['
                                                                              '1]/div['
                                                                              '3]/voucher-master-action/button[2]')))
    from_so_btn.click()
    time.sleep(1)
    action.key_up(Keys.CONTROL).perform()


try:
    sales_invoice_link = WebDriverWait(driver, 20).until(EC.element_to_be_clickable(
        (By.XPATH, '/html/body/app/main/pages/div/div[2]/div/dashboard/div/div/div[2]/div[1]/div[6]/a')))
    sales_invoice_link.click()
    time.sleep(1)
    action = ActionChains(driver)
    open_from_so()

    invoice_table = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH,
                                                                                '/html/body/app/main/pages/div/div['
                                                                                '2]/div/sales/addsales-invoice/div['
                                                                                '1]/div[3]/generic-popup-grid['
                                                                                '1]/div/div/div/div/div[1]/div['
                                                                                '3]/table/tbody')))

    # Get all td elements within the table
    tr_elements = invoice_table.find_elements(By.TAG_NAME, "tr")

    # Iterate through each td element and double-click on it
    for i in range(len(tr_elements)):
        action = ActionChains(driver)
        top_invoice = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,
                                                                                  '/html/body/app/main/pages/div/div['
                                                                                  '2]/div/sales/addsales-invoice/div['
                                                                                  '1]/div[3]/generic-popup-grid['
                                                                                  '1]/div/div/div/div/div[1]/div['
                                                                                  '3]/table/tbody/tr[1]')))
        action.double_click(top_invoice).perform()
        print("DOUBLE CLICK")
        time.sleep(1)

        saveButton = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH,
                                                                                 '/html/body/app/main/pages/div/div['
                                                                                 '2]/div/sales/addsales-invoice/div['
                                                                                 '1]/div['
                                                                                 '3]/voucher-master-action/button[6]')))
        saveButton.click()
        time.sleep(1)
        action.key_down(Keys.ESCAPE).perform()
        open_from_so()


except Exception as e:
    print(f'Sales Invoice link is not clickable or not found {e}')
