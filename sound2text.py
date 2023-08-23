import speech_recognition as sr
import os



def transcribe_audio(audio_file: str) -> str:
    pass

def dig_files(directory: str) -> None:
    for file in os.listdir(directory):
        if os.path.isdir(directory + "/" + file):
            dig_files(directory + "/" + file)
        else:
            print(directory + "/" + file)

if __name__ == "__main__":
    directory = "./SuperELMer"
    dig_files(directory)


