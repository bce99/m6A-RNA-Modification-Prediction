import pandas as pd

##########
#    Script for preprocessing data into specific format with feature engineering
# 
# 1. Directly apply this script onto csv file output from running /data_parsing/main.py
# 2. Dataframe is now compatible with trained model stored in .h5 file
# 3. Predict the outcome directly
##########



# Function to extract the specific sequence
def extract_specific_sequence(row):
    sequence_columns = [col for col in row.index if col.startswith('sequence_') and row[col] == 1]
    if sequence_columns:
        return sequence_columns[0].split('sequence_')[1]
    else:
        return None
    
def get_position_1to5(df):
    df['specific_sequence'] = df.apply(extract_specific_sequence, axis=1)
    
    df['1st_pos'] = df['specific_sequence'].apply(lambda x: x[0])
    df['2nd_pos'] = df['specific_sequence'].apply(lambda x: x[1])
    df['3rd_pos'] = df['specific_sequence'].apply(lambda x: x[2])
    df['4th_pos'] = df['specific_sequence'].apply(lambda x: x[3])
    df['5th_pos'] = df['specific_sequence'].apply(lambda x: x[4])
    
    return df

def categorise_positions(df):
    df['1st_pos'] = df['1st_pos'].astype('category')
    df['2nd_pos'] = df['2nd_pos'].astype('category')
    df['3rd_pos'] = df['3rd_pos'].astype('category')
    df['4th_pos'] = df['4th_pos'].astype('category')
    df['5th_pos'] = df['5th_pos'].astype('category')
    
    return df

# Define a function for standardization
def standardize_column_mean(column):
    return (column - column.mean()) / column.std()

def standardize_column_sd(column):
    return column / column.std()

def standardize_0data(df):
    grouped_data1 = df.groupby("transcript_id")

    # Apply the standardization function to the "0 mean" column within each group
    df["0 mean standardized"] = grouped_data1["0 mean"].transform(standardize_column_mean)
    df["0 sd standardized"] = grouped_data1["0 sd"].transform(standardize_column_sd)
    df["0 length standardized"] = grouped_data1["0 length"].transform(standardize_column_mean)
    
    return (df, df[['transcript_id', 'position']])
    
def get_dummies(df):
    final_predict_dataset = df.drop(columns=['transcript_id','position','0 length', '0 sd', '0 mean', '0 min', '0 max'])

    # Perform one-hot encoding for categorical columns
    final_predict_dataset = pd.get_dummies(final_predict_dataset, columns=['1st_pos', '2nd_pos', '3rd_pos', '4th_pos', '5th_pos'])
    
    return final_predict_dataset

def data_preprocess(file_path):
    df = pd.read_csv(file_path)
    df = get_position_1to5(df)
    seq_col = [col for col in df.columns.tolist() if col.startswith('sequence_')]
    df.drop(seq_col, axis=1, inplace=True)
    df.drop('specific_sequence', axis=1, inplace=True)
    df = categorise_positions(df)
    df = standardize_0data(df)[0]
    transcript = standardize_0data(df)[1]
    df = get_dummies(df)
    
    return (df, transcript)
