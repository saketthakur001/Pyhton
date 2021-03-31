from gtts import gTTS
import io
mp3_fp = io.BytesIO()
tts = gTTS('hello', lang='en')
tts.write_to_fp(mp3_fp)

# Load `mp3_fp` as an mp3 file in
# the audio library of your choice
io.open(mp3_fp)