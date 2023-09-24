import os
import time
import webbrowser as web
from datetime import datetime
from re import fullmatch
from typing import List
from urllib.parse import quote
import paperclip
import pyautogui as pg
import pyperclip
import keyboard
from pywhatkit.core import core, exceptions, log
from typing import Union
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time
import logging

pg.FAILSAFE = False

core.check_connection()
logging.basicConfig(
    format='%(asctime)s %(levelname)-8s %(message)s',
    level=logging.INFO,
    datefmt='%Y-%m-%d %H:%M:%S')

def __init__(self):
    session_driver = None

def get_element_by_xpath(driver, xpath):
    try:
        return driver.find_element(By.XPATH, xpath)
    except:
        return None

def initialize_driver(user_data_dir: str, profile_directory: str):
    logging.info('Initializing driver')
    chrome_options = webdriver.ChromeOptions()
    # chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument("--remote-debugging-port=9222")  # this

    # chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_argument(f"--user-data-dir={user_data_dir}")
    chrome_options.add_argument(f"--profile-directory={profile_directory}")
    driver = webdriver.Chrome(options=chrome_options)
    driver.get('https://web.whatsapp.com/')
    time.sleep(15)
    try:
        new_chat_span_xpath = "//span[@data-icon='new-chat']"
        if not driver.find_elements(By.XPATH, new_chat_span_xpath):
            logging.warning('Not logged in')
            logging.info("Waiting for QR code scan or until timeout in 50 seconds")
            WebDriverWait(driver,50).until(lambda driver: driver.find_element(By.XPATH, "//span[@data-icon='new-chat']"))

    except Exception as e:
        logging.ERROR(f"Exception occured {e}")
        driver.quit()
        return None
    return driver

def sendwhatmsg_using_selenium(session_driver: webdriver, phone_no: str, message: str):
    try:
        
        new_chat_element = get_element_by_xpath(session_driver, "//span[@data-icon='new-chat']")
        new_chat_element.click()
        time.sleep(2)
        number_textbox = get_element_by_xpath(session_driver, "//div[@title='Search input textbox']")
        number_textbox.click()
        number_textbox.send_keys(phone_no)
        time.sleep(3)
        contact_element = get_element_by_xpath(session_driver, "//div[@class='_3YS_f _2A1R8']/div[2]")
        contact_element.click()
        time.sleep(2)
        inp_xpath = '//div[@title="Type a message"]'
        input_box = session_driver.find_element(By.XPATH,inp_xpath)
        time.sleep(2)
        input_box.send_keys(message + Keys.ENTER)
        time.sleep(2)
    except Exception as e:
        logging.ERROR(f"Exception occured {e}")
    

def sendwhatmsg_instantly(
        phone_no: str,
        message: str,
        wait_time: int = 15,
        tab_close: bool = False,
        close_time: int = 3,
) -> None:
    """Send WhatsApp Message Instantly"""

    if not core.check_number(number=phone_no):
        raise exceptions.CountryCodeException("Country Code Missing in Phone Number!")

    phone_no = phone_no.replace(" ", "")
    if not fullmatch(r"^\+?[0-9]{2,4}\s?[0-9]{9,15}", phone_no):
        raise exceptions.InvalidPhoneNumber("Invalid Phone Number.")

    web.open(f"https://web.whatsapp.com/send?phone={phone_no}")
    time.sleep(wait_time)
    index = 0
    length = len(message)
    while index < length:
        letter = message[index]
        pg.write(letter)
        if letter == ":":
            index += 1
            while index < length:
                letter = message[index]
                if letter == ":":
                    pg.press("enter")
                    break
                pg.write(letter)
                index += 1
        index += 1
    pg.press("enter")
    log.log_message(_time=time.localtime(), receiver=phone_no, message=message)
    if tab_close:
        core.close_tab(wait_time=close_time)


