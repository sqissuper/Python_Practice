import tornado.web
import tornado.ioloop
import tornado.httpserver


class IndexCode(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        self.write("shiqiang is a perfect man!")


url = [
    (r'/api/index_code', IndexCode)
]


def main():
    my_app = tornado.web.Application(handlers=url)

    # my_app.listen(8080)
    # 实例化一个http服务器
    httpServer = tornado.httpserver.HTTPServer(my_app)
    httpServer.bind()
    httpServer.start(num_processes)

    tornado.ioloop.IOLoop.current().start()


if __name__ == "__main__":
    main()
