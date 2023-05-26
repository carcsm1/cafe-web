from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import csv

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)


class CafeForm(FlaskForm):
    cafe = StringField('Cafe name', validators=[DataRequired()])
    submit = SubmitField('Submit')

# Exercise:
# add: Location URL, open time, closing time, coffee rating, wifi rating, power outlet rating fields
# make coffee/wifi/power a select element with choice of 0 to 5.
#e.g. You could use emojis ☕️/💪/✘/🔌
# make all fields required except submit
# use a validator to check that the URL field has a URL entered.
# ---------------------------------------------------------------------------


# all Flask routes below
@app.route("/")
def home():
    return render_template("index.html")


@app.route('/add')
def add_cafe():
    form = CafeForm()
    if form.validate_on_submit():
        print("True")
    # Exercise:
    # Make the form write a new row into cafe-data.csv
    # with   if form.validate_on_submit()
    return render_template('add.html', form=form)


@app.route('/cafes')
def cafes():
    with open('cafe-data.csv', newline='', encoding="utf8") as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        list_of_rows = []
        print(csv_data)
        for row in csv_data:
            print(row)
            list_of_rows.append(row)
    return render_template('cafes.html', cafes=list_of_rows)

@app.route('/added', methods=["POST"])
def added():
    name = request.form["cafename"]
    location = request.form["location"]
    optime = request.form["optime"]
    cltime = request.form["cltime"]
    crating = request.form["crating"]
    wrating = request.form["wrating"]
    srating = request.form["srating"]
    new_row = [name,location,optime,cltime,crating,wrating,srating]
    print(new_row)
    with open('cafe-data.csv', 'a', newline='',encoding="utf8") as order_csv:
        order_csv_append = csv.writer(order_csv)
        order_csv_append.writerow(new_row)

    return render_template("index.html")


if __name__ == '__main__':
    app.run(debug=True)
