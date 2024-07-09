from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

def test_login_success(driver):
    username = driver.find_element(By.NAME, 'user-name') # localiza campo user
    username.send_keys('standard_user') # preenche user correto

    password = driver.find_element(By.NAME, 'password') # localiza campo senha
    password.send_keys('secret_sauce') # preenche senha correta
    password.send_keys(Keys.RETURN) # dá enter

    driver.implicitly_wait(10)
    expected_url = 'https://www.saucedemo.com/inventory.html' # verifica se a URL atual é a URL esperada após o login
    current_url = driver.current_url
    assert current_url == expected_url, f"Expected URL to be {expected_url} but got {current_url}"

def test_login_failure_user_lockedout(driver):
    username = driver.find_element(By.NAME, 'user-name') # localiza campo user
    username.send_keys('locked_out_user') # preenche user bloqueado

    password = driver.find_element(By.NAME, 'password') # localiza campo senha
    password.send_keys('secret_sauce') # preenche senha correta
    password.send_keys(Keys.RETURN) # dá enter

    driver.implicitly_wait(10)
    error_message = driver.find_element(By.XPATH, '//*[@id="login_button_container"]/div/form/div[3]/h3').text
    assert error_message == "Epic sadface: Sorry, this user has been locked out."

def test_login_failure_user_unknown(driver):
    username = driver.find_element(By.NAME, 'user-name') # localiza campo user
    username.send_keys('standard_user001') # preenche user bloqueado

    password = driver.find_element(By.NAME, 'password') # localiza campo senha
    password.send_keys('secret_sauce') # preenche senha correta
    password.send_keys(Keys.RETURN) # dá enter

    driver.implicitly_wait(10)
    error_message = driver.find_element(By.XPATH, '//*[@id="login_button_container"]/div/form/div[3]/h3').text
    assert error_message == "Epic sadface: Username and password do not match any user in this service"