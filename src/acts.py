import argparse  # Used to parse cli arguments
import json  # Used to load and write json files
from multiprocessing import Pool  # Used to run code in parallel
from os import path  # Used to skip existing files
import time  # Used to put process to sleep

import requests  # Used to fetch data
from tqdm import tqdm  # Used to capture progressbar

def get_acts(i):
    '''
    Helper function used in get_all_acts

    Gathers acts of an account and stores them on disk.
    '''
    pname = f'acts/{i["id"]}.json'
    if path.exists(pname):
        # Data already downloaded, skip
        return True
    try:
        acts = requests.get(f'https://mkr.tools/api/v1/cdp/{i["id"]}/actions').json()
    except Exception:
        print("Unable to fetch", i["id"])
        return False
    time.sleep(0.02) # So we don't reach limits

    with open(pname, 'w') as f:
        # Write to file
        json.dump(acts, f)
    return True

def get_all_acts(cdp='cdp.json'):
    '''
    Function to store actions of all accounts mentioned in cdp to disk.
    
    Caution: This method uses parallelization, set the number of threads if necessary
    '''
    # Load account ids
    with open(cdp) as f:
        d = json.load(f)
        print("Loading", len(d))

    # Run 6 processes in parallel
    with Pool(6) as p:
        # pass each account to get_acts
        list(tqdm(p.imap(get_acts, d), total=len(d)))


if __name__ == "__main__":
    # Create an argument parser to call get_acts
    ap = argparse.ArgumentParser()
    ap.add_argument('--cdp', default='cdp.json',
                    help='Location of cdp.json file')

    args = ap.parse_args()
    get_all_acts(args.cdp)
