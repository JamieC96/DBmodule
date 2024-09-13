from flask import Flask, request, redirect, url_for, render_template
from flask_sqlalchemy import SQLAlchemy

app= Flask(__name__, template_folder='templates')

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://axolotl_user:lNgpMsc7CQBobUvPv5LOJVd2FOB6uBd6@dpg-cri5gnbv2p9s73bkphtg-a/axolotl'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Survey(db.Model):
    __tablename__ = 'survey'
    id = db.Column(db.Integer, primary_key=True)
    owns = db.Column(db.Boolean, nullable=False)
    age = db.Column(db.Integer, nullable=True)
    gender = db.Column(db.String(10), nullable=True)
    name = db.Column(db.String(80), nullable=True)


@app.route("/")

@app.route("/index")
def index():
    return render_template("index.html")

@app.route("/basicinfo")
def basicinfo():
    return render_template("html/basicinfo.html")

@app.route("/keepingaxolotls")
def keepingaxolotls():
    return render_template("html/keepingaxolotls.html")

@app.route("/inthewild")
def inthewild():
    return render_template("html/inthewild.html")

@app.route("/gallery")
def gallery():
    return render_template("html/gallery.html")

@app.route("/survey")
def survey():
    return render_template("html/survey.html")

@app.route("/contact")
def contact():
    return render_template("html/contact.html")

@app.route('/submit', methods=['POST'])
def submit():
    try:
    
        owns = request.form.get('owns_axolotl') == 'on'  
        age = request.form.get('age', type=int)  
        gender = request.form.get('gender')  
        name = request.form.get('name')  
        
        new_survey = Survey(
            owns=owns,
            age=age,
            gender=gender,
            name=name
        )
        
        db.session.add(new_survey)
        db.session.commit()
        
        return redirect(url_for('survey'))

    except Exception as e:
        print(f"An error occurred: {e}")
        return "An error occurred while processing your request.", 500
if __name__ == "__main__":
    app.run(debug=False)