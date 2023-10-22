# Chat Application Documentation

This documentation provides instructions on how to set up and test the Chat Application. The Chat Application is a web-based chat system where users can register, enter a username, and send and receive messages in real-time.

## Prerequisites

Before testing the application, ensure you have the following software and tools installed:

- Python (version 3.6 or higher)
- Flask
- Flask-SocketIO
- Web browser

## Installation

1. Clone the project repository to your local machine:

   ```bash
   git clone [url of the repo]
   ```

2. Change into the project directory:

   ```bash
   cd chat-app
   ```

3. Create a virtual environment (optional but recommended):

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use: venv\Scripts\activate
   ```

4. Make sure the require packages are installed
   ```

## Usage

1. Start the Flask server:

   ```bash
   python app.py
   ```

2. Open a web browser and navigate to `http://localhost:5000` to access the Chat Application.

## Registration

1. On the Chat Application landing page, click the "Register Here" link.

2. Enter your desired username and click "Let's Go!" to register.

3. You will be redirected to the chat page.

## Chatting

1. On the chat page, enter your message in the input field labeled "What do you have in mind?".

2. Click the "Send" button to send your message.

3. Your message, along with your username, will be displayed in the chat box.

## Testing

To test the Chat Application, follow these steps:

1. Register with different usernames from separate browser tabs or devices to simulate multiple users.

2. Send messages from one user, and you should see messages displayed with the respective usernames.

3. Messages are sent and displayed in real-time using WebSocket communication.


## Contributing

Contributions are welcome. Please fork the project, make your changes, and submit a pull request.
