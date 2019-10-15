"""Greeting Flask app."""

from random import choice

from flask import Flask, request

# "__name__" is a special Python variable for the name of the current module
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza',
    'oh-so-not-meh', 'brilliant', 'ducky', 'coolio', 'incredible',
    'wonderful', 'smashing', 'lovely']


@app.route("/")
def start_here():
    """Home page."""

    return """<!doctype html><html>Hi! This is the home page.
              <br>Click here! <a href="/hello">Hello page</a>
            </html>"""


@app.route("/hello")
def say_hello():
    """Say hello and prompt for user's name."""

    return """
    <!doctype html>
    <html>
      <head>
        <title>Hi There!</title>
      </head>
      <body>
        <h1>Hi There!</h1>
        <form action="/greet">
          Our Compliment Form:<br>
          What's your name? <input type="text" name="person"><br>
          Compliment: 
          <input type="radio" name="compliment" value="chill">Chill
          <input type="radio" name="compliment" value="smart">Smart
          <input type="radio" name="compliment" value="kind">Kind
          <input type="radio" name="compliment" value="considerate">Considerate
          <input type="radio" name="compliment" value="pretty">Pretty
          <input type="radio" name="compliment" value="happy">Happy
          <br>
          <input type="submit" value="Submit">
        </form>
        <br><br><br>
        <form action="/diss">
          Our Mean Form:<br>
          What's your name? <input type="text" name="person"><br>
          Mean: 
          <input type="radio" name="diss" value="mean">Mean
          <input type="radio" name="diss" value="hateful">Hateful
          <input type="radio" name="diss" value="grumpy">Grumpy
          <br>
          <input type="submit" value="Submit">
        </form>
      </body>
    </html>
    """


@app.route("/greet")
def greet_person():
    """Get user by name."""

    player = request.args.get("person")
    compliment = request.args.get("compliment")

    # compliment = choice(AWESOMENESS)
    # y = x

    return """
    <!doctype html>
    <html>
      <head>
        <title>A Compliment</title>
      </head>
      <body>
        Hi, {}! I think you're {}!
      </body>
    </html>
    """.format(player, compliment)


@app.route("/diss")
def diss_person():
  """Diss the user."""

  player = request.args.get("person")
  diss = request.args.get("diss")

  return """
  <!doctype html>
  <html>
      <head>
      <title>A Diss</title>
      </head>
      <body>
        Hi, {}! I think you're {}!
      </body>
  </html>
  """.format(player, diss)

if __name__ == "__main__":
    # debug=True gives us error messages in the browser and also "reloads"
    # our web app if we change the code.
    app.run(debug=True, host="0.0.0.0")
