from flask import Flask, render_template, request, jsonify
from werkzeug.utils import secure_filename
import os
import subprocess

app = Flask(__name__)
  
@app.route('/', methods = ['GET', 'POST'])
def uploader_file():
   if request.method == 'POST':

      f = request.files['file']
      f.save(secure_filename(f.filename))
      subprocess.call("rm -f ./a.out", shell=True)
      retcode = subprocess.call("./test.sh", shell=True)
      result = "Score: " + str(retcode) + " out of 2 correct."
      code = ""
      with open('add.go','r') as fs:
         code += fs.read()
      return render_template('index.html', filename=f.filename, result=result, code=code)
   else:
      return render_template('index.html')
    
if __name__ == '__main__':
   app.run(host="0.0.0.0")