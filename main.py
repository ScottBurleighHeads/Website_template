from dotenv import load_dotenv
load_dotenv()

from flask import Flask, render_template
app = Flask(__name__)

from controllers import registerable_controllers
for controller in registerable_controllers:
    app.register_blueprint(controller)
