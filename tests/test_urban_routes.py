from email import message

from data import data
from pages.urban_routes_page import UrbanRoutesPage
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service


class TestUrbanRoutes:

    driver = None

    @classmethod #Se usan antes de un método setup
    #cls indica que todo lo que tenga cls pueda ser usado en cualquier método dentro de la clase.
    def setup_class(cls):
        options = Options()
        options.set_capability("goog:loggingPrefs", {'performance':'ALL'})
        cls.driver = webdriver.Chrome(service=Service(), options=options)
        cls.driver.get(data.urban_routes_url)
        cls.routes_page = UrbanRoutesPage(cls.driver)

    def test_set_route(self):
        address_from = data.address_from
        address_to = data.address_to
        self.routes_page.set_route(address_from, address_to)
        assert self.routes_page.get_from() == address_from
        assert self.routes_page.get_to() == address_to

    def test_select_comfort_tariff(self):
        self.routes_page.click_request_taxi_button()
        self.routes_page.click_comfort_tariff_icon()
        assert self.routes_page.read_comfort_tariff_assert() == "Manta y pañuelos"

    def test_phone_number_field(self):
        phone_number = data.phone_number
        self.routes_page.click_phone_number_field()
        self.routes_page.set_phone_number_field_input(phone_number)
        assert self.routes_page.get_assert_number_field() == phone_number
        self.routes_page.click_next_button()
        self.routes_page.set_phone_sms_code()
        self.routes_page.click_confirm_button()

    def test_add_credit_card(self):
        card_number = data.card_number
        ccv_code = data.card_code
        self.routes_page.click_payment_method_button()
        self.routes_page.click_button_add_credit_card()
        self.routes_page.set_credit_card_number_field(card_number)
        assert self.routes_page.get_assert_cc_number_field() == card_number
        self.routes_page.set_credit_card_code_field(ccv_code)
        assert self.routes_page.get_assert_card_code_field() == ccv_code
        self.routes_page.click_add_button_credit_card()
        self.routes_page.click_close_button_add_credit_card()

    def test_message_driver_field(self):
        message_driver = data.message_for_driver
        self.routes_page.set_messages_driver_field(message_driver)
        assert self.routes_page.get_assert_messages_driver_field() == message_driver

    def test_request_manta_panuelos(self):
        self.routes_page.click_request_manta_panuelos()
        assert self.routes_page.get_assert_switch_button() == True

    def test_request_ice_cream(self):
        self.routes_page.click_request_ice_cream()
        assert self.routes_page.get_assert_ice_cream_request() == '2'

    def test_request_for_travel(self):
        self.routes_page.click_request_for_travel()

    def test_wait_info_driver(self):
       self.routes_page.get_order_tittle()
       driver_name = self.routes_page.get_driver_name_assert()
       assert 'driver.name.' in driver_name

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
