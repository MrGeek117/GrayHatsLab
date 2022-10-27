import requests
from bs4 import BeautifulSoup


### ----- GET SESSION DATA OBJ ----- ###
class Session:
    def __init__(self):
        self.session = requests.Session()
        self.request = self.session.get("http://www.seed-server.com/login")
        self.soup = BeautifulSoup(self.request.text, 'html.parser')
        self.ts = self.soup.body.script.contents[0][643:653]
        self.token = self.soup.body.script.contents[0][670:692]
        

def PostRequest(SessionData, password):
    #SessionData = Session() ##Remove it and construct the Session Data outside
### ------ BUILD REQUEST ------ ###
    url = "http://www.seed-server.com/action/login"

### ------- POST REQUEST ------ ###

    l = SessionData.session.get(url, params = {
        "__elgg_token": SessionData.token,
        "__elgg_ts": SessionData.ts,
        "username": "alice",
        "password": password
        })
    
    nsoup = BeautifulSoup(l.text, 'html.parser')
    log_in_mess = nsoup.body.find('div', 'elgg-body').get_text()
    if log_in_mess == "You have been logged in.":
        print("Successfull")
        return True
    elif log_in_mess == "We could not log you in. Please check your username/email and password.":
        print("Unsuccessfull")
        return False
    else:
        print("WTF. This is unexpected...")

### --------------------------- ###