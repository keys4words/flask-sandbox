from flask import Flask, render_template, request, redirect, url_for
from config import PUBLIC_KEY, API_KEY
import stripe

app = Flask(__name__)

public_key = PUBLIC_KEY
stripe.api_key = API_KEY

@app.route('/')
def index():
    return render_template('index.html', public_key=public_key)


@app.route('/thankyou')
def thankyou():
    return render_template('thankyou.html')


@app.route('/payment', methods=['POST'])
def payment():
    customer = stripe.Customer.create(email=request.form['stripeEmail'],
                                    source=request.form['stripeToken'])

    charge = stripe.Charge.create(customer=customer.id,
                                amount=1999,
                                currency='usd',
                                description='Donation')
    return redirect(url_for('thankyou'))


if __name__ == "__main__":
    app.run(debug=True)
