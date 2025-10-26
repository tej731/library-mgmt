from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

books = []

@app.route('/')
def home():
    return render_template('add_book.html')

@app.route('/add', methods=['POST'])
def add_book():
    title = request.form.get('title')
    author = request.form.get('author')
    price = request.form.get('price')
    isbn = request.form.get('isbn')

    if not title or not author or not price or not isbn:
        return "<script>alert('All fields are required!');window.history.back();</script>"

    books.append({
        'title': title,
        'author': author,
        'price': price,
        'isbn': isbn
    })
    return redirect(url_for('catalog'))

@app.route('/catalog')
def catalog():
    return render_template('catalog.html', books=books)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5001, debug=True)
