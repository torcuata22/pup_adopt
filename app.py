from myproject import app 
from flask import render_template

@app.route('/')
def index():
    return render_template('home.html')

if __name__ == '__main__':
    app.run(debug=True)


#set up database (in terminal, type):
#flask db init
#flask db migrate -m "message here"
#flask db upgrade (makes the migrations)
#To run the application: python app.py