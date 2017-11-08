# Voice Profiling

## Data Collection

### Selecting some famous personalities 
  Source: Google trends
  We need such famous personalitites whose data can be easily found on YouTube and Wikidata
  
  Output: [list_of_personalities.csv]()
  
### Collecting auio/video data 
  Source: [YouTube Data API]()
  Code: [youtube-search.py]()
  Dependencies: 
  * Google Python API Client
  * Registered API for YouTube Data API on Google Cloud Console
  
  Output: [youtube-links.csv]()
  
### Collecting Profile data 
  Source: [Wikidata-search]()
  Code: [wikidata-search.py]()
  Dependencies:
  * npm 
  * requests
  
  Output: [wikidata.json]()
  and [selected-wikidata.csv]()
  
  Source: [Google Knowledge Graph API]()
  Code: [search-kg.py]()
  
### Extracting audio from the YouTube Links
  Source: [youtube-dl]()
  Code: [extract_youtube_videos.py]()
  Dependencies:
  * pip install youtube-dl
  
  Output: 
  Each audio file saved by the search terms in [list_of_personalities.csv]()
