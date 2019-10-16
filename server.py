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

COMPLIMENTS = {'low': ['ducky', 'coolio', 'wowza', 'oh-so-not-meh', 'neato'],
               'mid': ['smashing', 'lovely', 'wonderful', 'alright', 'okay'],
               'high': ['awesome', 'brilliant', 'terrific', 'fantastic', 
                        'fantabulous', 'incredible']
}

DISSES = {'low': ['mean', 'grumpy', 'bad', 'foolish', 'sickly'],
          'mid': ['a liar', 'cowardly', 'dumb', 'a worm'],
          'high': ['hateful', 'repulsive', 'toxic']
}
  

@app.route("/")
def start_here():
    """Home page."""

    return """<!doctype html><html>Hi! This is the home page.
            <br>
            <form action="/hello">
            Do you want a compliment or diss?
            <input type="radio" name="choice" value="compliment">Compliment
            <input type="radio" name="choice" value="diss">Diss
            <br>
            What level do you want?
            <input type="radio" name="level" value="low">Low
            <input type="radio" name="level" value="mid">Mid
            <input type="radio" name="level" value="high">High
            <br>
            <input type="submit">
            </html>"""


def make_form(choice, level):
  """Return a html for in a string format."""
  string = """
    <!doctype html>
    <html>
      <head>
        <title>Hi There!</title>
      </head>
      <body>
        <h1>Hi There!</h1> """
  if choice == 'compliment':
    string += """<form action="/greet">
          Our Compliment Form:<br>
          What's your name? <input type="text" name="person"><br>
          Compliment: """
    dictionary = COMPLIMENTS
  else:
    string += """<form action="/diss">
          Our Mean Form:<br>
          What's your name? <input type="text" name="person"><br>
          Mean: """
    dictionary = DISSES
  for word in dictionary[level]:
    string += f"""<input type="radio" name="greeting" value="{word}">{word.title()}"""
  string += """<br> <input type="submit" value="Submit">
              </form>
              </body>
              </html>
              """
  return string


@app.route("/hello")
def say_hello():
    """Say hello and prompt for user's name."""

    choice = request.args.get("choice")
    level = request.args.get("level")

    return make_form(choice, level)


@app.route("/greet")
def greet_person():
    """Get user by name."""

    player = request.args.get("person")
    compliment = request.args.get("greeting")

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
  diss = request.args.get("greeting")

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
