import pandas as pd
import gzip
import json

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

def parse_data(data_list):
    parsed_data = []
    for data in data_list:
        for transcript_id, positions in data.items():
            for position, details in positions.items():
                for sequence, readings in details.items():
                    for reading in readings:
                        parsed_data.append([transcript_id, int(position), sequence] + reading)
    return pd.DataFrame(parsed_data, columns=['transcript_id', 'position', 'sequence', '-1 length', '-1 sd', '-1 mean', '0 length', '0 sd', '0 mean', '+1 length', '+1 sd', '+1 mean'])

def output_parsed_data(data_list, file_path):
    df = parse_data(data_list)
    df.to_csv(f'DSA4266Processed_dataset{file_path[7]}_json.csv', index=False)
    

def run_parse_data():
    output_parsed_data(read_json_gz('dataset0.json.gz')[0], read_json_gz('dataset0.json.gz')[1])
    output_parsed_data(read_json_gz('dataset1.json.gz')[0], read_json_gz('dataset1.json.gz')[1])
    output_parsed_data(read_json_gz('dataset2.json.gz')[0], read_json_gz('dataset2.json.gz')[1])
    output_parsed_data(read_json_gz('dataset3.json.gz')[0], read_json_gz('dataset3.json.gz')[1])