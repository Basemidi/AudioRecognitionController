
import VoiceReco as Vc
import Controller
import eel
import TTS



@eel.expose
def voiceThread():

    Controller.Controller()



eel.init('web')

eel.start('main.html', cmdline_args=['--start-fullscreen', '--kiosk'])








