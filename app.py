from flask import Flask
from models import db
from routes import init_routes
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

# Initialize database
db.init_app(app)

# Register routes
init_routes(app)

if __name__ == '__main__':
    app.run(debug=True)