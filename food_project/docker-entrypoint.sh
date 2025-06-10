#!/bin/bash

# Exit on any failure
set -e

echo "Starting Django application..."

# Wait for database to be ready (if using external database)
echo "Waiting for database..."
while ! python -c "
import django
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'food_project.settings')
django.setup()
from django.db import connections
from django.db.utils import OperationalError
try:
    connections['default'].cursor()
    print('Database is ready!')
except OperationalError:
    exit(1)
"; do
  echo "Database is unavailable - sleeping"
  sleep 1
done

echo "Database is up - continuing..."

# Apply database migrations
echo "Applying database migrations..."
python manage.py migrate --noinput

# Collect static files
echo "Collecting static files..."
python manage.py collectstatic --noinput --clear

# Create superuser if it doesn't exist (optional)
if [ "$DJANGO_SUPERUSER_USERNAME" ] && [ "$DJANGO_SUPERUSER_PASSWORD" ] && [ "$DJANGO_SUPERUSER_EMAIL" ]; then
    echo "Creating superuser..."
    python manage.py shell -c "
from django.contrib.auth import get_user_model
User = get_user_model()
if not User.objects.filter(username='$DJANGO_SUPERUSER_USERNAME').exists():
    User.objects.create_superuser('$DJANGO_SUPERUSER_USERNAME', '$DJANGO_SUPERUSER_EMAIL', '$DJANGO_SUPERUSER_PASSWORD')
    print('Superuser created successfully')
else:
    print('Superuser already exists')
"
fi

echo "Starting Django server..."

# Execute the main command
exec "$@"
