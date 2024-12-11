
# Django Notes API

This project is a simple **Django REST Framework (DRF)** API to manage notes, inspired by Google Keep. It supports basic CRUD operations, categorization, and tagging of notes.

## Features
- **CRUD operations**: Create, Read, Update, and Delete notes.
- **Categorization and tags**: Assign categories and tags to each note.
- **Filtering**: Filter notes by title and tags.

## Installation

### Prerequisites
- Python 3.8 or higher
- Django 5.1+
- Django REST Framework
- drf-spectacular for API documentation

### Setup

1. **Clone the repository**:
   ```bash
   git clone https://github.com/JanSua/DRFNotesAPI.git
   cd DRFNotesAPI
   ```

2. **Create and activate a virtual environment**:
   ```bash
   python -m venv venv
   # On Windows
   venv\Scriptsctivate
   # On macOS/Linux
   source venv/bin/activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run migrations**:
   ```bash
   python manage.py migrate
   ```

5. **Run the server**:
   ```bash
   python manage.py runserver
   ```

6. **Access the API documentation**:
   Once the server is running, you can access the Swagger UI at:
   ```
   http://127.0.0.1:8000/swagger/
   ```

## Usage

- Use the available endpoints to manage notes and apply filters based on title or tags.

## Endpoints
- **POST /api/notes/**: Create a new note.
- **GET /api/notes/**: List all notes (supports filtering).
- **GET /api/notes/{id}/**: Retrieve a specific note.
- **PUT /api/notes/{id}/**: Update an existing note.
- **DELETE /api/notes/{id}/**: Delete a specific note.

## Technologies Used
- **Django 5.1+**: Web framework for the backend.
- **Django REST Framework (DRF)**: For building the RESTful API.
- **drf-spectacular**: For generating interactive Swagger documentation.
