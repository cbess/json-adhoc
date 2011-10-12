from adhoc import JSONAdhoc

# url for the request
url = ''

# the json string
json = """{ }"""

print JSONAdhoc(json).post(url)