# Moving Average Crossover Trading Strategy

This project implements a Moving Average Crossover Trading Strategy using Python. It uses historical stock data from Yahoo Finance to generate trading signals based on short-term and long-term moving averages.

## How to Run

### Prerequisites
Make sure you have Python 3.x installed along with the following libraries:
- `pandas`
- `numpy`
- `yfinance`
- `matplotlib`

You can install the required libraries using:
```bash
pip install pandas numpy yfinance matplotlib
```

### Steps to Run the Code

1. **Clone the repository**:
   ```bash
   git clone https://github.com/enesercanh/firstquantp.git
   cd firstquantp
   ```

2. **Run the script**:
   ```bash
   python backtester.py
   ```

The script will download stock data for AAPL from Yahoo Finance, generate trading signals based on moving averages, backtest the strategy, display performance metrics, and visualize the results.

---

## Customization

You can customize various parameters in the `main` function:

- **Ticker Symbol**: Change the `ticker` variable to fetch data for a different stock.
  ```python
  ticker = 'GOOGL'  # Example for Google stock
  ```

- **Date Range**: Modify the `start_date` and `end_date` to adjust the time period.
  ```python
  start_date = '2021-01-01'
  end_date = '2023-01-01'
  ```

- **Moving Averages**: Adjust the `short_window` and `long_window` to test different moving average periods.
  ```python
  short_window = 20
  long_window = 50
  ```

---

## Project Structure

```
|-- backtester.py    # Main script with the trading strategy code
|-- README.md                      # This file
```

---

## Explanation of the Code
- **fetch_data**: Downloads stock data.
- **moving_average_crossover_strategy**: Generates buy/sell signals based on moving averages.
- **backtest_strategy**: Simulates a trading portfolio.
- **calculate_metrics**: Computes performance metrics.
- **plot_results**: Visualizes stock prices, signals, and portfolio value.

---

## Additional Information
- Default parameters use Apple (AAPL) stock data from 2020 to 2023 with 40-day and 100-day moving averages.
- Ensure a stable internet connection to download stock data from Yahoo Finance.
- Modify the initial capital, number of shares per trade, or other variables for more customized backtesting.

Feel free to modify, improve, or extend this strategy. Contributions are welcome!

