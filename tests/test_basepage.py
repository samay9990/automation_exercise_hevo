import time

from pageobject.basepage import BasePage
from configutils import ConfigUtils


def test_navigate_to_url():
    basepage = BasePage()
    config = ConfigUtils()
    default_user_email = config.get_username()
    basepage.navigate_to_url()
    basepage.sign_in()
    time.sleep(5)

    
