import os

import eventlet
import socketio

static_files = {
    '/': 'pages/index.html'
}

sio = socketio.Server()
app = socketio.WSGIApp(sio, static_files=static_files)

if __name__ == '__main__':
    if 'PORT' in os.environ.keys():
        port = int(os.environ['PORT'])
    else:
        port = 8000

    eventlet.wsgi.server(eventlet.listen(('', port)), app)
