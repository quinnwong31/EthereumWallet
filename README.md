# Ethereum Wallet

## Description

In this Ethereum Wallet sample application, we take on the perspective of a Fintech Finder
customer in order to do the following:

- Generate a new Ethereum account instance by using a mnemonic seed phrase
  (which you created earlier in the module).

- Fetch and display the account balance associated with an Ethereum account
  address.

- Calculate the total value of an Ethereum transaction, including the gas estimate, that pays a Fintech Finder candidate for their work.

- Digitally sign a transaction that pays a Fintech Finder candidate, and send this transaction to the Ganache blockchain.

## Technologies

This example uses the following technologies:

- **Web3.py** - a Python library that allows us to talk to Ethereum nodes in our favorite language, Python. Web3.py is a software development kit (SDK) like any other SDK you've used to talk to other APIs. But this time, the API originates from an Ethereum node.
- **Ganache** - Ganache is a personal blockchain for rapid Ethereum and Corda distributed application development. You can use Ganache across the entire development cycle; enabling you to develop, deploy, and test your dApps in a safe and deterministic environment.
- **streamlit** - Streamlit is a platform for building rich, interactive web applications in the cloud using Python.

## Installation

The required libraries are stored in `requirements.txt`. To install the required libraries, do the following:

1. Open Terminal
2. Type `pip install -r requirements.txt`

## Usage

### Launching the Fintech Finder application

To launch the Fintech Finder application, do the following:

1. Launch terminal
2. Execute the following command:

```
streamlit run fintech_finder.py
```

### Verifying the Transaction

To verify that the transaction is successful, we can check the Accounts and Transactions tabs in Ganache:

1. **Accounts Tab** - Navigate to the Ganache accounts tab and locate your account (index 0).
   ![Ethereum accounts](/Images/eth_accounts.jpg)

2. **Transactions Tab** - Navigate to the Ganache transactions tab and locate the transaction.
   ![Transaction accounts](/Images/eth_transaction.jpg)

## Contributors

This sample application was authored by:

Quinn Wong (quinn.wong@gmail.com)
LinkedIn: https://www.linkedin.com/in/quinnwong/

## License

The MIT License (MIT)

Copyright (c) 2022 Quinn Wong

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
