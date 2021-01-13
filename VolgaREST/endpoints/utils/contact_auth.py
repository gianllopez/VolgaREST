from selenium.webdriver.support.expected_conditions import presence_of_element_located as appears
from selenium.common.exceptions import TimeoutException, ElementClickInterceptedException
from selenium.webdriver.support.wait import WebDriverWait as WaitFor
from rest_framework.exceptions import ValidationError
from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from django.core.mail import message, send_mail
from time import sleep as waitDOM
from django.conf import settings
from random import choices
from string import digits
from .constants import *

class ContactAuthentication:
   
   def __init__(self, credentials):
      options = ChromeOptions()
      exe = 'C:/Users/JOSE-LOPEZ/Documents/LUCAS (NO BORRAR)/VolgaREST/VolgaREST/endpoints/utils/chromedriver.exe'
      for x in ARGUMENTS:
         arg = f'--{x}' if ARGUMENTS.index(x) <= 3 else x
         options.add_argument(arg)
      self.driver = Chrome(executable_path=exe, options=options)
      self.credentials = credentials
      self.errors = {}
      self.codes = {}

   def destructure(self, data):
      return [x[1] for x in sorted(data.items())]
   
   def querySelector(self, selector, timeout=15):
      return WaitFor(driver=self.driver, timeout=timeout).until(appears((By.CSS_SELECTOR, selector)))

   def login(self, root, data):
      data['path'] = data.get('path', '/login')
      global session_cookie
      credentials, path, session_cookie, submit_btn = self.destructure(data)
      self.driver.get(root + path)
      for x in credentials:
         self.querySelector(x).send_keys(credentials[x])
      self.querySelector(submit_btn).click()
   
   def send_code(self, contact_config, user, authcode):
      login_data, message_data, root_url = self.destructure(contact_config)
      message_data['to'] = user
      self.login(root=root_url, data=login_data)
      while True:
         if self.driver.get_cookie(session_cookie):
            btns, to = self.destructure(message_data)
            waitDOM(0.5)
            self.driver.get(f'{root_url}/{to}')
            break
      btns['redirect-btn'] = btns.get('redirect-btn', 'div[aria-label="Mensaje"], div[aria-label="Message"]')
      follow_or_add, msg_entry, msg_redirect = self.destructure(btns)
      try:
         self.querySelector(follow_or_add, timeout=3).click()
      except TimeoutException:
         pass
      try:
         try:
            self.querySelector(msg_redirect).click()
         except ElementClickInterceptedException:
            pass
         self.querySelector(msg_entry).send_keys(CODE_MESSAGE(authcode), Keys.ENTER)
      except TimeoutException:
         account = ''
         for key, value in self.credentials.items():
            if value == user:
               account = key
         self.errors[account] = 'Esta cuenta no acepta mensajes directos, por ende no se puede autenticar.'

   def execute(self):
      for account, user in self.credentials.items():
         code = ''.join(choices(digits, k=6))
         if account != 'email':
            config = CONTACTS_CONSTANT[account]
            self.send_code(contact_config=config, user=user, authcode=code)
            self.codes[account] = code
         else:
            config = {
               'subject': 'Volga - Autenticación',
               'from_email': settings.EMAIL_HOST_USER,
               'recipient_list': [user],
               'message': CODE_MESSAGE(code)
            }
            send_mail(**config)
