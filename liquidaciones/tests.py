from django.test import LiveServerTestCase
import factory
from contribuyentes.tests import ContribuyenteFactory,UserFactory
from contribuyentes.models import *
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
from selenium.webdriver.support.select import Select

def click_impuesto(ff,id):
    select=Select(ff.find_element_by_name('0-impuesto'))
    for opcion in select.options:
        if opcion.get_attribute('value')==str(id):
            index=opcion.get_attribute('index')
            break
    ff.find_element_by_xpath('//input[@class="default"][@type="text"]').click()
    opcion=ff.find_element_by_xpath('//li[@id="form_field_select_4_chzn_o_%s"]'%index)
    opcion.click()
    return opcion

class ActEconomicaTest(LiveServerTestCase):
    fixtures=['rubros.json','impuestos.json']

    @classmethod
    def setUpClass(cls):
        cls.selenium = WebDriver(firefox_binary=FirefoxBinary(firefox_path='/home/overflow/firefox/firefox-bin'))
        super(ActEconomicaTest, cls).setUpClass()

    @classmethod
    def tearDownClass(cls):
        cls.selenium.quit()
        super(ActEconomicaTest, cls).tearDownClass()
    def test_Estimada(self):
        contribuyente=ContribuyenteFactory()
        contribuyente.rubro.add(Rubro.objects.get(id=1)) 
        contribuyente.rubro.add(Rubro.objects.get(id=2)) 
        usuario=UserFactory()
        usuario.set_password('123')
        usuario.save()
        self.selenium.get('%s%s' % (self.live_server_url, '/contrib/crear_pago/'))
             
        username_input = self.selenium.find_element_by_name("username")
        username_input.send_keys(usuario.username)
        password_input = self.selenium.find_element_by_name("password")
        password_input.send_keys('123')
        #self.selenium.find_element_by_xpath('//button[@type="submit"]').click()
        password_input.submit()
        assert 'Buscar Contribuyentes'in self.selenium.title #Logueado
        self.selenium.get('%s%s' % (self.live_server_url, '/contrib/crear_pago/'))
        contrib_input = self.selenium.find_element_by_name("0-contrib")
        contrib_input.send_keys(contribuyente.id_contrato)
        try:

            seleccionar= WebDriverWait(self.selenium, 10).until(lambda s: s.find_element_by_xpath('//li[@data-value="1"]').is_displayed())

        #contrib_input.send_keys(Keys.RETURN)
        finally:
            self.selenium.find_element_by_xpath('//li[@data-value="1"]').click()

        opcion=click_impuesto(self.selenium,2) #Actividad economica
        opcion.submit()
        current_step=self.selenium.find_element_by_name('liquidacion_wizard-current_step')
        assert '1' in current_step.get_attribute('value')
        select=Select(self.selenium.find_element_by_name('1-tipo_liquidacion'))
        select.select_by_visible_text('Estimada')
        current_step.submit()
        import pdb
        pdb.set_trace()
         


    
