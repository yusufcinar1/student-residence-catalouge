# Student Residence Catalogue (Django)

A simple Django application to manage student residences, rooms, students, and reservations.

## Features

* Manage **Residences** and their **Rooms**
* Register **Students**
* Create **Reservations** (student booking a room between dates)
* Validation rules:

  * End date must be after start date
  * Email validation for students
  * Room must belong to the correct residence
* Django Admin panel for easy data management
* Simple JSON API

---

## Tech Stack

* Python 3
* Django
* SQLite (default Django database)

---

## Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/yusufcinar1/student-residence-catalouge
cd student-residence
```

### 2. Create virtual environment

```bash
python -m venv venv
```

Activate it:

* Windows:

```bash
venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Apply migrations

```bash
python manage.py migrate
```

### 5. Create superuser (for admin panel)

```bash
python manage.py createsuperuser
```

### 6. Run the server

```bash
python manage.py runserver
```

Open in browser:

```
http://127.0.0.1:8000/
```

Admin panel:

```
http://127.0.0.1:8000/admin/
```

---

## API Endpoints

### 1. List Residences

**GET** `/api/residences/`

Response example:

```json
[
  {
    "id": 1,
    "name": "Istanbul Yurt",
    "city": "Istanbul",
  }
]
```

---


## Project Structure

```
student_residence/
├── manage.py
├── db.sqlite3
├── app/
│   ├── models.py
│   ├── views.py
│   ├── admin.py
│   ├── urls.py
│   └── migrations/
```

---

## Notes

* Uses SQLite for simplicity (no external database required)
* All models are manageable via Django Admin
* API returns JSON responses only

---

## Author

* Yusuf Cinar

---
