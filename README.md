# BaziMazi

BaziMazi is more than a marketplace — it introduces a streamlined approach to gaming commerce. Instead of navigating through complex trading platforms, users interact with an intuitive, category-driven system where every gaming item can be discovered through intelligent filtering. Every ad can be traced back to its publisher, whether from a local gamer or a regional collector. Listings can be filtered by multiple criteria as needed. The structured marketplace becomes a living ecosystem, ready to be browsed, saved, and connected through direct communication.

## Setup

Install dependencies:

```bash
pip install -r requirements.txt
```

Configure email settings (for user verification):

Edit `finalproject/settings.py` and update email configuration:

```python
EMAIL_HOST_USER = "your_email@gmail.com"
EMAIL_HOST_PASSWORD = "your_app_password"
```

Run database migrations:

```bash
python manage.py migrate
```

Run the application:

```bash
python manage.py runserver
```

Access the application at `http://127.0.0.1:8000/`

## Project Structure

```
bazimazi/
├── bazimazi/                 # Main Django application
│   ├── models.py             # Database models (User, Ad, Category, State, Type)
│   ├── views.py              # Business logic and API endpoints
│   ├── templates/            # HTML templates
│   └── static/               # CSS, images, and static assets
├── finalproject/             # Django project configuration
│   ├── settings.py           # Project settings
│   └── media/                # User-uploaded images
└── manage.py                 # Django management script
```

## Core Features

### 🎮 **Ad Management**
Create, edit, and manage gaming product listings with image uploads and detailed descriptions.

### 🔍 **Advanced Filtering**
Multi-criteria search system with real-time AJAX filtering by:
- **Category**: Gaming consoles, accessories, games
- **Price Range**: Custom price filtering with min/max values
- **Location**: State-based regional filtering
- **Image Availability**: Filter ads with or without images
- **Text Search**: Keyword-based title search

### 👤 **User System**
- Email-based registration with verification
- Session-based authentication
- Personal ad management dashboard
- Save interesting ads for later review

### 📱 **Responsive Design**
- Mobile-first Bootstrap 4.4.1 implementation
- Custom SCSS styling with responsive breakpoints
- Collapsible navigation for mobile devices

## Features

🎮 **Gaming Marketplace**: Specialized platform for video games and console trading

🔍 **Smart Filtering**: Multi-dimensional search with real-time updates

📱 **Responsive UI**: Mobile-optimized Bootstrap interface

💾 **Save System**: Personal ad collection and management

👤 **User Authentication**: Email verification and session management

🛠️ **Admin Panel**: Content management through Django admin

🖼️ **Image Management**: Pillow integration for ad images

⚡ **AJAX Integration**: Seamless user experience with dynamic content loading

## Dependencies

**Core**: Django 2.1.5, SQLite
**Media**: Pillow (image processing)
**Frontend**: Bootstrap 4.4.1, Font Awesome, Custom SCSS
**Email**: Django SMTP backend for user verification

## Development Notes

- Built as a CS50 Web Programming final project
- Demonstrates full-stack Django development
- Implements modern web development practices
- Chat functionality marked for future development

**Watch all of my CS50's Web Programming with Python and JavaScript projects videos here:**  https://www.youtube.com/watch?v=taz8kCE_kBs&list=PLMmG0ZlUCOZLE9nKuDH0uvbppuA_ByOuM
