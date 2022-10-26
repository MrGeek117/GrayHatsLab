import requests

#f = open("/home/c4ll3/elgg-testing/login_cracker/request_body", "r")
#data = f.read()

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
headers = {
"X-Elgg-Ajax-API": "2",
"X-Requested-With": "XMLHttpRequest",
"Content-Type": "multipart/form-data; boundary=---------------------------335837917637707572332315839054",
"Cookie": f"{cookie}"
}
### --------------------------- ###
# ------------------------------- #
###################################
### ------- POST REQUEST ------ ###
###################################
#l = s.post(url, headers = headers, data = data)
#print(l)
#print(l.text)
### --------------------------- ###
# ------------------------------- #