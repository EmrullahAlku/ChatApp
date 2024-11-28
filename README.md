
# Chat App with Django, Channels & WebSockets



This is a basic chat application built with Django. The application allows users to register, log in, create chat rooms, and send messages in real-time. The project demonstrates the use of Django Channels for WebSocket communication and includes features such as user authentication, message search, and account management.

![{1A108A2B-132A-4126-8842-26B517C94FF0}](https://github.com/user-attachments/assets/2123cc7c-7351-4215-9a40-7b0f83f8ff6b)
## Features

- User registration and authentication
- Real-time messaging with WebSockets
- Create and join chat rooms
- Search messages within chat rooms
- Delete messages in a chat room
- Responsive design

## Technologies Used

- Django
- Django Channels
- WebSockets
- HTML/CSS
- JavaScript

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/EmrullahAlku/ChatApp
   cd ChatApp

2. Create a virtual environment and activate it:
   ```bash
   python3 -m venv myenv # On Windows use `python -m venv myenv`
   source myenv/bin/activate  # On Windows use `myenv\Scripts\activate`
3. Install the required packages:
   ```bash
   pip install -r requirements.txt
4. Apply migrations
   ```bash
   python manage.py migrate
5. Create Admin
   ```bash
   python manage.py createsuperuser
6. Run the development server:
   ```bash
   python manage.py runserver
7. Open your browser and go to http://127.0.0.1:8000 to see the application.

## Usage

1. Register a new user or log in with an existing account.
2. Create a new chat room or join an existing one.
3. Start sending messages in real-time.
4. Use the search bar to find specific messages within a chat room.
5. Delete messages in a chat room if needed.
6. Delete your account from the profile dropdown menu.

## Project Structure


- `chat/`: Contains the main chat application code.
  - `templates/`: HTML templates for the application.
  - `models.py`: Defines the database models for the application.
  - `views.py`: Contains the view functions for handling requests.
  - `urls.py`: URL routing for the application.
  - `consumers.py`: WebSocket consumers for real-time messaging.
- `ChatApp/`: Contains the project settings and configuration.
-  `static/`: Static files such as CSS and JavaScript.
- `requirements.txt`: List of required Python packages.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request with your changes.

## Acknowledgements

- Django Documentation
- Django Channels Documentation
