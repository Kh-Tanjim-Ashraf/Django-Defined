import csv
import os
from product.models import Product

def run():
    # Construct the absolute path to the CSV file
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    csv_path = os.path.join(base_dir, 'scripts', 'product_data.csv')

    print(f"Reading data from: {csv_path}")

    with open(csv_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)  # Skip the header row

        count = 0

        for row in reader:
            # Adjust row indices (row[0], row[1], etc.) based on your CSV columns
            print(count, row)
            obj, created = Product.objects.get_or_create(
                name=row[0],
                quantity=row[1],
                price=row[2],
            )
            
            if created:
                count += 1
            else:
                print(f"Skipped (already exists): {obj}")

        print(f"Total {count} records have been created!")        

