from flask import Flask, request
import cgi

from caesar import rotate_string


app = Flask (__name__)
app.config['DEBUG'] = True


form = """
<!DOCTYPE html>

<html>
    <head>
        <style>
            form {{
                background-color: #eee;
                padding 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }}
            textarea {{
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }}
        </style>
    </head>
    <body>
        <!--create your form here-->
        <form action='/' method='POST'>
            <label> Rotate by
                <input name="rot" type="text" value="0"/>
                <textarea name="text" type="text">{0}</textarea>
            </label>

            <input type="submit"/>
            </form>

        
    </body>
</html>

"""

@app.route("/")
def index():
    return form.format('')

@app.route("/", methods=['POST'])
def encrypt():
    rot = int(request.form['rot'])

    crypt_message = ""
    for character in request.form['text']:
        crypt_message += rotate_string(character, rot)
        crypt_message = cgi.escape(crypt_message)
    return form.format (crypt_message)
  

app.run()
