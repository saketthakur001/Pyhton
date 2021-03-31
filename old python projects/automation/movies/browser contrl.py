movie = input('Enter the name: ')
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from pyautogui import hotkey

r = 'C:\chromedriver.exe'
driver = webdriver.Chrome(r)

driver.get('https://moviesverse.in/')

search = driver.find_element_by_name('s')
search.send_keys(movie)
search.send_keys(Keys.RETURN)

try:
    element = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.ID, "ClickMovieSearch" or 'https://matswhyask.cam/p/XfJBk7l2hVc9jvv11ubg1gi25R3VdYEi73Rc_LxI_7ai8qCdQas4pV4QnU61H*dxPeA43fchKjPlH8_xBzL_kqK6CL9zHYaw2J_sn*ujHlPwfb1LdbuWTg13Fuan9oQePfadFgkD6luvITYNyregDxXDhWKyU_yAZVNxB4rASyxtX0TWxGSLYIjfqgIuHdcsT8Xo*ZgBRPYeRJpIVlhHzTjUBz3wwdzRt2nUwB83H2qyExW4ddds948dH1_zZJx2IfqCfUt54eZhVVWodVMLAcwrCGa0lcq1RUrxqjWjw8cyTfBhAOZHYw*TCgBfxobd'))
    )
finally:
    hotkey('ctrl','w')

try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'title front-view-title'))
    )
finally:
    hotkey('win','d')

