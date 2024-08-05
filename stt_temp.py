from openai import OpenAI

client = OpenAI(api_key='')

audio_file = open(r"C:\Users\smkim\Downloads\download_record_20240711100516\temp_pk3.wav", "rb")
transcription = client.audio.transcriptions.create(
  model="whisper-1",
  file=audio_file
)
print(transcription.text)
