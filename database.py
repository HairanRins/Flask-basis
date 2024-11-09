import mysql.connector
from config import Config

def create_database():
    # Connectez-vous à MySQL sans spécifier de base de données
    db = mysql.connector.connect(
        host=Config.MYSQL_HOST,
        user=Config.MYSQL_USER,
        password=Config.MYSQL_PASSWORD
    )
    cursor = db.cursor()
    
    # Créez la base de données si elle n'existe pas
    cursor.execute("CREATE DATABASE IF NOT EXISTS book_management")
    cursor.execute("USE book_management")

    # Créez la table books
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS books (
        id INT AUTO_INCREMENT PRIMARY KEY,
        title VARCHAR(255) NOT NULL,
        author VARCHAR(255) NOT NULL
    )
    """)

    print("Database and table created successfully!")
    db.commit()
    cursor.close()
    db.close()

if __name__ == "__main__":
    create_database()
