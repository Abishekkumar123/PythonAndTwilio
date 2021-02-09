# ------------------------------------------------------------------------------
# Imports
import os
from twilio.rest import Client
# ------------------------------------------------------------------------------
# Configurations
account_sid = "AC1280e8d1a7c5e706f1f6535fc9ce1fc1"
auth_token = "fe97df05dc68433609bed34209991946"

# ------------------------------------------------------------------------------
# Setting the client with the configurations
client = Client(account_sid, auth_token)

# ------------------------------------------------------------------------------
# Creating the message
client.messages.create(
    to="+919861721472",
    from_="+17014017340",
    body="669575 is your SECRET one time password (OTP) for payment of Rs. 990.00 via GOOGLEPLAYMASTERM via Netbanking. Do not share it with anyone."
)
# ------------------------------------------------------------------------------
