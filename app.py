from flask import Flask, redirect
from routes.scan_routes import scan_bp

app = Flask(__name__)
app.secret_key = 'secret-key'

# Register blueprint under /scan
app.register_blueprint(scan_bp, url_prefix='/scan')

@app.route('/')
def home():
    return redirect('/scan/')  # Note the trailing slash for consistency

if __name__ == '__main__':
    app.run(debug=True)
