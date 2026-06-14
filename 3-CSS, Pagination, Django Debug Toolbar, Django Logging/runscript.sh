#!/bin/bash

# Make migrations into the DB
python manage.py makemigrations
python manage.py migrate

# Seed the DB
python manage.py runscript import_category_records
python manage.py runscript import_product_records
python manage.py runscript import_stock_records
python manage.py runscript generate_product_review_openai