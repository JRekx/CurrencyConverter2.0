import requests

# Function to fetch exchange rates from the API
def get_exchange_rates():
    url = 'https://api.exchangerate.host/latest'
    # Send an HTTP GET request to the API
    response = requests.get(url)
    # Parse the JSON response data
    data = response.json()

    # Create a new dictionary to store currency information
    currency_data = {}

    # Add currency symbols and codes to the currency_data dictionary
    for currency, rate in data.get('rates', {}).items():
        # Use get_currency_info() to get currency symbols and codes
        currency_info = get_currency_info(currency)
        currency_data[currency] = {
            'rate': rate,
            'symbol': currency_info['symbol'],
            'code': currency_info['code']
        }

    return currency_data

# Function to get currency symbols and codes based on currency code
def get_currency_info(currency_code):
    # Define a dictionary mapping currency codes to symbols and names
    currency_info = {
        'USD': {'symbol': '$', 'code': 'USD'},
        'EUR': {'symbol': '€', 'code': 'EUR'},
        'JPY': {'symbol': '¥', 'code': 'JPY'},
        'GBP': {'symbol': '£', 'code': 'GBP'},
        'AUD': {'symbol': 'A$', 'code': 'AUD'},
        'CAD': {'symbol': 'C$', 'code': 'CAD'},
        'CHF': {'symbol': 'Fr', 'code': 'CHF'},
        'CNY': {'symbol': '¥', 'code': 'CNY'},
        'SEK': {'symbol': 'kr', 'code': 'SEK'},
        'NZD': {'symbol': 'NZ$', 'code': 'NZD'},
        'KRW': {'symbol': '₩', 'code': 'KRW'},
        'SGD': {'symbol': 'S$', 'code': 'SGD'},
        'HKD': {'symbol': 'HK$', 'code': 'HKD'},
        'NOK': {'symbol': 'kr', 'code': 'NOK'},
        'MXN': {'symbol': 'Mex$', 'code': 'MXN'},
        'INR': {'symbol': '₹', 'code': 'INR'},
        'BRL': {'symbol': 'R$', 'code': 'BRL'},
        'ZAR': {'symbol': 'R', 'code': 'ZAR'},
        'RUB': {'symbol': '₽', 'code': 'RUB'},
        'TRY': {'symbol': '₺', 'code': 'TRY'}
    }
    
    # Return the currency symbol and code for the provided code, or empty values if not found
    return currency_info.get(currency_code, {'symbol': '', 'code': currency_code})

