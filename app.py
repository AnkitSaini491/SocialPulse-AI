from flask import Flask, render_template, request
from youtube import get_channel_data

app = Flask(__name__)

@@app.route("/analyze", methods=["POST"])
def analyze():

    channel = request.form["channel"]

    data = get_channel_data(channel)

    if data is None:
        return "Channel Not Found"

    videos = get_latest_videos(data["channelId"])

    return render_template(

        "dashboard.html",

        data=data,

        videos=videos

    )

    channel = request.form["channel"]

    data = get_channel_data(channel)

    if data is None:
        return "Channel Not Found"

    return render_template(
        "dashboard.html",
        data=data
    )
