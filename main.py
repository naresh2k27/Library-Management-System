import json
from dataclasses import dataclass, field


@dataclass
class Book:

    book_id: int
    title: str
    author: str
    total_copies: int
    available_copies: int

    def display_details(self) -> str:
        return f"Book ID: {self.book_id}\nBook Title: {self.title}\nAuthor of the Book: {self.author}\nTotal No.of Available Copies: {self.available_copies}\nTotal No.of Copies of the Book: {self.total_copies}\n"


@dataclass
class Member:
    member_id: int
    member_name: str
    borrowed_books: list[int] = field(default_factory=list)

    def display_details(self) -> str:
        return f"Member ID: {self.member_id}\nMember Name: {self.member_name}\nBorrowed Books: {self.borrowed_books}\n"


class Library:
    def __init__(self):
        self.books: dict[int, Book] = {}
        self.members: dict[int, Member] = {}

    def add_book(self, book: Book) -> str:
        if book.book_id not in self.books:
            self.books[book.book_id] = book
            return "Book Added SuccessFully!"

        return "Book Already Exists in Library!"

    def remove_book(self, book_id: int) -> str:

        if book_id not in self.books:
            return "Book Not Found!"

        book = self.books[book_id]

        if book.available_copies != book.total_copies:
            return "Not eligible for Remove the Book as still some copies are to be handover"

        del self.books[book_id]

        return "Book removed Successfully!"

    def register_member(self, member: Member) -> str:
        if member.member_id not in self.members:
            self.members[member.member_id] = member
            return "Member Registered SuccessFully!"

        return "Member Already Exists in Library!"

    def borrow_book(self, member_id: int, book_id: int) -> str:

        if member_id not in self.members:
            return "Sorry Member Not registered in library!"

        if book_id not in self.books:
            return "Sorry This book Not Available In this Library!"

        book = self.books[book_id]
        member = self.members[member_id]

        if book_id in member.borrowed_books:
            return "Member Already Borrowed this book!"

        if len(member.borrowed_books) >= 3:
            return "Sorry You have reached maximum limit of borrowed books so you cannot borrow"

        if book.available_copies <= 0:
            return "Sorry Copies of this book are Unavilable now!"

        book.available_copies -= 1
        member.borrowed_books.append(book_id)

        return "Yes the book is avilable and you can borrow it ! "

    def return_book(self, member_id: int, book_id: int) -> str:

        if member_id not in self.members:
            return "Sorry Member Not registered in library!"

        if book_id not in self.books:
            return "Sorry This book Not There In this Library!"

        book = self.books[book_id]
        member = self.members[member_id]

        if book_id not in member.borrowed_books:
            return "Member Did Not Borrowed this book!"

        book.available_copies += 1
        member.borrowed_books.remove(book_id)

        return "Book Returned Successfully!"

    def search_by_title(self, title: str) -> list[Book]:
        matching_books = []
        title = title.strip().lower()
        for book in self.books.values():
            if book.title.strip().lower() == title:
                matching_books.append(book)

        return matching_books

    def search_by_author(self, author: str) -> list[Book]:
        matching_books = []
        author = author.strip().lower()
        for book in self.books.values():
            if book.author.strip().lower() == author:
                matching_books.append(book)

        return matching_books

    def view_books(self) -> None:
        if not self.books:
            print("No Books Available!")
            return

        for book in self.books.values():
            print(book.display_details())

    def view_members(self) -> None:
        if not self.members:
            print("No Members Registered!")
            return

        for member in self.members.values():
            print(member.display_details())


def show_menu():
    while True:
        print("""========= Library Management =========

1. Add Book
2. Remove Book
3. Register Member
4. Borrow Book
5. Return Book
6. Search by Title
7. Search by Author
8. View Books
9. View Members
10. Exit
======================================""")
        try:
            choice = int(input())
            if choice < 1 or choice > 10:
                print("Enter Number From 1-10 only")
                continue
            return choice
        except ValueError:
            print("Enter Number From 1-10 only")


