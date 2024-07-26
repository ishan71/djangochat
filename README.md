

 MyProject - Django Chat Application

Welcome to **MyProject**, a chat application built using Django by **Ishandeep Singh**. This application allows users to communicate in real-time through text messages, providing a seamless and user-friendly chatting experience.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Introduction

**MyProject** is designed to facilitate real-time communication between users. It leverages Django's robust web framework and integrates WebSockets for live messaging capabilities.

## Features

- **User Authentication**: Secure registration and login system.
- **Real-time Chat**: Instant messaging using WebSockets.
- **Group Chat**: Create and join chat rooms.
- **Private Messaging**: One-on-one conversations.
- **User Profiles**: Personalize user profiles with custom information.
- **Message Notifications**: Get notified of new messages.
- **Responsive Design**: Mobile and desktop-friendly interface.

## Installation

### Prerequisites

- Python 3.x
- Django 3.x or later
- Django Channels (for WebSocket support)
- Redis (for channel layer backend)

### Steps

1. Clone the Repository

   ```bash
   git clone https://github.com/username/myproject.git
   cd myproject
   ```

2. Create a Virtual Environment

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. Install Dependencies

   ```bash
   pip install -r requirements.txt
   ```

4. Apply Migrations

   ```bash
   python manage.py migrate
   ```

5. Run the Development Server

   ```bash
   python manage.py runserver
   ```

6. Access the Application

   Open your browser and go to `http://localhost:8000` to start using the chat application.

 Usage

1. **Register an Account**: Create a new account or log in with an existing one.
2. **Join or Create Chat Rooms**: Start chatting in public rooms or create your own.
3. **Send Private Messages**: Click on a user's profile to start a private conversation.
4. **Customize Your Profile**: Update your profile information and settings.

 Contributing

Contributions are welcome! If you find any bugs or have suggestions for improvements, please open an issue or submit a pull request.

Steps to Contribute

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes.
4. Commit your changes (`git commit -m 'Add new feature'`).
5. Push to the branch (`git push origin feature-branch`).
6. Open a pull request.

License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

Contact

For any questions or inquiries, please contact "Ishandeep Singh" at ishandeep71@gmail.com.
