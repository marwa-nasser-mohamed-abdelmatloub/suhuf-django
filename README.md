

# 🌙 SOHF (Save Quran to People) - Django REST API

![Django](https://img.shields.io/badge/Django-4.2.20-green)
![DRF](https://img.shields.io/badge/DRF-3.14.0-red)
![Python](https://img.shields.io/badge/Python-3.13-blue)

**SOHF** is a Quran learning and management platform powered by Django and Django REST Framework. It features a fully customized user authentication system, profile handling, and an extendable foundation to support future roles such as teachers and students.

---

## 📚 Table of Contents

* [✨ Features](#-features)
* [🚀 Installation](#-installation)
* [📁 Project Structure](#-project-structure)
* [📖 API Documentation](#-api-documentation)
* [⚙️ Configuration](#-configuration)
* [🚢 Deployment](#-deployment)
* [🧠 Development Notes](#-development-notes)

---

## ✨ Features

* 🔐 **Custom User Model** — Flexible and extensible user authentication.
* 🔁 **Token and Session Authentication** — Choose between token-based or session-based login flows.
* 🖼 **Profile Picture Upload** — Users can upload avatars and manage profiles.
* 👥 **Role-Based Support** — Ready to implement role-specific logic (Teachers, Students, etc.).
* ⚡ **RESTful Endpoints** — Built with Django REST Framework for modern client-server communication.

---

## 🚀 Installation

### ✅ Prerequisites

Ensure the following are installed:

* Python 3.8+
* pip (Python package manager)
* Virtualenv (optional but recommended)

### 🛠 Setup Instructions

```bash
# Clone the repository
git clone https://github.com/yourusername/sohf-project.git
cd sohf-project

# Create and activate a virtual environment
python -m venv venv
source venv/bin/activate        # For Linux/macOS
# venv\Scripts\activate         # For Windows

# Install project dependencies
pip install -r requirements.txt

# Apply database migrations
python manage.py migrate

# Create a superuser account
python manage.py createsuperuser

# Run the development server
python manage.py runserver
```

---

## 📁 Project Structure

```bash
sohf-project/
│
├── config/                  # Project-level configuration
│   ├── settings.py          # Django settings module
│   └── urls.py              # URL routing for the entire project
│
├── accounts/                # User management app
│   ├── models.py            # CustomUser model
│   ├── serializers.py       # DRF serializers
│   ├── views.py             # API views for authentication & profiles
│   └── urls.py              # Endpoint routing for accounts
│
├── courses/                 # Future app for Quran content
│
├── manage.py                # Django's CLI entry point
└── requirements.txt         # List of required Python packages
```

---

## 📖 API Documentation

### 🔐 Authentication

| Endpoint                        | Method | Description       |
| ------------------------------- | ------ | ----------------- |
| `/api/accounts/users/register/` | POST   | Register new user |
| `/api-auth/login/`              | POST   | Login via session |
| `/api-auth/logout/`             | POST   | Logout (session)  |

### 👤 User Management

| Endpoint                    | Method            | Description              |
| --------------------------- | ----------------- | ------------------------ |
| `/api/accounts/users/`      | GET               | List all users (Admin)   |
| `/api/accounts/users/me/`   | GET               | Get current user info    |
| `/api/accounts/users/{id}/` | GET / PUT / PATCH | Get or update user by ID |

---

## ⚙️ Configuration

You can set environment variables to manage sensitive data such as database credentials, secret keys, and debug settings. You may use `.env` files with [django-environ](https://django-environ.readthedocs.io/) for convenience.

Example `.env`:

```ini
DEBUG=True
SECRET_KEY=your-secret-key
DATABASE_URL=postgres://user:password@localhost:5432/sohf
```

---

## 🚢 Deployment

You can deploy this project to platforms such as:

* **Heroku**
* **Render**
* **DigitalOcean**
* **AWS EC2**

Make sure to:

* Use production-ready settings (`DEBUG=False`)
* Configure `ALLOWED_HOSTS`
* Use a production database (PostgreSQL, etc.)
* Set up static/media file handling (e.g., using `WhiteNoise` or AWS S3)

---

## 🧠 Development Notes

* Follow [PEP8](https://peps.python.org/pep-0008/) coding standards.
* Unit tests and integration tests are recommended for all major features.
* Feel free to extend the `courses` app for adding Quran lessons, verses, quizzes, etc.

---

## 🙏 Contributing

Contributions are welcome! Please fork the repository and submit a pull request.

---

## 📩 Contact

For any inquiries or collaboration, feel free to reach out at:
**📧 [your.email@example.com](mailto:your.email@example.com)**

---

Would you like me to generate a badge for GitHub Actions (CI), code coverage, or license? Or create a version in Arabic too?
