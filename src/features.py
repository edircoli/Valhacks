from enum import Enum
from experiment import Experiment
from clinical_studies import ClinicalStudy
from pathlib import Path
import pandas as pd
from pandas import DataFrame
import os


class Features(Enum):
    FEATURE1='features1'



def read_data( file_prefix: str, base_path: Path,exp_prefix:bool):
    print('Searching base path: ', base_path.resolve())
    if exp_prefix:
        base_file_name = file_prefix
    else:
        base_file_name=file_prefix


    #print('With base name', base_file_name)
    file_names = [x for x in os.listdir(base_path) if x.startswith(base_file_name)]
    dataframes = []

    #print(file_names)

    for file_name in file_names:
        p = Path.joinpath(base_path, file_name)
        print('Loading file...', p.resolve())
        df = pd.read_csv(Path.joinpath(base_path, file_name), sep=',')
        #print(df.head())
        df = df.set_index('sample_id')
        dataframes.append(df)

    concat = pd.concat(dataframes, axis=0)
    return concat

def read(feature: Features, experiment: Experiment, base_path: Path,exp_prefix:True):
    # Get the file prefix from the feature value
    file_prefix = feature.value

    # Read the data
    df = read_data(study=experiment, file_prefix=file_prefix, base_path=base_path,exp_prefix=exp_prefix)

    return df



if __name__ == "__main__":
    print(__name__)
