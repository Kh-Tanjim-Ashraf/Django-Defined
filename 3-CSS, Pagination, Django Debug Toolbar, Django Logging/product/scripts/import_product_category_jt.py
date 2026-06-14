import csv
import os
from product.models import Product

def run():
    """
    Seeder function for Product-Category joining table
    """
    # Construct the absolute path to the CSV file
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    csv_path = os.path.join(base_dir, 'scripts', 'seeds/product_category_data.csv')

    with open(csv_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)    # Returns an iterator; each line converts into a list for the `reader()` function
        next(reader)  # Skip the header row

        count = 0

        for row in reader:
            # Adjust row indices (row[0], row[1], etc.) based on your CSV columns
            print(count, row)
            product = Product.objects.get(id=row[0])
            product.category.add(row[1])
            count += 1
        
        print(f"Total {count} records have been created!")