import yaml
# from pathlib import Path
import pathlib
import os


class YAMLHandler:
    def __init__(self, file_path=None, folder_path=None):
        self.file_path = file_path
        self.folder_path = str(folder_path)


    def read_yaml(self):
        with open(self.file_path, 'r') as file:
            try:
                data = yaml.safe_load(file)
                return data
            except yaml.YAMLError as e:
                print(f"Error reading YAML file: {e}")
                return None

    def get_value_from_dict(self, fulldata, parent_key, target_key):
        '''
        This function will return the specified parent and target key.
        '''
        data = fulldata[parent_key]
        # Function to recursively search for the target_key
        def _get_value_recursive(data, target_key):
            if isinstance(data, dict):
                for key, value in data.items():
                    if key == target_key:
                        return value
                    elif isinstance(value, dict):
                        nested_value = _get_value_recursive(value, target_key)
                        if nested_value is not None:
                            return nested_value
            return None

        # Call recursive function to find the value
        return _get_value_recursive(data, target_key)

    def get_multiple_value_from_dict(self, fulldata, parent_key, *sub_keys):
        '''
        This method will return values for multiple arguments / keys.
        '''
        data_dict = {}
        for key in sub_keys:
            value = self.get_value_from_dict(fulldata, parent_key, key)
            data_dict[key] = value

        return data_dict
    def get_test_case_specific_data(self, parent_key, *sub_keys):
        '''
        This method will read all the files from specified folder and returns
        dictionary data related to specified keys

        '''
        try:
            new_dict = {}
            print(os.listdir(self.folder_path))
            for x in os.listdir(self.folder_path):
                file_p = os.path.join(self.folder_path, x)
                file_p = pathlib.Path(file_p)
                class_obj = YAMLHandler(file_p)
                data = class_obj.read_yaml()
                new_dict.update(data)
            data_dict = {}
            if len(sub_keys) == 1:
                for key in sub_keys:
                    value = class_obj.get_value_from_dict(new_dict, parent_key, key)
                    data_dict[key] = value
                return data_dict
            elif len(sub_keys) > 1:
                for key in sub_keys:
                    value = class_obj.get_multiple_value_from_dict(new_dict, parent_key, key)
                    data_dict[key] = value
                return data_dict
        except Exception as error:
            raise error
