# add_product.py
import os
from supabase import create_client, Client #pip install supabase
from dotenv import load_dotenv # pip install python-dotenv
 
load_dotenv()
 
url = os.getenv("SUPABASE_URL")
key = os.getenv("SUPABASE_KEY")
sb: Client = create_client(url, key)
 
def display_availability():
    resp = sb.table("books").select("book_id, title, stock").execute()

    for book in resp.data:
        availability = "Available" if book["stock"] > 0 else "Out of Stock"
        print(f'{book["title"]} (Stock: {book["stock"]}) -> {availability}')

 
if __name__ == "__main__":
    display_availability()

 
 