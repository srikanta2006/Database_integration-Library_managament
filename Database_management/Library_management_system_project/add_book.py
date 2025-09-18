# add_product.py
import os
from supabase import create_client, Client #pip install supabase
from dotenv import load_dotenv # pip install python-dotenv
 
load_dotenv()
 
url = os.getenv("SUPABASE_URL")
key = os.getenv("SUPABASE_KEY")
sb: Client = create_client(url, key)
 
def add_book(title, author, category, stock):
    payload = {"title": title, "author": author, "category": category, "stock":stock}
    resp = sb.table("books").insert(payload).execute()
    return resp.data
 
if __name__ == "__main__":
    title = input("Enter title of the book: ").strip()
    author = input("Enter author of the book: ").strip()
    category = input("Enter category of the book: ").strip()
    stock = int(input("Enter the stock available: "))
 
    created = add_book(title, author, category, stock)
    print("Added:", created)
 
 