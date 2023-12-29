from pages.base_page import BasePage
from pages.order_page import OrderPage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage(BasePage):

  _USERNAME_TEXTBOX_LOCATOR = (By.ID, "user")
  _PASSWORD_TEXTBOX_LOCATOR = (By.ID, 'password')
  _LOGIN_BUTTON_LOCATOR = (By.ID, 'login')

  def __init__(self, driver) -> None:
    self.url = 'https://play1.automationcamp.ir/login.html'
    super().__init__(driver)
    self.navigate_to()
    WebDriverWait(self.driver, 10).until(
      EC.presence_of_element_located(self._USERNAME_TEXTBOX_LOCATOR)
      )

  def navigate_to(self) -> None:
    super()._navigate(self.url)
    

  @property
  def username_field(self):
    return self.driver.find_element(*self._USERNAME_TEXTBOX_LOCATOR)
  
  @property
  def password_field(self):
    return self.driver.find_element(*self._PASSWORD_TEXTBOX_LOCATOR)
  
  @property
  def login_button(self):
    return self.driver.find_element(*self._LOGIN_BUTTON_LOCATOR)

  def login(self, user='admin', password='admin') -> OrderPage:
    self.username_field.send_keys(user)
    self.password_field.send_keys(password)
    self.login_button.click()
    return OrderPage(self.driver)