#!/usr/bin/env python

import webapp2
from int2en import int2en

class MainHandler(webapp2.RequestHandler):
    def get(self):
        with open('html/index.html') as index:
            self.response.write(index.read())

    def post(self):
        self.response.write(int2en(self.request.get("num")))

app = webapp2.WSGIApplication([
    ('/', MainHandler),
], debug=False)
