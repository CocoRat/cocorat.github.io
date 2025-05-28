import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

from werkzeug.security import check_password_hash, generate_password_hash

from flaskr.db import get_db

bp = Blueprint("auth", __name__, url_prefix='/auth') # creates a lueprint named auth

@bp.route("/register", methods=("GET", "POST")) # associates the url register with the register view function
def register():
    '''
    If the user submitted the form, start validating input.
    request.form is a special dictionary with submitted form keys and values.
    if validation succeeds, insert the new user data into database
    Then redirect to login page
    '''
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        db = get_db()
        error = None

        if not username:
            error = "Username is required."
        elif not password:
            error = "Password is required."

        if error is None:
            try:
                db.execute(
                    "INSERT INTO user (username, password) VALUES (?,?)",
                    (username, generate_password_hash(password)),
                )
                db.commit()
            except db.IntegrityError:
                error = f"User {username} is already registered."
            else:
                return redirect(url_for("auth.login"))
        flash(error)
    return render_template("auth/register.html")

@bp.route("/login", methods=("GET", "POST"))
def login():
    '''
    fetchone() returns one row from the query
    checkpasswordhas() hases the submittied password in the same way
    as the stored hash and securely compares them.
    session is a fict that stores data across requests. when validation succeeds,
    the user id is stored in a new session. the data is stored in a cookie
    that is sent to the browser, and the brower sends it back with subsequent requests
    '''
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        db = get_db()
        error = None
        user = db.execute(
            "SELECT * FROM user WHERE username = ?", (username,)
        ).fetchone()

        if user is None:
            error = "Incorrect username."
        elif not check_password_hash(user['password'], password):
            error = "Incorrect password." 
        
        if error is None:
            session.clear()
            session["user_id"] = user['id']
            return redirect(url_for("index"))
        flash(error)
    return render_template('auth/login.html')

@bp.before_app_request # registers a function that runs before view function
def load_logged_in_user():
    '''
    Checks if a user id is stored in the session and gets that user's data from the db
    stores on g.user, which lasts for the length of the request
    '''
    user_id = session.get("user_id")

    if user_id is None:
        g.user = None
    else:
        g.user = get_db().execute(
            "SELECT * FROM user WHERE id = ?", (user_id,)
        ).fetchone()

@bp.route("/logout")
def logout():
    '''Removes user id from the session'''
    session.clear()
    return redirect(url_for("index"))

def login_required(view):
    '''
    decorator used to check that a user is logged in for each view
    '''
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            return redirect(url_for("auth.login"))
        
        return view(**kwargs)
    return wrapped_view
    