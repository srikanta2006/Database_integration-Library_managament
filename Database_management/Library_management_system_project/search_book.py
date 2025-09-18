import os
from supabase import create_client, Client #pip install supabase
from dotenv import load_dotenv # pip install python-dotenv
 
load_dotenv()
 
url = os.getenv("SUPABASE_URL")
key = os.getenv("SUPABASE_KEY")
sb: Client = create_client(url, key)

def search_books(keyword):
    resp = sb.table("books").select("*").or_(
        f"title.ilike.%{keyword}%,author.ilike.%{keyword}%,category.ilike.%{keyword}%"
    ).execute()
    return resp.data

if __name__ == "__main__":
    keyword = input("Enter author/title/category to search: ").strip()

    data=search_books(keyword)
    if(data):
        print(data)
    else:
        print("Not found")