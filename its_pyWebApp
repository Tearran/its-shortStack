import sys, os
from http.server import BaseHTTPRequestHandler, HTTPServer
path=os.listdir(os.path.dirname(__file__))

class MyServer(BaseHTTPRequestHandler):
        
    def do_GET(self):
        its_list = ''
        for x in os.listdir(os.path.dirname(__file__)):
            if x.endswith(".py"):
                its_list+=" <LI>"+x+"</LI>"
          
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(bytes("<html><head><title>ITS LKARS</title></head>", "utf-8"))
        self.wfile.write(bytes("<body style='background-color:#3c3c3c; color:#ffffff; '>", "utf-8"))
        self.wfile.write(bytes("<H1 style='text-align:center;' >Welcome to ITS LKARS</H1>", "utf-8"))
        self.wfile.write(bytes("<P style='text-align:center;'  >Linux Kernel to Access and Record Sensor data. (LKARS)</P>", "utf-8"))
        self.wfile.write(bytes("<H2 style='text-align:center;' >Include Tearrans Script(s). (ITS)</H2>", "utf-8"))
        self.wfile.write(bytes("<P style='text-align:center;' >Include This/these Script(s).</P>", "utf-8"))
        self.wfile.write(bytes("<UL>"+its_list+"</UL>", "utf-8"))
        self.wfile.write(bytes("</body></html>", "utf-8"))


if __name__ == "__main__":
    appServer = HTTPServer(('', 8000), MyServer)
    print("its local server")
    try:
        
        print("started at port 8000")
        appServer.serve_forever()
        
    except KeyboardInterrupt:       
        pass

    appServer.server_close()
    print("Server stopped.")
