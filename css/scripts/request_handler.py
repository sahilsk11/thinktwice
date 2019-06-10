#!/usr/bin/python

import cgi
import json
import api_call

print("Content-type: application/json\n\n")

form = cgi.FieldStorage()
product = form.getfirst("product", "")
price = form.getfirst("price", "")

