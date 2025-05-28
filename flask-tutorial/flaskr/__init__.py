import os
from flask import Flask

def create_app(test_config=None):
    #create and configure the app
    app = Flask(__name__, instance_relative_config=True) 
    '''
    __name__ is the name of the current python module. 
    instance_relative_config=True tells the app that configuration files are relative to the instance folder. 
    The instance folder is located outside the flaskr package and can hold data that shouldn't be committed to version control, 
    such as config secrets and the database file.
    '''
    
    app.config.from_mapping(
        SECRET_KEY = 'dev',
        DATABASE = os.path.join(app.instance_path, 'flaskr.sqlite'),
    )
    '''
    SECRET_KEY is used by Flask and extensions to keep data safe. It's set to dev to provide a convenient value during development,
    but it should be overridden with a random value when deploying.
    DATABASE is the path where the SQLite database file will be saved. 
    It’s under app.instance_path, which is the path that Flask has chosen for the instance folder.
    '''

    if test_config is None:
        #load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
        '''
        app.config.from_pyfile() overrides the default configuration with values 
        taken from the config.py file in the instance folder if it exists. 
        For example, when deploying, this can be used to set a real SECRET_KEY.
        '''
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)
    
    #ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
        '''
        os.makedirs() ensures that app.instance_path exists. Flask doesn’t 
        create the instance folder automatically, but it needs to be
        created because your project will create the SQLite database file there.
        '''
    except OSError:
        pass
    
    #a simple page that says hello
    @app.route("/hello")
    def hello():
        return 'Hello, world!'
    
    from . import db
    db.init_app(app)
    
    from . import auth
    app.register_blueprint(auth.bp)

    from . import blog
    app.register_blueprint(blog.bp)
    app.add_url_rule("/", endpoint='index')

    return app
