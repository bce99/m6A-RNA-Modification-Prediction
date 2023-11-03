import pandas as pd
import gzip
import json

from load_and_store_data_info import *
from parse_data import *

# To execute the loading and parsing script
# open your terminal and navigate to the current directory
# run 'python main.py'

if __name__ == "__main__":
    load_and_store_data_info()
    run_parse_data()