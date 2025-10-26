from flask import Flask, render_template, request

app = Flask(__name__)

# Sample library catalog with locations
library_books = [
    {"title": "C Programming", "author": "Dennis Ritchie", "location": "Shelf A1"},
    {"title": "Python Crash Course", "author": "Eric Matthes", "location": "Shelf B3"},
    {"title": "Data Structures", "author": "Narasimha Karumanchi", "location": "Shelf A2"},
    {"title": "Computer Networks", "author": "Andrew S. Tanenbaum", "location": "Shelf C1"},
    {"title": "DevOps Handbook", "author": "Gene Kim", "location": "Shelf D4"},
]

@app.route('/')
def home():
    return render_template('search.html')

@app.route('/search', methods=['POST'])
def search_book():
    book_name = request.form['book_name'].strip().lower()
    for book in library_books:
        if book['title'].lower() == book_name:
            return render_template('result.html', book=book)
    return render_template('result.html', book=None)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
