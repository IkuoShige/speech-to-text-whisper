# Normal user cannot use api by openai
import openai

openai.organization = "ORGANIZATION_ID"
openai.api_key = "OPENAI_API_KEY"

def speech_to_text(filepath):
    audio_file = open(filepath, "rb")

    response = openai.Audio.transcribe(model = "whisper-1", file = audio_file,)
    return response.text

filepath = "/home/ikuo/Downloads/chat-gpt-audio-test.wav"

result = speech_to_text(filepath)

print(result)
