import os
from flask import Flask, render_template_string, request, send_from_directory

app = Flask(__name__)

# Config
ALLOWED_IPS = ['127.0.0.1','192.168.0.164','192.168.0.203','192.168.0.206'] #ip authorized
PORT = 12345
# Exclude files
IGNORE_FILES = ['cheapdeck.py', 'launch.bat']
# IMG Check
IMG_EXTS = ['.png', '.jpg', '.jpeg', '.gif', '.svg']

@app.before_request
def limit_remote_addr():
    if request.remote_addr not in ALLOWED_IPS:
        return f"{request.remote_addr}", 403

def get_deck_items():
    items = []
    base_path = os.path.dirname(os.path.abspath(__file__))
    
    files = os.listdir(base_path)
    
    for filename in files:
        name, ext = os.path.splitext(filename)
        
        if os.path.isdir(filename) or filename in IGNORE_FILES or ext.lower() in IMG_EXTS:
            continue
            
        img_name = None
        for img_ext in IMG_EXTS:
            potential_img = f"{name}{img_ext}"
            if potential_img in files:
                img_name = potential_img
                break
        
        items.append({
            'name': name,
            'full_name': filename,
            'img': img_name
        })
    return items

@app.route('/')
def index():
    items = get_deck_items()
    return render_template_string("""
    <!DOCTYPE html>
    <html lang="fr">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
        <title>CheapDeck</title>
        <style>
            body { 
                background: #121212; color: white; font-family: 'Segoe UI', sans-serif; 
                margin: 0; padding: 20px; display: flex; justify-content: center;
                -webkit-tap-highlight-color: transparent;
            }
            .grid { 
                display: grid; 
                grid-template-columns: repeat(auto-fill, 150px); 
                gap: 20px; width: 100%; max-width: 1000px; justify-content: center; 
            }
            .card { 
                width: 150px; text-align: center; cursor: pointer; 
                user-select: none; transition: transform 0.1s;
            }
            .card:active { transform: scale(0.92); }
            .card img { 
                width: 140px; height: 140px; border-radius: 18px; 
                object-fit: cover; border: 2px solid #333;
                background: #1e1e1e;
                box-shadow: 0 8px 15px rgba(0,0,0,0.5);
            }
            .card span { 
                display: block; margin-top: 10px; font-size: 13px; 
                font-weight: 500; color: #bbb; overflow: hidden;
                text-overflow: ellipsis; white-space: nowrap;
            }
        </style>
    </head>
    <body>
        <div class="grid">
            {% for item in items %}
            <div class="card" onclick="run('{{ item.full_name }}')">
                <img src="/raw/{{ item.img or '' }}" alt="">
                <span>{{ item.name }}</span>
            </div>
            {% endfor %}
        </div>
        <script>
            function run(file) {
                fetch('/run/' + encodeURIComponent(file));
                if (window.navigator.vibrate) window.navigator.vibrate(40);
            }
        </script>
    </body>
    </html>
    """, items=items)

@app.route('/run/<path:filename>')
def run_file(filename):
    if filename in IGNORE_FILES: abort(403)
    path = os.path.abspath(filename)
    if os.path.exists(path):
        os.startfile(path)
        return "OK", 200
    return "Error", 404

@app.route('/raw/<path:filename>')
def get_static(filename):
    if not filename: return abort(404)
    return send_from_directory('.', filename)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=PORT)
