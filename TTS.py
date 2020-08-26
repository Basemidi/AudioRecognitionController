import pyttsx3


class voiceOut:

    def __init__(self):

        self.positivMap = self.loadText('positiv.dat')
        self.negativeMap = self.loadText('negative.dat')
        self.conf = self.loadText('conf.dat')

        self.engine = pyttsx3.init()
        voices = self.engine.getProperty('voices')
        self.engine.setProperty('voice', voices[1].id)
        self.engine.setProperty('rate', 150)

        self.engine.say("System is up and running, Boss!")
        self.engine.runAndWait()
        self.engine.say("Its good to be back!")
        self.engine.runAndWait()

    def speak(self, text):
        self.engine.say(text)
        self.engine.runAndWait()
    
    def loadText(self, name):

        t = []
        f = open('data/' + name, 'r')

        for line in f:
            t.append(line)
        
        f.close()
        return t




