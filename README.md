
# README : play-with-flask

    mkdir myproject
    
    cd myproject

    python3 -m venv venv

    virtualenv venv

    venv/bin/activate

	pip install Flask

To run the application you can either use the flask command or python’s -m switch with Flask. Before you can do that you need to tell your terminal the application to work with by exporting the FLASK_APP environment variable:

    $ export FLASK_APP=hello.py
    $ flask run

##### Alternatively you can use python -m flask:

    $ export FLASK_APP=hello.py
    $ python -m flask run
