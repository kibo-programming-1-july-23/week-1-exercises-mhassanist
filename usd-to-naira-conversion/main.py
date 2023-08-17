# Write your solution below

# Use this exchange rate
NAIRA_PER_DOLLAR = 424.55  # Central bank exchange rate

usd_value = float(input("Enter USD Value: "))

ngn_value = usd_value * NAIRA_PER_DOLLAR

print(f"{usd_value:.2f} USD is {ngn_value:.2f} NGN")
