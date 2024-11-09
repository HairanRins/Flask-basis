from flask import Flask, render_template , request , redirect , url_for , flash
import mysql.connector
from config import Config 

app = Flask(__name__)
app.config.from_object(Config)

# Fonction pour obtenir une connexion MySQL
def get_db_connection():
    return mysql.connector.connect(
        host=app.config['MYSQL_HOST'],
        user=app.config['MYSQL_USER'],
        password=app.config['MYSQL_PASSWORD'],
        database=app.config['MYSQL_DB']
    )

@app.route('/')
def index():
    db = get_db_connection()
    cur = db.cursor()
    cur.execute("SELECT * FROM books")
    data = cur.fetchall()
    cur.close()
    db.close()
    return render_template('index.html', books=data)

@app.route('/add', methods=['GET', 'POST'])
def add_book():
    if request.method == 'POST':
        title = request.form['title']
        author = request.form['author']
        db = get_db_connection()
        cur = db.cursor()
        cur.execute("INSERT INTO books (title, author) VALUES (%s, %s)", (title, author))
        db.commit()
        cur.close()
        db.close()
        flash('Livre ajouté avec succès')
        return redirect(url_for('index'))
    return render_template('add_book.html')

@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit_book(id):
    db = get_db_connection()
    cur = db.cursor()
    cur.execute("SELECT * FROM books WHERE id = %s", (id,))
    book = cur.fetchone()

    if request.method == 'POST':
        title = request.form['title']
        author = request.form['author']
        cur.execute("UPDATE books SET title = %s, author = %s WHERE id = %s", (title, author, id))
        db.commit()
        cur.close()
        db.close()
        flash('Livre mis à jour avec succès')
        return redirect(url_for('index'))
    cur.close()
    db.close()
    return render_template('edit_book.html', book=book)

@app.route('/delete/<int:id>', methods=['POST'])
def delete_book(id):
    db = get_db_connection()
    cur = db.cursor()
    cur.execute("DELETE FROM books WHERE id = %s", (id,))
    db.commit()
    cur.close()
    db.close()
    flash('Livre supprimé avec succès')
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)

