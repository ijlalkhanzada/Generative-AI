from flask import Flask, render_template, request, send_file, redirect, url_for, flash
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from PIL import Image
import numpy as np
import io
import os
from werkzeug.utils import secure_filename
import random
import datetime

app = Flask(__name__)
app.secret_key = 'your_secret_key'
app.config['UPLOAD_FOLDER'] = 'static/images'
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16 MB limit

# Ensure the upload folder exists
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

background_image_path = 'static/images/card_background.jpeg'
background = Image.open(background_image_path)
background = background.resize((800, 600))
background = np.array(background)

def generate_card(student_details):
    fig, ax = plt.subplots(figsize=(9, 6))

    card_border = patches.Rectangle((0, 0), 1, 1, transform=ax.transAxes, fill=False, color='teal', linewidth=4)
    ax.add_patch(card_border)

    ax.imshow(background, extent=[0.1, 0.9, 0.1, 0.9], aspect='auto', alpha=0.15)

    for i, (key, value) in enumerate(student_details.items()):
        if key == "Photo":
            continue
        ax.text(0.05, 0.90 - i*0.08, f"{key}: ", ha='left', va='top', fontsize=14, color='teal', weight='bold', 
                transform=ax.transAxes)
        ax.text(0.35, 0.90 - i*0.08, value, ha='left', va='top', fontsize=14, color='black', 
                transform=ax.transAxes)

    img = Image.open(student_details['Photo'])
    img = img.resize((120, 150))
    img = np.array(img)

    ax_img = fig.add_axes([0.75, 0.59, 0.15, 0.3])
    ax_img.imshow(img)
    ax_img.axis('off')
    border = patches.Rectangle((0, 0), 1, 1, transform=ax_img.transAxes, fill=False, color='teal', linewidth=2)
    ax_img.add_patch(border)

    footer_color_1 = patches.Rectangle((0, 0), 0.2, 0.05, transform=ax.transAxes, color='red')
    footer_color_2 = patches.Rectangle((0.2, 0), 0.2, 0.05, transform=ax.transAxes, color='green')
    ax.add_patch(footer_color_1)
    ax.add_patch(footer_color_2)
    ax.text(0.1, 0.02, "Q1", ha='center', va='center', fontsize=12, color='white', transform=ax.transAxes)
    ax.text(0.3, 0.02, "WMD", ha='center', va='center', fontsize=12, color='white', transform=ax.transAxes)

    ax.text(0.75, 0.05, "Authorized Signature", ha='center', va='center', fontsize=14, color='teal', weight='bold',
            transform=ax.transAxes)

    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis('off')

    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    plt.close(fig)
    return buf

def generate_roll_no():
    return f"RL-{random.randint(1000, 9999)}"

def generate_batch():
    current_year = datetime.datetime.now().year
    return f"Batch-{current_year}"

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        student_photo = request.files.get('photo')
        if student_photo and student_photo.filename:
            # Securely handle file upload
            filename = secure_filename(student_photo.filename)
            photo_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            student_photo.save(photo_path)

            student_details = {
                "Name": request.form['name'],
                "Roll No": request.form['roll_no'],
                "Distance Learning": request.form['distance_learning'],
                "City": request.form['city'],
                "Center": request.form['center'],
                "Campus": request.form['campus'],
                "Days / Time": request.form['days_time'],
                "Batch": request.form['batch'],
                "Photo": photo_path  # Use the uploaded photo
            }
            card_image = generate_card(student_details)
            flash("Card generated successfully!", "success")
            return send_file(card_image, mimetype='image/png', as_attachment=True, download_name='student_card.png')

        flash("Please upload a valid photo.", "danger")
        return redirect(url_for('index'))

    return render_template('index.html', roll_no=generate_roll_no(), batch=generate_batch())

if __name__ == '__main__':
    app.run(debug=True)
