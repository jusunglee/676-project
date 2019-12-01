# credits from https://stackabuse.com/deploying-a-flask-application-to-heroku/
from flask import Flask, request, jsonify, render_template
app = Flask(__name__)
from logistic_regression import MBTILogisticRegressionWithBagOfWords

BOW_LR_MODEL = MBTILogisticRegressionWithBagOfWords()

@app.route('/', methods=['GET'])
def respond():
    return render_template('index.html')

@app.route('/predict/', methods=['POST'])
def post_something():
    param = request.form.get('corpus')
    print(param)
    # You can add the test cases you made in the previous function, but in our case here you are just testing the POST functionality
    if param:
        mbti_type, prob = BOW_LR_MODEL.classify(param)
        return jsonify({
            "prediction": mbti_type,
            "confidence": prob,
        })
    else:
        return jsonify({
            "ERROR": "no name found, please send a name."
        })

if __name__ == '__main__':
    # Threaded option to enable multiple instances for multiple user access support
    app.run(port=5000, debug=True)