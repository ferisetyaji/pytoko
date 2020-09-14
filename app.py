from flask import Flask
from admin import admin
from models.general import crud

app = Flask(__name__)
app.register_blueprint(admin, url_prefix='/admin')

@app.route('/')
def index():
	data = crud.read('kategori')
	return 'hello world'