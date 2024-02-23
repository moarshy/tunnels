import os
import requests
from dotenv import load_dotenv
from fastapi import FastAPI

load_dotenv()

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/ping")
async def ping():
    return {"message": "pong"}


### FAILED ATTEMPT TO USE IP ADDRESS
# @app.get("/ip")
# async def get_ip():
#     response = requests.get('https://httpbin.org/ip')
#     ip = response.json()['origin']

#     return JSONResponse(status_code=200, content={"ip": ip, 'reach_me': "http://"+ip+":8000"})

# def get_public_ip():
#     response = requests.get('https://httpbin.org/ip')
#     return response.json()['origin']




if __name__ == "__main__":
    import uvicorn

    # Setup ngrok; ephemeral public URL
    # from pyngrok import ngrok
    # ngrok.set_auth_token(os.getenv("NGROK_AUTH_TOKEN"))
    # ngrok_tunnel = ngrok.connect(8000, 'http')
    # print("Public URL:", ngrok_tunnel.public_url)

    # Use py-localtunnel
    ## once the server is running, run the following command in another terminal
    ## pylt port  8000


    # Start the server
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
