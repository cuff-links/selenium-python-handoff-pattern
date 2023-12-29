from pages.login_page import LoginPage


def test_login_and_add_pizza_to_cart(driver):
  login_page = LoginPage(driver)
  order_page = login_page.login()
  assert order_page.place_pizza_order({'quantity': 1}) == True

