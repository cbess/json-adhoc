# JSON Adhoc

Provides an adhoc environment to test JSON POST and GET requests.

Modify and run `main.py`.

Example:
    
    from adhoc import JSONAdhoc
    
    # prints the response
    print JSONAdhoc(json_string).get(url)
    