from flask import Flask
from flask import jsonify
from flask import render_template
from flask import request
from wtforms import Form, validators, StringField

from com.demo.dao.CustomerDao import CustomerDao
# template folder location should be relevant to current file i.e. CustomersController.py
from com.demo.domain.Customer import Customer

app = Flask(__name__, template_folder='../../../templates');
app.config.from_object(__name__)


class ReusableForm(Form):
    name = StringField('name:', validators=[validators.required()])
    address = StringField('address:', validators=[validators.required()])


@app.route("/")
def home():
    form = ReusableForm(request.form)
    return render_template("customers.html", form=form);


@app.route("/customers/json")
def get_customers_json():
    customer_dao = CustomerDao();
    return jsonify(customer_dao.getCustomers());


@app.route("/customers")
def get_all_customers():
    form = ReusableForm(request.form)
    return render_template("customers.html", form=form);


@app.route("/save", methods=['POST'])
def save_customer():
    if request.method == 'POST':
        name = request.form['name'];
        address = request.form['address'];
        if name == '' or address == '':
            return "Customer data not saved. Name or Address is empty."
        customer = Customer(name, address);
        customer_dao = CustomerDao();
        customer_dao.insertRecord(customer);
    # Return all customers form
    form = ReusableForm(request.form)
    return render_template("customers.html", form=form);


@app.route("/create")
def get_save_customer_page():
    form = ReusableForm(request.form)
    return render_template("createcustomer.html", form=form);


if __name__ == '__main__':
    app.run(debug=True);
