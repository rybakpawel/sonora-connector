from fastapi import FastAPI, HTTPException
from fastapi.responses import StreamingResponse
import requests
import base64
from io import BytesIO
from pydantic import BaseModel

app = FastAPI(title="Sonora Connector API")

DJANGO_API_URL = "http://sonora-backend:8000/api/ai/search_for_answer/"

class AudioPayload(BaseModel):
    filename: str
    contentType: str
    audioBase64: str

@app.post("/ask-audio/")
async def ask_audio(payload: AudioPayload):
    print(f"Otrzymano plik audio: {payload.filename}")

    response = {
        "success": True,
        "answer": "odpowiedź"
    }

    return response

    # files = {"audio": (audio.filename, await audio.read(), audio.content_type)}

    # try:
    #     response = requests.post(DJANGO_API_URL, files=files, timeout=60)
    # except requests.exceptions.RequestException as e:
    #     raise HTTPException(status_code=502, detail=f"Problem z połączeniem do API Django: {str(e)}")

    # if response.status_code != 200:
    #     raise HTTPException(status_code=response.status_code, detail=response.text)

    # try:
    #     data = response.json()
    #     return data
    # except ValueError:
    #     return StreamingResponse(BytesIO(response.content), media_type="audio/mpeg")
