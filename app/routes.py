from flask import render_template, redirect, url_for, request, flash
from app import app, db
from app.models import Book, Author, Borrow
  

@app.route("/library/", methods=['GET', 'POST'])
def index():
    books = Book.query.all()

    if request.method == 'POST':
        book_id = request.form.get('book_id')
        book = Book.query.get(book_id)

        if request.form['action'] == 'Wypożyczenie':
            try:
                borrower_name = request.form['borrower_name']
                book.borrow_book(borrower_name)
            except KeyError:
                return "Nieprawidłowe żądanie", 400 

        elif request.form['action'] == 'Zwróć':
            if not book.borrows:
                return "Nie można zwrócić książki, która nie została wypożyczona"
            book.return_book()
        
        books = Book.query.all()

    return render_template('index.html', books=books)


@app.route("/library/add_book", methods=['POST'])
def add_book():
    title = request.form['title']
    author_name = request.form['author']
    author = Author.query.filter_by(name=author_name).first()

    if not author:
        author = Author(name=author_name)
        db.session.add(author)

    book = Book(title=title)
    book.authors.append(author)

    db.session.add(book)
    db.session.commit()

    return redirect(url_for('index'))


@app.route("/library/<int:book_id>", methods=['GET', 'POST'])
def book_details(book_id):
    book = Book.query.get(book_id)

    if request.method == 'POST':
        title = request.form['title']
        status = request.form['status']
        borrower_name = request.form['borrower_name']

        book.update_book(title, status, borrower_name)
        
        db.session.commit()

        flash('Zmiany zostały zapisane!', 'success')
        print("Flash message set.")
        return redirect(url_for('index'))
    
    return render_template('book_det.html', book=book)


if __name__ == "__main__":
    app.run(debug=True)
    

  


    



