from django.shortcuts import render
from django.http import HttpResponse
from google.cloud import storage
import json

def upload(request):
    data = request.POST
    print(data)
    data = data.get('filename')
    print(data)
    """Uploads a file to the bucket."""
    # bucket_name = "your-bucket-name"
    # source_file_name = "local/path/to/file"
    # destination_blob_name = "storage-object-name"

    storage_client = storage.Client()
    bucket = storage_client.bucket('waev')
    blob = bucket.blob(data)

    audio=f"/Users/michael/waev/secrets/media/{data}"
    blob.upload_from_filename(audio)

    print(
        "File {} uploaded to {}.".format(
            data, data
        )
    )

# filename= POST.request(filename)   
# audio=f"/Users/michael/waev/secrets/media/{request.POST}"
# upload('waev', audio , filename)

