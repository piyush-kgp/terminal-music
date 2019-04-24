# # -*- coding: utf-8 -*-
#
# # Sample Python code for youtube.search.list
# # See instructions for running these code samples locally:
# # https://developers.google.com/explorer-help/guides/code_samples#python
#
import os
import config
import googleapiclient.discovery
config =  config.Config()
API_KEY = config.api_key
MAXRESULTS = 10
ORDER = "relevance"

def request(query):
    # Disable OAuthlib's HTTPS verification when running locally.
    # *DO NOT* leave this option enabled in production.
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

    api_service_name = "youtube"
    api_version = "v3"
    DEVELOPER_KEY = API_KEY

    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, developerKey = DEVELOPER_KEY)

    request = youtube.search().list(
        part="snippet",
        type="video",
        maxResults=MAXRESULTS,
        order=ORDER,
        q=query
    )
    response = request.execute()
    return {item['id']['videoId']: item['snippet']['title'] for item in response['items']}

if __name__ == "__main__":
    print(request("anoushka shankar"))
