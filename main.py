from website import create_app

app = create_app()

if __name__ == "__main__":
    app.run(debug=True) # Automatically re-run the server after changes. Turn "OFF" in PRODUCTION.