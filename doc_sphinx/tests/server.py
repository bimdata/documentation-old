from http.server import HTTPServer, SimpleHTTPRequestHandler
import os
from threading import Thread

web_dir = os.path.join(os.path.dirname(__file__), "../../html_doc")
os.chdir(web_dir)


server = HTTPServer(("localhost", 1212), SimpleHTTPRequestHandler)


def threaded_function():
    server.serve_forever()


thread = Thread(target=threaded_function)
thread.daemon = True


def start_server():
    thread.start()


def close_server():
    server.server_close()
    thread.join(1)
