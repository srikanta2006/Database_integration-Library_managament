import os
from supabase import create_client, Client  # pip install supabase
from dotenv import load_dotenv  # pip install python-dotenv

load_dotenv()

url = os.getenv("SUPABASE_URL")
key = os.getenv("SUPABASE_KEY")
sb: Client = create_client(url, key)

def borrow(member_id, book_id):
    # Get current stock
    book = sb.table("books").select("stock").eq("book_id", book_id).execute()

    if book.data and book.data[0]["stock"] > 0:
        current_stock = book.data[0]["stock"]

        # Insert borrow record
        sb.table("borrow_records").insert({"member_id": member_id, "book_id": book_id}).execute()

        # Decrease stock by 1
        resp = sb.table("books").update({"stock": current_stock - 1}).eq("book_id", book_id).execute()
        return resp.data
    else:
        return None


if __name__ == "__main__":
    member_id = input("Enter id of the member: ").strip()
    book_id = input("Enter id of the book: ").strip()

    borrowed = borrow(member_id, book_id)

    if borrowed:
        print("Book borrowed")
    else:
        print("Stock not available")
