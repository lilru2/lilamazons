import json
import os

import eventlet
import psycopg2
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

# PostgreSQL
if 'DATABASE_URL' in os.environ.keys():
    db_url = os.environ['DATABASE_URL']
else:
    db_url = json.load(open('config.json'))['db_url']

con = psycopg2.connect(db_url)
cur = con.cursor()


#*>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
#*                                                                   SOCKET.IO
# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
@sio.on('connect')
def connect(sid, env):
    print(f'Connected: {sid}')

@sio.on('disconnect')
def disconnect(sid):
    print(f'Disconnected: {sid}')

@sio.on('registration')
def registration(sid, details):
    cur.execute(
        'SELECT count(*) FROM users WHERE username=%(username)s',
        { 'username': details['username'] }
    )

    if cur.fetchone()[0]: # Username is taken
        sio.emit('username_taken', room=sid)

    else:
        # TODO: Actually use password hash rather than the plaintext password.
        cur.execute("""
            INSERT INTO users (username, password_hash)
            VALUES (%(username)s, %(password_hash)s)
            """,
            {
                'username':      details['username'],
                'password_hash': details['password']
            }
        )
        con.commit()

        sio.emit('registered', room=sid)

@sio.on('login')
def login(sid, details):
    cur.execute(
        'SELECT * FROM users WHERE username=%(username)s',
        { 'username': details['username'] }
    )
    res = cur.fetchone()

    if res: # User exists
        print(f'Login from {res[0]}')

    else:
        sio.emit('no_such_user', room=sid)


#*>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
#*                                                                         RUN
# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
if __name__ == '__main__':
    if 'PORT' in os.environ.keys():
        port = int(os.environ['PORT'])
    else:
        port = 8000

    eventlet.wsgi.server(eventlet.listen(('', port)), app)

    # Shutdown
    cur.close()
    con.close()
