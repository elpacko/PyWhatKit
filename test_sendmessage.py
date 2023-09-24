import os

from pywhatkit import whats
def test_send_message():
    session_driver = whats.initialize_driver(f"{os.getenv('LOCALAPPDATA')}\\Google\\Chrome\\User Data", "Profile 0")
    if session_driver:
        whats.sendwhatmsg_using_selenium(session_driver, "+", "Sending message trough Selenium:\n Message #1")
        whats.sendwhatmsg_using_selenium(session_driver, "+", "Sending message trough Selenium:\n Message #2")

if __name__ == "__main__":
    test_send_message()