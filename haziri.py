#!/usr/bin/env python
#author: @karngyan

from selenium import webdriver
import sys
from selenium.webdriver.firefox.options import Options
from time import sleep


def Haziri(username, password):
  opts = Options()
  opts.headless = True

  browser = webdriver.Firefox(options = opts)
  # browser = webdriver.Chrome(options = opts)
  browser.get(r"http://115.114.127.54:8080/psp/bitcsprd/EMPLOYEE/HRMS/")

  # sleep(5)
  ########################################################################## Login Start
  search_form_password = None
  search_form_username = None
  while search_form_password == None or search_form_username == None:
      search_form_username = browser.find_element_by_id('userid')
      search_form_password = browser.find_element_by_id('pwd')
  search_form_username.send_keys(username)
  search_form_password.send_keys(password)


  search_form_submit = browser.find_element_by_name('Submit')
  search_form_submit.click()

  try:
    invalid_cred = browser.find_element_by_id('login_error')
    return [{'status' : 'invalid credentials'}]
  except:
    a=1
  ########################################################################## Login End


  browser.get(r'http://115.114.127.54:8080/psp/bitcsprd/EMPLOYEE/HRMS/c/SA_LEARNER_SERVICES.SSS_STUDENT_CENTER.GBL?Page=SSS_STUDENT_CENTER')


  browser.switch_to.frame(browser.find_element_by_name('TargetContent'))#Fucker Dimaag ka dahi kr diya tha iframe ne
  attendance_btn = browser.find_element_by_id('DERIVED_SSS_SCR_SSS_LINK_ANCHOR7')
  attendance_btn.click()
  sleep(20)
  radio_btn = browser.find_element_by_css_selector("input[type='radio'][value='0']")
  radio_btn.click()
  continue_btn = browser.find_element_by_class_name('SSSBUTTON_CONFIRMLINK')
  continue_btn.click()
  sleep(10)
  table = browser.find_element_by_class_name('PSLEVEL2GRIDWBO')
  table = table.text.split('View')
  # for row in table:
  #   print(row)
  browser.quit()
  return table
