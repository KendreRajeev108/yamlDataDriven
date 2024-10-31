import yaml
# from pathlib import Path
import pathlib
import os


# from typing import Any, Dict, List

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
                print(len(sub_keys))
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
            print(error)

    # def get_key_from_dict(self, fulldata, parent_key, target_value):
    #     data = fulldata[parent_key]
    #     # Function to recursively search for the target_key
    #     def _get_key_recursive(data, target_value):
    #         if isinstance(data, dict):
    #             # print(data.items())
    #             for key, value in data.items():
    #                 print(key)
    #                 print(value)
    #                 # value = {}
    #                 print(value)
    #                 if value == target_value:
    #                     return value
    #                 elif isinstance(key, dict):
    #                     nested_key = _get_key_recursive(key, target_value)
    #                     if nested_key is not None:
    #                         return nested_key
    #         return None
    #     return _get_key_recursive(data, target_value)

file_pth = 'D:\\Users\\rkendre\\Rajeev\\learning\\previous_projects\\jciExacqPoc\\exacqpoc\\file_handeling\\Lib\\Python\\ymlData\\data.yml'
if __name__ == '__main__':
    fol_path = "/file_handeling/Lib/Python/yamlFiles"
    abs_path = pathlib.Path().absolute()
    # print('before',abs_path)
    
    up_path = str(abs_path).replace('\\','/')
    # print('after',up_path)
    final_path = up_path.__add__(fol_path)
    final_path = pathlib.Path(final_path)
    # print('*****',final_path)
    # print(pathlib.Path.exists(final_path))

    yaml_handler = YAMLHandler(folder_path=final_path)
    # yaml_data = yaml_handler.read_yaml()
    # print(yaml_handler)
    # print(yaml_handler.get_all_data('TEST-T534', 'username'))
    # print(yaml_handler.get_all_data('TEST-T534', 'Camera', 'Isconnected', 'IP'))
    print(yaml_handler.get_all_data('TEST-T533', 'Camera', 'Isconnected', 'IP'))
    




#     # test case id and username
#     # yaml_data = yaml_handler.read_yaml()
#     # print((yaml_handler.get_value_from_dict(yaml_data, 'TEST-T530', 'username')))
#     # print('************************')
#     # print((yaml_handler.get_value_from_dict(yaml_data, 'TEST-T530', 'Camera')))
#     # print('************************')
#     # print((yaml_handler.get_multiple_value_from_dict(yaml_data, 'TEST-T530', 'Camera', 'Isconnected', 'IP'))) # 3 args
#     # print('************************')
#     # print((yaml_handler.get_multiple_value_from_dict(yaml_data, 'TEST-T530', 'Camera', 'Isconnected'))) # 2 args

    
#     # folder_path = r'\file_handeling\Lib\Python\yamlFiles'
#     # abs_path = pathlib.Path().absolute()
#     # final_path = str(abs_path).__add__(folder_path)
#     # final_path = pathlib.Path(final_path)
#     # print(final_path)
#     # print(pathlib.Path.exists(final_path))