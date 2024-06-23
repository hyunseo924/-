#%%
#1
class Book:
    def __init__(self,title,author,publication_year):
        self.title=title
        self.author=author
        self.publication_year=publication_year
        self.borrow_status=False
     
    def Process_borrow(self):
        if self.borrow_status==True:
            print("The information is incorrect...<대여 중>")
            return 
        self.borrow_status=True
    def Process_return(self):
        if self.borrow_status==False:
            print("The information is incorrect...<이미 반납 된 책>")
            return 
        self.borrow_status=False
    def Display_book_info(self):
        print(f"{self.title}/ {self.author}/ {self.publication_year}/ {self.borrow_status}")

    
class Management:
    
    def __init__(self,max_num=5):
        self.Books=[]      
        self.max_num=max_num
        
    def Register_book(self,book_num):
        if len(self.Books)<self.max_num:
            self.Books.append(book_num)
        else: 
            print("Memory is full. You can no longerregister.")
            print("*********************************************")
            
    def Check_out_book(self,title):
        for i in range(len(self.Books)):
            if self.Books[i].title == title:
                self.Books[i].Process_borrow()
                self.Books[i].Display_book_info()
                print("*********************************************")
                return
        print("The information is incorrect..<an unregistered book>")
        print("*********************************************")

    def Return_book(self,title):
        for i in range(len(self.Books)):
            if self.Books[i].title == title:
                self.Books[i].Process_return()
                self.Books[i].Display_book_info()
                print("*********************************************")
                return 
        print("The information is incorrect...<an unregistered book>")
        print("*********************************************")

    def Search_book(self,title):
        for i in range(len(self.Books)):
            if self.Books[i].title==title:
                self.Books[i].Display_book_info()
                return 
        print("The information is incorrect. <{self.title} doesn't exist.>")
        print("*********************************************")

    def Display_all(self):
        for i in range(len(self.Books)):
            self.Books[i].Display_book_info()
        print("*********************************************")

#2
import random
Books=[]
class Magazine(Book):
    def __init__(self, title, author, publication_year,genre,volume):
        super().__init__(title, author, publication_year)
        self.borrow_status=False
        self.genre=genre
        self.volume=volume
        book_id=''
        for i in range(5): 
            book_id += random.choice(['A','B','C','1','2','3','4','5','6','7','8','9'])
        self.book_id=book_id
    def Display_book_info(self):
        print(f"{self.title}/ {self.author}/ {self.publication_year}/ {self.borrow_status}/ {self.genre}/ {self.book_id}")
  
class Library(Management):
    def __init__(self,max_num,library_name,operation_hours,location):
        super().__init__(max_num)
        self.library_name=library_name
        self.operation_hours=operation_hours
        self.location=location
        self.category={}
    
    def Display_library_info(self):
        print("*******************************************")
        print(f"Library name: {self.library_name}\nOperation hours: {self.operation_hours}\nLocation: {self.location}\n")
        print("*******************************************")

    def Register_book(self, book_num):
        if len(self.Books)<self.max_num:
            for i in self.Books:
                if i.book_id == book_num.book_id:
                    print("이미 존재하는 book id입니다. Magazine에 새로 등록하여 다른 id를 받으세요.")
                    break
            self.Books.append(book_num)
        else: 
            print("Memory is full. You can no longerregister.")
            return
        if type(book_num) == Magazine:
            if book_num.genre in self.category.keys():
                self.category[book_num.genre].append(book_num)
            else:
                self.category[book_num.genre]=[book_num]
    def Search_by_genre(self,genre):
        if genre in self.category.keys():  
            print(f"Magazine of {genre} genre:")
            sorted_mz=self.Sort_by_volume(self.category[genre])
            for mz in sorted_mz:
                mz.Display_book_info()
        else:
            print(f"There are no magazine of the {genre}")
    def Sort_by_volume(self,selected_mz):
        return sorted(selected_mz, key=lambda a: (a.title, a.volume))

