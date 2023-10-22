from flask import Flask, render_template, request, session, url_for, redirect
from flask_socketio import SocketIO

app = Flask(__name__)
app.config['SECRET_KEY'] = 'whatever_man' # This would most likely be edited and saved in an env
socketio =  SocketIO(app)

@app.route('/') # Route for the index page :-)
def chat():
    username = session.get('username', 'Anonymous')
    if 'username' in session:
        return render_template('index.html', username=username)
    return redirect(url_for('register'))   

@app.route('/register', methods=['GET', 'POST']) # Route for the registration form. Yes, I realise this is very insecure without flask-security
def register():
    if request.method == 'POST':
        session['username'] = request.form['username']
        return redirect(url_for('chat'))
    return render_template('registration.html')       
    

@socketio.on('message') #It basically means this function ahould be triggered whenever the socket receives a message :-)
def handle_message(data):
    message = data['message']
    username = session.get('username', 'Anononymous') # Getting username or default to Anon if none
    socketio.emit('message', {'username': username, 'message': message}) # This now displays the message to all connected clients together with the username of the sender 


if __name__ == '__main__': 
    socketio.run(app, debug=True)    