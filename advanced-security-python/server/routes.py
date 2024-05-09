
from flask import request, render_template, make_response

from server.webapp import flaskapp, cursor
from server.models import Book


@flaskapp.route('/')
def index():
    name1 = request.args.get('name')
    author = request.args.get('author')
    read = bool(request.args.get('read'))

    
    if name1:
        cursor.execute(
            "SELECT * FROM books WHERE name LIKE '%" + name1 + "%'"
        )
        books = [Book(*row) for row in cursor]

    elif author:
        cursor.execute(
            "SELECT * FROM books WHERE author LIKE '%" + author + "%'"
        )
        books = [Book(*row) for row in cursor]

    else:
        cursor.execute("SELECT name, author, read FROM books")
        books = [Book(*row) for row in cursor]

    return render_template('books.html', books=books)



