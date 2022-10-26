import requests
from bs4 import BeautifulSoup


### ----- GET SESSION DATA OBJ ----- ###
class Session:
    def __init__(self):
        self.session = requests.Session()
        self.session.headers.update({
        "Host": "www.seed-server.com",
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:106.0) Gecko/20100101 Firefox/106.0",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.5",
        "Accept-Encoding": "gzip, deflate",
        "DNT": "1",
        "Connection": "keep-alive",
        "Upgrade-Insecure-Requests": "1"
        })
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
        "password": "seedalice"
        })
    nsoup = BeautifulSoup(l.text, 'html.parser')
    print(nsoup.body.find('div', 'elgg-body').get_text())


### --------------------------- ###

