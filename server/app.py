#!/usr/bin/env python3

from flask import Flask, request, current_app, g, make_response

contracts = [{"id": 1, "contract_information": "This contract is for John and building a shed"},{"id": 2, "contract_information": "This contract is for a deck for a buisiness"},{"id": 3, "contract_information": "This contract is to confirm ownership of this car"}]
customers = ["bob","bill","john","sarah"]
app = Flask(__name__)

# Contract route
@app.route('/contract/<int:id>')
def get_contract(id):
    """
    Route for retrieving contract information by ID
    
    Args:
        id (int): The contract ID from the URL
        
    Returns:
        str: Contract information with status 200 if found
             404 response if contract not found
    """
    # Search for the contract with the given ID
    for contract in contracts:
        if contract["id"] == id:
            # Contract found - return contract_information with 200 status
            return contract["contract_information"], 200
    
    # Contract not found - return 404 status
    return "", 404

# Customer route
@app.route('/customer/<customer_name>')
def check_customer(customer_name):
    """
    Route for checking if a customer exists without returning any data
    
    Args:
        customer_name (str): The customer name from the URL
        
    Returns:
        Response: Empty response with status 204 if customer found
                 404 response if customer not found
    """
    # Check if the customer name exists in the customers list
    if customer_name.lower() in customers:
        # Customer found - return empty response with 204 status
        response = make_response("", 204)
        return response
    
    # Customer not found - return 404 status
    return "", 404

if __name__ == '__main__':
    app.run(port=5555, debug=True)