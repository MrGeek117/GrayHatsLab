import os
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

### ------ BUILD REQUEST ------ ###

    url = "http://www.seed-server.com/action/login"

### ------- POST REQUEST ------ ###

    l = SessionData.session.get(url, params = {
        "__elgg_token": SessionData.token,
        "__elgg_ts": SessionData.ts,
        "username": "alice",
        "password": password
        })

### ----- HANDLE RESPONSE ----- ###
    
    nsoup = BeautifulSoup(l.text, 'html.parser')
    log_in_mess = nsoup.body.find('div', 'elgg-body').get_text()

    de_counter = 0
    ue_counter = 0

    if log_in_mess == "You have been logged in.":
        return True
        
    elif log_in_mess == "We could not log you in. Please check your username/email and password.":
        return False

    elif log_in_mess == "Your account has been locked for too many log in failures.":
        print("Account locked, retry later...")
        os._exit(0)

    elif "Duplicate entry" in log_in_mess:
        print("Duplicate entry.")
        de_counter += 1
        if de_counter > 10:
            print("Too many duplicate entries, quitting...")
            os._exit(0)
    else:
        print("Unknown error")
        ue_counter += 1
        if ue_counter > 10:
            print("Too many unknown errors, quitting...")
            os._exit(0)

### --------------------------- ###