from flask import Flask, render_template, jsonify, request
from flask_cors import CORS
import fun

app = Flask(__name__)
CORS(app)

certificateData = {},

@app.route("/certificateData", methods = ['GET', 'POST'])
def certificateData():
    # certificateData

    if request.method == "GET":
        # mai jab lungi
        return certificateData
    elif request.method == "POST":
        content = request.get_json()
        certificateData = content
        print(certificateData)
        print(type(certificateData['tempID']))
        fun.make_sertifyMe(certificateData['tempID'],certificateData['speaker1'],certificateData['speaker2'],certificateData['fileName'],certificateData['emailCheck'])
        # mai jab bhej rhi
        return certificateData
        
app.run(debug=True)