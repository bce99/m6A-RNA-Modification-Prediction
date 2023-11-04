import pandas as pd
import gzip
import json
from collections import Counter

def read_json_gz(file_path:str):
    # Create a list to hold the JSON objects
    data_list = []

    # Open and decompress the gz file, then load the JSON data line by line
    with gzip.open(file_path, 'rt', encoding='utf-8') as file:
        for line in file:
            # Parse the JSON data for the line and append to data_list
            json_obj = json.loads(line.strip())
            data_list.append(json_obj)

    # Example: Convert the first JSON object to a Pandas DataFrame
    df = pd.json_normalize(data_list[0])
    
    return (data_list, file_path)

def count_acgt_letters(input_string):
    letter_counts = dict(Counter(input_string))
    acgt_counts = {
        'A': letter_counts.get('A', 0),
        'C': letter_counts.get('C', 0),
        'G': letter_counts.get('G', 0),
        'T': letter_counts.get('T', 0),
    }
    
    return acgt_counts

def count_data(data_list):
    parsed_data = []  
    for data in data_list:
        for transcript_id, positions in data.items():
            for position, details in positions.items():
                for sequence, readings in details.items():
                    letter_counts = count_acgt_letters(sequence[1:6]) 
                    for reading in readings:
                        value = reading[3:6]
                        parsed_data.append([transcript_id, int(position), sequence[1:6],letter_counts['A'], letter_counts['C'], letter_counts['G'], letter_counts['T']] + value)

    columns = ['transcript_id', 'position','sequence', 'A', 'C', 'G', 'T', '0 length', '0 sd', '0 mean']

    return pd.DataFrame(parsed_data, columns=columns)

def output_parsed_data(data_list, file_path):
    df = count_data(data_list)
    df['0 min'] = df['0 mean'] - df['0 sd']*1.96
    df['0 max'] = df['0 mean'] + df['0 sd']*1.96
    df = pd.get_dummies(df, columns=['sequence'], prefix='sequence')
    
    df.to_csv(f'Parsed_Data{file_path[7]}.csv', index=False)
    

def run_parse_data():
    output_parsed_data(read_json_gz('dataset0.json.gz')[0], read_json_gz('dataset0.json.gz')[1])
    output_parsed_data(read_json_gz('dataset1.json.gz')[0], read_json_gz('dataset1.json.gz')[1])
    output_parsed_data(read_json_gz('dataset2.json.gz')[0], read_json_gz('dataset2.json.gz')[1])
    output_parsed_data(read_json_gz('dataset3.json.gz')[0], read_json_gz('dataset3.json.gz')[1])