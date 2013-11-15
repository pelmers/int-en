import webapp2, os
from int2en import int2en

# Leaving this here because I might use templates one day
#JINJA_ENV = jinja2.Environment(
        #loader = jinja2.FileSystemLoader(os.path.dirname(__file__)),
        #extensions = ['jinja2.ext.autoescape'],
        #autoescape=True)

class MainHandler(webapp2.RequestHandler):
    def get(self):
        with open('html/index.html') as index:
            self.response.write(index.read())

    def post(self):
        self.response.write(int2en(self.request.get("num")))

