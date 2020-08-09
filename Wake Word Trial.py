import porcupine
import pyaudio
import struct
import Command

pa = pyaudio.PyAudio()

handle = porcupine.create(keyword_file_paths=['C:/Users/blant/Desktop/Projects/GitHub Projects/Assistant/Resources/assistant_windows.ppn'],sensitivities=[1])

audio_stream = pa.open(
            rate=handle.sample_rate,
            channels=1,
            format=pyaudio.paInt16,
            input=True,
            frames_per_buffer=handle.frame_length)


while True:
        pcm = audio_stream.read(handle.frame_length)
        pcm = struct.unpack_from("h" * handle.frame_length, pcm)
        result = handle.process(pcm)
        if result:
            Command.listen()


