import requests
from update_RB.py import update_RB_file, set_boundary

####################################
### ----- GET SESSION DATA ----- ###
####################################
s = requests.Session()
r = s.get("http://www.seed-server.com/refresh_token")
cookies = r.headers["Set-Cookie"].split(";")
cookie = cookies[0]
x = r.text.split("\"")
ts = x[4]
ts = ts[1:len(ts)-1]
token = x[7]
### --------------------------- ###
# ------------------------------- #
###################################
### ------ BUILD REQUEST ------ ###
###################################
url = "http://www.seed-server.com/action/login"
boundary = str(set_boundary())
headers = {
"X-Elgg-Ajax-API": "2",
"X-Requested-With": "XMLHttpRequest",
"Content-Type": "multipart/form-data; boundary=f"{boundary}",
"Cookie": f"{cookie}"
}
### --------------------------- ###
# ------------------------------- #
###################################
### ------- POST REQUEST ------ ###
###################################


l = s.post(url, headers = headers, data = update_RB_file("User","Password", token, ts))
print(l)
print(l.text)
### --------------------------- ###
# ------------------------------- #
