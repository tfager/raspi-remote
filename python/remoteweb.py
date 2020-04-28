from flask import Flask, render_template, redirect, url_for
import paho.mqtt.client as mqtt

MQTT_TOPIC = "remote"
MQTT_SERVER = "raspberrypi.local"

app = Flask(__name__, template_folder="templates")
mqtt_client = mqtt.Client()
mqtt_client.enable_logger()

actions = {"music": "Play Music",
           "music_off": "Stop Music",
           "computer_audio": "Computer Audio",
           "netflix": "Netflix",
           "computer": "Computer Screen",
           "livetv": "Live TV",
           "playstation": "Playstation",
           "chromecast": "Chromecast",
           "tv_off": "TV Off"}

@app.route("/")
def main():
    return render_template("./main.html.j2",
                          actions=actions)


@app.route("/action/<action>", methods=["GET"])
def do_action(action):
    if action in actions.keys():
        mqtt_client.publish(MQTT_TOPIC, action)
    return redirect(url_for('main'))

def create_app():
    mqtt_client.connect_async(MQTT_SERVER, 1883, 60)
    mqtt_client.loop_start()
    return app

if __name__ == "__main__":
    create_app()
