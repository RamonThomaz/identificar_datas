from pandas import read_csv

class BaseTraining():
    def __init__(self, training_input_path, model_output_path):
        self.training_input_path = training_input_path
        self.model_output_path = model_output_path
        self.training_input_data = None
        self.model = None


    def read_training_data(self) -> bool:
        self.training_input_data = read_csv(self.training_input_path)