def sendimg_or_video_immediately(
        phone_no: str,
        path: str,
        wait_time: int = 15,
        tab_close: bool = False,
        close_time: int = 3,
) -> None:
    """Send WhatsApp Message Instantly"""

    if not core.check_number(number=phone_no):
        raise exceptions.CountryCodeException("Country Code Missing in Phone Number!")

    phone_no = phone_no.replace(" ", "")
    if not fullmatch(r"^\+?[0-9]{2,4}\s?[0-9]{9,15}", phone_no):
        raise exceptions.InvalidPhoneNumber("Invalid Phone Number.")

    web.open(f"https://web.whatsapp.com/send?phone={phone_no}")
    time.sleep(wait_time)
    core.find_link()
    time.sleep(1)
    core.find_photo_or_video()

    pyperclip.copy(os.path.abspath(path))
    print("Copied")
    time.sleep(1)
    keyboard.press("ctrl")
    keyboard.press("v")
    keyboard.release("v")
    keyboard.release("ctrl")
    time.sleep(1)
    keyboard.press("enter")
    keyboard.release("enter")
    time.sleep(1)
    keyboard.press("enter")
    keyboard.release("enter")
    if tab_close:
        core.close_tab(wait_time=close_time)


def sendwhatdoc_immediately(
        phone_no: str,
        path: str,
        wait_time: int = 15,
        tab_close: bool = True,
        close_time: int = 3,
) -> None:
    """Send WhatsApp Message Instantly"""

    if not core.check_number(number=phone_no):
        raise exceptions.CountryCodeException("Country Code Missing in Phone Number!")

    phone_no = phone_no.replace(" ", "")
    if not fullmatch(r"^\+?[0-9]{2,4}\s?[0-9]{9,15}", phone_no):
        raise exceptions.InvalidPhoneNumber("Invalid Phone Number.")

    web.open(f"https://web.whatsapp.com/send?phone={phone_no}")
    time.sleep(wait_time)
    core.find_link()
    time.sleep(1)
    core.find_document()
    pyperclip.copy(os.path.abspath(path))
    print("Copied")
    time.sleep(1)
    keyboard.press("ctrl")
    keyboard.press("v")
    keyboard.release("v")
    keyboard.release("ctrl")
    time.sleep(1)
    keyboard.press("enter")
    keyboard.release("enter")
    time.sleep(1)
    keyboard.press("enter")
    keyboard.release("enter")
    if tab_close:
        core.close_tab(wait_time=close_time)


def sendwhatmsg(
        phone_no: str,
        message: Union[list, str],
        time_hour: int,
        time_min: int,
        wait_time: int = 15,
        tab_close: bool = False,
        close_time: int = 3,
) -> None:
    """Send a WhatsApp Message at a Certain Time"""
    if not core.check_number(number=phone_no):
        raise exceptions.CountryCodeException("Country Code Missing in Phone Number!")

    phone_no = phone_no.replace(" ", "")
    if not fullmatch(r'^\+?[0-9]{2,4}\s?[0-9]{9,15}', phone_no):
        raise exceptions.InvalidPhoneNumber("Invalid Phone Number.")

    if time_hour not in range(25) or time_min not in range(60):
        raise Warning("Invalid Time Format!")

    current_time = time.localtime()
    left_time = datetime.strptime(
        f"{time_hour}:{time_min}:0", "%H:%M:%S"
    ) - datetime.strptime(
        f"{current_time.tm_hour}:{current_time.tm_min}:{current_time.tm_sec}",
        "%H:%M:%S",
    )

    if left_time.seconds < wait_time:
        raise exceptions.CallTimeException(
            "Call Time must be Greater than Wait Time as WhatsApp Web takes some Time to Load!"
        )

    sleep_time = left_time.seconds - wait_time
    print(
        f"In {sleep_time} Seconds WhatsApp will open and after {wait_time} Seconds Message will be Delivered!"
    )
    time.sleep(sleep_time)
    if isinstance(message, list):
        core.send_message_list(message=message, receiver=phone_no, wait_time=wait_time)
    else:
        core.send_message(message=message, receiver=phone_no, wait_time=wait_time)
        log.log_message(_time=current_time, receiver=phone_no, message=message)

    if tab_close:
        core.close_tab(wait_time=close_time)


