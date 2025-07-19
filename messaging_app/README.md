# Messaging API

A robust and scalable RESTful API built with Django and Django REST Framework for managing user messaging conversations and messages. This project demonstrates best practices in API development including model design, serializers, viewsets, and clean URL routing.

---

## Overview

This project implements a messaging system backend API that allows users to create conversations, send messages, and manage user roles and profiles. It follows Django's best practices for project structure and RESTful API design.

---

## Features

* User management with roles (`guest`, `host`, `admin`)
* Conversations with multiple participants
* Sending and retrieving messages within conversations
* UUID primary keys for all models
* Timestamp fields with automatic creation times
* Nested serialization for conversations including messages

---

## Tech Stack

* Python 3.11+
* Django 4.x
* Django REST Framework
* SQLite (default, configurable to other databases)
* `django-environ` for environment variables (optional)

---

## Setup and Installation

### Prerequisites

* Python 3.11+ installed
* `venv` for virtual environments

### Steps

```bash
# Clone the repo
git clone https://github.com/yourusername/messaging_api.git
cd messaging_api

# Create virtual environment
python -m venv venv

# Activate virtual environment
# Windows (PowerShell)
.\venv\Scripts\Activate.ps1
# Linux/Mac
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Apply migrations
python manage.py migrate

# Create superuser (optional)
python manage.py createsuperuser

# Run development server
python manage.py runserver
```

---

## Project Structure

```
messaging_app/
├── chats/
│   ├── migrations/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── serializers.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── messaging_app/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── manage.py
└── requirements.txt
```

---

## Models

### User

* UUID primary key (`user_id`)
* `first_name`, `last_name`, `email` (unique)
* `phone_number` (optional)
* `role` (`guest`, `host`, `admin`)
* `created_at` timestamp

### Conversation

* UUID primary key (`conversation_id`)
* `participants` (many-to-many relationship with `User`)
* `created_at` timestamp

### Message

* UUID primary key (`message_id`)
* `sender` (foreign key to `User`)
* `conversation` (foreign key to `Conversation`)
* `message_body` (text)
* `sent_at` timestamp

---

## Serializers

* **UserSerializer:** Serializes user details, used nested inside other serializers.
* **ConversationSerializer:** Serializes conversations including nested participant users and nested messages.
* **ConversationCreateSerializer:** Used when creating or updating conversations; accepts participant IDs to establish many-to-many relationships.
* **MessageSerializer:** Serializes messages including sender details.
* **MessageCreateSerializer:** Used to create or update messages.

---

## Views (Viewsets)

* **ConversationViewSet:** Handles CRUD operations on conversations. Uses different serializers for listing (`ConversationSerializer`) and creating/updating (`ConversationCreateSerializer`).
* **MessageViewSet:** Handles CRUD operations on messages. Uses different serializers for listing (`MessageSerializer`) and creating/updating (`MessageCreateSerializer`).
* Both viewsets use `AllowAny` permissions for simplicity but can be customized for authentication.

---

## API Endpoints

| Method | Endpoint                   | Description                   |
| ------ | -------------------------- | ----------------------------- |
| GET    | `/api/conversations/`      | List all conversations        |
| POST   | `/api/conversations/`      | Create a new conversation     |
| GET    | `/api/conversations/{id}/` | Retrieve conversation details |
| GET    | `/api/messages/`           | List all messages             |
| POST   | `/api/messages/`           | Send a new message            |
| GET    | `/api/messages/{id}/`      | Retrieve message details      |

---

## Testing

Run the Django test suite:

```bash
python manage.py test
```

---