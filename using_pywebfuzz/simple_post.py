from pywebfuzz import utils

location = "http://127.0.0.1/DVWA-1.0.8/login.php"

headers = {
              "Host": "127.0.0.1",
              "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:33.0) Gecko/20100101 Firefox/33.0",
              "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
              "Accept-Language": "en-us,en;q=0.5",
              "Keep-Alive": "115",
              "Connection": "keep-alive",
              "Referer": "http://127.0.0.1/DVWA-1.0.8/login.php",
	      "Content-Length": "44"
          }

postdata="username=admin&password=password&Login=Login"

headers, content, code, time  = utils.make_request(location, method="POST", postdata=postdata, headers=headers)

print headers
print content
print code
print time
