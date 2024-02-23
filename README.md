# Tunneling Services for Development Nodes

This document provides a summary of different tunneling services suitable for development purposes, including `ngrok`, `py-localtunnel`, and `PyPagekite`. These services allow developers to expose a local development server to the Internet, facilitating testing and sharing of web applications without deploying them to a public server.

## ngrok

[ngrok](https://ngrok.com/) is a popular tunneling service that provides a secure way to expose local servers to the internet. 

### Getting Started with ngrok

1. **Sign Up**: First, sign up for an account on the ngrok website.
2. **Authentication Token**: After signing up, retrieve your authentication token from the ngrok dashboard.
3. **Set Auth Token**: Store the authentication token in a `.env` file or use the ngrok CLI to add your auth token.
4. **Serve with ngrok**: Use ngrok to serve your `main.py` or any other application by executing a command like `ngrok http 8000`.

### Features and Pricing
- **Free Tier**: The free tier offers basic features with some limitations on the number of simultaneous tunnels and connections.
- **Pricing**: Check the [pricing page](https://ngrok.com/pricing) for detailed information on available plans and features.

## py-localtunnel

[py-localtunnel](https://github.com/jakbin/py-localtunnel) offers a simple way to expose local servers to the internet, acting as an alternative to ngrok.

### Getting Started with py-localtunnel

1. **Installation**: Install py-localtunnel using pip: `pip install py-localtunnel`.
2. **Run Uvicorn App**: Start your FastAPI or other ASGI app with Uvicorn.
3. **Expose with py-localtunnel**: In a separate terminal, run `pylt port PORT_NO` to expose your app.

### Considerations
- **Project Status**: py-localtunnel appears to be a smaller, possibly less maintained project. Assess for suitability in your projects.
- **Security**: Review the project's security measures as detailed documentation may be limited.

## PyPagekite

[PyPagekite](https://pagekite.net/) facilitates exposing local web servers to the internet with an emphasis on ease of use and flexibility.

### Getting Started with PyPagekite

1. **Download and Setup**: Follow the [quickstart guide](https://pagekite.net/support/quickstart/) to download and set up PyPagekite on your system.
2. **Alter Shebang**: Depending on your system, you may need to modify the shebang line in the `/usr/local/bin/pagekite.py` script.
3. **Use PyPagekite**: Start your local server and then use a command like `pagekite.py 8000 yoursubdomain.pagekite.me` to expose it. Sign up may be required beforehand.

### Features and Pricing
- **Free Tier**: PyPagekite offers a trial period with limited features.
- **Pricing**: Visit the [pricing page](https://pagekite.net/pricing/) for more details on plans and features.

### Final Note

Each service offers unique features and limitations. Evaluate based on your project requirements, considering factors like ease of use, security, and cost.
