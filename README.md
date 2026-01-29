## Binance Futures Testnet Trading Bot

### Features
- Market & Limit orders
- BUY / SELL support
- Binance USDT-M Futures Testnet
- CLI-based input
- Structured logging
- Robust validation & error handling

### Setup
1. Create Binance Futures Testnet account
2. Generate API keys
3. Create `.env` file with credentials
4. Install dependencies

```
pip install -r requirements.txt
```

Run Examples

Market Order:
```
python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.001
```
Limit Order:
```
python cli.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.001 --price 50000
Logs
```
Logs are stored in logs/bot.log
---