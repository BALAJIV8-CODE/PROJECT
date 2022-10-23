#convert text words into audio

#import gtts 
#import os 
from gtts import gTTS
import os

 #text stored
storeText_1 = 'Department : BCA , year : 3 , name : balaji , lazy reader : python script'

#determine language to spell
language = 'en'

#convert the text
myText_2 = gTTS(text=storeText_1, lang=language,slow=True)
#save the text to audio format
myText_2.save("bca-department.mp3")
#play audio saved
os.system("mpg321 bca-department.mp3")
