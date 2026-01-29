## Binance Futures Testnet Trading Bot
A CLI-based Python trading bot for Binance USDT-M Futures Testnet supporting Market and Limit orders with proper validation, structured logging, and error handling.

### What is CLI?
A CLI is a command-line interface that allows users to interact with an application using textual commands. In my project, the CLI parses user input and delegates execution to the core business logic.

### Features
- Market & Limit order placement
- BUY / SELL support
- Binance USDT-M Futures Testnet integration
- CLI-based input using argparse
- Structured logging of requests, responses, and errors
- Robust validation and exception handling
- Logs stored in logs/bot.log

### Setup
1. Create Binance Futures Testnet account
```
https://testnet.binancefuture.com
```
2. Generate Futures Testnet API keys (enable Futures permission)
3. Create a .env file in the project root:
```
BINANCE_API_KEY=your_api_key
BINANCE_API_SECRET=your_api_secret
```
4. Install dependencies
```
pip install -r requirements.txt
```

### Run Examples
#### Market Order:
```
python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.003
```
#### Limit Order:
```
python cli.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.003 --price 90000
```
Note: Binance Futures enforces minimum notional value and price band rules. Quantities and prices should comply with exchange constraints.

### Logs
All API requests, responses, and errors are logged to:
```
logs/bot.log
```
The log file includes entries for:
- One Market order
- One Limit order
