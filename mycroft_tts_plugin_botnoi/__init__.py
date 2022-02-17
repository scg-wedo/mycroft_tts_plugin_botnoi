#!/usr/bin/env python3
# -*- coding: utf-8 -*- 

from typing import TextIO
import requests
from mycroft.tts import TTS, TTSValidator

class botnoiTTSPlugin(TTS):
    """Interface to Botnoi TTS."""
    def __init__(self, lang=None, config=None):
        super(botnoiTTSPlugin, self).__init__(lang, config, BotnoiTTSValidator(self))

    def get_tts(self, sentence, wav_file):
        token = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2NDUzNTg5NjQsImlkIjoiZjgxZDFlYmEtNTQ4Zi00ZjdiLWI1N2YtZDYxZjFhNGFlNmI3IiwiaXNzIjoiRVd0MGxYWHNzUVMzUklsMkVUVWczQnRYVEdHVkdFSlciLCJuYW1lIjoiS2VuIiwicGljIjoiaHR0cHM6Ly9wcm9maWxlLmxpbmUtc2Nkbi5uZXQvMGhMd0dtOElpUUUxaDZGRHdadUdCc0QwWlJIVFVOT2hVUUFub0lPRmhIU1d4ZWNWWUdUM05VYXcxSEhUOVFkd0VQUlNkWk9Bb1hTejFRIn0.P8BVEzgxdDgob5xXd6wEKdlKGqBR6G6cO7qKYrfbUaM'
        url = "https://openapi.botnoi.ai/service-api/text2speech-female?text="+str(sentence)+"&speaker=tonkhaow&format=wav"
        # url = "https://tts.botnoi.ai/demo/api/doctts?text="+str(sentence)+"&speaker=tonkhaow&api_key=1qL0ISiB1cjXjQ0HD-1sjjTHesZrkx9A_ym-ifUxCTWI"
        headers = {'Authorization': 'Bearer '+str(token)}
        # response = requests.request("GET", url)
        response = requests.request("GET", url, headers = headers)
        with open(wav_file, 'wb') as file:
            file.write(response.content)
        return (wav_file, None)  # No phonemes

class BotnoiTTSValidator(TTSValidator):
    def __init__(self, tts):
        super(BotnoiTTSValidator, self).__init__(tts)

    def validate_lang(self):
        pass

    def validate_connection(self):
        pass

    def get_tts_class(self):
        return botnoiTTSPlugin
