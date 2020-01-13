import os

import eventlet
import socketio


#*>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
#*                                                                       SETUP
# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
static_files = {
    '/': 'pages/index.html',
    '/js/client.js': 'public/js/client.js'
}

sio = socketio.Server()
app = socketio.WSGIApp(sio, static_files=static_files)


#*>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
#*                                                                   SOCKET.IO
# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
@sio.on('connect')
def connect(sid, env):
    print(f'Connected: {sid}')

@sio.on('disconnect')
def disconnect(sid):
    print(f'Disconnected: {sid}')


#*>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
#*                                                                         RUN
# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
if __name__ == '__main__':
    if 'PORT' in os.environ.keys():
        port = int(os.environ['PORT'])
    else:
        port = 8000

    eventlet.wsgi.server(eventlet.listen(('', port)), app)
