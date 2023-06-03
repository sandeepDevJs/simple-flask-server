from flask import Flask, redirect, url_for, render_template, request

app=Flask(__name__)

@app.route('/')
def welcome():
    return render_template("index.html");
    

@app.route('/success/<int:score>')
def success(score):
    return render_template("result.html", score=score)

@app.route('/fail/<int:score>')
def fail(score):
    return render_template("result.html", score=score)

@app.route('/result/<int:marks>')
def resultpage(marks):
    result =""
    if marks > 35:
        result = "success"
    else:
        result = "fail"
    return redirect(url_for(result, score=marks))


@app.route('/submit', methods=["GET", "POST"])
def submit():
    if request.method == "POST":
        fname = request.form['fname']
        lname = request.form['lname']
        marks = int(request.form['marks'])

        print(fname, lname)

        return redirect(url_for("resultpage", marks=marks))
        
    return


if __name__=='__main__':
    app.run(debug=True)