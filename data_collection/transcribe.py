#!/usr/bin/env python
import io
import os
import sys
import json

# Imports the Google Cloud client library
from google.cloud import speech
from google.cloud.speech import enums
from google.cloud.speech import types

# Instantiates a client
client = speech.SpeechClient()

# The name of the audio file to transcribe
from os import listdir
from os.path import isfile, join
#onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]

file_name = os.path.join(os.path.dirname(__file__),sys.argv[1])
print(file_name)

# Loads the audio into memory
with io.open(file_name, 'rb') as audio_file:
    content = audio_file.read()
    audio = types.RecognitionAudio(content=content)

config = types.RecognitionConfig(
    encoding=enums.RecognitionConfig.AudioEncoding.LINEAR16,
    sample_rate_hertz=16000,
    language_code='en-US')

# Detects speech in the audio file
response = client.recognize(config, audio)
print(response)
for result in response.results:
    print('Transcript {}:\n {}'.format(file_name, result.alternatives[0].transcript))
    with open("../subtitles/"+file_name[:-4]+".json", "a") as outfile:
    	json.dump(result.alternatives[0].transcript, outfile)
