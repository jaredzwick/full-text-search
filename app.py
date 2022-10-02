from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

# Initialize app
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Declare model for ORM
class Patent(db.Model):
    patent_id = db.Column(db.Integer, primary_key=True)
    patent_text = db.Column(db.String(4096))


@app.route('/')
def home_page():
    return render_template('index.html')

# Route for home page;
# [results] is a list of all Patent Objects that match the text from the search query
@app.route('/search', methods=['GET', 'POST'])
def search():
    if request.method == 'POST':
        results = Patent.query.filter(Patent.patent_text.like('%'+request.form['srch']+'%')).all()
        return render_template('search_results.html', patent_list=results)
    else:
        return render_template('index.html')

if __name__=='__main__':
    app.run(debug=True)