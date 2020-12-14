import argparse  # Used to parse cli arguments
import pandas as pd  # Used to handle data frames
import matplotlib.pyplot as plt  # Used to plot


def vis(df_file):
    df = pd.read_csv(df_file)

    # Cleanup column name and timestamps
    df['ind'] = df['Unnamed: 0']
    df = df.drop(columns=['Unnamed: 0'])
    df = df.set_index('ind')
    df.time = pd.to_datetime(df.time)
    df.timestamp = pd.to_datetime(df.timestamp)
    df = df.sort_values('timestamp')
    df = df.set_index('timestamp')

    print(df.head())

    print("Acts:", df.act.unique())

    # Visualize action counts

    df[['act', 'idx']].groupby('act').count().plot(kind='bar')
    plt.show()

    # Visualize usage over time
    
    a = df[['time']].groupby([df['time'].dt.date]).count().plot()
    a.set_xticklabels([""])

    plt.show()

    # Visualize action usage over time

    i = 0
    fig, axes = plt.subplots(2, 4)
    fig.set_figheight(7)
    fig.set_figwidth(15)
    for act in df.act.unique():
        tdf = df[df.act==act]
        a = axes[i%2][i//2]
        tdf[['time']].groupby([tdf['time'].dt.date]).count().plot(ax=a)
        a.title.set_text(act)
        a.set_xticklabels([""])
        i += 1

    plt.show()

    # Cummulative total collateral over time

    ax = df.ink.cumsum().plot()
    ax.title.set_text("Total Locked Collateral Over Time")

    plt.show()

    # Cummulative total debt over time

    ax = df.ire.cumsum().plot()
    ax.title.set_text("Total Outstanding Debt Over Time")
    plt.show()

    # Ratio over time
    
    ratio = (df.ink.cumsum() / df.ire.cumsum())
    print(ratio)
    ratio.plot()
    plt.show()

    print("Cups:", df.lad.nunique())
    print("Transactions:", len(df))
    print("Blocks:", df.block.nunique())


if __name__ == "__main__":
    # Create an argument parser to call vis
    ap = argparse.ArgumentParser()
    ap.add_argument('--df', default='full_df.csv',
                    help='Location of full_df.csv file')

    args = ap.parse_args()
    vis(args.df)
