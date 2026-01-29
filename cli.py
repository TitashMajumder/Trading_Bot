import argparse
import logging
from bot.logging_config import setup_logging
from bot.validators import validate_inputs
from bot.orders import OrderService

setup_logging()
logger = logging.getLogger(__name__)

def main():
     parser = argparse.ArgumentParser(description="Binance Futures Trading Bot")
     parser.add_argument("--symbol", required=True)
     parser.add_argument("--side", required=True)
     parser.add_argument("--type", required=True)
     parser.add_argument("--quantity", type=float, required=True)
     parser.add_argument("--price", type=float)

     args = parser.parse_args()

     try:
          validate_inputs(
               args.symbol,
               args.side,
               args.type,
               args.quantity,
               args.price
          )

          service = OrderService()

          if args.type == "MARKET":
               response = service.place_market(
                    args.symbol, args.side, args.quantity
               )
          else:
               response = service.place_limit(
                    args.symbol, args.side, args.quantity, args.price
               )

          print("\n Order Placed Successfully")
          print(f"Order ID: {response.get('orderId')}")
          print(f"Status: {response.get('status')}")
          print(f"Executed Qty: {response.get('executedQty')}")
          print(f"Avg Price: {response.get('avgPrice', 'N/A')}")

     except Exception as e:
          logger.exception("Order failed")
          print(f"\n Order Failed: {e}")

if __name__ == "__main__":
     main()