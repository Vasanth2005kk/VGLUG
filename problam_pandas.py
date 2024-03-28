import pandas as pd

output=pd.read_csv('datas.csv')

col_strat=0
col_end=5

row_start=0
row_end=10
for _ in range((len(output.axes[0])+1)//10):
    for _ in range((len(output.columns))//5):
        df=pd.DataFrame(output.iloc[row_start:row_end,col_strat:col_end])
        print(df.to_string())

        col_strat+=5
        col_end+=5

    col_strat=0
    col_end=5

    row_start+=10
    row_end+=10

    print('<=============================================>\n<=============================================>')