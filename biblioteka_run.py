from app import app
from app.models import Book, Author, Borrow


@app.shell_context_processor
def make_shell_context():
    return {
        "Książka": Book,
        "Autor": Author,
        "Wypożyczenie": Borrow
    }