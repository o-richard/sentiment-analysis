from fastapi import FastAPI
from model import result

app = FastAPI()


@app.post("/")
async def sentiment(text: str):
    text_result = result(text)
    # Store the text intepretation of the result
    value = ""
    if text_result == 4:
        value = "The text you have entered is positive."
    elif text_result == 0:
        value = "The text you have entered is negative."
    else:
        value = "The text you have entered could not be processed."
    return {"result": value}
