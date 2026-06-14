import random
import os
import openai
from openai import OpenAI
from dotenv import load_dotenv
from product.models import Product, Review

load_dotenv()

"""
Db seeding function for product-review table using GROQ-Cloud API.
"""

# Instantiate the GROQ-CLOUD API
client = OpenAI(
    api_key=os.getenv("GROQ_KEY"),
    base_url="https://api.groq.com/openai/v1"
)

# Function to generate product-review comment
def generate_review(product_name, rating):
    try:
        prompt = f"Write a realistic, one-sentence e-commerce product review for a '{product_name}'. The rating given is {rating}/5. Do not include the rating in the text."
        
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {"role": "user", "content": prompt}
            ]
        )
        return {
                "product": product_name,
                "rating": rating,
                "comment": response.choices[0].message.content.strip().strip('"')
            }
    except openai.RateLimitError as e:
        print(f"Rate limit error: {e}")
        return None

"""
***Sample GROQ-powered Product-Review record***

5 Sunflower Seeds
{
    'product': <Product: Sunflower Seeds>, 
    'rating': 4, 
    'comment': 'I was really pleased with the quality and freshness of these sunflower seeds, which germinated quickly and grew into healthy plants, although I did find the packaging to be a bit flimsy and prone to tearing.'
}
"""

def partial_insert(review_object, prod, missing=False):
    # Note: Request for product-review generation to GROQ only if the product-review-record does not exist; So that, it'll avoid invoking the GROQ-API unnecessarily for the product-review that's already exists.
    review = generate_review(product_name=prod, rating=random.randint(1, 5))

    if review:
        # Update the product-review object
        review_object.rating=review.get('rating')
        review_object.review_content=review.get('comment')
        review_object.save()

        if missing:
            print(f"Updated rating {review_object.rating} of review-id:{review_object.id} for product-id:{review_object.product.id}. Product: {review_object.product.name}. It data was missed to populate due to exceeding GROQ usage limit previously, thus populating now.")

        return False
    else:
        # Cannot generate the product-review, since the GROQ usage limit is exceeded.
        return True
        

def run():
    products = Product.objects.all()

    count = 1

    for prod in products:
        obj, created = Review.objects.get_or_create(product=prod)

        if created:
            count+=1

            # A single product-review record is created, but initially they review & rating table is empty; With this `partial_insert()` function, those fields will be populated.
            groq_limit_exceeded = partial_insert(review_object=obj, prod=prod)
            
            if groq_limit_exceeded:
                print("Groq Cloud API's rate limit is exceeded. Please try after the limit is reset.")
                break
            
            print(f"Count:{count} Product_Id:{obj.product.id} Product review: {obj}")
        else:
            # If the review-record gets created previously w/ only the product-id, and immediately after that creation, the GROQ usage limit exceed, (Later Period) only then the object's record will update the review & rating again.

            # Check if the retrieved product-review record has empty review & rating field, then again generate data for those fields using the GROQ Cloud API.
            if not (obj.rating and obj.review_content):
                groq_limit_exceeded = partial_insert(review_object=obj, prod=prod, missing=True)

                if groq_limit_exceeded:
                    print("Groq Cloud API's rate limit is exceeded. Please try after the limit is reset.")
                    break

            print(f"Skipped (already exists): {obj}")
        
    print(f"Total {count} records have been created!")