
import requests
from config import API_KEY


def search_channel(channel_name):
    url = (
        "https://www.googleapis.com/youtube/v3/search"
        f"?part=snippet&type=channel&q={channel_name}&key={API_KEY}"
    )

    response = requests.get(url).json()

    if "items" not in response or len(response["items"]) == 0:
        return None

    return response["items"][0]["snippet"]["channelId"]


def get_channel_data(channel_name):

    channel_id = search_channel(channel_name)

    if channel_id is None:
        return None

    url = (
        "https://www.googleapis.com/youtube/v3/channels"
        f"?part=snippet,statistics"
        f"&id={channel_id}"
        f"&key={API_KEY}"
    )

    response = requests.get(url).json()

    if "items" not in response or len(response["items"]) == 0:
        return None

    item = response["items"][0]

    return {
        "channelId": channel_id,
        "name": item["snippet"]["title"],
        "logo": item["snippet"]["thumbnails"]["high"]["url"],
        "description": item["snippet"]["description"],
        "country": item["snippet"].get("country", "Unknown"),
        "published": item["snippet"]["publishedAt"][:10],
        "subscribers": "{:,}".format(
            int(item["statistics"].get("subscriberCount", 0))
        ),
        "views": "{:,}".format(
            int(item["statistics"].get("viewCount", 0))
        ),
        "videos": "{:,}".format(
            int(item["statistics"].get("videoCount", 0))
        ),
        "score": "95/100"
    }


def get_latest_videos(channel_id):

    url = (
        "https://www.googleapis.com/youtube/v3/search"
        f"?key={API_KEY}"
        f"&channelId={channel_id}"
        f"&part=snippet"
        f"&type=video"
        f"&order=date"
        f"&maxResults=6"
    )

    response = requests.get(url).json()

    videos = []

    if "items" not in response:
        return videos

    for item in response["items"]:

        videos.append({
            "title": item["snippet"]["title"],
            "thumbnail": item["snippet"]["thumbnails"]["high"]["url"],
            "videoId": item["id"]["videoId"]
        })

    return videos


def get_top_video(channel_id):

    url = (
        "https://www.googleapis.com/youtube/v3/search"
        f"?key={API_KEY}"
        f"&channelId={channel_id}"
        f"&part=snippet"
        f"&type=video"
        f"&order=viewCount"
        f"&maxResults=1"
    )

    response = requests.get(url).json()

    if "items" not in response or len(response["items"]) == 0:
        return None

    item = response["items"][0]

    return {
        "title": item["snippet"]["title"],
        "thumbnail": item["snippet"]["thumbnails"]["high"]["url"],
        "videoId": item["id"]["videoId"]
    }
