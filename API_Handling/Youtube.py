import requests


def fetch_video_data():
    url = "https://api.freeapi.app/api/v1/public/youtube/videos"

    response = requests.get(url)
    response.raise_for_status()

    content = response.json()

    if content.get("success") and content.get("data"):
        video = content["data"]["data"][4]["items"]

        channel_id = video["snippet"]["channelId"]
        title = video["snippet"]["title"]
        duration = video["contentDetails"]["duration"]

        return channel_id, title, duration

    raise Exception("Failed to fetch data")


def main():
    try:
        channel_id, title, duration = fetch_video_data()

        print(f"Channel ID: {channel_id}")
        print(f"Title: {title}")
        print(f"Duration: {duration}")

    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()