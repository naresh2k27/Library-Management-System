from main import Library, Book, Member


def test_add_book_success():
    library = Library()
    book = Book(101, "DSA", "Striver", 10, 10)

    result = library.add_book(book)

    assert result == "Book Added SuccessFully!"
    assert len(library.books) == 1
    assert 101 in library.books


def test_add_duplicate_book():
    library = Library()
    book = Book(101, "DSA", "Striver", 10, 10)

    library.add_book(book)

    result = library.add_book(book)

    assert result == "Book Already Exists in Library!"
    assert len(library.books) == 1


def test_register_member_success():
    library = Library()

    member = Member(1, "Naresh")

    result = library.register_member(member)

    assert result == "Member Registered SuccessFully!"
    assert len(library.members) == 1
    assert 1 in library.members


def test_register_duplicate_member():
    library = Library()

    member = Member(1, "Naresh")

    library.register_member(member)

    result = library.register_member(member)

    assert result == "Member Already Exists in Library!"
    assert len(library.members) == 1


def test_remove_book_success():
    library = Library()

    book = Book(101, "DSA", "Striver", 10, 10)

    library.add_book(book)

    result = library.remove_book(101)

    assert result == "Book removed Successfully!"
    assert len(library.books) == 0
    assert 101 not in library.books


def test_remove_book_not_found():
    library = Library()

    result = library.remove_book(101)

    assert result == "Book Not Found!"
    assert len(library.books) == 0


def test_borrow_book_success():
    library = Library()

    book = Book(101, "DSA", "Striver", 5, 5)
    member = Member(1, "Naresh")

    library.add_book(book)
    library.register_member(member)

    result = library.borrow_book(1, 101)

    assert result == "Yes the book is avilable and you can borrow it ! "
    assert book.available_copies == 4
    assert 101 in member.borrowed_books


def test_borrow_book_no_copies():
    library = Library()

    book = Book(101, "DSA", "Striver", 5, 0)
    member = Member(1, "Naresh")

    library.add_book(book)
    library.register_member(member)

    result = library.borrow_book(1, 101)

    assert result == "Sorry Copies of this book are Unavilable now!"
    assert book.available_copies == 0
    assert member.borrowed_books == []


def test_return_book_success():
    library = Library()

    book = Book(101, "DSA", "Striver", 5, 5)
    member = Member(1, "Naresh")

    library.add_book(book)
    library.register_member(member)

    library.borrow_book(1, 101)

    result = library.return_book(1, 101)

    assert result == "Book Returned Successfully!"
    assert book.available_copies == 5
    assert member.borrowed_books == []


def test_search_by_title():
    library = Library()

    book1 = Book(101, "DSA", "Striver", 5, 5)
    book2 = Book(102, "OS", "Galvin", 3, 3)

    library.add_book(book1)
    library.add_book(book2)

    result = library.search_by_title("DSA")

    assert len(result) == 1
    assert result[0].book_id == 101
    assert result[0].title == "DSA"
