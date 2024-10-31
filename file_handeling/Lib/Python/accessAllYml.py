from ymlData.yamldata import YAMLHandler
import os
from pathlib import Path
from common_methods import Common_operations


# ************************** accessing all functions in this file ******************

file_p = 'D:/Users/rkendre/Rajeev/learning/previous_projects/jciExacqPoc/exacqpoc/file_handeling/Lib/Python/ymlData/data.yml'

def collect_all_file_data():
    '''
    '''
    
    data = YAMLHandler(file_path = file_p)
    yaml_handler = data.read_yaml()

    # print(yaml_handler)
    print(data.get_value_from_dict(yaml_handler, 'TEST-T530', 'username'))
    print('************************')
    print((data.get_value_from_dict(yaml_handler, 'TEST-T530', 'Camera')))
    print('************************')
    print((data.get_multiple_value_from_dict(yaml_handler, 'TEST-T530', 'Camera', 'Isconnected', 'IP'))) # 3 args
    print('************************')
    print((data.get_multiple_value_from_dict(yaml_handler, 'TEST-T530', 'Camera', 'Isconnected'))) # 2 args
    print((data.get_multiple_value_from_dict(yaml_handler, 'TEST-T530', 'Camera', 'LiveStreaming'))) # 2 args



# collect_all_file_data()


# get the data for specified keys
final_path = Common_operations().get_folder_path()
yaml_handler = YAMLHandler(folder_path=final_path)
# print(yaml_handler.get_test_case_specific_data('TEST-T534', 'username'))
# print(yaml_handler.get_all_data('TEST-T534', 'Camera', 'Isconnected', 'IP'))
print(yaml_handler.get_test_case_specific_data('TEST-T533', 'Camera', 'Isconnected', 'IP'))
