import tornado.web
import tornado.ioloop
import tornado.httpserver
import tornado.options
from tornado.options import define, options

define("port", default=8000, type=int)
define("list", default=[], type=str, multiple=True)


class IndexCode(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        self.write("shiqiang is a perfect man!")


url = [
    (r'/api/index_code', IndexCode)
]


def main():
    options.parse_command_line()
    print("list", options.list)
    my_app = tornado.web.Application(handlers=url)
    httpServer = tornado.httpserver.HTTPServer(my_app)
    httpServer.listen(options.port)

    tornado.ioloop.IOLoop.current().start()


if __name__ == "__main__":
    main()
