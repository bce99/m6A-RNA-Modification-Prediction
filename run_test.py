import pandas as pd
import warnings
warnings.filterwarnings("ignore")
import tensorflow as tf

from tensorflow import keras
from keras.models import load_model

from data_parsing.load_and_store_data_info import *
from data_parsing.parse_data import *

from data_preprocessing.preprocess_parsed_data import *

if __name__ == "__main__":
    
    ### Here we use data2 as data to test run on 
    
    # Convert label info and parse compressed data2.json.gz file into .csv files
    load_and_store_data_info()
    output_parsed_data(read_json_gz('dataset2.json.gz')[0], read_json_gz('dataset2.json.gz')[1])
    
    # Preprocess parsed data2 into format compatible with trained model
    test_data2, transcript = data_preprocess('Parsed_Data2.csv')
    
    # # Take the first 500 rows
    # test_data2 = test_data2.iloc[:5000, :]
    
    # Load the model from .h5 file
    model = load_model('model_NN_final.h5')
    
    # Perform prediction 
    test_data2_pred_prob = model.predict(test_data2)
    
    # Merge with transcript id and position columns
    test_data2_pred_p = pd.DataFrame(pd.DataFrame(test_data2_pred_prob))
    test_data2_pred_p.columns = ['score']
    result_data2 = pd.merge(transcript, test_data2_pred_p, left_index=True, right_index=True, how='inner')
    agg_functions = {'score': 'max'}

    result_data2 = result_data2.groupby(['transcript_id', 'position']).agg(agg_functions).reset_index()
    result_data2.rename({'position':'transcript_position'}, inplace=True)
    
    result_data2.to_csv('Test_Data2_Result.csv', index=False)
