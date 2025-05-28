import sqlite3
from datetime import datetime

import click
from flask import current_app, g

'''
g is a special object unique for each request. It is
used to store data that might be accessed by multiple functions during the request.

current_app is another special object that points to the Flask application handling the request. 
'''

def get_db():
    '''
Will be called when the application has been created and is handling a request
    '''

    if 'db' not in g:
        g.db = sqlite3.connect(
            current_app.config['DATABASE'], 
            detect_types=sqlite3.PARSE_DECLTYPES
        ) #estbalishes connection to the file pointed at by the DATABASE key
        g.db.row_factory = sqlite3.Row # tells the connection to return rows that behave like dicts
    return g.db

def close_db(e=None):
    '''
    close_db checks if a connection was created by checking if g.db was set. 
    If the connection exists, it is closed.
    '''
    db = g.pop('db', None)

    if db is not None:
        db.close()

def init_db():
    db = get_db() #get_db returns a database connection, which is used to execute the commands read from the file.
    with current_app.open_resource('schema.sql') as f: #open_resource() opens a file relative to the flaskr package
        db.executescript(f.read().decode('utf8'))

@click.command('init-db') #defines a command line command called init-db that calls the init_db function and shows a success message to the user.

def init_db_command():
    '''Clear the existing data and create new tables.'''
    init_db()
    click.echo("Initialized the database.")

sqlite3.register_converter(
    "timestamp", lambda v: datetime.fromisoformat(v.decode())
) #The call to sqlite3.register_converter() tells Python how to interpret timestamp values in the database. We convert the value to a datetime.datetime.

def init_app(app):
    app.teardown_appcontext(close_db) # tells Flask to call that function when cleaning up after returning the response
    app.cli.add_command(init_db_command) # adds a new command that cna be called with the flask command

