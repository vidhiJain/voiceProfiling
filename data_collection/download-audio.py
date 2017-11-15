# from openpyxl import load_workbook
import numpy as np
import pandas as pd
import os

workbook = pd.ExcelFile("video_links_data.xlsx")
df = workbook.parse("video_links_data")  # Parse the sheet into a dataframe
name = df['name']
tag = df['tag']

df['url']=""
for i in xrange(0,len(df['name'])):
    df['url'][i] = "http://www.youtube.com/watch?v="+df['tag'][i]

# for i in range(3):
for i in range(0,len(df['name'])):
    flag = False
    print i
    request =  "youtube-dl --extract-audio --audio-format mp3 "+df['url'][i]
    try:
        os.system(request)
        flag = True
    error:
        print("Error at"+name)
        flag = False
    with open("audio_downloaded", "a") as outfile:
        writer = csv.writer(csvfile, delimiter=',',
                quotechar='"', quoting=csv.QUOTE_MINIMAL)
        writer.writerow([name, tag, flag])
