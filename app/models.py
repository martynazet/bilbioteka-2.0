from app import db


books_authors = db.Table('books_authors',
    db.Column('book_id', db.Integer, db.ForeignKey('book.id')),
    db.Column('author_id', db.Integer, db.ForeignKey('author.id'))
    )
    

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(128), index=True)
    status = db.Column(db.String(50), default='Na półce')
    authors = db.relationship('Author', secondary=books_authors, back_populates='books')
    borrows = db.relationship('Borrow', back_populates='book')

    def borrow_book(self, borrower_name):
        borrow = Borrow(borrower_name=borrower_name)
        self.borrows.append(borrow)
        self.status = 'Wypożyczona'

        db.session.add(borrow)
        db.session.commit()

    def return_book(self):
        if self.borrows:
            self.borrows.pop()
            self.status = 'Na półce'
            db.session.commit()

    def update_book(self, title, status, borrower_name=None):
        self.title = title
        self.status = status
        if self.borrows:
            self.borrows[-1].borrower_name = borrower_name
        else:
            borrow = Borrow(borrower_name=borrower_name)
            self.borrows.append(borrow)
        
        db.session.commit()
        

class Author(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True)
    books = db.relationship('Book', secondary=books_authors, back_populates='authors')


class Borrow(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    book_id = db.Column(db.Integer, db.ForeignKey('book.id'))
    borrower_name = db.Column(db.String(64), index=True)
    book = db.relationship('Book', back_populates='borrows')