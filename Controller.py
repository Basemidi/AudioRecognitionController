
#THIS part is the Controller it transforms text requests comming from the voiceReco to actions.

import VoiceReco as VR
import TTS
import eel

import datetime


class Controller:

    def __init__(self):
        self.ears = VR.VoiceReco()
        self.voice = TTS.voiceOut()

        self.trigger = False

        for line in self.ears.recovoice():

            if line == 'friday':
                self.voice.speak('Boss?')
                self.trigger = True

            if self.trigger and not (line == ''):

                if ('what' in line or 'get' in line) and ('time' in line or 'date' in line):

                    timestring = datetime.datetime.now().strftime('%H:%M:%S')
                    datestring = datetime.datetime.now().strftime('%d %B %Y')

                    self.voice.speak(timestring)
                    self.voice.speak(datestring)

                self.trigger = False


        


    