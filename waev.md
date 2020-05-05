# Waev

###### an audio transcription service.

## Project Overview
Waev is a web application that allows a user to upload an audio file to be transcribed and returned in line by line timecoded text format. The user can then request an .XML file of the transcript for external use. The application will be built with Vue with Django Rest Framework and utilize a python speech recognition package called SpeechRecognition, an audio package called FFmpeg, and the pydub audio manipulation module. 

## Features

**As an audiobook user**, i want to be able to find the time at which a portion of text occurs in my audio file so that i can easily pick up where i left off in my physical print copy. 

Tasks:
- Transcribe audio file into a string
- Display the string on a page as text with corresponding timecodes for each line
- Create an input element that allows the user to search for a section of text and returns it's corresponding timecode

**As an extension developer**, i want to be able to create an XML transcript of an audio file that can be used to interact with the functionality of various third party applications.

Tasks:
- Allow user to export timecoded transcript of audio as .XML file

**As any user**, i want to be able to log in to my account and save all my transcribed audio files.

- Create User model and create account page, link transcripted files to account

## Data Model

#### AudioFile
- audio file
- transcript (textfield)
- xml file (textfield)
- ForeignKey User

#### User
- username
- password
- email address
- date joined
- first name
- last name

## Schedule

Week 1
- Tue-Wed: Research libraries and plan/sketch layout, create project in VS Code and setup DRF + models
- Thu-Fri: implement user functionality in django

Week 2
- Mon-Wed: Install audio and speech recognition packages, begin testing on sample audio files
Thu-Fri: Build front end in Vue, integrate transcription into results page

Week 3:
- Mon-Tuesday: Integrate .XML export/download
- Wed-Thurs: Finish front end and final testing
- Friday: Finish up/Present?

Week 4:
- Monday: Present?
- Tue-Friday: polish up code, fix any bugs, research deployment



