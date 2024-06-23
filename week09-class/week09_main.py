from week09_prob import Book,Management, Magazine,Library
#1 main()
print("1번 main()\n")
#i
book1=Book('Python programming','John',2019)
book2=Book('Deep learning','Kelleher',2019)
book3=Book('Digital image processing','Pearson',2018)
#ii
management=Management(max_num=3)
management.Register_book(book1)
management.Register_book(book2)
management.Register_book(book3)
management.Check_out_book('Deep learning')
management.Check_out_book('Deep learning')
management.Check_out_book('Python home') 
management.Check_out_book('Python programming') 


management.Return_book('Deep learning') 
management.Display_all()

#2 main()
print("\n2번 main()\n")
mz1=Magazine('Science', 'John', 2020, 'Science', 67)
mz2=Magazine('Beauty','Adam', 2018, 'Fashion', 92)
mz3=Magazine('Style', 'Emma', 2019, 'Fashion', 43)
mz4=Magazine('New science', 'Steve', 2022, 'Science',73)
mz5=Magazine('Science', 'Sam', 2023, 'Science',79)
library=Library(max_num=5, library_name="BME", operation_hours='9 AM to 6 PM', location='seoul')
library.Register_book(mz1) 
library.Register_book(mz2) 
library.Register_book(mz3) 
library.Register_book(mz4)
library.Register_book(mz5)  
library.Display_library_info() 
library.Search_by_genre('Science')

