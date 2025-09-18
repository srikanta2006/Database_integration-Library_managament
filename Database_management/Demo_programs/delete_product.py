import os
from supabase import create_client, Client #pip install supabase
from dotenv import load_dotenv # pip install python-dotenv
 
load_dotenv()
 
url = os.getenv("SUPABASE_URL")
key = os.getenv("SUPABASE_KEY")
sb: Client = create_client(url, key)

def delete(id):
    resp = sb.table("products").delete().eq("product_id", id).execute()
    return resp.data

if __name__ == "__main__":
    id = input("Enter product ID to delete: ").strip()
    dele=delete(id)
    if(dele):
        print("product deleted")
    else:
        print("Unable to delete")