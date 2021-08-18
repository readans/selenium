# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class TestCargarservicios():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_cargarservicios(self):
    # Test name: cargar servicios
    # Step # | name | target | value
    # 1 | open | https://dev.keepworking.online/ | 
    self.driver.get("https://dev.keepworking.online/")
    # 2 | setWindowSize | 1376x744 | 
    self.driver.set_window_size(1376, 744)
    # 3 | runScript | window.scrollTo(0,969) | 
    self.driver.execute_script("window.scrollTo(0,969)")
    # 4 | assertElementPresent | css=.is-custom-content-card:nth-child(6) .card-row-profile | 
    elements = self.driver.find_elements(By.CSS_SELECTOR, ".is-custom-content-card:nth-child(6) .card-row-profile")
    assert len(elements) > 0
    # 5 | waitForElementPresent | css=.is-custom-content-card:nth-child(6) .card-row-profile | 30000
    WebDriverWait(self.driver, 30000).until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, ".is-custom-content-card:nth-child(6) .card-row-profile")))
    # 6 | runScript | window.scrollTo(0,1594) | 
    self.driver.execute_script("window.scrollTo(0,1594)")
    # 7 | runScript | window.scrollTo(0,2910) | 
    self.driver.execute_script("window.scrollTo(0,2910)")
    # 8 | runScript | window.scrollTo(0,3302) | 
    self.driver.execute_script("window.scrollTo(0,3302)")


test = TestCargarservicios()
test.setup_method(False)
test.test_cargarservicios()