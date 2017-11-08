#!/usr/bin/python

from apiclient.discovery import build
from apiclient.errors import HttpError
from oauth2client.tools import argparser
import csv
import pandas as pd 

# Set DEVELOPER_KEY to the API key value from the APIs & auth > Registered apps
# tab of
#   https://cloud.google.com/console
# Please ensure that you have enabled the YouTube Data API for your project.
with open("google_api_key", "wb") as keyfile:
	api_key = keyfile.read()
DEVELOPER_KEY = api_key
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"

term_list = []
with open('testList.csv', 'r') as f:
  reader = csv.reader(f)
  term_list = list(reader)

search_term_list = [str(item[0]).replace(" ", "+") + str("+Speech") for item in term_list]

def youtube_search(options, video_name, key):
  youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,
    developerKey=DEVELOPER_KEY)

  # Call the search.list method to retrieve results matching the specified
  # query term.
  for item in search_term_list:
     # DEBUG
    print "Search term", item
    search_response = youtube.search().list(
      q=item,
      part="id,snippet",
      maxResults=options.max_results
    ).execute()

    # Add each result to the appropriate list, and then display the lists of
    # matching videos, channels, and playlists.
    for search_result in search_response.get("items", []):
      if search_result["id"]["kind"] == "youtube#video":
        video_name.append(search_result["snippet"]["title"])
        key.append(search_result["id"]["videoId"])
        print "Video name", search_result["snippet"]["title"]
        print "key", search_result["id"]["videoId"]

if __name__ == "__main__":
  argparser.add_argument("--q", help="Search term", default="Google")
  argparser.add_argument("--max-results", help="Max results", default=5)
  args = argparser.parse_args()
 
  video_name = []
  key = []
  try:
    youtube_search(args, video_name, key)
  except HttpError, e:
    print "An HTTP error %d occurred:\n%s" % (e.resp.status, e.content)
  videos = {"video_name":video_name, "key":key, "search_term": term_list}
    # DEBUG
  # print "Videos:\n", "\n".join(videos), "\n"
  # Write to csv
  df = pd.DataFrame(videos, columns=['video_name', 'key', 'search_term'])
  with open("links.csv", "a") as datafile:
    df.to_csv(datafile, header=False, index = False)
