from flask import Flask, render_template
from collections import OrderedDict

app = Flask(__name__)

puz = OrderedDict(
    start = {"Text": "This would be some text", "Hints": []},
    what  = {"Text": "This would be some text2", "Hints": []},
    hah   = {"Text": "This would be some text3", "Hints": []},
)

@app.route("/")
def index():
   return render_template("index.html")

@app.route("/puzzle")
def puzzle_main():
    return render_template("puzzle_index.html", content="", heading="#dogec0in-vip Puzzle Hunt")

@app.route("/puzzle/<level>")
def puzzle(level):
    if level not in puz:
        return render_template("puzzle_level.html", heading="Incorrect", puzzle="You guessed wrong :c", showGuess=False)
    p = puz[level]
    return render_template("puzzle_level.html", heading="Level %s of %s" % (list(puz.keys()).index(level), len(puz)), puzzle=p["Text"], showGuess=True)

if __name__ == "__main__":
  app.run(debug=True, host="0.0.0.0", port=8004)
