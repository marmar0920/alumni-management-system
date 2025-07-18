from backend import create_app

app = create_app()

@app.route("/_test_login_template")
def _test_login_template():
    return render_template("login.html")

if __name__ == "__main__":
    app.run(debug=True)
