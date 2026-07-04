import requests

API_KEY = "YOUR_API_KEY"


def search_channel(channel_name):

    url = (
        f"https://www.googleapis.com/youtube/v3/search"
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
        f"https://www.googleapis.com/youtube/v3/channels"
        f"?part=snippet,statistics"
        f"&id={channel_id}"
        f"&key={API_KEY}"
    )

    response = requests.get(url).json()

    item = response["items"][0]

    return {

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
