# coding=UTF-8
# python native module
import urllib
import threading
import thread
import argparse
import os.path
import json
import pprint
# tornado module
import tornado.httpserver
import tornado.httputil as httputil
import tornado.ioloop
import tornado.web
from tornado.options import define, options
from  tornado.escape import json_decode
from  tornado.escape import json_encode
# mongodb module
import pymongo
from pymongo import MongoClient

#localhost:8000/index
DB_IP = "localhost"
DB_PORT = 27017

def main():
    parser = argparse.ArgumentParser(description='ptt-clustering server')
    parser.add_argument('port', type=int, help='listening port for ptt-clustering server')
    args = parser.parse_args()
    
    print("Server starting......")

    http_server = tornado.httpserver.HTTPServer(Application())
    http_server.listen(args.port)

    try:
        tornado.ioloop.IOLoop.instance().start()
    except KeyboardInterrupt:
        tornado.ioloop.IOLoop.instance().stop()

class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r"/index", IndexHandler),
            (r"/chart", ChartHandler),
            (r"/user",UserHandler),
            (r"/test", TestHandler),
            (r"/testajax", AjaxHandler),
        ]

        settings = dict(
            template_path=os.path.join(os.path.dirname(__file__), "templates"),
            static_path=os.path.join(os.path.dirname(__file__), "static"),
        )
        super(Application, self).__init__(handlers, **settings)

class BaseHandler(tornado.web.RequestHandler):
    @property
    def db(self):
        pass
        #return self.settings['db']

class IndexHandler(BaseHandler):
    def get(self):
        abc = ["Item 1", "Item 2", "Item 3"]
        self.render("index.html", abc = abc)

class ChartHandler(BaseHandler):
    def get(self):
        self.render("chart.html")

class UserHandler(BaseHandler):
    def get(self):
        self.render("user.html")

    def post(self):
        username = self.get_argument("username")
        print username
        self.render("user.html", username = username)
        
'''
class IndexHandler(BaseHandler):
    def get(self):
        createMessage = ""
        abc = ["Item 1", "Item 2", "Item 3"]
        self.render("index.html", abc = abc, createMessage = createMessage)

    def post(self):
        newusername = self.get_argument("newusername")
        newpassword = self.get_argument("newpassword")
        print newusername, newpassword
        newUser = collection.find_one({"username": newusername})
        if newUser == None:
            post = {
            "username": newusername,
            "password": newpassword
            }
            collection.insert_one(post)
            createMessage = "new user"
        else:
            createMessage = "old user"
        self.render("index.html", createMessage = createMessage)
'''

class TestHandler(BaseHandler):
    def get(self):
        abc = ["Item 1", "Item 2", "Item 3"]
        self.render("test.html",title="My title", abc = abc)

class AjaxHandler(tornado.web.RequestHandler):
    def get(self):
        example_response = {}
        example_response['name'] = 'example'
        example_response['width'] = 1020

        self.write(json.dumps(example_response))

    def post(self):
        json_obj = json_decode(self.request.body)
        print('Post data received')

        for key in list(json_obj.keys()):
            print('key: %s , value: %s' % (key, json_obj[key]))

        # new dictionary
        response_to_send = {}
        response_to_send['newkey'] = json_obj['key1']

        print('Response to return')

        pprint.pprint(response_to_send)

        self.write(json.dumps(response_to_send))

if __name__ == '__main__':
    main()
