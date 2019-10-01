"""
CatPlay
Version 1.0
Jigar Hira
June 2019
"""


from http import server


PAGE = """\
        <html>
        <head>
        <title>picamera MJPEG streaming demo</title>
        </head>
        <body>
        <h1>PiCamera MJPEG Streaming Demo</h1>
        <img src="stream.mjpg" width="640" height="480" />
        </body>
        </html>
        """

class StreamingHandler(server.BaseHTTPRequestHandler):
    """
    HTTP handler for incoming server requests.
    """
    def do_GET(self):
        """
        Handler for GET requests
        """
        if self.path == '/':
            self.send_response(301)
            self.send_header('Location', '/index.html')
            self.end_headers()
        elif self.path == '/index.html':
            with open('index.htmll', 'rb') as content
            self.send_response(200)
            self.send_header('Content-Type', 'text/html')
            self.send_header('Content-Length', len(content))
            self.end_headers()
            self.wfile.write(content.read())
        elif self.path == '/stream.mjpg':
            self.send_response(200)
            self.send_header('Age', 0)
            self.send_header('Cache-Control', 'no-cache, private')
            self.send_header('Pragma', 'no-cache')
            self.send_header('Content-Type', 'multipart/x-mixed-replace; boundary=FRAME')
            self.end_headers()
            try:
                while True:
                    with output.condition:
                        output.condition.wait()
                        frame = output.frame
                    self.wfile.write(b'--FRAME\r\n')
                    self.send_header('Content-Type', 'image/jpeg')
                    self.send_header('Content-Length', len(frame))
                    self.end_headers()
                    self.wfile.write(frame)
                    self.wfile.write(b'\r\n')
            except Exception as e:
                logging.warning(
                    'Removed streaming client %s: %s',
                    self.client_address, str(e))
        else:
            self.send_error(404)
            self.end_headers()


class StreamingServer(socketserver.ThreadingMixIn, server.HTTPServer):
    """
    DOCSTRING
    """
    allow_reuse_address = True
    daemon_threads = True









# Unit test
if __name__ == '__main__':
    with picamera.PiCamera(resolution='640x480', framerate=24) as camera:
        output = StreamingOutput()
        camera.start_recording(output, format='mjpeg')
        try:
            address = ('', 8000)
            server = StreamingServer(address, StreamingHandler)
            server.serve_forever()
        finally:
            camera.stop_recording()

# EOF