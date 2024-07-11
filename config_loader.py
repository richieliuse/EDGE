import yaml


class ConfigLoader:
    def __init__(self, config_file="config.yaml"):
        self.config_file = config_file
        self.config = self.load_config()

    def load_config(self):
        with open(self.config_file, "r") as file:
            config = yaml.safe_load(file)
        return config

    def get_data_config(self):
        return self.config.get("data", {})

    def get_training_config(self):
        return self.config.get("training", {})

    def get_predict_config(self):
        return self.config.get("predict", {})
