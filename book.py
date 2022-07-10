class Book:
    def __init__(self,id,name,description,isbn,page_count,issued,author,year):
        self.id = id
        self.name = name
        self.isbn = isbn 
        self.description = description 
        self.page_count = page_count
        self.issued = issued 
        self.author = author 
        self.year = year 
    # to dic method
    def to_dict(self):
        dictionary ={
            'id':self.id,
            'name':self.name,
            'description': self.description,
            'isbn': self.isbn,
            'page_count': self.page_count,
            'issued': self.issued,
            'author': self.author,
            'year': self.year
        }
        return dictionary
# book = Book(12,'Hustle','never_give_up','112-22-334',3444,True,'Sudhanshu',2011)