def take_book(library: Library) -> Book:
    while True:
        try:
            book_id: int = int(input("Enter Book's ID:"))
            if book_id in library.books:
                print("Book_id Already Exists!")
                continue
            break
        except ValueError:
            print("Invalid Integer!")

    title: str = input("Enter Book's Title:")
    author: str = input("Enter Author's Name:")
    while True:
        try:
            total_books: int = int(input("Enter Total No.Of Books:"))
            if total_books <= 0:
                print("Please Enter Positive Number of Books only!")
                continue
            else:
                break
        except ValueError:
            print("Invalid Integer")

    return Book(book_id, title, author, total_books, total_books)


def take_book_id() -> int:
    while True:
        try:
            book_id: int = int(input("Enter Book's ID:"))
            return book_id

        except ValueError:
            print("Invalid Integer!")


def take_member_id() -> int:
    while True:
        try:
            member_id: int = int(input("Enter Member's ID:"))
            return member_id
        except ValueError:
            print("Invalid Integer!")


def take_member(library: Library) -> Member:
    while True:
        try:
            member_id: int = int(input("Enter Member's ID:"))
            if member_id in library.members:
                print("Member_id Already Exists!")
                continue
            break
        except ValueError:
            print("Invalid Integer!")
    member_name = input("Enter Member Name:")

    return Member(member_id, member_name)


def load_books(library):

    try:
        with open("books.json") as f:
            book_json = json.load(f)
            for key in book_json:
                book_id = book_json[key]["book_id"]
                title = book_json[key]["title"]
                author = book_json[key]["author"]
                total_books = book_json[key]["total_copies"]
                available_copies = book_json[key]["available_copies"]

                b = Book(book_id, title, author, total_books, available_copies)

                library.add_book(b)
    except FileNotFoundError:
        return


def save_books(library):

    with open("books.json", "w") as f:
        books_dic = {}
        book = library.books
        for key in book:
            books_dic[key] = {
                "book_id": key,
                "title": book[key].title,
                "author": book[key].author,
                "total_copies": book[key].total_copies,
                "available_copies": book[key].available_copies,
            }
        json.dump(books_dic, f, indent=2, sort_keys=True)


def load_members(library):

    try:
        with open("members.json") as f:
            member_json = json.load(f)
            for key in member_json:
                member_id = member_json[key]["member_id"]
                member_name = member_json[key]["member_name"]
                borrowed_books = member_json[key]["borrowed_books"]

                m = Member(member_id, member_name)
                m.borrowed_books = borrowed_books

                library.register_member(m)

    except FileNotFoundError:
        return


def save_members(library):

    with open("members.json", "w") as f:
        members_dic = {}
        member = library.members
        for key in member:
            members_dic[key] = {
                "member_id": key,
                "member_name": member[key].member_name,
                "borrowed_books": member[key].borrowed_books,
            }
        json.dump(members_dic, f, indent=2, sort_keys=True)


def main():
    library = Library()
    load_books(library)
    load_members(library)

    while True:
        choice = show_menu()

        match choice:
            case 1:
                print(library.add_book(take_book(library)))
                save_books(library)
            case 2:
                print(library.remove_book(take_book_id()))
                save_books(library)
            case 3:
                print(library.register_member(take_member(library)))
                save_members(library)
            case 4:
                print(library.borrow_book(take_member_id(), take_book_id()))
                save_books(library)
                save_members(library)
            case 5:
                print(library.return_book(take_member_id(), take_book_id()))

                save_books(library)
                save_members(library)
            case 6:
                title: str = input("Enter Title of the book")
                books = library.search_by_title(title)
                if not books:
                    print("No Books Found with this Title!")

                for book in books:
                    print(book.display_details())

            case 7:
                author: str = input("Enter Author name of the Book")
                books = library.search_by_author(author)
                if not books:
                    print("No Books Found with this Author!")
                for book in books:
                    print(book.display_details())

            case 8:
                library.view_books()

            case 9:
                library.view_members()

            case 10:
                break


if __name__ == "__main__":
    main()
