from flask import Flask
import random
import time

app = Flask(__name__)

@app.route("/")
def home():
    # Random delay (simulate slowness)
    if random.randint(1, 6) == 3:
        time.sleep(5)        # causes timeouts

    # Random crash
    if random.randint(1, 8) == 5:
        return 1 / 0        # division by zero crash

    # Random internal error
    if random.randint(1, 10) == 7:
        raise Exception("Random internal failure")

    return "Hello from buggy app — sometimes I crash 😈"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=6000)
