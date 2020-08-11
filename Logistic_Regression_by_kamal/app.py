from flask import Flask , request , app , Response
from flask_cors import CORS
from Logistic_Deploy import predObj
from wsgiref import simple_server


app = Flask(__name__)
CORS(app)
app.config[ 'DEBUG' ] = True

class ClientApi:
    def __init__(self):
        self.predObj = predObj()

@app.route('/predict', methods=['POST'])
def predRoute():
    try:
        if request.json['data'] is not None:
            data = request.json['data']
            print('data is {}'.format(data))
            pred = predObj()
            res = pred.pred_log(data)
            print(res)
            return Response(res)
    except ValueError:
        return Response('value not found')

    except Exception as e:
        print('Exception is' , e)
        return Response(e)


# port = int(os.getenv("PORT"))

if __name__ == "__main__":
    print('app is running')
    clientapp = ClientApi()
    host = '0.0.0.0'
    port = 5000
    app.run(debug=True)
    httpd = simple_server.make_server(host, port, app)
    print("Serving on %s %d" % (host, port))
    httpd.serve_forever()

