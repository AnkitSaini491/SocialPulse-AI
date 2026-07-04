import requests

API_KEY = "YOUR_YOUTUBE_API_KEY"

def get_channel_data(channel_name):

    return {
        "name": channel_name,
        "subscribers": "Loading...",
        "views": "Loading...",
        "videos": "Loading...",
        "score": "Loading..."
    }
