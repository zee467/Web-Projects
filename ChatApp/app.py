from flask import Flask, render_template
from flask_socketio import SocketIO

app = Flask(__name__)
socketio =  SocketIO(app)

@app.route('/') # Route for the index page :-)
def chat():
    return render_template('index.html') # to render the index.html instead :-)

@socketio.on('message') #It basically means this function ahould be triggered whenever the socket receives a message :-)
def handle_message(data):
    message = data['message']
    socketio.emit('message', {'message': message}) # To send the message to all users connected. At least I hope that is what it does. God abeg


if __name__ == '__main__': # This loop still confuses me. Idk why its here. If either of you could explain it for me that would be great :-)
    socketio.run(app, debug=True) # I'll set debug as true just incase I have wwritten rubbish. Haha.      