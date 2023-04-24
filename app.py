from flask import Flask,render_template,request,send_file
import pickle
import numpy as np
import xgboost

model=pickle.load(open('xgb_classifier_final.pkl','rb'))
app=Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict_placement():
    cgpa=float(request.form.get('cgpa'))
    age=int(request.form.get('age'))
    internships=int(request.form.get('internships'))
    stream=int(request.form.get('stream'))
    backs=int(request.form.get('backs'))
    

    result=model.predict(np.array([age,internships,cgpa,backs,stream]).reshape(1,5))

    if result[0]==1:
        filename='placed.jpg'
    else:
        filename='not_placed.jpg'

    return send_file(filename,mimetype='image/gif')


if __name__=='__main__':
    app.run(debug=False,host='0.0.0.0')