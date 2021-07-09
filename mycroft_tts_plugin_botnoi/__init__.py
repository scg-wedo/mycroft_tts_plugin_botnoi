import requests
from mycroft.tts import TTS, TTSValidator

class botnoiTTSPlugin(TTS):
    """Interface to Botnoi TTS."""
    def __init__(self, lang, config):
        super(botnoiTTSPlugin, self).__init__(lang, config, BotnoiTTSValidator(
            self), 'mp3')

    def get_tts(self, sentence, wav_file):
        url = "https://openapi.botnoi.ai/service-api/text2speech-female?text=สวัสดี&speaker=tonkhaow"
        headers = {
            'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2MjYwNjMyMzAsImlkIjoiZjgxZDFlYmEtNTQ4Zi00ZjdiLWI1N2YtZDYxZjFhNGFlNmI3IiwiaXNzIjoiRVd0MGxYWHNzUVMzUklsMkVUVWczQnRYVEdHVkdFSlciLCJuYW1lIjoiS2VuIiwicGljIjoiaHR0cHM6Ly9wcm9maWxlLmxpbmUtc2Nkbi5uZXQvMGhMd0dtOElpUUUxaDZGRHdadUdCc0QwWlJIVFVOT2hVUUFub0lPRmhIU1d4ZWNWWUdUM05VYXcxSEhUOVFkd0VQUlNkWk9Bb1hTejFRIn0.qcaqEGfARKFyGRCLnMvPDsCnLgwNaWvnaHh6wDPzmPo'
        }
        response = requests.request("GET", url, headers = headers)
        with open(str(wav_file), 'wb') as file:
            file.write(response.content)
        return (wav_file, None)  # No phonemes

class BotnoiTTSValidator(TTSValidator):
    def __init__(self, tts):
        super(BotnoiTTSValidator, self).__init__(tts)

    def validate_lang(self):
        lang = self.tts.lang
        if lang.lower() != "th":
            raise ValueError("Language not supported by botnoiTTS: {}"
                             .format(lang))

    def validate_connection(self):
        try:
            url = "https://openapi.botnoi.ai/service-api/text2speech-female?text=สวัสดี&speaker=tonkhaow"
            headers = {
                'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2MjYwNjMyMzAsImlkIjoiZjgxZDFlYmEtNTQ4Zi00ZjdiLWI1N2YtZDYxZjFhNGFlNmI3IiwiaXNzIjoiRVd0MGxYWHNzUVMzUklsMkVUVWczQnRYVEdHVkdFSlciLCJuYW1lIjoiS2VuIiwicGljIjoiaHR0cHM6Ly9wcm9maWxlLmxpbmUtc2Nkbi5uZXQvMGhMd0dtOElpUUUxaDZGRHdadUdCc0QwWlJIVFVOT2hVUUFub0lPRmhIU1d4ZWNWWUdUM05VYXcxSEhUOVFkd0VQUlNkWk9Bb1hTejFRIn0.qcaqEGfARKFyGRCLnMvPDsCnLgwNaWvnaHh6wDPzmPo'
            }
            requests.request("GET", url, headers = headers)
        except Exception:
            raise Exception(
                'BotnoiTTS server could not be verified. Please check your '
                'internet connection.')

    def get_tts_class(self):
        return BotnoiTTSValidator