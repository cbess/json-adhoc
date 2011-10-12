import json
import os
import urllib2


class JSONAdhoc(object):
    """Represents a JSON adhoc environment wrapper
    """
    def __init__(self, json_string, headers=None):
        self.json_string = json_string
        self._response = None
        self.request_type = None
        if headers is None:
            self.headers = { 'content-type': 'application/json' }
        else:
            self.headers = headers
        pass
        
    def post(self, url, is_async=False):
        """Posts the internal JSON string to the target URL
        """
        self.request_type = 'POST'
        return self.send_request(url)
        
    def get(self, url, is_async=False):
        """Performs a GET request to the target URL using the internal JSON
        """
        self.request_type = 'GET'
        return self.send_request(url)
        
    def send_request(self, url, is_async=False):
        """Sends the JSON request
        """
        body = ''
        if self.request_type == 'POST':
            body = self.json_string
        elif self.request_type == 'GET':
            # add the json to the URL
            url = '%s%s' % (url, self.json_string)
            pass
        # perform the request
        req = urllib2.Request(url, body, self.headers)
        response_stream = urllib2.urlopen(req)
        self._response = response_stream.read()
        return self.response()
        
    def response(self):
        """Returns the response to the last GET or POST operation.
        """
        return self._response
