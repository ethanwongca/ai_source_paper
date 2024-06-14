import os 
import utils.gemini as gemini
import utils.pdf_parser as parser
from flask import Flask, request, jsonify, render_template, url_for, send_file
import sqlite3
import pandas as pd 

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
DATABASE = 'data/clinical_trials.db'
EXEL_OUTPUT = 'data/clinical_trials.xlsx'


