import os
from supabase import create_client, Client  # pip install supabase
from dotenv import load_dotenv  # pip install python-dotenv

load_dotenv()

url = os.getenv("SUPABASE_URL")
key = os.getenv("SUPABASE_KEY")
sb: Client = create_client(url, key)

def member_details(member_id):
    # Get member info
    member = sb.table("members").select("*").eq("member_id", member_id).execute()
    # Get borrowed books
    borrowed = (
        sb.table("borrow_records")
        .select("book_id, books(title, author)")
        .eq("member_id", member_id)
        .execute()
    )
    return {"member": member.data, "borrowed_books": borrowed.data}

if __name__ == "__main__":
    member_id = input("Enter id of the member to display: ").strip()

    data=member_details(member_id)
    if(data):
        print(data)
    else:
        print("Not found")

    
