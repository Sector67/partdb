# all the imports. ALL OF THEM
import os
import sqlite3
from flask import Flask, g, render_template, jsonify, request


# create our app
app = Flask(__name__)

# set up default config
app.config.update(dict(
    DATABASE=os.path.join(app.root_path, 'partdb.db')
))
app.config.from_envvar('PARTSDB_SETTINGS', silent=True)


def connect_db():
    rv = sqlite3.connect(app.config['DATABASE'])
    rv.row_factory = sqlite3.Row
    return rv


def get_db():
    if not hasattr(g, 'db'):
        g.db = connect_db()
    return g.db


@app.teardown_appcontext
def close_db(err):
    if hasattr(g, 'db'):
        g.db.close()


def init_db():
    db = get_db()
    with app.open_resource('schema.sql', mode='r') as f:
        db.cursor().executescript(f.read())
    with app.open_resource('data.sql', mode='r') as f:
        db.cursor().executescript(f.read())
    db.commit()


def clean_name(some_var):
    return ''.join(char for char in some_var if char.isalnum())


@app.cli.command('initdb')
def initialize_db_cmd():
    init_db()
    print("Initialized the database")


@app.route('/')
def index_query():
    return render_template('iquery.html')


@app.route('/parts/query')
def part_query():
    search_field = request.args.get('field')
    search_query = request.args.get('query')

    db = get_db()
    parts = db.execute('select drawer, partnum, description from parts where instr({}, ?)'.format(search_field), (search_query,)).fetchall()
    return render_template('query_results.html', results=parts)

