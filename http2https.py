import tornado.ioloop
import tornado.web
import requests

URL = "https://"


class MainHandler(tornado.web.RequestHandler):
    def _get_url(self):
        url = "{0}{1}{2}".format(
            URL, self.request.remote_ip, self.request.uri)
        print(url)
        return url

    def get(self):
        req = requests.get(self._get_url(), headers=self.request.headers)
        self.write(req.text)

    def post(self):
        req = requests.post(self._get_url(), headers=self.request.headers,
                            body=self.request.body)
        self.write(req.text)

    def put(self):
        req = requests.put(self._get_url(), headers=self.request.headers,
                           body=self.request.body)
        self.write(req.text)

    def delete(self):
        req = requests.delete(self._get_url(), headers=self.request.headers,
                              body=self.request.body)
        self.write(req.text)


def make_app():
    return tornado.web.Application([
        (r"/.*", MainHandler),
    ])


if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
