#Library Management System
#Book Operations Class
library = {}
class Book:
    def __init__(self, bookID, title, author):
        self.is_available = True
        self.title = title
        self.bookID = bookID
        self.author = author

    def get_title(self):
        return self.title
    
    def get_bookID(self):
        return self.bookID
    
    def get_author(self):
        return self.author
    
    def set_author(self, new_author):
        self.author = new_author
    
    def is_available(self):
        return self.is_available

    def add_book(library):
        bookID = input("Enter book ID: ")
        title = input("Enter title of book: ")
        author = input("Enter author of book: ")
        library[bookID] = Book(bookID, title, author)
        print(f"For ID {library[bookID].get_bookID()}, title: {library[bookID].get_title()} author: {library[bookID].get_author()} to book inventory. ")

    def availability(self):
        if self.is_available:
            self.is_available = False
            return True
        else:
            return False

    def borrow_book(self, library, userlist):
        bookID = input("Enter book ID: ")
        userID = input("Enter name of borrower: ")
        if bookID in library:
            if self.is_available:
                user.new_loanstatus = True
                self.is_available = False
                print(f"{library[bookID].get_title} checked out by {userlist[userID].get_user}")
            else:
                print(f"{library[bookID].get.title} is not available. ")
        else:
            print(f"{bookID} is not in library.")
  
    def return_book(library, userlist):
        bookID = input("Enter ID of book being returned: ")
        userID = input("Enter ID of borrower: ")
        if bookID in library:
            self.is_available = True
            userlist.new_loanstatus = False
            print(f"{library[bookID].get_title} returned by {userlist[userID].get_user}")
        else:
            print(f"{bookID} is not in valid. ")

    def search_book(self):
        try:
            bookID = input("Enter ID of book: ")
            if bookID in library:
                print(f"{library[bookID].get_title} is in library.")
        except ValueError as e:
            print(f"{bookID} is not valid.")
        except Exception as e:
            print(f"{bookID} is not in library.")

    def display_books(library):
        print("***Library Booklist***")
        for key, values in library.items():
            print(f"{library[bookID].get_bookID}, {library[bookID].get_title}, {library[bookID].get.author}")

#Library Management System
#User Operations Class
userlist = {}
class UserOps(Book):
    def __init__(self, user, userID, loanstatus):
        #super().__init__(self, bookID, title, author)
        self.__user = user
        self.__userID = userID
        self.loanstatus = False

    def get_user(self):
        return self.__user
    
    def get_userID(self):
        return self.__userID

    def get_loanstatus(self):
        return self.loanstatus
    
    def set_loanstatus(self, new_loanstatus):
        self.loanstatus = new_loanstatus

    def add_user(userlist):
        userID = input("Enter user ID: ")
        user = input("Enter name of user: ")
        userlist[userID] = UserOps(userID, user, loanstatus = False)
        print(f"For ID {userlist[userID].get_userID()}, user: {userlist[userID].get_user()} loanstatus: {userlist[userID].get_loanstatus()} ")


    def display_user(userlist):
        print("***User List***")
        for key, values in userlist.items():
            print(f"{userlist[userID].get_userID}, {userlist[userID].get_user}, {userlist[userID].get_loanstatus}")

#Library Management System
#Author Operations Class

authorlist = {}
class Author(Book):
    def __init__(self, title, author, biography):
        super().__init__(self, bookID, title, author)
        self.biography = biography

    def get_bio(self):
        return self. biography
    
    def set_bio(self, new_biography):
        self.biography = new_biography
    
    def display_authorinfo(self):
        title = input("Enter title of book to search for: ")
        if title in library:
            name = input("Enter name of author: ")
            name = self.author
            biography =  input("Enter short biography of author: ")
            authorlist[self.author] = Author(self.title, self.author, biography)
            print("This is a brief description of the author's information. ")
            print(f"Title {authorlist[title]}, Author {authorlist[self.author]}")
            print(f"Biography of {authorlist[title]}.")
        else:
            print(f"{title} not found.")
#Library Management System
#Genre Operations Class           

genrelist = ["fantasy", "horror", "science fiction", "classics", "comics", "comedy", "romance", "history", "thriller", "adventure"]
genres = {}
class Genre(Book):
    def __init__(self, bookID, title, author, description, category):
        super().__init__(self, title)
        self.description = description
        self.category = category

    def get_description(self):
        return self.description
    
    def get_category(self):
        return self.category
    
    def set_description(self, new_description):
        self.description = new_description

    def set_category(self, new_category):
        self.category = new_category

    def add_genre(library):
        title = input("Enter title: ")
        if title in library:
            category = input("Enter category of author: ")
            description = input("Enter description ")
            if description == "":
                description = "null"
            if category in genrelist:
                genres[self.title] = Genre(self.title, self.author, category, description)
            else:
                genres[self.title] = Genre(self.title, self.author, category, description)
        else:
            print(f"Title {title} is not in library.")

    def display_genre(genres):
        print("***Genre of Books List***")
        for key, values in genres.items():
            print(f"{genres[self.title].get_title}, {genres[self.title].get_category}, {genres[self.title].get.author}, {genres[self.title].get.description}")



            
    

def main():
    while True:       
        print("Welcome to the Library Management System")
        print("Main Menu")
        print("a - Book Operations ")
        print("b - User Operations ")
        print("c - Author Operations ")
        print("d - Genre Operations ")
        print("e - Quit ")
        choices = input("Enter the letter next to your choice, from a to e: ")

        if choices == "a":
            choice = int(input("Enter 1, 2, 3, 4, or 5 for which action you want to perform: "))
            if choice == 1:
                Book.add_book(library)
            if choice == 2:
                Book.borrow_book(library, userlist)
            if choice == 3:
                Book.return_book(library, userlist)
            if choice == 4:
                Book.search_book(library)
            if choice == 5:
                Book.display_books(library)
            else:
                print(f"Your choice {choice} is invalid")
        
        if choices == "b":
            choice = int(input("Enter 1, 2 for which action you want to perform: "))
            if choice == 1:
                UserOps.add_user(userlist)
            if choice == 2:
                UserOps.display_user(userlist)

        if choices == "c":
            Author.display_authorinfo(authorlist)

        if choices == "d":
            choice = int(input("Enter 1, 2 for which action you want to perform: "))
            if choice == 1:
                Genre.add_genre(genres)
            if choice == 2:
                Genre.display_genre(genres)

        if choices == "e":
            exit()

if __name__ == "__main__":
    main()