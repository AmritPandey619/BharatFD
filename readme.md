# FAQ Management System

This project is a **FAQ Management System** built with Django. It allows users to manage frequently asked questions (FAQs), including multilingual support, WYSIWYG editing for answers, and an API for querying FAQ data.

## Features

- **Multilingual Support**: FAQ questions and answers can be translated into different languages.
- **WYSIWYG Editor**: The answers to FAQs are managed using a rich text editor (django-ckeditor).
- **API**: A REST API for retrieving and managing FAQs, with support for language selection.
- **Caching**: Translations are cached for improved performance using Redis.
- **Translation Automation**: Translations are automatically created using Google Translate API or googletrans, with fallback to English.

## Requirements

- Python 3.8+
- Django 3.x+
- Django REST Framework
- django-ckeditor
- Google Translate API or googletrans
- Redis (for caching)

## Setup

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/faq-management-system.git
cd faq-management-system
```
### 2. Create a virtual environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
```
### 3. Install dependencies
```bash
pip install -r requirements.txt
```
### 4. Set up Redis (for caching)
Install Redis on your machine or use a Redis cloud provider.
Make sure to configure Redis connection settings in your settings.py under CACHES.
### 5. Run migrations
```bash
python manage.py migrate
```
### 6. Create a superuser
To access the Django admin panel, create a superuser:

```bash
python manage.py createsuperuser
```
### 7. Run the development server
```bash
python manage.py runserver
```
### 8. Access the application
- Admin Panel: http://127.0.0.1:8000/admin
- API Documentation: http://127.0.0.1:8000/api/faqs/

## API Endpoints
### List FAQs
GET /api/faqs/ - 
Get a list of all FAQs with multilingual support. You can use the ?lang= query parameter to specify the language (e.g., ?lang=hi for Hindi).

### Create FAQ
POST /api/faqs/ - 
Create a new FAQ entry. The request body should include question, answer, and optionally, language-specific translations.

### Example Request
```bash
{
  "question": "What is Machine Learning?",
  "answer": "A subset of Artificial Intelligence.",
  "question_hi": "क्या है मशीन लर्निंग?"
}
```

## Testing

### Run unit tests
```bash
pytest
```
Tests include:

Model method tests
API endpoint tests
Translation functionality tests

## Deployment
Deploy on AWS/GCP
This project can be deployed on cloud platforms like AWS or GCP. You can use services like EC2 or Google App Engine for deployment. Make sure to configure your production database and caching settings (Redis) appropriately.

## License
This project is licensed under the MIT License - see the LICENSE file for details.


---

### **Explanation of Sections:**

1. **Project Description**: Provides a brief overview of the project.
2. **Features**: Lists key functionalities (multilingual support, WYSIWYG editor, API, etc.).
3. **Requirements**: Specifies the dependencies and tools required to run the project.
4. **Setup**: Step-by-step instructions for setting up the project on a local machine.
5. **API Documentation**: Information about the available API endpoints.
6. **Testing**: Instructions for running unit tests using `pytest`.
7. **Deployment**: Brief information on how to deploy the application on cloud platforms like AWS or GCP.
8. **License**: A mention of the project license.

---
