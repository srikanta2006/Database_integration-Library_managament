import os
from supabase import create_client, Client #pip install supabase
from dotenv import load_dotenv # pip install python-dotenv
 
load_dotenv()
 
url = os.getenv("SUPABASE_URL")
key = os.getenv("SUPABASE_KEY")
sb: Client = create_client(url, key)


def update_member(member_id, new_email):
    resp = sb.table("members").update({"email": new_email}).eq("member_id", member_id).execute()
    return resp.data



if __name__ == "__main__":
    member_id = input("Enter member ID: ").strip()
    new_email = input("Enter email_id to update: ").strip()
    updated=update_member(member_id, new_email)
    if(updated):
        print("Updated", updated)
    else:
        print("Not updated")