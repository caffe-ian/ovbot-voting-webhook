from flask import Flask, abort, request
import motor.motor_asyncio
import time
import os

app = Flask(__name__) 

db_url = ""

@app.route("/upvote/***", methods = ["POST"])
async def upvote():
    cluster = motor.motor_asyncio.AsyncIOMotorClient(db_url)
    db = cluster['maindb']
    cll = db['userdata']  
    try:
        auth = request.headers["Authorization"]
        if auth == "***":
            content = request.get_json(force=True)
            userid = content['id']
            await cll.update_one({"id": int(userid)}, {"$set": {"dbl": 1}})
            await cll.update_one({"id": int(userid)}, {"$set": {"timer.dbl": round(time.time())+43200}})
        elif auth == "***":
            content = request.get_json(force=True)
            userid = content['user']
            await cll.update_one({"id": int(userid)}, {"$set": {"topgg": 1}})
            await cll.update_one({"id": int(userid)}, {"$set": {"timer.topgg": round(time.time())+43200}})
        elif auth == "***":
            content = request.get_json(force=True)
            userid = content['user']
            await cll.update_one({"id": int(userid)}, {"$set": {"timer.topggserver": round(time.time())+43200}})
        else:
            abort(403)
    except KeyError:
        abort(403)
    return 'processed'
  
if __name__ == "__main__":
    print("Connected to server")
    app.run(host="0.0.0.0", port=os.getenv("PORT"), debug=True)
