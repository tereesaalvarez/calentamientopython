investment_in_bitcoin = 1.2
bitcoin_to_euros = 40000
#1st write a function to calculate bitcoin to euro
def bitcoin_to_euros (bitcoin_amount, bitcoin_value_euros):
    usd_value = investment_in_bitcoin * bitcoin_to_euros
    return usd_value
investment_in_usd = bitcoin_to_euros (investment_in_bitcoin, bitcoin_to_euros)
if investment_in_bitcoin <= 30000:
    print ("Investment below 30,000€! SELL!")
else:
    print ("Investment above 30,000€")