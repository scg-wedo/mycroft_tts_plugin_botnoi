#!/usr/bin/env python3
# -*- coding: utf-8 -*- 

# import requests
# from mycroft.tts import TTS, TTSValidator

# class botnoiTTSPlugin(TTS):
#     """Interface to Botnoi TTS."""
#     def __init__(self, lang, config):
#         super().__init__(lang, config, BotnoiTTSValidator(self))

#     def get_tts(self, sentence, wav_file):
#         url = "https://openapi.botnoi.ai/service-api/text2speech-female?text=สวัสดี&speaker=tonkhaow"
#         headers = {
#             'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2MjYzMDgxMjYsImlkIjoiZjgxZDFlYmEtNTQ4Zi00ZjdiLWI1N2YtZDYxZjFhNGFlNmI3IiwiaXNzIjoiRVd0MGxYWHNzUVMzUklsMkVUVWczQnRYVEdHVkdFSlciLCJuYW1lIjoiS2VuIiwicGljIjoiaHR0cHM6Ly9wcm9maWxlLmxpbmUtc2Nkbi5uZXQvMGhMd0dtOElpUUUxaDZGRHdadUdCc0QwWlJIVFVOT2hVUUFub0lPRmhIU1d4ZWNWWUdUM05VYXcxSEhUOVFkd0VQUlNkWk9Bb1hTejFRIn0.jFbxULw3Mm9zY47n-QGVVQSsYUhy_T1Xqh_zoBrnHCY'
#         }
#         response = requests.request("GET", url, headers = headers)
#         with open(str('tts.wav'), 'wb') as file:
#             file.write(response.content)
#         return ('tts.wav', None)  # No phonemes

# class BotnoiTTSValidator(TTSValidator):
#     def __init__(self, tts):
#         super(BotnoiTTSValidator, self).__init__(tts)

#     def validate_lang(self):
#         pass

#     def validate_connection(self):
#         pass

#     def get_tts_class(self):
#         return botnoiTTSPlugin


from gtts import gTTS
from gtts.lang import tts_langs

from mycroft.tts import TTS, TTSValidator

supported_langs = tts_langs()


class botnoiTTSPlugin(TTS):
    """Interface to google TTS."""
    def __init__(self, lang, config):
        if lang.lower() not in supported_langs and \
                                     lang[:2].lower() in supported_langs:
            lang = lang[:2]
        super(botnoiTTSPlugin, self).__init__(lang, config, GoogleTTSValidator(
            self), 'mp3')

    def get_tts(self, sentence, wav_file):
        """Fetch tts audio using gTTS.
        Arguments:
            sentence (str): Sentence to generate audio for
            wav_file (str): output file path
        Returns:
            Tuple ((str) written file, None)
        """
        tts = gTTS(text=sentence, lang=self.lang)
        tts.save(wav_file)
        return (wav_file, None)  # No phonemes


class GoogleTTSValidator(TTSValidator):
    def __init__(self, tts):
        super(GoogleTTSValidator, self).__init__(tts)

    def validate_lang(self):
        lang = self.tts.lang
        if lang.lower() not in supported_langs:
            raise ValueError("Language not supported by gTTS: {}"
                             .format(lang))

    def validate_connection(self):
        try:
            gTTS(text='Hi').save(self.tts.filename)
        except Exception:
            raise Exception(
                'GoogleTTS server could not be verified. Please check your '
                'internet connection.')

    def get_tts_class(self):
        return botnoiTTSPlugin