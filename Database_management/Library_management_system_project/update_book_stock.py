import os
from supabase import create_client, Client #pip install supabase
from dotenv import load_dotenv # pip install python-dotenv
 
load_dotenv()
 
url = os.getenv("SUPABASE_URL")
key = os.getenv("SUPABASE_KEY")
sb: Client = create_client(url, key)


def update_book_stock(book_id, new_stock):
    resp = sb.table("books").update({"stock": new_stock}).eq("book_id", book_id).execute()
    return resp.data


if __name__ == "__main__":
    book_id = input("Enter book ID: ").strip()
    new_stock = int(input("Enter stock value to update: ").strip())
    updated=update_book_stock(book_id, new_stock)
    if(updated):
        print("Stock value updated", updated)
    else:
        print("Not updated")