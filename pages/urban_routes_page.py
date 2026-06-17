from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from helpers import utilities
from selenium.webdriver.common.keys import Keys


"""
Paso 1. Localiza el elemento
Paso 2. Crear un metodo  getter.  def get_request_taxi_button(self):
        NOTA: Un getter seimpre retorna el elemento
Paso 3. Definir la accion que quiero y puedo hacer con el elemento 
        setter --> escribir --> Elementos input y text area
        clickers --> Dar Clikc --> Botones y links
        readers --> Leer --> Propiedades de los elementos get_property('value')

"""
class UrbanRoutesPage:
    from_field = (By.ID, 'from')
    to_field = (By.ID, 'to')
    request_taxi_button = (By.CSS_SELECTOR, '.button.round')
    comfort_tariff_icon = (By.XPATH, '//div[@class="tcard-title" and text()="Comfort"]')
    comfort_tariff_assert = (By.XPATH, '//div[@class="r-sw-label" and text()="Manta y pañuelos"]')
    phone_number_field = (By.XPATH, '//div[@class="np-text" and text()="Número de teléfono"]')
    phone_number_field_input =(By.ID, 'phone')
    next_button = (By.CSS_SELECTOR, '.button.full')
    sms_code_field = (By.ID, 'code')
    confirm_button = (By.XPATH, '//*[@id="root"]/div/div[1]/div[2]/div[2]/form/div[2]/button[1]')
    payment_method_button = (By.CSS_SELECTOR, '.pp-text')
    button_add_credit_card = (By.XPATH, '//div[text()="Agregar tarjeta"]')
    credit_card_number_field = (By.ID, 'number')
    credit_card_code_field = (By.CSS_SELECTOR, "#code.card-input")
    add_button_credit_card = (By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div[2]/form/div[3]/button[1]')
    close_button_add_credit_card = (By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div[1]/button')
    messages_driver_field = (By.CSS_SELECTOR, '#comment.input')
    request_manta_panuelos =  (By.XPATH, '//div[@class="switch"]/span')
    request_manta_panuelos_assert = (By.CLASS_NAME, 'switch-input')
    request_ice_cream = (By.XPATH, '//div[@class="counter-plus"]')
    counter_ice_cream = (By.CLASS_NAME, 'counter-value')
    request_for_travel = (By.XPATH, '//div[@class="smart-button-wrapper"]')
    order_tittle = (By.CSS_SELECTOR, '.order-header-title')
    name_driver = (By.XPATH, '//div[contains(text(),"driver.name.")]')

    def __init__(self, driver):
        self.driver = driver
        self.wait=WebDriverWait(self.driver, 5)
        self.wait_order=WebDriverWait(self.driver, 50)

    #Esté metodo escribe al campo from que está en la varibale de clase from_field, la dirección de origen
    def set_from(self, from_address):
        self.wait.until(EC.presence_of_element_located(self.from_field)).send_keys(from_address)

    # Esté metodo escribe al campo to que está en la variable to_fiel, la dirección de destino
    def set_to(self, to_address):
        self.wait.until(EC.presence_of_element_located(self.to_field)).send_keys(
            to_address)

    #Este metodo obtiene el valor que está escrito (get.property ve el DOM)
    def get_from(self):
        return self.driver.find_element(*self.from_field).get_property('value')

    # Este metodo obtiene el valor que está escrito (get.property ve el DOM)
    def get_to(self):
        return self.driver.find_element(*self.to_field).get_property('value')

    def set_route(self, address_from, address_to):
        self.set_from(address_from)
        self.set_to(address_to)

#Metodos para usar el boton pedir taxi
    def get_request_taxi_button(self):
        return self.wait.until(EC.element_to_be_clickable(self.request_taxi_button)
        )

    def click_request_taxi_button(self):
        self.get_request_taxi_button().click()

#Metodos para seleccionar el icono de tarifa comfort
    def get_comfort_tariff_icon(self):
        return self.wait.until(EC.element_to_be_clickable(self.comfort_tariff_icon)
        )

    def click_comfort_tariff_icon(self):
        self.get_comfort_tariff_icon().click()

    def get_comfort_tariff_assert(self):
        return self.wait.until(EC.presence_of_element_located(self.comfort_tariff_assert))

    def read_comfort_tariff_assert(self):
        return self.get_comfort_tariff_assert().text

#Metodos para agregar el numero de telefono
    def get_phone_number_field(self):
        return self.wait.until(EC.element_to_be_clickable(self.phone_number_field)
        )
    def click_phone_number_field(self):
        self.get_phone_number_field().click()

    def set_phone_number_field_input(self, number_input):
        self.wait.until(EC.element_to_be_clickable(self.phone_number_field_input)).send_keys(number_input)

    def get_assert_number_field(self):
        return self.wait.until(EC.element_to_be_clickable(self.phone_number_field_input)).get_attribute('value')

    def get_next_button(self):
        return self.wait.until(EC.element_to_be_clickable(self.next_button))

    def click_next_button(self):
        self.get_next_button().click()

    #Metodos para solicitar el codigo
    def get_sms_code_field(self):
        return self.wait.until(EC.visibility_of_element_located(self.sms_code_field))

    def get_code(self):
        code = utilities.retrieve_phone_code(self.driver)
        return code

    def set_phone_sms_code(self):
        self.get_sms_code_field().send_keys(self.get_code())

    def get_confirm_button(self):
        return self.wait.until(EC.element_to_be_clickable(self.confirm_button))

    def click_confirm_button(self):
        self.get_confirm_button().click()

#Metodos para agregar tarjeta de credito

    def get_payment_method_button(self):
        return self.wait.until(EC.element_to_be_clickable(self.payment_method_button))

    def click_payment_method_button(self):
        self.get_payment_method_button().click()

    def get_button_add_credit_card(self):
        return self.wait.until(EC.element_to_be_clickable(self.button_add_credit_card))

    def click_button_add_credit_card(self):
        self.get_button_add_credit_card().click()

    def get_credit_card_number_field(self):
        return self.wait.until(EC.visibility_of_element_located(self.credit_card_number_field))

    def set_credit_card_number_field(self, number_input):
        self.get_credit_card_number_field().send_keys(number_input)

    def get_assert_cc_number_field(self):
        return self.wait.until(EC.element_to_be_clickable(self.credit_card_number_field)).get_attribute('value')

    def get_credit_card_code_field(self):
        return self.wait.until(EC.visibility_of_element_located(self.credit_card_code_field))

    def set_credit_card_code_field(self, code_input):
        self.get_credit_card_code_field().send_keys(code_input)
        self.get_credit_card_code_field().send_keys(Keys.TAB)

    def get_add_button_credit_card(self):
        return self.wait.until(EC.element_to_be_clickable(self.add_button_credit_card))

    def get_assert_card_code_field(self):
        return self.wait.until(EC.element_to_be_clickable(self.credit_card_code_field)).get_attribute('value')

    def click_add_button_credit_card(self):
        self.get_add_button_credit_card().click()

    def get_close_button_add_credit_card(self):
        return self.wait.until(EC.element_to_be_clickable(self.close_button_add_credit_card))

    def click_close_button_add_credit_card(self):
        self.get_close_button_add_credit_card().click()

#Crear mensaje para conductor
    def get_messages_driver_field(self):
        return self.wait.until(EC.visibility_of_element_located(self.messages_driver_field))

    def set_messages_driver_field(self, message):
        self.get_messages_driver_field().send_keys(message)

    def get_assert_messages_driver_field(self):
        return self.wait.until(EC.element_to_be_clickable(self.messages_driver_field)).get_attribute('value')

#Pedir Manta y pañuelos
    def get_request_manta_panuelos(self):
        return self.wait.until(EC.element_to_be_clickable(self.request_manta_panuelos))

    def click_request_manta_panuelos(self):
        self.get_request_manta_panuelos().click()

    def get_assert_switch_button(self): #Crear un localizador nuevo para esta parte
        return self.wait.until(EC.element_located_selection_state_to_be(self.request_manta_panuelos_assert, True))

#Pedir 2 helados
    def get_request_ice_cream(self):
        return self.wait.until(EC.element_to_be_clickable(self.request_ice_cream))

    def click_request_ice_cream(self):
        self.get_request_ice_cream().click()
        self.get_request_ice_cream().click()

    def get_assert_ice_cream_request(self):
        return self.wait.until(EC.visibility_of_element_located(self.counter_ice_cream )).text

#Pedir el taxi
    def get_request_for_travel(self):
        return self.wait.until(EC.element_to_be_clickable(self.request_for_travel))

    def click_request_for_travel(self):
        self.get_request_for_travel().click()

# Esperar a que aparezca la informacion del conductor en el modal
    def get_order_tittle(self):
        return self.wait_order.until(EC.visibility_of_element_located(self.order_tittle))

    def get_driver_name_assert(self):
        return self.wait_order.until(EC.visibility_of_element_located(self.name_driver)).text
