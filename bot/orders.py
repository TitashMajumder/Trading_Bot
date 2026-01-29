from .client import BinanceFuturesClient

class OrderService:
     def __init__(self):
          self.client = BinanceFuturesClient()

     def place_market(self, symbol, side, quantity):
          return self.client.create_order(
               symbol=symbol,
               side=side,
               type="MARKET",
               quantity=quantity
          )

     def place_limit(self, symbol, side, quantity, price):
          return self.client.create_order(
               symbol=symbol,
               side=side,
               type="LIMIT",
               quantity=quantity,
               price=price,
               timeInForce="GTC"
          )