import pandas as pd
import numpy as np
import yfinance as yf
import matplotlib.pyplot as plt

def fetch_data(ticker, start_date, end_date):
    data = yf.download(ticker, start=start_date, end=end_date)
    return data['Close'] 

def moving_average_crossover_strategy(prices, short_window, long_window):
    signals = pd.DataFrame(index=prices.index)
    signals['price'] = prices
    signals['short_mavg'] = prices.rolling(window=short_window, min_periods=1).mean()
    signals['long_mavg'] = prices.rolling(window=long_window, min_periods=1).mean()
    signals['signal'] = 0.0
    signals['signal'][short_window:] = np.where(
        signals['short_mavg'][short_window:] > signals['long_mavg'][short_window:], 1.0, 0.0
    )
    signals['positions'] = signals['signal'].diff()
    return signals

def backtest_strategy(signals):
    initial_capital = 10000.0
    positions = pd.DataFrame(index=signals.index).fillna(0.0)
    positions['stock'] = 100 * signals['signal']  # Assume 100 shares per trade
    portfolio = positions.multiply(signals['price'], axis=0)
    pos_diff = positions.diff()
    portfolio['holdings'] = (positions.multiply(signals['price'], axis=0)).sum(axis=1)
    portfolio['cash'] = initial_capital - (pos_diff.multiply(signals['price'], axis=0)).sum(axis=1).cumsum()
    portfolio['total'] = portfolio['cash'] + portfolio['holdings']
    portfolio['returns'] = portfolio['total'].pct_change()
    return portfolio

def calculate_metrics(portfolio):
    cumulative_returns = (portfolio['total'][-1] - portfolio['total'][0]) / portfolio['total'][0]
    sharpe_ratio = np.sqrt(252) * (portfolio['returns'].mean() / portfolio['returns'].std())
    max_drawdown = (portfolio['total'].cummax() - portfolio['total']).max()
    return cumulative_returns, sharpe_ratio, max_drawdown

def plot_results(signals, portfolio):
    plt.figure(figsize=(14, 7))
    plt.plot(signals['price'], label='Price')
    plt.plot(signals['short_mavg'], label='Short Moving Average')
    plt.plot(signals['long_mavg'], label='Long Moving Average')
    plt.plot(signals.loc[signals.positions == 1.0].index, 
             signals.short_mavg[signals.positions == 1.0], '^', markersize=10, color='g', lw=0, label='Buy Signal')
    plt.plot(signals.loc[signals.positions == -1.0].index, 
             signals.short_mavg[signals.positions == -1.0], 'v', markersize=10, color='r', lw=0, label='Sell Signal')
    plt.title('Moving Average Crossover Strategy')
    plt.legend()
    plt.show()

    plt.figure(figsize=(14, 7))
    plt.plot(portfolio['total'], label='Portfolio Value')
    plt.title('Portfolio Performance')
    plt.legend()
    plt.show()

def main():
    # Parameters
    ticker = 'AAPL'
    start_date = '2020-01-01'
    end_date = '2023-01-01'
    short_window = 40
    long_window = 100

    # Fetch data
    prices = fetch_data(ticker, start_date, end_date)

    # Generate trading signals
    signals = moving_average_crossover_strategy(prices, short_window, long_window)

    # Backtest the strategy
    portfolio = backtest_strategy(signals)

    # Calculate performance metrics
    cumulative_returns, sharpe_ratio, max_drawdown = calculate_metrics(portfolio)
    print(f"Cumulative Returns: {cumulative_returns:.2%}")
    print(f"Sharpe Ratio: {sharpe_ratio:.2f}")
    print(f"Max Drawdown: {max_drawdown:.2f}")

    # Visualize results
    plot_results(signals, portfolio)

if __name__ == "__main__":
    main()