import os

#you need to import not just FLASK but also session and flask_session
from flask import Flask,session
from flask import render_template
from flask_session import Session

#Making the app
######################################################################
def create_app(test_config=None):
    """Create and configure an instance of the Flask application."""
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        # a default secret that should be overridden by instance config
        SECRET_KEY="dev",
        # store the database in the instance folder
        DATABASE=os.path.join(app.instance_path, "flaskr.sqlite"),
    )
    #configure a session and session type
    Session(app)
    app.config['SESSION_TYPE'] = 'filesystem'


    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile("config.py", silent=True)
    else:
        # load the test config if passed in
        app.config.update(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

######################################################################


#Home page
    @app.route("/")
    def index():

        return render_template("index.html")


#Page Second
    @app.route("/next_page")
    def template_test():
        return render_template('next.html', my_string="Wheeeee!", my_list=[0,1,2,3,4,5])



    #def next_page():
    #    return render_template("next.html")

    #Needed to start the session that stores the data 
    sess = Session()
    sess.init_app(app)
    
#Making the app run
    return app




"""
    @app.route("/hello")
    def hello():
        return "Hello, World!"

    # register the database commands
    from flaskr import db

    db.init_app(app)

    # apply the blueprints to the app
    from flaskr import auth, blog

    #app.register_blueprint(auth.bp)
    #app.register_blueprint(blog.bp)


    #make url_for('index') == url_for('blog.index')
    # in another app, you might define a separate main index here with
    # app.route, while giving the blog blueprint a url_prefix, but for
    # the tutorial the blog will be the main index
    app.add_url_rule("/", endpoint="index")

    
"""
    