# JSON Adhoc

- Sample JSON examples are from [JSON.org](http://json.org/example.html)
- Sample JSON can be accessed from lorem json:
    [http://loremjson.appspot.com](http://loremjson.appspot.com/)

Provides an adhoc environment to test JSON POST and GET requests.

Modify and run `main.py`.

Example:
    
    from adhoc import JSONAdhoc
    
    # prints the response
    print JSONAdhoc(json_string).get(url)