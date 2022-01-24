import tornado.web
import tornado.ioloop


class IndexCode(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        self.write("shiqiang is a perfect man!")


url = [
    (r'/api/v1/index_code', IndexCode)
]


def main():
    my_app = tornado.web.Application(handlers=url)
    my_app.listen(8080)
    tornado.ioloop.IOLoop.current().start()
    print("control over")


if __name__ == "__main__":
    main()
