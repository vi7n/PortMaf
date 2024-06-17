import yfinance as yf
import matplotlib.pyplot as plt
from freeoptionschain import FOC

# Create an instance of FOC
ref_FOC = FOC()

# Fetch current stock price for NVIDIA
stock_price = ref_FOC.get_stock_price("NVDA")

# Fetch options chain for NVIDIA $1200 CALL options expiring on June 7, 2024
options_chain = ref_FOC.get_options_chain("NVDA", "2024-06-07", OptionType.CALL)

# Filter the options chain for the $1200 strike price
call_option = options_chain[options_chain["strike"] == 1200]

# Fetch minute level data for NVIDIA stock for June 7, 2024
nvidia_data = yf.download(
    tickers="NVDA", start="2024-06-07", end="2024-06-08", interval="1m"
)

# Plotting the stock price
plt.figure(figsize=(14, 7))
plt.subplot(2, 1, 1)
plt.plot(nvidia_data.index, nvidia_data["Close"], label="NVIDIA Stock Price")
plt.title("NVIDIA Stock Price and $1200 Call Option Price on June 7, 2024")
plt.ylabel("Stock Price (USD)")
plt.legend()

# Plotting the call option price
plt.subplot(2, 1, 2)
plt.plot(
    call_option.index,
    call_option["lastPrice"],
    label="NVIDIA $1200 Call Option Price",
    color="orange",
)
plt.xlabel("Time")
plt.ylabel("Option Price (USD)")
plt.legend()

plt.tight_layout()
plt.show()
