from dexscreener import DexscreenerClient

client = DexscreenerClient()

pair = client.get_token_pair("ethereum", "0x88e6A0c2dDD26FEEb64F039a2c41296FcB3f5640")
print(pair)
