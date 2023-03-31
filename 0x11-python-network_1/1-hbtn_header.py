#!/usr/bin/python3
"""
script that takes in a URL, sends a request to the URL
and displays the value of the X-Request-Id variable
found in the header of the response
"""
import urllib.request
import sys

url = sys.argv[1]
if __name__ == "__main__":
    with urllib.request.urlopen(url) as response:
        headers = response.headers

        print("{}".format(headers.get('X-Request-Id')))
