import os
import io
import tornado.web
import tornado.httpserver
import sqlite3 as lite


class Application(tornado.web.Application):

    def __init__(self):
        handlers = [
            (r"/", UsersHandler),
            (r"/login.html", UsersHandler)
        ]
        settings = {
            "template_path": os.path.join(os.path.dirname(__file__), 'templates'),
            "static_path": os.path.join(os.path.dirname(__file__), "static"),
            "debug": False
        }
        tornado.web.Application.__init__(self, handlers, **settings)

class MainHandler(tornado.web.RequestHandler):

    def get(self):
        print("GET ", self.request.uri)
        self.render("login.html")

class UsersHandler(tornado.web.RequestHandler):

    def get(self):
        print("GET ", self.request.uri)
        self.render("login.html", msg="")

    def post(self):
        print("POST call")
        print("POST ", self.request.uri, "\nBODY ", self.request.body)
        con = lite.connect('demo.db')
        dat = ""
        uname = self.get_argument('username')
        pwd = self.get_argument('password')
        cur = con.cursor()
        cur.execute("SELECT * FROM Users WHERE User ='" +
                        uname + "' AND Password ='" + pwd + "'")
        cur_resp = cur.fetchone()
        if not cur_resp:
            dat = "Login Failed"
        else:
            dat = "Login Success, Hello " + str(cur_resp[1])
        self.render("login.html", msg=dat)



def create_db():
    con = lite.connect('demo.db')
    with con:
        cur = con.cursor()
        cur.execute(
            "SELECT count(*) FROM sqlite_master WHERE type = 'table' AND name = 'Users'")
        exc = cur.fetchone()[0]
        if exc == 0:
            cur.execute("CREATE TABLE Users(Id INT, User TEXT, Password TEXT)")
            cur.execute("INSERT INTO Users VALUES(1,'admin','admin')")
            cur.execute("INSERT INTO Users VALUES(2,'FOS','FOS')")
            cur.execute("INSERT INTO Users VALUES(3,'sagar','lall0l')")
            cur.execute("INSERT INTO Users VALUES(4,'alias','ohrealli')")
            cur.execute("INSERT INTO Users VALUES(5,'jacky','st40ngp@55')")
            cur.execute("INSERT INTO Users VALUES(6,'sam','tomTOM123')")
            cur.execute("INSERT INTO Users VALUES(7,'maxi','D@ni3lDizaark')")
            cur.execute("INSERT INTO Users VALUES(8,'lelol','Leeee@Looo@!$')")
            cur.fetchone()


def main():
    #create_db()
    applicaton = Application()
    http_server = tornado.httpserver.HTTPServer(applicaton)
    http_server.bind(7777, address='127.0.0.1')
    http_server.start()
    print("Server Started: http://127.0.0.1:7777")
    tornado.ioloop.IOLoop.instance().start()

if __name__ == "__main__":
    main()

