from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

def get_data():
    # Connect to the SQLite database
    conn = sqlite3.connect('rpowners.db')
    cursor = conn.cursor()
    
    # Fetch all records from the rpownerstable
    cursor.execute("SELECT name, tower, floor, flat FROM rpownerstable")
    data = cursor.fetchall()
    
    # Close the connection
    conn.close()
    
    return data

@app.route('/')
def index():
    data = get_data()
    return render_template('index.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)