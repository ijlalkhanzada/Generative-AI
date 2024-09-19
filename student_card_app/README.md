<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
</head>
<body>

<h1>Student Card Generator App</h1>

<p>This is a Flask-based web application that allows you to generate student ID cards dynamically. Users can fill in details such as name, roll number, batch, city, and other necessary information to generate the card. The app also supports uploading student photos and downloading the generated card as an image.</p>

<h2>Features</h2>
<ul>
    <li><strong>Dynamic Form Inputs:</strong> Users can input details like name, roll number, batch, and more.</li>
    <li><strong>File Upload Support:</strong> Upload a student photo to include on the card.</li>
    <li><strong>Cascading Dropdowns:</strong> The app includes cascading dropdowns where:
        <ul>
            <li>Major cities of Pakistan are listed in the <strong>City</strong> dropdown.</li>
            <li>Auditoriums (centers) populate based on the selected city.</li>
            <li>Campuses are populated based on the selected center.</li>
        </ul>
    </li>
    <li><strong>Automatic Roll Number &amp; Batch Generation:</strong> Roll numbers and batch numbers are automatically generated and cannot be edited by the user.</li>
    <li><strong>Form Reset:</strong> After the card is generated and downloaded, the form inputs are automatically reset for the next use.</li>
    <li><strong>Responsive UI:</strong> Built using Bootstrap for a clean and responsive user interface.</li>
</ul>

<h2>Technologies Used</h2>
<ul>
    <li><strong>Python (Flask):</strong> Backend framework.</li>
    <li><strong>HTML/CSS (Bootstrap):</strong> Frontend for the form and styling.</li>
    <li><strong>JavaScript:</strong> For form validation and cascading dropdowns.</li>
    <li><strong>Matplotlib &amp; PIL:</strong> Used for generating the student card as an image.</li>
    <li><strong>Werkzeug:</strong> Secure handling of uploaded files.</li>
</ul>

<h2>Installation</h2>

<p>To run this project locally, follow these steps:</p>

<h3>1. Clone the repository</h3>
<pre><code>git clone https://github.com/yourusername/student-card-generator.git
cd student-card-generator
</code></pre>

<h3>2. Create a virtual environment</h3>
<pre><code>python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
</code></pre>

<h3>3. Install dependencies</h3>
<pre><code>pip install -r requirements.txt
</code></pre>

<h3>4. Run the application</h3>
<pre><code>python app.py
</code></pre>

<p>The app will be accessible at <code>http://127.0.0.1:5000</code>.</p>

<h2>Usage</h2>
<ol>
    <li>Open the app in your browser (<code>http://127.0.0.1:5000</code>).</li>
    <li>Fill out the form with the student's information:
        <ul>
            <li>Name, Roll Number, City, Center, Campus, etc.</li>
            <li>Upload the student's photo.</li>
        </ul>
    </li>
    <li>The <strong>City</strong> dropdown includes major cities in Pakistan, and selecting a city will populate the <strong>Center</strong> dropdown with auditoriums available in that city. Similarly, selecting a center will populate the <strong>Campus</strong> dropdown.</li>
    <li>Click <strong>Generate Card</strong>.</li>
    <li>The card will be generated, and you can download it as a PNG image.</li>
</ol>

<h2>Folder Structure</h2>

<pre><code>student-card-generator/
│
├── app.py                      # Main Flask app file
├── templates/
│   └── index.html              # HTML template for the form
├── static/
│   ├── images/                 # Folder for uploaded images and assets
│   └── css/                    # Optional custom styles (if any)
├── README.md                   # This file
├── requirements.txt            # List of dependencies
└── venv/                       # Virtual environment (not included in version control)
</code></pre>

<h2>Screenshots</h2>

<h3>Form Page</h3>
<p>[Insert a screenshot of the form]</p>

<h3>Generated Card</h3>
<p>[Insert a screenshot of the generated student card]</p>

<h2>Future Improvements</h2>
<ul>
    <li>Adding more fields to the student card, such as course details.</li>
    <li>Implementing more sophisticated roll number generation logic.</li>
    <li>Adding database support for student record storage.</li>
</ul>

<h2>Contributing</h2>
<p>Feel free to fork this project and submit a pull request if you want to contribute new features, enhancements, or bug fixes.</p>

<h2>License</h2>
<p>This project is open-source and available under the <a href="LICENSE">MIT License</a>.</p>

</body>
</html>
