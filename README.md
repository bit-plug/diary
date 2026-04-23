# Learning Log

A Django web application that helps users keep track of their learning journey. Users can create topics for different subjects they're learning and add entries (notes) to document their progress, thoughts, and insights.

## Features

- **User Authentication**: Secure registration and login system
- **Private Learning Logs**: Each user owns their own topics and entries
- **Topic Management**: Create, view, and organize learning topics
- **Entry Tracking**: Add detailed notes and entries to topics
- **Entry Editing**: Modify existing entries as learning progresses
- **Responsive Design**: Built with Bootstrap 5 for mobile-friendly interface

## Technology Stack

- **Backend**: Django 6.0.1
- **Frontend**: HTML, CSS, Bootstrap 5
- **Database**: SQLite (development), configurable for production
- **Authentication**: Django's built-in authentication system

## Installation

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd learning_log
   ```

2. **Create and activate virtual environment**:
   ```bash
   python -m venv ll_env
   source ll_env/bin/activate  # On Windows: ll_env\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run migrations**:
   ```bash
   python manage.py migrate
   ```

5. **Create superuser (optional)**:
   ```bash
   python manage.py createsuperuser
   ```

6. **Run the development server**:
   ```bash
   python manage.py runserver
   ```

7. **Access the application**:
   Open your browser and go to `http://127.0.0.1:8000/`

## Usage

1. **Register**: Create a new account or login if you already have one
2. **Create Topics**: Add subjects you're currently learning
3. **Add Entries**: Write detailed notes about your learning progress
4. **Edit Entries**: Update your entries as you gain more insights
5. **Track Progress**: Review your learning journey over time

## Project Structure

```
learning_log/
├── learning_log/          # Main Django project settings
├── learning_logs/         # Main app for topics and entries
├── users/                 # User authentication app
├── templates/             # HTML templates
├── static/                # Static files (CSS, JS, images)
├── db.sqlite3            # SQLite database
├── manage.py             # Django management script
└── ll_env/               # Virtual environment
```

## Models

- **Topic**: Represents a learning subject (e.g., "Python Programming")
- **Entry**: Individual notes or entries related to a topic

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## License

This project is open source and available under the [MIT License](LICENSE).
