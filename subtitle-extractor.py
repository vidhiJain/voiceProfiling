import os
import subprocess
import csv 

videos = []
with open('video_links_data.csv', 'r') as infile:
	reader = csv.reader(infile)
	videos = list(reader)

for item in videos:
	text="youtube-dl --all-subs --skip-download https://www.youtube.com/watch?v="+ item[1]
	output=subprocess.call(text,shell=True)
	with open('subtitle.csv', 'a') as outfile:
		if item < 0:
			print "Failure for ", item[0]
		else:
			writer = csv.writer(outfile,  delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL) 
			writer.writerow([str(item[0]), str(item[1]), str(item[2])])
