import csv
import os
from product.models import Category

def run():
    # Construct the absolute path to the CSV file
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    csv_path = os.path.join(base_dir, 'scripts', 'seeds/category_data.csv')

    with open(csv_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)    # Returns an iterator; each line converts into a list for the `reader()` function
        next(reader)  # Skip the header row

        count = 0

        for row in reader:
            # Adjust row indices (row[0], row[1], etc.) based on your CSV columns
            print(count, row)
            obj, created = Category.objects.get_or_create(
                name=row[1]
            )

            if created:
                count += 1
            else:
                print(f"Skipped (already exists): {obj}")
        
        print(f"Total {count} records have been created!")