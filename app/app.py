from fastapi import FastAPI

app = FastAPI()


@app.post("/otp/test/{num}")
def check_otp(num: int):
    return ("num: {}".format(str(num)))
