# app.py
from flask import Flask, render_template, request, redirect, url_for, flash
import sqlite3

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Needed for flashing messages

# SQLite database configuration
DATABASE = 'bookings.db'

def get_db():
    db = sqlite3.connect(DATABASE)
    db.row_factory = sqlite3.Row
    return db

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():  # Renamed function to 'about'
    return render_template('about.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/logout')
def logout():
    return render_template('logout.html')



@app.route('/bookings', methods=['POST', 'GET'])
def bookings():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        date = request.form['date']
        time = request.form['time']
        num_guests = request.form['num_guests']
        
        db = get_db()
        cursor = db.cursor()
        cursor.execute('INSERT INTO bookings (name, email, phone, date, time, num_guests) VALUES (?, ?, ?, ?, ?, ?)', (name, email, phone, date, time, num_guests))
        db.commit()
        db.close()
        
        
        return redirect(url_for('reservations'))
    else:
        # Handle GET request (display form)
        return render_template('reservation.html')
    

@app.route('/reserved_table')
def reservations():
    db = get_db()
    cursor = db.cursor()
    cursor.execute('SELECT * FROM bookings')
    reservations = cursor.fetchall()
    db.close()
    return render_template('reserved_table.html', reservations=reservations)

@app.route('/cancel_booking/<int:id>', methods=['POST'])
def cancel_booking(id):
    if request.method == 'POST':
        db = get_db()
        cursor = db.cursor()
        cursor.execute('DELETE FROM bookings WHERE id = ?', (id,))
        db.commit()
        db.close()
        flash('Booking canceled successfully!', 'success')
        return redirect(url_for('reservations'))
    else:
        # Handle GET request
        return redirect(url_for('reservations'))
    
# Add this route to handle editing bookings
@app.route('/edit_booking/<int:id>', methods=['GET', 'POST'])
def edit_booking(id):
    db = get_db()
    cursor = db.cursor()
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        date = request.form['date']
        time = request.form['time']
        num_guests = request.form['num_guests']
        cursor.execute('UPDATE bookings SET name=?, email=?, phone=?, date=?, time=?, num_guests=? WHERE id=?',
                       (name, email, phone, date, time, num_guests, id))
        db.commit()
        db.close()
        flash('Booking updated successfully!', 'success')
        return redirect(url_for('reservations'))
    else:
        cursor.execute('SELECT * FROM bookings WHERE id = ?', (id,))
        booking = cursor.fetchone()
        db.close()
        return render_template('edit_booking.html', booking=booking)


if __name__ == '__main__':
    app.run(debug=True)