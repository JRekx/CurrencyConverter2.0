from flask import Flask, render_template, request
import requests
from helpers import get_exchange_rates, get_currency_info

app = Flask(__name__)

# Route for the homepage
@app.route('/', methods=['GET', 'POST'])
def index():
    # Get the latest exchange rates using the get_exchange_rates() function
    exchange_rates = get_exchange_rates()
    error_message = None  # Initialize the error message variable
    result = ""  # Initialize the result variable

    if request.method == 'POST':
        # Extract form data when a POST request is made
        amount = request.form.get('amount')
        from_currency = request.form.get('from_currency')
        to_currency = request.form.get('to_currency')

        # Check if the provided currency codes are valid
        if from_currency in exchange_rates and to_currency in exchange_rates:
            try:
                amount = float(amount)
                # Perform currency conversion
                converted_amount = amount * exchange_rates[to_currency]['rate'] / exchange_rates[from_currency]['rate']
                result = f"{amount:.2f} {exchange_rates[from_currency]['symbol']} is equal to {converted_amount:.2f} {exchange_rates[to_currency]['symbol']}"
            except ValueError:
                error_message = "Invalid amount. Please enter a valid number."
        else:
            error_message = "Invalid currency codes. Please enter valid currency codes."

    # Render the HTML template with exchange rate data, result, and error message
    return render_template('index.html', result=result, exchange_rates=exchange_rates, error_message=error_message)

if __name__ == '__main__':
    app.run(debug=True)
