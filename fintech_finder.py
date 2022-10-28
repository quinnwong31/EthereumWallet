# Cryptocurrency Wallet

################################################################################
# For this Challenge, you will assume the perspective of a Fintech Finder
# customer in order to do the following:

# * Generate a new Ethereum account instance by using your mnemonic seed phrase
# (which you created earlier in the module).

# * Fetch and display the account balance associated with your Ethereum account
# address.

# * Calculate the total value of an Ethereum transaction, including the gas
# estimate, that pays a Fintech Finder candidate for their work.

# * Digitally sign a transaction that pays a Fintech Finder candidate, and send
# this transaction to the Ganache blockchain.

# * Review the transaction hash code associated with the validated blockchain transaction.

# Once you receive the transaction’s hash code, you will navigate to the Transactions
# section of Ganache to review the blockchain transaction details. To confirm that
# you have successfully created the transaction, you will save screenshots to the
# README.md file of your GitHub repository for this Challenge assignment.

################################################################################
# Imports
import streamlit as st
from dataclasses import dataclass
from typing import Any, List
from web3 import Web3
w3 = Web3(Web3.HTTPProvider('HTTP://127.0.0.1:7545'))
from crypto_wallet import generate_account, get_balance, send_transaction


################################################################################
# Fintech Finder Candidate Information

# Database of Fintech Finder candidates including their name, digital address, rating and hourly cost per Ether.
# A single Ether is currently valued at $1,500
candidate_database = {
    "Lane": ["Lane", "0xaC8eB8B2ed5C4a0fC41a84Ee4950F417f67029F0", "4.3", .20, "Images/lane.jpeg"],
    "Ash": ["Ash", "0x2422858F9C4480c2724A309D58Ffd7Ac8bF65396", "5.0", .33, "Images/ash.jpeg"],
    "Jo": ["Jo", "0x8fD00f170FDf3772C5ebdCD90bF257316c69BA45", "4.7", .19, "Images/jo.jpeg"],
    "Kendall": ["Kendall", "0x8fD00f170FDf3772C5ebdCD90bF257316c69BA45", "4.1", .16, "Images/kendall.jpeg"]
}

# A list of the FinTech Finder candidates first names
people = ["Lane", "Ash", "Jo", "Kendall"]

def get_people():
    """Display the database of Fintech Finders candidate information."""
    db_list = list(candidate_database.values())

    for number in range(len(people)):
        st.image(db_list[number][4], width=200)
        st.write("Name: ", db_list[number][0])
        st.write("Ethereum Account Address: ", db_list[number][1])
        st.write("FinTech Finder Rating: ", db_list[number][2])
        st.write("Hourly Rate per Ether: ", db_list[number][3], "eth")
        st.text(" \n")

################################################################################
# Streamlit Code

# Streamlit application headings
st.markdown("# Fintech Finder!")
st.markdown("## Hire A Fintech Professional!")
st.text(" \n")

################################################################################
# Streamlit Sidebar Code - Start

st.sidebar.markdown("## Client Account Address and Ethernet Balance in Ether")

##########################################
# Step 1 - Part 4:
# Create a variable named `account`. Set this variable equal to a call on the
# `generate_account` function. This function will create the Fintech Finder
# customer’s (in this case, your) HD wallet and Ethereum account.

#  Call the `generate_account` function and save it as the variable `account`
account = generate_account()

##########################################

# Write the client's Ethereum account address to the sidebar
st.sidebar.write(account.address)

##########################################
# Step 1 - Part 5:
# Define a new `st.sidebar.write` function that will display the balance of the
# customer’s account. Inside this function, call the `get_balance` function and
#  pass it your Ethereum `account.address`.

# Call `get_balance` function and pass it your account address
balance = get_balance(w3, account.address)
st.sidebar.write(balance)

##########################################

# Create a select box to chose a FinTech Hire candidate
person = st.sidebar.selectbox('Select a Person', people)

# Create a input field to record the number of hours the candidate worked
hours = st.sidebar.number_input("Number of Hours")

st.sidebar.markdown("## Candidate Name, Hourly Rate, and Ethereum Address")

# Identify the FinTech Hire candidate
candidate = candidate_database[person][0]

# Write the Fintech Finder candidate's name to the sidebar
st.sidebar.write(candidate)

# Identify the FinTech Finder candidate's hourly rate
hourly_rate = candidate_database[person][3]

# Write the inTech Finder candidate's hourly rate to the sidebar
st.sidebar.write(hourly_rate)

# Identify the FinTech Finder candidate's Ethereum Address
candidate_address = candidate_database[person][1]

# Write the inTech Finder candidate's Ethereum Address to the sidebar
st.sidebar.write(candidate_address)

# Write the Fintech Finder candidate's name to the sidebar

st.sidebar.markdown("## Total Wage in Ether")

################################################################################
# Step 2: Sign and Execute a Payment Transaction

##########################################
# Step 2 - Part 1:
# * Write the equation that calculates the candidate’s wage. This equation
# should assess the candidate’s hourly rate from the candidate database
# (`candidate_database[person][3]`) and then multiply this hourly rate by
# the value of the `hours` variable. Save this calculation’s output as a
# variable named `wage`.
# * Write the `wage` variable to the Streamlit sidebar by using `st.sidebar.write`.

# Calculate total `wage` for the candidate by multiplying the candidate’s hourly
# rate from the candidate database (`candidate_database[person][3]`) by the
# value of the `hours` variable
wage = candidate_database[person][3] * hours

# Write the `wage` calculation to the Streamlit sidebar
st.sidebar.write(wage)

##########################################
# Step 2 - Part 2:
# * Save the transaction hash that the `send_transaction` function returns as a
# variable named `transaction_hash`, and have it display on the application’s
# web interface.
if st.sidebar.button("Send Transaction"):

    # Call the `send_transaction` function and pass it 3 parameters:
    # Your `account`, the `candidate_address`, and the `wage` as parameters
    # Save the returned transaction hash as a variable named `transaction_hash`
    transaction_hash = send_transaction(w3, account, candidate_address, wage)

    # Markdown for the transaction hash
    st.sidebar.markdown("#### Validated Transaction Hash")

    # Write the returned transaction hash to the screen
    st.sidebar.write(transaction_hash)

    # Celebrate your successful payment
    st.balloons()

# The function that starts the Streamlit application
# Writes FinTech Finder candidates to the Streamlit page
get_people()

