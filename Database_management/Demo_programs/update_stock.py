import os
from supabase import create_client, Client #pip install supabase
from dotenv import load_dotenv # pip install python-dotenv
 
load_dotenv()
 
url = os.getenv("SUPABASE_URL")
key = os.getenv("SUPABASE_KEY")
sb: Client = create_client(url, key)

def update(id, stock):
    resp = sb.table("products").update({"stock":stock}).eq("product_id",id).execute()
    return resp.data

if __name__ == "__main__":
    id = input("Enter product ID: ").strip()
    stock = int(input("Enter stock value to update: ").strip())
    updated=update(id, stock)
    if(updated):
        print("Stock value updated", updated)
    else:
        print("Not updated")
    
 