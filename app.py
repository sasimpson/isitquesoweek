from flask import Flask
from flask import render_template
from datetime import datetime, timedelta

app = Flask(__name__)

@app.route('/')
def index():
    today = datetime.now()
    #get beginning of the week (monday)
    bow = today - timedelta(today.weekday())
    #go back week by week until we get to the previous month's monday
    while(bow.month == today.month):
        bow = bow - timedelta(7)
    #go forward two weeks to get the second monday of the month
    valid_second_week = bow + timedelta(14)
    #does the requested date fit in this week?
    if today >= valid_second_week and today < (valid_second_week + timedelta(7)):
        status = "Yep!"
        background = "goldenrod"
    else:
        status = "Nope"
        background = "#ccc"

    return render_template('index.html', status=status, background=background)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
