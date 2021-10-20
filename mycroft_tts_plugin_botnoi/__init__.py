#!/usr/bin/env python3
# -*- coding: utf-8 -*- 

from typing import TextIO
import requests
from mycroft.tts import TTS, TTSValidator
token = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2MzQ5Nzk3NzgsImlkIjoiYjU5NTY2ZTMtYjg2Yi00YmMzLWIwMDktNDZlOGNlYzI4NjYzIiwiaXNzIjoiVVN4WGp1c2w4SmNsTFJjWFhYd21ud253TjlkV2JqOHQiLCJuYW1lIjoiOlB1bm4iLCJwaWMiOiJodHRwczovL3Byb2ZpbGUubGluZS1zY2RuLm5ldC8waGtPTFl6VWhZTkdCeElCOGJud2RMTjAxbE9nMEdEaklvQ1VaN1VsSWtPbGxVR1hJLUdSTi1CZ01wWWxKZUVTZGxUVVF1VlFNaWFRTloifQ.1WNw3USXEXmct5KA1xzkxTHUlUI7T5uDwc4yYnaMR2Q'

class botnoiTTSPlugin(TTS):
    """Interface to Botnoi TTS."""
    def __init__(self, lang=None, config=None):
        super(botnoiTTSPlugin, self).__init__(lang, config, BotnoiTTSValidator(self))

    def get_tts(self, sentence, wav_file):
        url = "https://openapi.botnoi.ai/service-api/text2speech-female?text="+str(sentence)+"&speaker=tonkhaow"
        headers = {
            'Authorization': 'Bearer '+str(token)
        }
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
