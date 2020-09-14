from flask import Blueprint, redirect, render_template, request, url_for, session
from werkzeug.utils import secure_filename
from models.general import crud
import sqlite3

UPLOAD_FOLDER = '/uploads'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

admin = Blueprint('admin', __name__, static_folder='static', template_folder='templates')
admin.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@admin.route('/')
def dashboard():
	return render_template('admin/dashboard.html')


@admin.route('/stok')
def stok():
	return render_template('admin/stok.html')


@admin.route('/tambah_stok')
def tambah_stok():



	if request.method == 'POST':
		if 'add' in request.form:
			crud.insert('stok', {
					'nama':request.form['produk'],
					'deskripsi':request.form['deskripsi'],
					''
				})

	data = {
		'title' : 'Tambah ',
		'kategori' : crud.read('kategori')
	}

	return render_template('admin/stok_form.html', data=data)


@admin.route('/kategori', methods=['GET', 'POST'])
def kategori():

	if request.method == 'POST':
		if 'add' in request.form:
			crud.insert('kategori', {'nama':request.form['nama']})
			return redirect(url_for('admin.kategori'))

		if 'edit' in request.form:
			crud.update('kategori', {'nama':request.form['nama']}, {'id_kategori':request.form['edit']})
			return redirect(url_for('admin.kategori'))

		if 'del' in request.form:
			crud.delete('kategori', {'id_kategori':request.form['del']})
			return redirect(url_for('admin.kategori'))

	data = crud.read('kategori')

	return render_template('admin/kategori.html', data=data)


@admin.route('logout')
def logout():
	return 'logout'