"""
Python script to listen on port 8888 to handle HTTP request and redirect theme
to the HTTPS server running in localhost.
"""
import tornado.ioloop
import tornado.web
import requests
import json

URL = "https://localhost"


class MainHandler(tornado.web.RequestHandler):
    def _get_url(self):
        url = "{0}{1}".format(
            URL, self.request.uri)
        print(url)
        return url

    def _respond(self, req):
        self.set_status(req.status_code)
        for key, value in req.headers.items():
            self.add_header(key, value)
        self.write(req.text)
        self.flush()

    def get(self):
        req = requests.get(self._get_url(), headers=self.request.headers,
                           verify=False)
        self._respond(req)

    def post(self):
        json_request = json.loads(self.request.body)
        req = requests.post(self._get_url(), headers=self.request.headers,
                            json=json_request, verify=False)
        self._respond(req)

    def put(self):
        json_request = json.loads(self.request.body)
        req = requests.put(self._get_url(), headers=self.request.headers,
                           json=json_request, verify=False)
        self._respond(req)

    def delete(self):
        req = requests.delete(self._get_url(), headers=self.request.headers,
                              verify=False)
        self._respond(req)


def make_app():
    return tornado.web.Application([
        (r"/.*", MainHandler),
    ])


if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
