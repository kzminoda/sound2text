import speech_recognition as sr
import os
import re



def transcribe_audio(path_to_mp3: str) -> str:
        output = os.path.basename(path_to_mp3) + ".txt"
        print(path_to_mp3)

def dig_files(directory: str) -> None:
    for file in os.listdir(directory):
        if os.path.isdir(directory + "/" + file):
            dig_files(directory + "/" + file)
        else:
            mp3 = directory + "/" + file
            p1 = r'Hop Skip Jump'
            p2 = r'Jump\.mp3'
            if re.search(p1, mp3) and re.search(p2, mp3):
                transcribe_audio(mp3)

if __name__ == "__main__":
    directory = "./SuperELMer"
    dig_files(directory)


