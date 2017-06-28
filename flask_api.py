from flask import Flask, redirect, render_template, request, url_for
from datetime import datetime
import pandas as pd
import Property_Estimator as prop_e


app = Flask(__name__)


users = {}

@app.route('/', methods=['GET', 'POST'])


def estimator():

    if request.method == 'GET':
        return render_template('property_val_estimator.html')

    ip_addr = request.environ['REMOTE_ADDR']

    if request.form['email'] != '':
        mail = request.form['email']
        user[ip_addr] = mail
    elif ip_addr in users:
        mail = users[ip_addr]
    else:
        mail = ip_addr

    # can these be compress to the same object?
    user_exp = request.form['exp/rent_roll']
    user_units = request.form['units']
    user_sqft = request.form['sqft']
    user_year = request.form['year_built']
    user_zip = request.form['zipper']

    mf = prop_e.clean_data()
    model = prop_e.regression(mf,user_exp,user_units,user_sqft,user_sqft,user_year,user_zip)



    return redirect(url_for('estimator'))

if __name__ == '__main__':
    app.run(debug=True, port=4444)
