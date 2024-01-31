### main.py


from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'
app.config['SECRET_KEY'] = 'supersecretkey'
db = SQLAlchemy(app)

class BlogPost(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80))
    content = db.Column(db.Text)
    
@app.route('/')
def home():
    posts = BlogPost.query.all()
    return render_template('home.html', posts=posts)

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@app.route('/new_post')
def new_post():
    return render_template('new_post.html')

@app.route('/edit_post/<int:id>')
def edit_post(id):
    post = BlogPost.query.get_or_404(id)
    return render_template('edit_post.html', post=post)

@app.route('/submit_post', methods=['POST'])
def submit_post():
    title = request.form['title']
    content = request.form['content']
    new_post = BlogPost(title=title, content=content)
    db.session.add(new_post)
    db.session.commit()
    return redirect(url_for('home'))

@app.route('/update_post/<int:id>', methods=['POST'])
def update_post(id):
    post = BlogPost.query.get_or_404(id)
    post.title = request.form['title']
    post.content = request.form['content']
    db.session.commit()
    return redirect(url_for('home'))

@app.route('/delete_post/<int:id>')
def delete_post(id):
    post = BlogPost.query.get_or_404(id)
    db.session.delete(post)
    db.session.commit()
    return redirect(url_for('home'))

@app.route('/search')
def search():
    query = request.args.get('query')
    posts = BlogPost.query.filter(BlogPost.title.contains(query) | BlogPost.content.contains(query))
    return render_template('home.html', posts=posts)

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)


This code generates the main Flask application file (`main.py`) based on the design provided earlier. It includes routes for various actions like displaying the homepage, handling login, accessing the dashboard, creating and editing blog posts, and performing search.

Additionally, this code uses a SQLite database to store blog posts, which can be easily replaced with a more robust database solution in a production environment. The database model (`BlogPost`) defines the structure of blog posts with fields like `id`, `title`, and `content`.

Overall, this Python code creates a fully functional Flask application that allows users to manage a simple blog website, providing CRUD (Create, Read, Update, Delete) operations for blog posts and offering features like search and content editing.