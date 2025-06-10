from flask import Flask, request, send_file

app = Flask(__name__)

characters = [
    {
        "name": "Arjun Roy",
        "role": "Cyber Intelligence Officer",
        "bio": "💻 A RAW agent and OSINT expert. Leads covert cyber ops across borders using zero-trace reconnaissance and active botnet monitoring.",
        "img": "pic1.png",
        "music": ""
    },
    {
        "name": "Meher Sinha",
        "role": "Digital Forensics Specialist",
        "bio": "🧠 CHFI certified, Meher is Mumbai's top cybercell analyst. She can extract deleted payloads, trace spoofed IPs, and recover compromised drives like a magician.",
        "img": "pic2.png",
        "music": ""
    },
    {
        "name": "Inspector Gajraj Jadhav",
        "role": "Senior Inspector, Cyber Crime Branch – Mumbai",
        "bio": "🚨 A no-nonsense cop from Maharashtra. Combines old-school policing with digital raids. Known for tracking down Discord gangs and SIM-swap cartels.",
        "img": "pic3.png",
        "music": "simba.mp3"
    }
]

@app.route('/')
def home():
    return '''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Bhari Traffic
इतना ट्रैफिक… सरकार भी नहीं रोक पाएगी 😈</title>
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <link href="https://fonts.googleapis.com/css2?family=Orbitron:wght@500&display=swap" rel="stylesheet">
        <style>
            body {
                background: #000;
                color: #00ffe1;
                font-family: 'Orbitron', sans-serif;
                text-align: center;
                padding: 20px;
            }
            h1 {
                color: #ff00cc;
            }
            .story {
                background: #111;
                border: 2px dashed #00ffe1;
                padding: 20px;
                margin: 20px auto;
                border-radius: 10px;
                max-width: 500px;
                font-size: 1em;
                line-height: 1.5em;
                box-shadow: 0 0 10px #00ffe1;
                font-family: 'Orbitron', sans-serif;
                white-space: pre-wrap;
                word-wrap: break-word;
            }
            img {
                width: 90vw;
                max-width: 380px;
                border: 3px solid #00ffe1;
                border-radius: 12px;
                margin: 20px 0;
            }
            .btn {
                padding: 10px 20px;
                background: #00ffe1;
                color: #000;
                font-weight: bold;
                border: none;
                border-radius: 8px;
                text-decoration: none;
                box-shadow: 0 0 10px #00ffe1;
            }
            .btn:hover {
                background: #00ffff;
                box-shadow: 0 0 20px #00ffff;
            }
        </style>
    </head>
    <body>
        <h1>🕵️ Operation: Bhari Traffic</h1>

<p>इतना ट्रैफिक… सरकार भी नहीं रोक पाएगी 😈</p>
        <img src="/file/img1.png" alt="Mission Image">
        <div class="story" id="storyBox"></div>
        <a href="/characters" class="btn">🎭 Meet the Characters</a>
        <script>
            const text = `
🚨 A wave of DDoS attacks has crippled India's digital systems.

🔍 RAW and Cyber Crime Branch teams suspect a teen hacker from Discord & Telegram.

👤 Your mission begins with intelligence gathered by 3 operatives.

💡 Dive in. Decode. Disrupt. This is your call to cyberspace.
            `;
            let i = 0;
            function typeWriter() {
                if (i < text.length) {
                    document.getElementById("storyBox").innerHTML += text.charAt(i);
                    i++;
                    setTimeout(typeWriter, 22);
                }
            }
            window.onload = typeWriter;
        </script>
    </body>
    </html>
    '''

@app.route('/characters')
def characters_view():
    i = int(request.args.get('i', 0))
    character = characters[i]
    next_i = i + 1 if i + 1 < len(characters) else 0
    prev_i = i - 1 if i > 0 else len(characters) - 1

    next_button = (
        f'<a href="/characters?i={next_i}" class="btn">→ Next</a>'
        if i + 1 < len(characters)
        else '<a href="https://diedromeo.github.io/jj/" class="btn special">🚀 Start Challenges</a>'
    )

    return f'''
    <!DOCTYPE html>
    <html>
    <head>
        <title>{character["name"]}</title>
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <link href="https://fonts.googleapis.com/css2?family=Orbitron:wght@500&display=swap" rel="stylesheet">
        <style>
            body {{
                background: linear-gradient(145deg, #000, #0f0f0f);
                color: #00ffe1;
                font-family: 'Orbitron', sans-serif;
                text-align: center;
                padding: 40px;
            }}
            h1 {{
                font-size: 2em;
                color: #ff00cc;
            }}
            h3 {{
                font-size: 1.2em;
                color: #fff;
                margin-top: -10px;
            }}
            .bio {{
                background: #111;
                border: 2px dashed #00ffe1;
                padding: 20px;
                margin: 20px auto;
                border-radius: 10px;
                max-width: 500px;
                font-size: 1em;
                min-height: 120px;
            }}
            img {{
                width: 300px;
                border-radius: 15px;
                border: 3px solid #00ffe1;
                margin-top: 20px;
            }}
            .btn {{
                display: inline-block;
                margin: 15px;
                padding: 12px 25px;
                background: #ff00cc;
                color: #fff;
                text-decoration: none;
                border-radius: 8px;
                font-size: 1em;
                box-shadow: 0 0 10px #ff00cc;
            }}
            .btn:hover {{
                background: #ff33dd;
                box-shadow: 0 0 20px #ff33dd;
            }}
            .special {{
                background: #00ff99;
                color: #000;
                font-weight: bold;
                box-shadow: 0 0 15px #00ff99;
            }}
        </style>
    </head>
    <body>
        {'<audio autoplay loop><source src="/file/' + character["music"] + '" type="audio/mpeg"></audio>' if character["music"] else ''}
        <h1>{character["name"]}</h1>
        <h3>{character["role"]}</h3>
        <img src="/file/{character["img"]}" alt="{character["name"]}">
        <div class="bio" id="bio"></div>
        <div>
            {'<a href="/characters?i=' + str(prev_i) + '" class="btn">← Previous</a>' if i > 0 else ''}
            {next_button}
        </div>
        <script>
            const bio = `{character["bio"]}`;
            let i = 0;
            const box = document.getElementById("bio");
            function typeWriter() {{
                if (i < bio.length) {{
                    box.innerHTML += bio.charAt(i);
                    i++;
                    setTimeout(typeWriter, 25);
                }}
            }}
            window.onload = typeWriter;
        </script>
    </body>
    </html>
    '''

@app.route('/file/<path:filename>')
def serve_file(filename):
    return send_file(filename)

if __name__ == '__main__':
    app.run(debug=True)
