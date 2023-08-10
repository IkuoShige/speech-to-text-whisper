# Normal user cannot use api by openai
import openai

openai.organization = "org-fTcnhNYzMeXa8Kl8lhg6W7nm"
openai.api_key = "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"

def speech_to_text(filepath):
    audio_file = open(filepath, "rb")

    response = openai.Audio.transcribe(model = "whisper-1", file = audio_file,)
    return response.text

filepath = "/home/ikuo/Downloads/chat-gpt-audio-test.wav"

result = speech_to_text(filepath)

print(result)
