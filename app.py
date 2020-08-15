from flask import Flask, url_for, make_response, request, render_template
from markupsafe import escape
from video_queue import run_video, run_image
from namelist import convert

app = Flask(__name__)

app.config['DEBUG'] = True


@app.route("/")
def root():
#    return render_template('main_sys.html') #this line use for running the queue system
    return render_template('main.html')

@app.route('/sucessed', methods=['POST'])
def post():

    username = request.form['username']
    # tweetNum = request.form['tweetNum']
    a = convert(username)
    if isinstance(a, list):
        run_video(a)
    else:
        exit()

    return render_template('result.html')