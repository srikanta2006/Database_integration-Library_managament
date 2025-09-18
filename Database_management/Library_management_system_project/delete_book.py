
import os
from supabase import create_client, Client  # pip install supabase
from dotenv import load_dotenv  # pip install python-dotenv

load_dotenv()

url = os.getenv("SUPABASE_URL")
key = os.getenv("SUPABASE_KEY")
sb: Client = create_client(url, key)
def delete_book(book_id):
    borrowed = sb.table("borrow_records").select("*").eq("book_id", book_id).execute()
    if borrowed.data:  # book is borrowed
        return {"error": "Cannot delete book that is borrowed"}
    resp = sb.table("books").delete().eq("book_id", book_id).execute()
    return resp.data


if __name__ == "__main__":
    book_id = input("Enter id of the book to delete: ").strip()

    data=delete_book(book_id)
    if(data):
        print(data)
    else:
        print("Not found")