from flask import Flask, render_template, Blueprint
from flask_restful import Resource, Api

app = Flask(__name__)

api_user = Blueprint('api', __name__)
api = Api(api_user)


@app.route("/")
def main():
    return render_template('index.html')

@app.route('/testdb')
def testdb():
  if db.session.query("1").from_statement("SELECT 1").all():
    return 'It works.'
  else:
    return 'Something is broken.'
    

@app.context_processor
def passer_aux_templates():
    def formater_distance(dist):
        unite = 'm'
        if dist > 1000:
            dist /= 1000.0
            unite = 'km'
        return u'{0:.2f}{1}'.format(dist, unite)
    return dict(format_dist=formater_distance)


class UserApi(Resource):
    def get(self,id):
    	#abort(404, message="user {} doesn't exist".format(id))
    	return {'status': 'successs'}

    def put(self,id):
    	pass
    
    def delete(self,id):
     	pass



api.add_resource(UserApi, '/users/<int:id>',endpoint='user')

app.register_blueprint(api_user)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80,debug=True)

