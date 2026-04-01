class Book:
    def __init__(self, book_id, title, author):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.is_available = True


class Member:
    def __init__(self, member_id, name):
        self.member_id = member_id
        self.name = name
        self.borrowed_books = []


class Library:
    def __init__(self):
        self.books = {}
        self.members = {}

    def add_book(self):
        book_id = input("Enter Book ID: ")
        title = input("Enter Title: ")
        author = input("Enter Author: ")

        self.books[book_id] = Book(book_id, title, author)
        print("Book added successfully!")

    def add_member(self):
        member_id = input("Enter Member ID: ")
        name = input("Enter Name: ")

        self.members[member_id] = Member(member_id, name)
        print("Member added successfully!")

    def lend_book(self):
        book_id = input("Enter Book ID: ")
        member_id = input("Enter Member ID: ")

        if book_id in self.books and member_id in self.members:
            book = self.books[book_id]
            member = self.members[member_id]

            if book.is_available:
                book.is_available = False
                member.borrowed_books.append(book)
                print("Book issued successfully!")
            else:
                print("Book is not available!")
        else:
            print("Invalid Book ID or Member ID!")

    def return_book(self):
        book_id = input("Enter Book ID: ")
        member_id = input("Enter Member ID: ")

        if book_id in self.books and member_id in self.members:
            book = self.books[book_id]
            member = self.members[member_id]

            if book in member.borrowed_books:
                book.is_available = True
                member.borrowed_books.remove(book)
                print("Book returned successfully!")
            else:
                print("This member didn't borrow the book!")
        else:
            print("Invalid Book ID or Member ID!")

    def display_books(self):
        print("\n--- Book List ---")
        for book in self.books.values():
            status = "Available" if book.is_available else "Issued"
            print(f"{book.book_id} | {book.title} | {book.author} | {status}")


# Menu-driven system
library = Library()

while True:
    print("\n--- Library Menu ---")
    print("1. Add Book")
    print("2. Add Member")
    print("3. Lend Book")
    print("4. Return Book")
    print("5. Display Books")
    print("6. Exit")

    choice = input("Enter choice: ")

    if choice == '1':
        library.add_book()
    elif choice == '2':
        library.add_member()
    elif choice == '3':
        library.lend_book()
    elif choice == '4':
        library.return_book()
    elif choice == '5':
        library.display_books()
    elif choice == '6':
        print("Exiting...")
        break
    else:
        print("Invalid choice!")