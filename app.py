from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    result = None

    if request.method == "POST":
        user_input = request.form.get("answer")
        correct_answer = ""

        if user_input.strip() == correct_answer:
            result = "correct"
        else:
            result = "incorrect"

    return render_template("index.html", result=result)


if __name__ == "__main__":
    app.run(debug=True)