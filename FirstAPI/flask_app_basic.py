
# A very simple Flask Hello World app for you to get started with...

from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello from Flask!'

# Importante: Para o pythonanywhere.com comentar as linhas abaixo
if __name__ == '__main__':
    app.run()