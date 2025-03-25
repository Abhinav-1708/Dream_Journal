from flask import Flask, request, jsonify, send_from_directory
import os
import csv
from datetime import datetime

app = Flask(__name__)

# Define the folder to store dream entries and the CSV file name
DREAM_ENTRIES_FOLDER = 'dream_entries'
CSV_FILENAME = 'dreams.csv'

if not os.path.exists(DREAM_ENTRIES_FOLDER):
    os.makedirs(DREAM_ENTRIES_FOLDER)

csv_filepath = os.path.join(DREAM_ENTRIES_FOLDER, CSV_FILENAME)

@app.route('/')
def index():
    # Serve the index.html file from the root folder
    return send_from_directory('.', 'index.html')

@app.route('/save_dream', methods=['POST'])
def save_dream():
    data = request.get_json()
    selected_date = data.get('date')
    dream = data.get('dream')

    if not selected_date or not dream:
        return jsonify({'success': False, 'message': 'Missing date or dream content.'}), 400

    try:
        file_exists = os.path.isfile(csv_filepath)
        with open(csv_filepath, 'a', newline='', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile)
            # Write header if file is being created for the first time
            if not file_exists:
                writer.writerow(['Selected Date', 'Timestamp', 'Dream'])
            timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            writer.writerow([selected_date, timestamp, dream])
        return jsonify({'success': True, 'message': 'Dream saved successfully!'})
    except Exception as e:
        return jsonify({'success': False, 'message': f'Error saving dream: {str(e)}'}), 500

if __name__ == '__main__':
    app.run(debug=True)
