from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    if request.method == "POST":
        try:
            # Pega o valor da expressão passada no formulário
            expression = request.form["expression"]
            # Avalia a expressão matemática
            result = eval(expression)
        except Exception as e:
            result = "Error: " + str(e)

    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)
