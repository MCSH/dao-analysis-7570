import argparse  # Used to parse cli arguments
import json  # Used to parse json files

import pandas as pd  # Used to capture data frames
from tqdm import tqdm  # Used to draw progress bars

# Monkey patching pandas' json library for faster json parse
pd.io.json._json.loads = lambda s, *a, **kw: json.loads(s)


def concat_mkrs(cdp='cdp.json'):
    # Load the account ids
    df = pd.read_json(cdp)

    dfs = []
    for i in tqdm(df['id'].iloc, total=len(df)):
        # Parse individual transactions
        dfs.append(pd.read_json(f"acts/{i}.json"))

    # Unpack them
    full = []
    for f in dfs:
        for j in f.iloc:
            full.append(j)

    print(len(full), "transactions")

    # Create a Pandas data frame
    full = pd.DataFrame(full)
    print(full.head())

    # Write to CSV
    full.to_csv("full_df.csv")

if __name__ == "__main__":
    # Create an argument parser to call concat_mkrs
    ap = argparse.ArgumentParser()
    ap.add_argument('--cdp', default='cdp.json',
                    help='Location of cdp.json file')

    args = ap.parse_args()
    concat_mkrs(args.cdp)
