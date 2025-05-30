import subprocess

from flask import Flask, request
app = Flask(__name__)


@app.route('/wake', methods=['GET'])
def wake():
    mac_address = request.args.get('mac')
    if not mac_address:
        return "MAC address required", 400

    try:
        subprocess.run(["sudo", "wakeonlan", mac_address], check=True)
        return f"Magic packet sent to {mac_address}", 200
    except subprocess.CalledProcessError:
        return "Failed to send WoL packet", 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
