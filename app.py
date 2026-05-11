from flask import Flask, render_template, redirect, request
from config import Config
from models import db, Book, Transaction
from forms import BookForm

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)

@app.before_first_request
def create_tables():
    db.create_all()

@app.route("/", methods=["GET", "POST"])
def index():
    form = BookForm()
    if form.validate_on_submit():
        book = Book.query.filter_by(name=form.book_name.data, category=form.category.data, available=True).first()
        if book:
            book.available = False
            transaction = Transaction(student_name=form.student_name.data, book=book)
            db.session.add(transaction)
            db.session.commit()
            return render_template("message.html", msg="Book issued successfully.")
        else:
            return render_template("message.html", msg="Book not available.")
    return render_template("index.html", form=form)

@app.route("/return", methods=["GET", "POST"])
def return_book():
    form = BookForm()
    if form.validate_on_submit():
        transaction = Transaction.query.join(Book).filter(
            Transaction.student_name == form.student_name.data,
            Book.name == form.book_name.data,
            Book.category == form.category.data,
            Book.available == False
        ).first()
        if transaction:
            transaction.book.available = True
            db.session.delete(transaction)
            db.session.commit()
            return render_template("message.html", msg="Book returned successfully.")
        return render_template("message.html", msg="You did not borrow this book.")
    return render_template("index.html", form=form)

@app.route("/donate", methods=["GET", "POST"])
def donate_book():
    form = BookForm()
    if form.validate_on_submit():
        new_book = Book(name=form.book_name.data, category=form.category.data)
        db.session.add(new_book)
        db.session.commit()
        return render_template("message.html", msg="Thank you for your donation.")
    return render_template("index.html", form=form)

@app.route("/books")
def list_books():
    books = Book.query.all()
    return render_template("dashboard.html", books=books)

@app.route("/track")
def track():
    transactions = Transaction.query.all()
    return render_template("dashboard.html", books=[t.book for t in transactions])

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
