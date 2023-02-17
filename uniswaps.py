from uniswap import Uniswap

address = "0x9aaB929c32B3CCe2ec0FdBbB21DdD070Fb359fb6"          # or None if you're not going to make transactions
private_key = "d2f44d1e20aaa08f84b18cc4f9ec02bf26e29611e2e100130c7e04e249f982b8"  # or None if you're not going to make transactions
version = 2                       # specify which version of Uniswap to use
provider = "https://mainnet.infura.io/v3/01a4dfb5b0b74e93b7524bb07f529db2"    # can also be set through the environment variable `PROVIDER`
uniswap = Uniswap(address=address, private_key=private_key, version=version, provider=provider)

# Some token addresses we'll be using later in this guide
eth = "0x0000000000000000000000000000000000000000"
bat = "0x0D8775F648430679A709E98d2b0Cb6250d2887EF"
dai = "0x6B175474E89094C44Da98b954EedeAC495271d0F"

a = uniswap.get_price_input(eth, dai, 10**18)
print(a)
