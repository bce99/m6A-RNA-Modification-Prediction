import pandas as pd

from data_preprocessing import *

test_data1 = data_preprocess('../data_parsing/Parsed_Data2.csv')

test_data1.to_csv('data_parsing/test_preprocessed_data2.csv', index=False)