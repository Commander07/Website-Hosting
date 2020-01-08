import os
from werkzeug.utils import secure_filename
from flask import Flask, render_template, request, redirect, url_for, flash
app = Flask('app')
app.config['UPLOAD_FOLDER'] = "./uploads"
app.secret_key = "uhe*lh'E%JJ)/:BVy=4ZDN?Qvo`|ZR"
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024
ALLOWED_EXTENSIONS = set(['html', 'css', 'js'])
def allowed_file(filename):
  return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
@app.route('/')
def index():
  return render_template("index.html")
@app.route('/create',methods=["GET","POST"])
def create():
  if request.method == 'POST':
        # check if the post request has the file part
    if 'file' not in request.files:
      flash('No file part')
      return redirect(request.url)
    file = request.files['file']
    if file.filename == '':
      flash('No file selected for uploading')
      return redirect(request.url)
    if file and allowed_file(file.filename):
      filename = secure_filename(file.filename)
      file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
      flash('File successfully uploaded')
      return redirect('/')
    else:
      flash('Allowed file types are txt, pdf, png, jpg, jpeg, gif')
      return redirect(request.url)
  elif request.method == 'GET':
    return render_template("create.html")
app.run(host='0.0.0.0', port=8080)