import sqlite3
from flask import Flask, render_template, request, redirect, url_for, session, jsonify
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = 'super_secret_ai_hub_key_replace_me'

def get_db_connection():
    conn = sqlite3.connect('ai_hub.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route("/")
def home():
    is_logged_in = 'user_id' in session
    limited = not is_logged_in
    categories = {}
    user_favorites = []
    
    if is_logged_in:
        conn = get_db_connection()
        tools_db = conn.execute('SELECT * FROM tools').fetchall()
        fav_rows = conn.execute('SELECT tool_id FROM favorites WHERE user_id = ?', (session['user_id'],)).fetchall()
        user_favorites = [row['tool_id'] for row in fav_rows]
        conn.close()
        
        # Group tools by category
        for row in tools_db:
            tool = dict(row)
            cat = tool["category"]
            if cat not in categories:
                categories[cat] = []
            categories[cat].append(tool)
    
    return render_template("index.html", categories=categories, limited=limited, user_favorites=user_favorites)



@app.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]

        conn = get_db_connection()
        user = conn.execute("SELECT * FROM users WHERE email = ?", (email,)).fetchone()
        
        if user:
            conn.close()
            return render_template("signup.html", error="Email already exists.")
        
        hashed_password = generate_password_hash(password)
        conn.execute("INSERT INTO users (email, password) VALUES (?, ?)", (email, hashed_password))
        conn.commit()
        
        # Log the user in
        new_user = conn.execute("SELECT id, email FROM users WHERE email = ?", (email,)).fetchone()
        session["user_id"] = new_user["id"]
        session["email"] = new_user["email"]
        conn.close()
        
        return redirect(url_for("home"))
        
    return render_template("signup.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]
        
        conn = get_db_connection()
        user = conn.execute("SELECT * FROM users WHERE email = ?", (email,)).fetchone()
        conn.close()
        
        if user and check_password_hash(user["password"], password):
            session["user_id"] = user["id"]
            session["email"] = user["email"]
            return redirect(url_for("home"))
        else:
            return render_template("login.html", error="Invalid email or password.")
            
    return render_template("login.html")

@app.route("/logout")
def logout():
    session.pop("user_id", None)
    session.pop("email", None)
    return redirect(url_for("home"))

@app.route("/toggle_favorite/<int:tool_id>", methods=["POST"])
def toggle_favorite(tool_id):
    if 'user_id' not in session:
        return jsonify({"error": "Unauthorized"}), 401
        
    user_id = session['user_id']
    conn = get_db_connection()
    
    existing = conn.execute('SELECT id FROM favorites WHERE user_id = ? AND tool_id = ?', (user_id, tool_id)).fetchone()
    
    if existing:
        conn.execute('DELETE FROM favorites WHERE id = ?', (existing['id'],))
        status = 'removed'
    else:
        conn.execute('INSERT INTO favorites (user_id, tool_id) VALUES (?, ?)', (user_id, tool_id))
        status = 'added'
        
    conn.commit()
    conn.close()
    
    return jsonify({"status": status})

@app.route("/favorites")
def favorites():
    if 'user_id' not in session:
        return redirect(url_for('login'))
        
    conn = get_db_connection()
    fav_tools_db = conn.execute('''
        SELECT t.* FROM tools t
        JOIN favorites f ON t.id = f.tool_id
        WHERE f.user_id = ?
    ''', (session['user_id'],)).fetchall()
    
    fav_rows = conn.execute('SELECT tool_id FROM favorites WHERE user_id = ?', (session['user_id'],)).fetchall()
    user_favorites = [row['tool_id'] for row in fav_rows]
    conn.close()
    
    categories = {"Your Favorites": []}
    for row in fav_tools_db:
        categories["Your Favorites"].append(dict(row))
        
    return render_template("favorites.html", categories=categories, limited=False, user_favorites=user_favorites)


if __name__ == "__main__":
    app.run(debug=True, port=5000)
