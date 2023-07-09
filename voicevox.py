import json
import requests
import wave
class Himari:
    def generate_wav(text, speaker=14, filepath='./audio.wav'):
        host = 'localhost'
        port = 50021
        params = (
            ('text', text),
            ('speaker', speaker),
        )
        response1 = requests.post(
            f'http://{host}:{port}/audio_query',
            params=params
        )
        headers = {'Content-Type': 'application/json'}
        response2 = requests.post(
            f'http://{host}:{port}/synthesis',
            headers=headers,
            params=params,
            data=json.dumps(response1.json())
        )

        wf = wave.open(filepath, 'wb')
        wf.setnchannels(1)
        wf.setsampwidth(2)
        wf.setframerate(24000) # 24000Hz
        wf.writeframes(response2.content)
        wf.close()
