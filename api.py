from flask import Flask, redirect, render_template, request, url_for
from datetime import datetime
import pandas as pd
import Property_Estimator


app = Flask(__name__)

entries = []
users = {}

@app.route('/', methods=['GET', 'POST'])

def estimator():

    if request.method == 'GET'
        return render_template('estimator_temp', entries=entries)

    ip_addr = request.environ['REMOTE_ADDR']

    # can these be compress to the same object?
    user_exp = request.form['exp/rent_roll']
    user_units = request.form['units']
    user_sqft = request.form['sqft']
    user_year = request.form['year_built']
    user_zip = request.form['zipper']

    model = Property_Estimator(user_exp,user_units,user_sqft,user_sqft,user_year,user_zip)

    if request.form['email'] != '':
        mail = request.form['email']
        user[ip_addr] = mail
    elif ip_addr in users:
        mail = users[ip_addr]
    else:
        mail = ip_addr







    answers = pd.DataFrame({'cap':[entries[0]],'units':[entries[1]], 'sqft':[entries[2]],'yearbuilt':[entries[3]], 'zipper':[entries[4]]})

    retrun redirect(url_for('estimator'))

if __name__ == '__main__':
    app.run(debug=True, port=4444)
