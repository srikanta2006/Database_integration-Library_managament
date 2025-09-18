# main.py
import sys

# Import functions from your files
from add_book import add_book
from add_member import add_member
from books_availability import display_availability
from search_book import search_books
from member_book_details import member_details
from update_book_stock import update_book_stock
from update_member_info import update_member
from delete_book import delete_book
from delete_member import delete_member
from borrow_book import borrow


def main():
    while True:
        print("\n====== Library Management System ======")
        print("1. Register new member")
        print("2. Add new book")
        print("3. List all books with availability")
        print("4. Search books")
        print("5. Show member details and borrowed books")
        print("6. Borrow a book")
        print("7. Update book stock")
        print("8. Update member info")
        print("9. Delete member")
        print("10. Delete book")
        print("0. Exit")
        choice = input("Enter choice: ").strip()

        match choice:
            case "1":
                name = input("Enter member name: ")
                email = input("Enter member email: ")
                print(add_member(name, email))

            case "2":
                title = input("Enter book title: ")
                author = input("Enter book author: ")
                category = input("Enter category: ")
                stock = int(input("Enter stock: "))
                print(add_book(title, author, category, stock))

            case "3":
                books = display_availability()
                for book in books:
                    print(book)

            case "4":
                keyword = input("Enter keyword (title/author/category): ")
                results = search_books(keyword)
                for book in results:
                    print(book)

            case "5":
                member_id = input("Enter member ID: ")
                details = member_details(member_id)
                print(details)

            case "6":
                member_id = input("Enter member ID: ")
                book_id = input("Enter book ID: ")
                print(borrow(member_id, book_id))

            case "7":
                book_id = input("Enter book ID: ")
                new_stock = int(input("Enter new stock: "))
                print(update_book_stock(book_id, new_stock))

            case "8":
                member_id = input("Enter member ID: ")
                new_email = input("Enter new email: ")
                print(update_member(member_id, new_email))

            case "9":
                member_id = input("Enter member ID: ")
                print(delete_member(member_id))

            case "10":
                book_id = input("Enter book ID: ")
                print(delete_book(book_id))

            case "0":
                print("Exiting...")
                sys.exit()

            case _:
                print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()
