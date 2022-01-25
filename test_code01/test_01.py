# tornado基础web框架模块
import tornado.web

# tornado的核心IO循环模块，封装了Linux的epoll和BDS的kqueue
import tornado.ioloop


# 业务处理类
class IndexCode(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        self.write("shiqiang is a perfect man!")


url = [
    (r'/api/v1/index_code', IndexCode)
]


def main():
    # 实例化一个类
    # Application：tornado.web框架的核心应用类，与服务器对应的接口，保存了路由映射表
    my_app = tornado.web.Application(handlers=url)

    # 绑定监听端口，等待客户端链接状态
    my_app.listen(8080)

    """
    IOLoop.current()：返回当前线程IOLoop实例
    start()：开启循环，同时开启了监听
    """
    tornado.ioloop.IOLoop.current().start()


if __name__ == "__main__":
    main()
