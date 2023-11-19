from core import create_app

# application instance that receives client requests
app = create_app()

if __name__ == "__main__":
    app.run(debug=True)