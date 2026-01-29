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

```bash
pip install -r requirements.txt

Run Examples

Market Order:

python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.001

Limit Order:

python cli.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.001 --price 50000
Logs

Logs are stored in logs/bot.log



---


# 📊 What Interviewers Will Like About This


✅ Clean separation of concerns  
✅ Production-style logging  
✅ Defensive validation  
✅ CLI UX  
✅ Easily extensible (Stop-Limit / TWAP can be added in 1 file)


---


## 🚀 Want a QUICK Bonus?
I can add **Stop-Limit** or **TWAP** in **10 minutes flat** to push you into the *top tier*.


Just say:
> “Add Stop-Limit”  
or  
> “Add TWAP”


You’re very well positioned with this one 👌
::contentReference[oaicite:0]{index=0}