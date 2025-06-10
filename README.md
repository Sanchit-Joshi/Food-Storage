# 🍎 Food Storage Management System

A Django-based web application designed to help you efficiently manage your food inventory, track expiration dates, and generate smart shopping lists. Never let food go to waste again!

## 🌟 Features

- **Inventory Management**: Add, edit, and delete food items with detailed information
- **Category Organization**: Organize food items by categories with ideal quantity tracking
- **Expiration Tracking**: Monitor items approaching their best-before dates
- **Smart Shopping Lists**: Generate shopping lists based on low stock items
- **Stock Overview**: Get a comprehensive view of your current inventory
- **Search Functionality**: Quickly find specific food items
- **Responsive Design**: Works seamlessly on desktop and mobile devices

## 🛠️ Tech Stack

- **Backend**: Django 5.2.1
- **Database**: SQLite (development) / PostgreSQL (production ready)
- **Frontend**: HTML, CSS, Bootstrap
- **Form Enhancement**: django-widget-tweaks
- **Containerization**: Docker & Docker Compose

## 📋 Prerequisites

Before you begin, ensure you have the following installed:

- Python 3.11 or higher
- pip (Python package installer)
- Git
- Docker (optional, for containerized deployment)

## 🚀 Quick Start

### Option 1: Local Development Setup

1. **Clone the repository**

   ```bash
   git clone https://github.com/yourusername/Food-Storage.git
   cd Food-Storage/food_project
   ```

2. **Create a virtual environment**

   ```bash
   python -m venv venv
   ```

3. **Activate the virtual environment**

   - Windows:
     ```bash
     venv\Scripts\activate
     ```
   - macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

4. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

5. **Apply database migrations**

   ```bash
   python manage.py migrate
   ```

6. **Create a superuser (optional)**

   ```bash
   python manage.py createsuperuser
   ```

7. **Run the development server**

   ```bash
   python manage.py runserver
   ```

8. **Access the application**
   Open your browser and navigate to `http://127.0.0.1:8000`

### Option 2: Docker Setup

1. **Clone the repository**

   ```bash
   git clone https://github.com/yourusername/Food-Storage.git
   cd Food-Storage/food_project
   ```

2. **Build and run with Docker Compose**

   ```bash
   docker-compose up --build
   ```

3. **Access the application**
   Open your browser and navigate to `http://localhost:8000`

## 📁 Project Structure

```
Food-Storage/
├── README.md
├── LICENSE
├── .gitignore
└── food_project/
    ├── manage.py
    ├── requirements.txt
    ├── Dockerfile
    ├── docker-compose.yml
    ├── db.sqlite3
    ├── food_project/          # Main project settings
    │   ├── __init__.py
    │   ├── settings.py
    │   ├── urls.py
    │   ├── wsgi.py
    │   └── asgi.py
    └── inventory/             # Main application
        ├── models.py          # Data models
        ├── views.py           # View functions
        ├── urls.py            # URL patterns
        ├── forms.py           # Django forms
        ├── admin.py           # Admin interface
        ├── apps.py
        ├── tests.py
        ├── migrations/        # Database migrations
        └── templates/         # HTML templates
            └── inventory/
                ├── home.html
                ├── add_food_item.html
                ├── edit_food.html
                ├── stock_overview.html
                ├── expiring_soon.html
                ├── shopping_list.html
                └── search_results.html
```

## 🎯 Usage Guide

### Adding Food Items

1. Navigate to the home page
2. Click "Add Food Item"
3. Fill in the required information:
   - Name
   - Category
   - Quantity and Unit
   - Best Before Date
   - Ideal Quantity

### Managing Categories

1. Go to "Add Category"
2. Create new categories with ideal quantities
3. Organize your food items efficiently

### Monitoring Expiration Dates

1. Visit "Expiring Soon"
2. See items approaching their best-before dates
3. Take action to prevent food waste

### Generating Shopping Lists

1. Access "Shopping List"
2. View items that are below their ideal quantities
3. Plan your grocery shopping efficiently

### Searching Items

1. Use the search functionality on the home page
2. Find specific food items quickly
3. View detailed information about each item

## 🔧 Configuration

### Environment Variables

For production deployment, create a `.env` file in the `food_project` directory:

```env
SECRET_KEY=your-secret-key-here
DEBUG=False
ALLOWED_HOSTS=yourdomain.com,www.yourdomain.com
DATABASE_URL=postgresql://user:password@localhost:5432/foodstorage
```

### Database Configuration

The project uses SQLite by default for development. For production, consider using PostgreSQL:

1. Install PostgreSQL adapter:

   ```bash
   pip install psycopg2-binary
   ```

2. Update `settings.py` with your database configuration

## 🧪 Testing

Run the test suite:

```bash
python manage.py test
```

Run specific app tests:

```bash
python manage.py test inventory
```

## 📦 Deployment

### Production Checklist

- [ ] Set `DEBUG = False`
- [ ] Configure proper `SECRET_KEY`
- [ ] Set up production database
- [ ] Configure static files serving
- [ ] Set up proper logging
- [ ] Configure email backend
- [ ] Set up monitoring

### Docker Production Deployment

1. Build production image:

   ```bash
   docker build -t food-storage:prod .
   ```

2. Run with environment variables:
   ```bash
   docker run -p 8000:8000 --env-file .env food-storage:prod
   ```

## 🤝 Contributing

We welcome contributions! Please follow these steps:

### Getting Started

1. **Fork the repository**

   ```bash
   git fork https://github.com/yourusername/Food-Storage.git
   ```

2. **Create a feature branch**

   ```bash
   git checkout -b feature/amazing-feature
   ```

3. **Set up development environment**
   ```bash
   cd Food-Storage/food_project
   python -m venv venv
   source venv/bin/activate  # or venv\Scripts\activate on Windows
   pip install -r requirements.txt
   python manage.py migrate
   ```

### Development Guidelines

- Follow PEP 8 style guidelines
- Write meaningful commit messages
- Add tests for new features
- Update documentation as needed
- Ensure all tests pass before submitting

### Code Style

- Use 4 spaces for indentation
- Maximum line length: 120 characters
- Use descriptive variable and function names
- Add docstrings to functions and classes

### Testing Guidelines

- Write unit tests for new models and views
- Test edge cases and error conditions
- Aim for high test coverage
- Use Django's built-in testing framework

### Submitting Changes

1. **Run tests**

   ```bash
   python manage.py test
   ```

2. **Commit your changes**

   ```bash
   git add .
   git commit -m "Add: Brief description of your feature"
   ```

3. **Push to your fork**

   ```bash
   git push origin feature/amazing-feature
   ```

4. **Create a Pull Request**
   - Provide a clear description of changes
   - Reference any related issues
   - Add screenshots for UI changes

### Reporting Issues

When reporting bugs, please include:

- Python and Django versions
- Steps to reproduce the issue
- Expected vs actual behavior
- Error messages (if any)
- Screenshots (for UI issues)

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Django community for the excellent framework
- Contributors who help improve this project
- Bootstrap for responsive design components

## 📞 Support

- **Issues**: [GitHub Issues](https://github.com/yourusername/Food-Storage/issues)
- **Discussions**: [GitHub Discussions](https://github.com/yourusername/Food-Storage/discussions)
- **Email**: your.email@example.com

## 🔄 Changelog

### v1.0.0 (Current)

- Initial release
- Basic inventory management
- Category organization
- Expiration tracking
- Shopping list generation
- Docker support

---

**Made with ❤️ for reducing food waste and efficient inventory management**
