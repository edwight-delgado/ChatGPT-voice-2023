
from gtts import gTTS
import os, time 



class Talk:
    def __init__(self,lang='es') -> None:
        self.language = lang

    def speak(self,text):
        print(text)
        myobj = gTTS(text=text, lang=self.language, slow=False)
    
        # Saving the converted audio in a mp3 file named
        # welcome 
        myobj.save('buffer.mp3')
        os.system("mpg321 buffer.mp3")
        time.sleep(2)
        os.remove('buffer.mp3')