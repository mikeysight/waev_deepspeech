from django.shortcuts import render, redirect
from django.http import HttpResponse

from google.cloud import storage
from google.cloud import speech_v1
from google.cloud.speech_v1 import enums

from .models import AudioFile
import json
import sox
from django.conf import settings

def upload(request):
    # retrieves filename from post request
    data = json.loads(request.body)
    filename = data.get('filename')
    
    #google upload to bucket parameters
    storage_client = storage.Client()
    bucket = storage_client.bucket('waev')
    blob = bucket.blob(filename+'.flac')
    audio=f"{settings.MEDIA_ROOT}/{filename}"

    #convert audio file to mono FLAC, 16000 samplerate to optimize transcription
    tfm=sox.Transformer()
    tfm.convert(samplerate=16000, n_channels=1)
    new_audio=audio+'.flac'
    audio=tfm.build(audio, new_audio)

    #upload file to bucket
    blob.upload_from_filename(new_audio)
    print("file uploaded!")

    return HttpResponse()

def transcribe(request):
    # retrieve filename and file id from post request
    data=json.loads(request.body)
    filename= data.get('filename')
    file_id= data.get('id')

    #google speech-to-text API parameters
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

    #transcribe audio file
    operation = client.long_running_recognize(config, audio)
    print(u"Waiting for operation to complete...")
    response = operation.result()
   
    #create custom response to save to DB and then send back to front end
    transcription_response=[]
    for result in response.results:
        alternative = result.alternatives[0]
        for word in alternative.words:
            word_dict = {'text': f"{word.word}", 'timestamp': f"{word.start_time.seconds}"}
            transcription_response.append(word_dict)
    
    transcript_json = json.dumps(transcription_response)

    #update transcript in database
    audiofile=AudioFile.objects.get(id=file_id)
    audiofile.transcript=transcript_json
    audiofile.save()

    return HttpResponse(transcript_json)



