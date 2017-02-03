Transcription Service
######################################################################
| 
| Problem: Wav files exist in tables used for a content management system.
| 		   A person must listen to the file and then transcribe the applicable 
|		   portions of the file.
| Solution: Scan the tables where the files exist. Use the Google Cloud Speech API
|           to convert the wav files into text and insert back into the table to be
|		    read.


File Structure
**********************************************************************
| ./
| +-- bin
| |  +-- scribe.py
| +-- src
| |  +-- AppSettings.py
| |  +-- ImapConnection.py
| +-- settings
| |  +-- Ex1
| |      +-- Ex2
| License
| README
......................................................................
