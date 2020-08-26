

import deepspeech as dp
import collections, queue
import webrtcvad
import numpy as np
import pyaudio



class VoiceReco:

    FORMAT = pyaudio.paInt16
    CHANNELS = 1
    FRATE = 16000
    BLOCKSPSECONDS = 50

    def __init__(self):

        def callback(in_data, frame_count, time_info, status_flags):
            self.audio_queue.put(in_data)
            return None, pyaudio.paContinue

        self.speech = dp.Model('models/deepspeech-0.7.0-models.pbmm')
        self.ioaudio = pyaudio.PyAudio()
        self.vad = webrtcvad.Vad(3)
        self.audio_queue = queue.Queue()

        self.stream = self.ioaudio.open(format=pyaudio.paInt16,
                                        channels=1,
                                        input=True,
                                        rate=self.FRATE,
                                        frames_per_buffer=int(self.FRATE /
                                                              self.BLOCKSPSECONDS),
                                        stream_callback=callback
                                        )
        self.stream.start_stream()

    def readframes(self):
        while True:
            yield self.audio_queue.get()

    def speechcollector(self):
        voice_collector = collections.deque()
        silent_count = 17

        for frame in self.readframes():

            voice_collector.append(frame)

            if not self.vad.is_speech(frame, self.FRATE):
                silent_count += 1
            else:
                silent_count = 0

            if 17 > silent_count > 15:
                for i in voice_collector:
                    yield i
                voice_collector.clear()
                yield None
            else:
                yield None

    def recovoice(self):

        stream = self.speech.createStream()
        trig = True

        for f in self.speechcollector():

            if f is not None:
                stream.feedAudioContent(np.frombuffer(f, dtype=np.int16))
                if not trig:
                    trig = True
            else:
                if trig:
                    tex = stream.finishStream()
                    print(tex)
                    trig = False
                    stream = self.speech.createStream()
                    yield tex

