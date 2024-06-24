import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# 1
df = pd.read_csv('medical_examination.csv')

# 2
df['overweight'] = (df['weight'] / (df['height'] / 100) ** 2 > 25) * 1

# 3
df[['cholesterol', 'gluc']] = (df[['cholesterol', 'gluc']] > 1) * 1

# 4
def draw_cat_plot():
    # 5
    df_cat = pd.melt(df,id_vars='cardio',value_vars=['active','alco','cholesterol','gluc','overweight','smoke'] )

    # 6
    

    # 7


    # 8
    fig = sns.catplot(df_cat, kind='count', x='variable',hue='value', col='cardio')
    fig.set(ylabel='total')
    
    fig = fig.figure


    # 9
    fig.savefig('catplot.png')
    return fig


# 10
def draw_heat_map():
    # 11
    df_heat = df.loc[(df['ap_lo'] <= df['ap_hi']) & (df['height'] >= df['height'].quantile(0.025)) 
                & (df['height'] <= df['height'].quantile(0.975)) & (df['weight'] >= df['weight'].quantile(0.025)) 
                & (df['weight'] <= df['weight'].quantile(0.975))]
    
    # print(df_heat.head())

    # 12
    corr = df_heat.corr()

    # 13
    mask = np.triu(corr)



    # 14
    fig, ax = plt.subplots(figsize=(9,9))

    # 15

    sns.heatmap(corr, mask=mask, vmin=-0.14, vmax=0.3, annot=True, fmt=".1f", square=True, cbar_kws = {'orientation' : 'vertical'})
    # 16
    fig.savefig('heatmap.png')
    return fig

