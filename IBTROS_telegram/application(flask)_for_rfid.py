#!/usr/bin/env python3

"""
Author: donsky
For: www.donskytech.com
Purpose: Create a REST Server Interface using Flask for future IOT Projects
"""

import logging
import sqlite3
import json
from flask import Flask, request, jsonify
from pathlib import Path

app = Flask(__name__)

# Configure logging to write to console
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger()

# Get the directory path of the current script
current_directory = Path(__file__).resolve().parent

# Construct the path to the SQLite database file in the same directory
db_path = current_directory / "database.sqlite"

@app.route('/student/isauthorized', methods=['GET'])
def message():
    notes = request.args.get('notes', '').strip()
    length = len(notes)
    logger.info(f"Received the following query parameter notes={notes}, len={length}")

    # Connect to the SQLite database using the constructed path
    conn = sqlite3.connect(str(db_path))
    cursor = conn.cursor()

    cursor.execute("SELECT COUNT(*) FROM ORDERS WHERE notes=?", (notes,))
    result = cursor.fetchone()
    row_count = result[0]
    logger.info(f"query result :: {row_count}")
    cursor.close()

    # Prepare the response data
    if row_count > 0:
        message_result = {"is_authorized": True}
    else:
        message_result = {"is_authorized": False}
    logger.info(f"message_result :: {message_result}")
    return jsonify(message_result)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8081, debug=True)
