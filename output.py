import pyttsx3

def text_to_speech(text):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    
    # 여성 목소리로 설정 (한국어 여성 목소리 ID를 찾는 과정)
    for voice in voices:
        if 'female' in voice.name:
            engine.setProperty('voice', voice.id)
            break

    engine.say(text)
    engine.runAndWait()
