from backend import create_app
from flask import render_template

app = create_app()
print("Template search path:", app.jinja_loader.searchpath)

@app.route("/_test_login_template")
def _test_login_template():
    return render_template("login.html")

if __name__ == "__main__":
    app.run(debug=True)
