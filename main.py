from flask import Flask, request, render_template, redirect, url_for, send_file
import os
import sqlite3
import pandas as pd
from utils.pdf_parser import Grobid
from utils.gemini import Gemini

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
DATABASE = 'data/clinical_trials.db'
EXCEL_OUTPUT = 'data/clinical_trials.xlsx'

# Ensure the upload folder exists
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs('data', exist_ok=True)

# Initialize GROBID and Gemini
grobid = Grobid()
gemini = Gemini()

# Initialize SQLite database
def init_db():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS trials (
        id INTEGER PRIMARY KEY,
        content TEXT NOT NULL
    )
    ''')
    conn.commit()
    conn.close()

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        if 'file' not in request.files:
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            return redirect(request.url)
        if file:
            file_path = os.path.join(UPLOAD_FOLDER, file.filename)
            file.save(file_path)
            process_file(file_path)
            return redirect(url_for('upload_file'))
    return render_template('upload.html')

@app.route('/download')
def download_file():
    return send_file(EXCEL_OUTPUT, as_attachment=True)

def process_file(file_path):
    # Step 1: Extract data with GROBID
    extracted_text = grobid.parse(file_path)
    if not extracted_text:
        print("Failed to extract data.")
        return

    # Step 2: Use Gemini to classify the text
    prompt = f"Determine if the following text is from a clinical trial: {extracted_text}"
    result = gemini.prompt_model(prompt)
    if result and "clinical trial" in result.lower():
        store_in_db(extracted_text)
        store_as_excel()

def store_in_db(text):
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute('INSERT INTO trials (content) VALUES (?)', (text,))
    conn.commit()
    conn.close()

def store_as_excel():
    conn = sqlite3.connect(DATABASE)
    df = pd.read_sql_query("SELECT * FROM trials", conn)
    df.to_excel(EXCEL_OUTPUT, index=False)
    conn.close()

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
