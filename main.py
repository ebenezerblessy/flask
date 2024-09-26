from flask import Flask, request, render_template, jsonify
from database import init_app
import mysql.connector

app = Flask(__name__)
conn = init_app(app)


# Route to display the HTML form
@app.route('/')
def form():
    return render_template('form.html')


# Route to handle form data after submission
@app.route('/submit', methods=['POST'])
def submit():
    name = request.form.get('name', 'None')
    email = request.form.get('email', 'None')
    age = request.form.get('age', 'None')
    mobile = request.form.get('mobile', 'None')
    department = request.form.get('department', 'None')
    location = request.form.get('location', 'None')
    company = request.form.get('company', 'None')

    try:
        # Use the connection established in init_app
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO users (name, email, age, mobile, department, location, company) "
            "VALUES (%s, %s, %s, %s, %s, %s, %s)",
            (name, email, age, mobile, department, location, company))
        conn.commit()  # Commit changes
        cursor.close()
    except Exception as e:
        return f"Error connecting to the database: {str(e)}", 500  # Return error message if there's an issue

    return render_template('result.html', name=name, email=email, age=age, mobile=mobile,
                           department=department, location=location, company=company)


@app.route('/api/users', methods=['GET'])
def get_users():
    try:
        cursor = conn.cursor(dictionary=True)  # Use dictionary=True for readable results
        cursor.execute("SELECT * FROM users")  # Fetch all user data
        users = cursor.fetchall()  # Get all records
        cursor.close()
        return jsonify(users), 200  # Return the user data as JSON
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True, port=8000)
