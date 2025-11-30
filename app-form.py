from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from flask import Flask, render_template

class MyForm(FlaskForm):
    name = StringField("你的名字", validators=[DataRequired()])
    submit = SubmitField("送出")

app = Flask(__name__)
app.config["SECRET_KEY"] = "geo"

@app.route("/", methods=["GET", "POST"])
def index():
    form = MyForm()
    if form.validate_on_submit():
        return f"Hello, {form.name.data}!"
    return render_template("form.html", form=form)

if __name__ == "__main__":
    app.run(debug=True)