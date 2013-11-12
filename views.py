import webapp2, jinja2, os
from i2e import num2str

JINJA_ENV = jinja2.Environment(
        loader = jinja2.FileSystemLoader(os.path.dirname(__file__)),
        extensions = ['jinja2.ext.autoescape'],
        autoescape=True)

class MainHandler(webapp2.RequestHandler):
    def get(self):
        template = JINJA_ENV.get_template('templates/index.html')
        self.response.write(template.render({}))

    def post(self):
        self.response.write(num2str(self.request.get("num")))

