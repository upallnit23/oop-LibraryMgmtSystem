#Library Management System
#Book Operations Class

class Book:
    def __init__(self, title):
        self.booklist = {"Python for Beginners": 6, "The Light in Us": 2} #Book array in dict. form, with title and stock number
        self.title = title

    def add_book(self):
        title = input("Enter title of book: ")
        amount = int(input("Enter amount of book title to add"))
        if title in self.booklist:
            self.booklist[title] += amount
        else:
            self.booklist[title] = amount
        print(f"{title} added to bookstore.")

    def borrow_book(self, title, new_userID):
        if self.booklist.get(title) > 0:
            new_userID = int(input("Enter userID: "))
            self.set_userID(new_userID)
            self.booklist[title] -= 1
            self.booklist.update[userID] = new_userID
            self.booklist[new_userID] += title
            self.booklist.user_status(status)
            print(f"{title} borrowed by {new_userID}.")
        else:
            (f"{title} is not available.")

    def return_book(self, self.__userID, self.__status):
        title = input("Enter title of book returned: ")
        if title in self.booklist:
            self.booklist[title] += 1
            self.booklist.user_status(self.__status)
            self.booklist.retuser_status(self.__status)
            print(f"{title} returned by {self.__userID}.")
        else:
            print(f"{title} not found.")

    def search4_book(self):
        title = input("Enter title of book to search for: ")
        if title in self.booklist:
            print(f"{self.booklist[title]} is found.")
        else:
            print(f"{self.booklist[title]} not found.")


    def display_books(self):
        print("***Library Booklist***")
        for title, amount in self.booklist.items()
        print(f"{self.booklist[title]}, {self.booklist[amount]}")

#Library Management System
#User Operations Class

class UserOperations(Book):
    def __init__(self, title, username, userID, status):
        super().__init__(self, title)
        self.__username = username
        self.__userID = userID
        self.__status = status

    def get_username(self):
        return self.__username
    
    def get_userID(self):
        return self.__userID

    def get_status(self):
        return self.__status
    
    def set_status(self, new_status):
        self.__status = new_status

    def user_status(self, userID, status):
        self.booklist[status] += "borrowed"
    
    def retuser_status(self, userID, status):
        self.booklist[status] += "returned"
    
    def display_user_status(self):
        print("***User Status***")
        for userID, status in self.booklist.items()
        print(f"{self.booklist[userID]}, {self.booklist[status]}")
#Library Management System
#Author Operations Class

authorlist = []

class Author(Book):
    def __init__(self, title, name, biography):
        super().__init__(self, title)
        self.name = name
        self.biography = biography
    
    def display_authorinfo(self):
        title = input("Enter title of book to search for: ")
        if title in self.booklist:
            self.name = input("Enter name of author: ")
            self.biography =  input("Enter short biography of author: ")
            #authorlist.append(title)
            authorlist.update({"Title": title, "Author": self.name, "Biography": self.biography})
            print("This is a brief description of the author's information. ")
            print(f"Title {authorlist[title]}, Author {authorlist[self.name]}")
            print(f"Biography of {authorlist[title]}.")
        else:
            print(f"{self.booklist[title]} not found.")
#Library Management System
#Genre Operations Class           

genrelist = ["fantasy", "horror", "science fiction", "classics", "comics", "comedy", "romance", "history", "thriller", "adventure"]

class Genre(Book):
    def __init__(self, title, description, category):
        super().__init__(self, title)
        self.description = description
        self.category = category

    def add_genre(self):
        title = input("Enter title of book: ")
        if title in self.booklist:
            print("Genre list is printed below ")
            print(genrelist)
            category = input("Enter category of book: ")
            if 
            description = input("Enter brief description of book: ")
            category = input("Enter category of title: ")
        if category in genrelist:
        print(f"{title} added to bookstore.")
    

    """def main():
        print("Welcome to the Library Management System")
        print("Main Menu")
        print("1. Book Operations ")
        print("2. User Operations ")
        print("3. Author Operations ")
        print("4. Genre Operations ")
        print("5. Quit ")
        choice = int(input("Enter 1, 2, 3, 4, or 5 for which action you want to perform: "))

        if choice is 1:
            add_book()
        if choice is 2:
            borrow_book()
        if choice is 3:
            return_book()
        if choice is 4:
            search4_book()
        if choice is 5:
            display_booklist()
        else:
            print("Thank you for using the Library Management System")
            exit()"""