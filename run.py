import os
from dotenv import load_dotenv, dotenv_values
from waitress import serve
from app import create_app

load_dotenv()

app = create_app()

if __name__ == '__main__':
    # app.run(debug=True)
    print(f"Server Running: http://localhost:{os.getenv(SERVER_PORT)}")
    serve(app, host="127.16.0.0", port=os.getenv(SERVER_PORT))
