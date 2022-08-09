import logging
import hero.sale_auctions as hero_sales
import auction_core as auction_core
import sys
import time
from web3 import Web3

log_format = '%(asctime)s|%(name)s|%(levelname)s: %(message)s'

logger = logging.getLogger("DFK-auctions")
logger.setLevel(logging.DEBUG)
logging.basicConfig(level=logging.INFO, format=log_format, stream=sys.stdout)

user = '0x022a09f4cB866d4d70853C9f8D50Ce33f1Fa0db7'
rpc_address = 'https://api.harmony.one'
auction_address = '0x13a65B9F8039E2c032Bc022171Dc05B30c3f2892'
duration = 60
winner = '0x0000000000000000000000000000000000000000'
private_key = '04eb989e6a6a6da5ae1ddff81a0688b8ec161446c1f18f3165a4f20a3688c9b6'
gas_price_gwei = 300
tx_timeout_seconds = 60
w3 = Web3(Web3.HTTPProvider(rpc_address))
nonce = 0

if __name__ == "__main__":
    for i in auction_core.get_user_auctions(auction_address, user, rpc_address):
        price = hero_sales.get_auction(auction_address, i, rpc_address)
        price = price - price*0.01
        price = price / 1000000000000000000
        price = round(price, 2)
        price = price * 1000000000000000000
        pr = str(int(price))
        price = int(pr)
        auction_core.cancel_auction(auction_address, i, private_key , nonce , gas_price_gwei, tx_timeout_seconds, rpc_address, logger)
        auction_core.create_auction(auction_address, i, price, price, duration, winner, private_key, nonce, gas_price_gwei, tx_timeout_seconds, rpc_address, logger)