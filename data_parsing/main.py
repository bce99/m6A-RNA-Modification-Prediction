import pandas as pd
import gzip
import json

from load_and_store_data_info import *
from parse_data import *

if __name__ == "__main__":
    load_and_store_data_info()
    run_parse_data()