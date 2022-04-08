from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
# from the first attempt - I had hardcoded the front end - this time i actually used the correct source codes
# added the full_name field as this was missing previously
    user_info = [
        {'first_name' : 'Michael', 'last_name' : 'Choi', 'full_name' : 'Michael Choi'},
        {'first_name' : 'John', 'last_name' : 'Supsupin', 'full_name' : 'John Supsupin'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen', 'full_name' : 'Mark Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel', 'full_name' : 'KB Tonel'}
    ]

    return render_template("index.html", user = user_info)

if __name__=="__main__":
    app.run(debug=True) #fixed my code to include app.run debug as this was also missing

    #originally had an issue trying to run server after install of flask 2.0.3 -> fixed via -> pipfile -> [package] flask = '==2.0.3' <- removed == to have flask = '2.0.3'  