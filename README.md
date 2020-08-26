# AudioRecognitionController
Provided is the foundation of a Voice Controller System based on Mozillas DeepSpeech Model


It comes with a simple user interface made with eel, Html Css and Javascript.

The Heart piece of this programm is the Contoller Class. It initiates the Voice Recorder which then starts 
collecting microphone inputs. This Audiostream gets saved and passed to the speech recognition if it contains
spoken parts. The returned text can then be used to perform tasks according to what has been said.

I used the pretrained Model provided by Mozilla for the inferenz, you can download it from their 
GitHub Page:

https://github.com/mozilla/STT/releases


Place the Model in the models folder and check if the naming is correct.
