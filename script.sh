pip install -r requirement.txt
python manage.py populate

# Convert static asset files
python manage.py collectstatic --no-input
