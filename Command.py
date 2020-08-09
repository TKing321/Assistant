import speech_recognition as sr
from playsound import playsound


def listen():
    rec = sr.Recognizer()
    mic = sr.Microphone()
    playsound('./Resources/beep-08b.mp3')
    vocal = recognize_speech_from_mic(rec, mic)
    if vocal["error"]:
        print("ERROR: {}".format(vocal["error"]))
        return

    command = format(vocal["transcription"])
    print(command)
    command = command.split(" ")
    print(command)


def recognize_speech_from_mic(recognizer, microphone):
    if not isinstance(recognizer, sr.Recognizer):
        raise TypeError("`recognizer` must be `Recognizer` instance")

    if not isinstance(microphone, sr.Microphone):
        raise TypeError("`microphone` must be `Microphone` instance")

    with microphone as source:
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    # set up the response object
    response = {
        "success": True,
        "error": None,
        "transcription": None
    }

    # try recognizing the speech in the recording
    # if a RequestError or UnknownValueError exception is caught,
    #     update the response object accordingly
    try:
        response["transcription"] = recognizer.recognize_google(audio)
    except sr.RequestError:
        # API was unreachable or unresponsive
        response["success"] = False
        response["error"] = "API unavailable"
    except sr.UnknownValueError:
        # speech was unintelligible
        response["error"] = "Unable to recognize speech"

    return response
