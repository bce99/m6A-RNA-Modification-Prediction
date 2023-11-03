import pandas as pd

def load_and_store_data_info():
    # Load the data
    data_info = pd.read_csv('data.info', header=None, names=['gene_id', 'transcript_id', 'transcript_position', 'label'])
    
     # Store data_info file so that dont need to process 
    data_info.to_csv('DSA4266Processed_m6alabel_datainfo.csv', index=False)