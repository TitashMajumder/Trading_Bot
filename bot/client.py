import logging
from binance.client import Client
from dotenv import load_dotenv
import time
import os

load_dotenv()
logger = logging.getLogger(__name__)

class BinanceFuturesClient:
     def __init__(self):
          self.client = Client(
               os.getenv("BINANCE_API_KEY"),
               os.getenv("BINANCE_API_SECRET"),
               testnet=True
          )
          self.client.FUTURES_URL = "https://testnet.binancefuture.com"
          server_time = self.client.futures_time()
          self.client.timestamp_offset = server_time["serverTime"] - int(time.time() * 1000)
        
     def create_order(self, **kwargs):
          logger.info(f"Order request: {kwargs}")
          response = self.client.futures_create_order(**kwargs)
          logger.info(f"Order response: {response}")
          return response