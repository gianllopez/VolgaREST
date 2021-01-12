ARGUMENTS = [
   'headless',
   'disable-dev-shm-usage',
   'disable-notifications',
   'no-sandbox',
   'user-agent=Chrome/87.0.4280.141',
   'log-level=3'
]

INSTAGRAM = {
   'root-url': 'https://www.instagram.com',
   'login': {
      'path': '/accounts/login',
      'form': {
         'input[name="username"]': 'gianlop3z',
         'input[name="password"]': 'al capone'
      },
      'submit-btn': '#loginForm button.sqdOP.L3NKy.y3zKF',
      'session-cookie': 'sessionid'
   },
   'message': {
      # 'to': 'gianlop3z', / This must be added in contact function.
      'DOM-to-use': {
         'follow-btn': 'div.Igw0E.IwRSH.eGOV_.ybXk5._4EzTm button',
         'redirect-btn': 'div._862NM button',
         'message-input': 'div.Igw0E.IwRSH.eGOV_.vwCYk.ItkAi > textarea'
      }
   }
}

FACEBOOK = {
   'root-url': 'https://www.facebook.com',
   'login': {
      'form': {
         'input[name="email"]': 'lopezarizagianlucas@gmail.com',
         'input[name="pass"]': 'megazepol04'
      },
      'submit-btn': '#loginbutton',
      'session-cookie': 'c_user'
   },
   'message': {
      # 'to': 'therealgoat01', / This must be added in contact function.
      'DOM-to-use': {
         'add-btn': '.bp9cbjyn.j83agx80.fop5sh7t div[aria-label="Add Friend"]',
         'message-input': 'div[data-pagelet="ChatTab"] div._1mf._1mj'
      }
   }
}

TWITTER = {
   'root-url': 'https://twitter.com',
   'login': {
      'form': {
         'input[name="session[username_or_email]"].r-30o5oe': 'gianlop3z',
         'input[name="session[password]"].r-30o5oe': 'megazepol'
      },
      'submit-btn': 'div[data-testid="LoginForm_Login_Button"]',
      'session-cookie': 'auth_token'
   },
   'message': {
      # 'to': 'gianlop3z', / This must be added in contact function.
      'DOM-to-use': {
         'follow-btn': 'div[data-testid="323485251-follow"]',
         'message-input': '.public-DraftStyleDefault-block'
      }
   }
}

def CODE_MESSAGE(code):
   return 'Gracias por registrate con Volga, este es tu código de autenticación para esta red de contacto: ' + str(code)
