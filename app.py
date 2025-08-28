from flask import Flask, render_template, request, redirect, flash, url_for
import mysql.connector

app = Flask(__name__)
app.secret_key = "8c6faad5c5e749c2afbb1a9d88bdb7d6"  

db_config = {
    'host': '127.0.0.1',       
    'port': 3307,             
    'user': 'root',            
    'password': 'Newp@ssword123', 
    'database': 'contact_messaging_cm'
}


@app.route('/')
def home():
    return render_template('home.html', lang="en")

@app.route('/home_ar')
def home_ar():
    return render_template('home.html', lang='ar')


@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        subject = request.form['subject']
        message = request.form['message']

        try:
            conn = mysql.connector.connect(**db_config)
            cursor = conn.cursor()
            sql = "INSERT INTO messages (Name, Email, Phone, Subject, Message) VALUES (%s, %s, %s, %s, %s)"
            values = (name, email, phone, subject, message)
            cursor.execute(sql, values)
            conn.commit()
            cursor.close()
            conn.close()

            
            if request.referrer and "/home_ar" in request.referrer:
                return redirect(url_for("success_page_ar"))
            else:
                return redirect(url_for("success_page"))

        except mysql.connector.Error as err:
            return f"Database error: {err}"
    return "Invalid Request"


        
@app.route('/success')
def success_page():
    return render_template('success.html', lang='en')


@app.route('/success_ar')
def success_page_ar():
    return render_template('success.html', lang='ar')

@app.route('/admin')
def admin_page():
    search = request.args.get('search', '')
    sort = request.args.get('sort', '')

    sql_query = "SELECT * FROM messages"
    params = []

    if search:
        sql_query += " WHERE Name LIKE %s OR Subject LIKE %s"
        params.extend([f"%{search}%", f"%{search}%"])

    allowed_sorts = ['Name', 'Subject', 'Submission_time']
    if sort in allowed_sorts:
        sql_query += f" ORDER BY {sort}"

    try:
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor(dictionary=True)
        cursor.execute(sql_query, params)
        messages = cursor.fetchall()
        cursor.close()
        conn.close()
    except mysql.connector.Error as err:
        return f"Database error: {err}"

    return render_template('admin.html', messages=messages, search=search)

@app.route('/delete/<int:msg_id>')
def delete_message(msg_id):
    try:
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()
        cursor.execute("DELETE FROM messages WHERE ID = %s", (msg_id,))
        conn.commit()
        cursor.close()
        conn.close()
    except mysql.connector.Error as err:
        return f"Database error: {err}"
    return redirect(url_for('admin_page'))

if __name__ == '__main__':
    app.run(debug=True)
