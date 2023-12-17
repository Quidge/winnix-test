from flask import Flask
import settings

app = Flask(__name__)

@app.get("/hello")
def route():
    return "world"

if __name__  == "__main__":
    setting_1 = settings.SETTING_1
    print("setting 1", setting_1)
    app.run()