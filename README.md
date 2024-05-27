# ai_clinical_trial
 Determining whether a pdf is a clinical trial

# Things to do
- We want to compare Gemini API, with zero-shot, one-shot, and few-shot prompting 
- Read papers on prompting and the paper on Gemini API 
- 1st Goal is to get the zero-shot working 

# Draft 
# Technology Overview 
Technologies Outline
Chrome Extension
Languages: JavaScript (TypeScript optional)
Chrome APIs: chrome.runtime, chrome.tabs, chrome.storage
Frontend Framework: Vanilla JavaScript or a lightweight framework like Svelte if necessary
Backend
Language: Python
Web Framework: Flask
File Handling: werkzeug for secure filename handling
Database: PostgreSQL (or other free databases like SQLite or a free tier of managed databases)
Database Driver: psycopg2 for PostgreSQL connection
Environment Variables: python-dotenv to manage environment variables
HTTP Requests: requests library to call external APIs (Google Gemini API)
CSV Handling: pandas library to export data to CSV

## Architecture Overview 

Architecture Overview
Chrome Extension
Popup UI:

Provides a user interface to upload PDF files.
Sends PDF files to the backend server for analysis.
Background Script:

Manages communication between the popup and backend server.
Backend
Flask Server:

Handles incoming HTTP requests.
Processes file uploads using werkzeug.
PDF Processing:

Reads and extracts text from PDFs.
Sends extracted text to the Google Gemini API for classification.
Database:

Stores the filename and classification result (whether the PDF is a clinical trial).
Free databases: PostgreSQL (with free tier options like Heroku Postgres), SQLite (file-based, no server required).
CSV Export:

Exports data from the database to a CSV file using pandas.