from flask import Flask, render_template, request
from helpers.extract_candidates import extract_candidates
from flask import jsonify
from Book import Book
from Library import Library
from Member import Member

app = Flask(__name__)

# Create a library object and add some books
my_library = Library('My Library')


# Define routes for each page
@app.route("/")
def index():
    return render_template("index.html", library=my_library)

@app.route("/Books.html")
def Books():
    return render_template("Books.html", library=my_library.books)

@app.route("/Members.html")
def Members():
    return render_template("Members.html", library=my_library.members)

@app.route("/search")
def search():
    query = request.args.get("q")
    if query and query.strip():
        query = query.lower()
        results = my_library.search_books(query)
    else:
        results = []
    return render_template("search.html", query=query, results=results)

@app.route('/add_book', methods=['POST'])
def add_book():
    title = request.form['title']
    author = request.form['author']
    year = request.form['year']
    new_book = Book.add_book(title, author, year)
    all_books = Book.get_all_books()
    return render_template('Books.html',books=all_books, message='Book added successfully!')

@app.route('/add_member', methods=['POST'])
def add_member():
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    new_member = Member.add_member(first_name, last_name)
    all_members = Member.get_all_members()
    return render_template('Members.html', members=all_members, message='Member added successfully!')

@app.route('/delete_book', methods=['POST'])
def delete_book():
    title = request.form['title']
    Book.delete_book(title)
    all_books = Book.get_all_books()
    return render_template('Books.html', books=all_books, message=f"Book {title} deleted successfully!")

@app.route('/delete_member', methods=['POST'])
def delete_member():
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    Member.delete_member(first_name, last_name)
    all_members = Member.get_all_members()
    return render_template('Members.html', members=all_members, message=f"Member {first_name} {last_name} deleted successfully!")




@app.route('/extract', methods=['POST'])
def extract():
    narrative = request.get_json()['narrative']
    try:
        candidate_classes, candidate_attributes, candidate_operations = extract_candidates(narrative)
        return jsonify({
            'candidate_classes': candidate_classes,
            'candidate_attributes': candidate_attributes,
            'candidate_operations': candidate_operations
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500



# Run the app
if __name__ == "__main__":
    app.run(debug=True)
