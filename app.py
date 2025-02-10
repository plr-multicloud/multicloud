from flask import Flask, redirect

app = Flask(__name__)

@app.route('/')
def redirect_to_aws():
    return redirect("http://simulation-multicloud.s3.us-east-2.amazonaws.com/index.html", code=302)  # Change to your AWS URL

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
