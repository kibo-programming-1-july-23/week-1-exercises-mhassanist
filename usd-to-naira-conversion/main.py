# Write your solution below

# Use this exchange rate
NAIRA_PER_DOLLAR = 424.55  # Central bank exchange rate


# enter value in usd
usd = float(input("Enter value in USD: "))
# convert to naira
naira = usd * NAIRA_PER_DOLLAR
# print result
print("{:.2f}".format(usd) + " USD is " + "{:.2f}".format(naira) + " NGN")
