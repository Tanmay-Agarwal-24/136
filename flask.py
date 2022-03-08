from flask import Flask,jsonify,request
from main import data_list
app=Flask(__name__)
@app.route("/")
def index():
    return jsonify({
       "data":data_list,
       "message":"succes"
         }),200

@app.route("/planet")
def planet():
    name=request.args.get("name")
    planet_data=next(item for item in data_list if item["name"]==name)
    return jsonify({
       "data":data_list,
       "message":"succes"
         }),200

if __name__ =="__main__":
      app.run()