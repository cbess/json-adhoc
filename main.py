from adhoc import JSONAdhoc

# url for the request
url = 'http://ajax.googleapis.com/ajax/services/search/web?v=1.0&q=Google'

# the json string
json = """ """

print JSONAdhoc(json).get(url)