
import os
from supabase import create_client, Client  # pip install supabase
from dotenv import load_dotenv  # pip install python-dotenv

load_dotenv()

url = os.getenv("SUPABASE_URL")
key = os.getenv("SUPABASE_KEY")
sb: Client = create_client(url, key)
def delete_member(member_id):
    borrowed = sb.table("borrow_records").select("*").eq("member_id", member_id).execute()
    if borrowed.data:  # has borrowed books
        return {"error": "Cannot delete member with borrowed books"}
    resp = sb.table("members").delete().eq("member_id", member_id).execute()
    return resp.data

if __name__ == "__main__":
    member_id = input("Enter id of the member to delete: ").strip()

    data=delete_member(member_id)
    if(data):
        print(data)
    else:
        print("Not found")