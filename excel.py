import pandas as pd
from binances import *

set = []
my_path = 'C:/Users/admin/PycharmProjects/dexcex/tokens.csv'
df = pd.read_csv(my_path)
user_agent = df['baseToken']

info = client.get_all_tickers()

for i in range(len(info)):
    for j in range(len(user_agent)):
        if info[i]['symbol'][-3:] == 'BTC':
            cash = info[i]['symbol'][:-3]
            if cash == user_agent[j]:
                set.append([df['chainId'][j], df['dexId'][j], df['baseToken'][j], df['pairAddress'][j]])
            elif cash == user_agent[j][1:]:
                set.append([df['chainId'][j], df['dexId'][j], df['baseToken'][j], df['pairAddress'][j]])
        elif info[i]['symbol'][-4:] == 'USDT':
            cash = info[i]['symbol'][:-4]
            if cash == user_agent[j]:
                set.append([df['chainId'][j], df['dexId'][j], df['baseToken'][j], df['pairAddress'][j]])
            elif cash == user_agent[j][1:]:
                set.append([df['chainId'][j], df['dexId'][j], df['baseToken'][j], df['pairAddress'][j]])

print(set)
raw_data = pd.DataFrame(set)  #데이터 프레임으로 전환
raw_data.to_csv(path_or_buf='C:/Users/admin/PycharmProjects/dexcex/test1.csv', header=['chainId','dexId','baseToken','pairAddress'], index=False) #엑셀로 저장