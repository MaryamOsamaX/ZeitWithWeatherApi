from flask import Flask , render_template ,url_for ,request
import requests
import json
app = Flask(__name__ ,  template_folder='templates')

@app.route("/",methods = ['POST', 'GET'])
def home():

    if request.method == 'POST':
        result = request.form
        url='http://api.openweathermap.org/data/2.5/weather?APPID=9c81052dfd3e0256818521f463e98e86&q='+result['Numbers']+'&units=metric'
        print(result['Numbers'])
        data = requests.get(url)
        jdata = data.json()
        print(jdata)
        print(jdata['main']['temp'])
        return render_template('home.html',result = jdata['main']['temp'])
    return render_template('home.html')
if __name__ =='__main__':
    app.run(debug=True)
