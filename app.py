from flask import Flask , render_template , request
import datetime
import os
from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv()

def create_app():
    app = Flask(__name__)
    client = MongoClient(os.getenv("MONGODB_URI"))
    app.db = client.microblog
    
    @app.route("/" , methods=["GET" , "POST"])
    def home():
        if request.method == "POST": 
            entry_content = request.form.get("content")
            formatted_date  =  datetime.date.today().strftime("%Y-%m-%d")
            app.db.entries.insert_one({"content" : entry_content , "date" : formatted_date})
        
        all_entries = app.db.entries.find({})
        entries_with_date =[
            (entry["content"] , 
            entry["date"] , 
            datetime.datetime.strptime(entry["date"], "%Y-%m-%d").strftime("%b %d") ) for entry in all_entries
        ]
        return render_template("home.html" , entries = entries_with_date)
    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
