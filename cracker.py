import requests

headers = {
"Host": "www.seed-server.com",
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; rv:102.0) Gecko/20100101 Firefox/102.0",
"Accept": "application/json, text/javascript, */*; q=0.01",
"Accept-Language": "en-US,en;q=0.5",
"Accept-Encoding": "gzip, deflate",
"Referer": "http://www.seed-server.com/login",
"X-Elgg-Ajax-API": "2",
"X-Requested-With": "XMLHttpRequest",
"Content-Type": "multipart/form-data; boundary=---------------------------23149188723087745730519093566",
#"Content-Length": "558",
#"Origin": "http://www.seed-server.com",
#"DNT": "1",
#"Connection": "keep-alive",
"Cookie": "Elgg=ithv8nt4af8rvn3naaagaaug7k"
}
url = "http://www.seed-server.com/action/login"
f = open("/home/c4ll3/elgg-testing/login_cracker/request_body", "r")
payload = f.read()
test = requests.post(url, headers = headers, data = payload)
print(test)
print(test.request.headers)
print(test.request.url)
print(test.request.body)
print(test.content)