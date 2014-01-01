import webapp2, os
from int2en import int2en

class MainHandler(webapp2.RequestHandler):
    def get(self):
        with open('html/index.html') as index:
            self.response.write(index.read())

    def post(self):
        self.response.write(int2en(self.request.get("num")))

