import requests
from bs4 import BeautifulSoup
from update_RB import update_RB_file, set_boundary

####################################
### ----- GET SESSION DATA ----- ###
####################################
s = requests.Session()
s.headers.update({
"Host": "www.seed-server.com",
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; rv:102.0) Gecko/20100101 Firefox/102.0",
"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
"Accept-Language": "en-US,en;q=0.5",
"Accept-Encoding": "gzip, deflate",
"DNT": "1",
"Connection": "keep-alive",
"Upgrade-Insecure-Requests": "1"
})
r = s.get("http://www.seed-server.com/login")
soup = BeautifulSoup(r.text, 'html.parser')
# print(soup.body.script)
# print(soup.body.script.contents[0][643:653])
# print(soup.body.script.contents[0][670:693])
ts = soup.body.script.contents[0][643:653]
token = soup.body.script.contents[0][670:692]
### --------------------------- ###
# ------------------------------- #
###################################
### ------ BUILD REQUEST ------ ###
###################################
url = "http://www.seed-server.com/action/login"
### --------------------------- ###
# ------------------------------- #
###################################
### ------- POST REQUEST ------ ###
###################################
l = s.get(url, params = {
    "__elgg_token": token,
    "__elgg_ts": ts,
    "username": "alice",
    "password": "seedalic"
})
nsoup = BeautifulSoup(l.text, 'html.parser')
print(nsoup.body.find('div', 'elgg-body').get_text())
### --------------------------- ###
# ------------------------------- #