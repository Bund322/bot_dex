from selenium import webdriver
import time
import cv2

from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


try:
    o = Options()
    o.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options=o)
    driver.get('https://map.dex.art/ru/try-demo?location=SpacAd')

    time.sleep(150)
    driver.save_screenshot('screenshot.png')

    # Загрузите скриншот
    screenshot = cv2.imread('screenshot.png')

    # Загрузите изображение кнопки, которую вы хотите найти
    button_image = cv2.imread('button.png')  # Замените на путь к изображению кнопки

    # Ищите кнопку на скриншоте
    result = cv2.matchTemplate(screenshot, button_image, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

    # Получите координаты кнопки
    button_x, button_y = max_loc

    current_x = button_x + 30
    current_y = button_y + 20

    print(current_x, current_y)

    actions = ActionChains(driver)
    actions.move_by_offset(current_x, current_y)
    actions.click()
    actions.perform()

    time.sleep(5)

    driver.save_screenshot('screenshot.png')
    # Загрузите скриншот
    screenshot = cv2.imread('screenshot.png')

    # Загрузите изображение кнопки, которую вы хотите найти
    button_image = cv2.imread('button1.png')  # Замените на путь к изображению кнопки

    # Ищите кнопку на скриншоте
    result = cv2.matchTemplate(screenshot, button_image, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

    # Получите координаты кнопки
    button_x, button_y = max_loc

    current_x = button_x - current_x + 30
    current_y = button_y - current_y + 20

    print(current_x, current_y)

    actions = ActionChains(driver)
    actions.move_by_offset(current_x, current_y)
    actions.click()
    actions.perform()

    time.sleep(2)
    # Введите текст в поле
    actions = ActionChains(driver)
    input_text = 'Person'
    actions.send_keys(input_text)
    actions.perform()

    time.sleep(2)

    button_image = cv2.imread('button2.png')  # Замените на путь к изображению кнопки

    # Ищите кнопку на скриншоте
    result = cv2.matchTemplate(screenshot, button_image, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

    # Получите координаты кнопки
    button_x, button_y = max_loc

    current_x = button_x - current_x
    current_y = button_y - current_y

    print(current_x, current_y)

    actions = ActionChains(driver)
    actions.move_by_offset(current_x, current_y)
    actions.click()
    actions.perform()


finally:
    time.sleep(2)
    driver.quit()