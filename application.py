from flask import Flask, render_template, request
from flask_debugtoolbar import DebugToolbarExtension


app = Flask(__name__)


# Required to use Flask sessions and the debug toolbar
app.secret_key = "ABC"

@app.route("/")
def index_page():
    """Show an index page."""

    # return "<html><body>This is the homepage.</body></html>"

    # Alternately, we could make this a Jinja template in `templates/`
    # and return that result of rendering this, like:
    #
    return render_template("application-form.html")

@app.route("/response", methods=["GET", "POST"])
def response():
    firstname = request.args.get('firstname')
    lastname = request.args.get('lastname')
    salary = request.args.get('salary')
    position = request.args.get('position')

    return render_template('application-response.html', firstname=firstname, lastname=lastname, salary=salary, position=position)

if __name__ == "__main__":
    # We have to set debug=True here, since it has to be True at the
    # point that we invoke the DebugToolbarExtension
    app.debug = True

    # Use the DebugToolbar
    DebugToolbarExtension(app)

    app.run(host="0.0.0.0")

