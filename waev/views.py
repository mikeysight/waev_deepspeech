from django.shortcuts import render, redirect
from django.http import HttpResponse
from google.cloud import storage
from google.cloud import speech_v1
from google.cloud.speech_v1 import enums
from .models import AudioFile
import json
import sox

def upload(request):
    data = json.loads(request.body)
    filename = data.get('filename')

    storage_client = storage.Client()
    bucket = storage_client.bucket('waev')
    blob = bucket.blob(filename+'.flac')

    audio=f"/Users/michael/waev/secrets/media/{filename}"
    tfm=sox.Transformer()
    tfm.convert(samplerate=16000, n_channels=1)
    new_audio=audio+'.flac'
    audio=tfm.build(audio, new_audio)
    blob.upload_from_filename(new_audio)

    return HttpResponse()

def transcribe(request):
    data=json.loads(request.body)
    filename= data.get('filename')
    file_id= data.get('id')
    print(file_id)

    client = speech_v1.SpeechClient()
    sample_rate_hertz = 16000
    language_code = "en-US"

    config = {
        "sample_rate_hertz": sample_rate_hertz,
        "language_code": language_code,
        "encoding": "FLAC",
        "enable_word_time_offsets": True,
    }
    storage_uri=f"gs://waev/{filename}.flac"
    audio = {"uri": storage_uri}
    operation = client.long_running_recognize(config, audio)

    # print(u"Waiting for operation to complete...")
    response = operation.result()
    # print(response)
    
    transcription_response=[]

    for result in response.results:
        alternative = result.alternatives[0]
        for word in alternative.words:
            word_dict = {'text': f"{word.word}", 'timestamp': f"{word.start_time.seconds}:{word.start_time.nanos}"}
            # print(word_dict)
            transcription_response.append(word_dict)
    # print(transcription_response)
    transcript_json = json.dumps(transcription_response)
    # print(transcript_json)
    audiofile=AudioFile.objects.get(id=file_id)
    audiofile.transcript=transcript_json
    audiofile.save()


    return HttpResponse(transcript_json)



