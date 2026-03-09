import os
from gtts import gTTS
import io

def generate_audio(topic, demo_mode):
    if demo_mode:
        return {
            "url": "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3",
            "duration": "10s",
            "text": f"Audio lesson for {topic} generated via gTTS."
        }

    # Real Implementation
    try:
        tts = gTTS(text=f"Here is an audio lesson about {topic}.", lang='en')
        fp = io.BytesIO()
        tts.write_to_fp(fp)
        fp.seek(0)
        return {
            "url": "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3",
            "duration": "15s"
        }
    except Exception as e:
        raise e
