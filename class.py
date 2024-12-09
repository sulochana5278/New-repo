class libraryitem:
    def __init__(self,title,author,year):
        self.title  = title
        self.author = author
        self.year = year
    def display(self):
            print(f"my name is {self.author}")
    
class Books(libraryitem):
    def __init__(self,title,author,year,genre):
        super().__init__(title,author,year)
        self.genre=genre
    def display_info(self):
        print(f"title={self.title},author={self.author},year={self.year},genre={self.genre}")
books_instance=Books("Paddington","Michael Bond","1958","Halloween")
books_instance.display_info()

class Magazine (libraryitem):
    def __init__(self,title,author,year,issue_number):
        super().__init__(title,author,year)
        self.issue_number=issue_number
    def display_info(self):
        print(f"title={self.title},author={self.author},year={self.year},issue_number={self.issue_number}")
magazine_instance=Magazine("Time_magazine","Henry Luce","1923","10")
print("my name is amulya")
magazine_instance.display_info()


#iam using list to keep track of libraryitems

libraryitem=[] #created a empty list
libraryitem.append(Books("Paddington","Michael Bond","1958","Halloween"))#then iam adding instances of books by using append to add items in a empty list
libraryitem.append(Magazine("Time_magazine","Henry Luce","1923","10"))

for item in libraryitem:
    item.display_info()
    print()