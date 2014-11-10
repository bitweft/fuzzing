from pywebfuzz import utils

location = "http://google.com"

headers, content, code, time = utils.make_request(location)

print headers
print content
print code
print time

