
def create_books_2Dlist(file_name):
    '''None->2D list'''
    lines = open(file_name).read().splitlines()
    books=[]
    for line in lines:
        raw_book=line.split('\t')
        book=[]

        # add date info first in iso format as it is good for comparisons
        (m,d,y) = raw_book[3].strip().split('/')
        isodate = y + '-' + ('0'+m)[-2: ] + '-' + ('0'+d)[-2: ]
        book.append(isodate)
        for i in range(len(raw_book)):
            if not(i==3):
                book.append(raw_book[i].strip())
        books.append(book)
    return books

def search_by_year(books, year1, year2):
    '''(2D list)->None'''
    print('\nAll Titles between', year1, 'and', str(year2)+':\n')
    count=0
    for book in books:
        if str(year1)+'-01'+'-01'<=book[0] and book[0]<=str(year2)+'-12'+'-31':
            print(book[1]+', by '+book[2], '('+book[0]+')')
            count=count+1
    if count==0:
        print("No books found in that range of years.")



file_name=input("Enter the name of the file: ")
file_name=file_name.strip()
books=create_books_2Dlist(file_name)

#print(books)