def sendwhatmsg_to_group(
        group_id: str,
        message: str,
        time_hour: int,
        time_min: int,
        wait_time: int = 15,
        tab_close: bool = False,
        close_time: int = 3,
) -> None:
    """Send WhatsApp Message to a Group at a Certain Time"""

    if time_hour not in range(25) or time_min not in range(60):
        raise Warning("Invalid Time Format!")

    current_time = time.localtime()
    left_time = datetime.strptime(
        f"{time_hour}:{time_min}:0", "%H:%M:%S"
    ) - datetime.strptime(
        f"{current_time.tm_hour}:{current_time.tm_min}:{current_time.tm_sec}",
        "%H:%M:%S",
    )

    if left_time.seconds < wait_time:
        raise exceptions.CallTimeException(
            "Call Time must be Greater than Wait Time as WhatsApp Web takes some Time to Load!"
        )

    sleep_time = left_time.seconds - wait_time
    print(
        f"In {sleep_time} Seconds WhatsApp will open and after {wait_time} Seconds Message will be Delivered!"
    )
    time.sleep(sleep_time)
    core.send_message(message=message, receiver=group_id, wait_time=wait_time)
    log.log_message(_time=current_time, receiver=group_id, message=message)
    if tab_close:
        core.close_tab(wait_time=close_time)


def sendwhatmsg_to_group_instantly(
        group_id: str,
        message: str,
        wait_time: int = 15,
        tab_close: bool = False,
        close_time: int = 3,
) -> None:
    """Send WhatsApp Message to a Group Instantly"""

    current_time = time.localtime()
    time.sleep(4)
    core.send_message(message=message, receiver=group_id, wait_time=wait_time)
    log.log_message(_time=current_time, receiver=group_id, message=message)
    if tab_close:
        core.close_tab(wait_time=close_time)


def sendwhatsmsg_to_all(
        phone_nos: List[str],
        message: str,
        time_hour: int,
        time_min: int,
        wait_time: int = 15,
        tab_close: bool = False,
        close_time: int = 3,
):
    for phone_no in phone_nos:
        sendwhatmsg(
            phone_no, message, time_hour, time_min, wait_time, tab_close, close_time
        )


def sendwhats_image(
        receiver: str,
        img_path: str,
        time_hour: int,
        time_min: int,
        caption: str = "",
        wait_time: int = 15,
        tab_close: bool = False,
        close_time: int = 3,
) -> None:
    """Send Image to a WhatsApp Contact or Group at a Certain Time"""

    if (not receiver.isalnum()) and (not core.check_number(number=receiver)):
        raise exceptions.CountryCodeException("Country Code Missing in Phone Number!")

    current_time = time.localtime()
    left_time = datetime.strptime(
        f"{time_hour}:{time_min}:0", "%H:%M:%S"
    ) - datetime.strptime(
        f"{current_time.tm_hour}:{current_time.tm_min}:{current_time.tm_sec}",
        "%H:%M:%S",
    )

    if left_time.seconds < wait_time:
        raise exceptions.CallTimeException(
            "Call Time must be Greater than Wait Time as WhatsApp Web takes some Time to Load!"
        )

    sleep_time = left_time.seconds - wait_time
    print(
        f"In {sleep_time} Seconds WhatsApp will open and after {wait_time} Seconds Image will be Delivered!"
    )
    time.sleep(sleep_time)
    core.send_image(
        path=img_path, caption=caption, receiver=receiver, wait_time=wait_time
    )
    log.log_image(_time=current_time, path=img_path, receiver=receiver, caption=caption)
    if tab_close:
        core.close_tab(wait_time=close_time)


def open_web() -> bool:
    """Opens WhatsApp Web"""

    try:
        web.open("https://web.whatsapp.com")
    except web.Error:
        return False
    else:
        return True
