from flask import Flask
app = Flask(__name__)


from flask import render_template
from flask import request
import image_fuzzy_clustering as fem
import os
import secrets
from PIL import Image
from flask import url_for, current_app

@app.route('/')
def upload():
    return render_template('index.html')


@app.route('/success', methods=['POST'])
def success():
    if request.method == 'POST':
        i=request.form.get('cluster')
        f = request.files['file']
        fname, f_ext = os.path.splitext(f.filename)
        original_pic_path=save_img(f, f.filename)
        destname = 'em_img.jpg'
        fem.plot_cluster_img(original_pic_path,i)
    return render_template('success.html')

def save_img(img, filename):
    picture_path = os.path.join(current_app.root_path, 'static/images', filename)
    # output_size = (300, 300)
    i = Image.open(img)
    # i.thumbnail(output_size)
    i.save(picture_path)

    return picture_path



if __name__ == '__main__':
    app.run(debug=True)  