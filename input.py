import speech_recognition as sr

def get_audio_input():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("음성 입력을 기다리는 중... 말해보세요!")
        audio = recognizer.listen(source)
        try:
            user_input = recognizer.recognize_google(audio, language="ko-KR")
            print(f"사용자: {user_input}")
            return user_input
        except sr.UnknownValueError:
            print("음성을 인식하지 못했습니다. 다시 시도해주세요.")
            return ""
        except sr.RequestError:
            print("음성 인식 서비스에 접근할 수 없습니다.")
            return ""
