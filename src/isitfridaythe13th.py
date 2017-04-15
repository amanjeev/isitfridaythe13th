import datetime
import webapp2
from google.appengine.ext.webapp.util import run_wsgi_app

now = datetime.datetime.now()


class MainPage(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/html'
        isitfridaythe13th = 'NO'
        if now.weekday() == 4 and now.day == 13:
            isitfridaythe13th = 'YES'

        self.response.out.write(
            '<!DOCTYPE html><html lang ="en"><head><meta http-equiv="content-type" content="text/html; charset=utf-8" /><title>Is it Friday the 13th?</title></head><body style="text-align: center; padding-top: 200px;"><div class="content" style="font-weight: bold; font-size: 220px; font-family: Arial,sans-serif; text-decoration: none; color: black;">' + isitfridaythe13th + '<div class="disclaimer" style="font-size:10px; ">All times are in UTC</div></div></body></html>')


app = webapp2.WSGIApplication([('/', MainPage)], debug=True)


def main():
    run_wsgi_app(app)


if __name__ == "__main__":
    main()
