from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class OrderPage(BasePage):

  _PIZZA_ORDER_FORM_LOCATOR = (By.ID, "pizza_order_form")
  _QUANTITY_TO_ORDER = (By.ID, "quantity")
  _ADD_TO_CART_LOCATOR = (By.ID, 'submit_button')
  _ADDED_PIZZA_CART_MESSAGE_LOCATOR = (By.ID, 'added_message')

  def __init__(self, driver):
    super().__init__(driver)
    WebDriverWait(self.driver, 10).until(
        EC.presence_of_element_located(self._PIZZA_ORDER_FORM_LOCATOR)
    )

  
  @property
  def number_to_order(self):
    return self.driver.find_element(*self._QUANTITY_TO_ORDER)

  @property
  def add_to_cart_button(self):
    return self.driver.find_element(*self._ADD_TO_CART_LOCATOR)


  def place_pizza_order(self, order_notes):
    self.number_to_order.send_keys(order_notes['quantity'])
    self.add_to_cart_button.click()
    WebDriverWait(self.driver, 10).until(
        EC.visibility_of_element_located(self._PIZZA_ORDER_FORM_LOCATOR)
    )
    return True
