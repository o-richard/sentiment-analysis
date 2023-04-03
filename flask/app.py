from model import result

from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        text = request.form["text"]
        # Ensure the text is not null
        if text == ("" or None):
            return render_template("index.html")
        text_result = result(text)
        # Store the text intepretation of the result
        value = ""
        # Store whether the obtain result is expected i.e 0 or 4
        expected = True
        if text_result == 4:
            value = "positive"
        elif text_result == 0:
            value = "negative"
        else:
            expected = False
            value = "The text you have entered could not be processed."
        return render_template("result.html", text=text, result=value, expected=expected)
    else:
        return render_template("index.html")


if __name__ == "__main__":
    app.run()
