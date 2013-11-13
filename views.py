import webapp2, os
from i2e import num2str

#JINJA_ENV = jinja2.Environment(
        #loader = jinja2.FileSystemLoader(os.path.dirname(__file__)),
        #extensions = ['jinja2.ext.autoescape'],
        #autoescape=True)

class MainHandler(webapp2.RequestHandler):
    def get(self):
        with open('html/index.html') as index:
            self.response.write(index.read())

    def post(self):
        self.response.write(num2str(self.request.get("num")))

