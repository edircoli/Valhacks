from enum import Enum
from experiment import Experiment
from pathlib import Path
import pandas as pd


class Targets(Enum):
    OBJECTIVE='objective'

    
class TargetType(Enum):
    CATEGORICAL = "categorical"
    BINARY = "binary"
    REGRESSION = "regression"

def read_target(experiment: Experiment, target: Targets, type: TargetType, base_path: Path, categories = None):
    if categories is None:
        file_name = experiment.value + '/targets/' + target.value + '.' + type.value + '.csv'
    else:
        file_name = experiment.value + '/targets/' + target.value + '.' + type.value + '.' + str(categories) + '.csv'
    df = pd.read_csv(Path.joinpath(base_path, file_name), sep=',')
    df = df.set_index('sample_id')
    return df

def write_target(dataframe,experiment: Experiment, target: Targets, type: TargetType, base_path: Path, categories = None):
    col_name=dataframe.columns.to_list()[0]
    dataframe = dataframe.rename(columns={col_name: 'target'})

    if categories is None:
        file_name = experiment.value + '/targets/' + target.value + '.' + type.value + '.csv'
    else:
        file_name = experiment.value + '/targets/' + target.value + '.' + type.value + '.' + str(categories) + '.csv'

    dataframe.to_csv(Path.joinpath(base_path, file_name))
    print('Successfuly saved in ',Path.joinpath(base_path, file_name))


if __name__ == "__main__":
    print(__name__)