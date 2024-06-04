import os
import sys
import json
import yaml

class file_operations(object):
    '''
    '''

    def get_file_type(file_path):
        """
        This function will return filetype.
        Args:
            String file_path: file path
        """
        try:
            typeList = file_path.split('.')
            print(typeList)
            return typeList[1]
        except Exception as error:
            raise error

    def read_data_from_file(self, file_path, keyOne, keyTwo):
        """
        This method will read the data from file, based on their file type
        Args:
            "file_path" : path of the file
            String keyOne : key one 
            String keyTwo : key two
        Returns:
            String file_data: file data
        """
        
        try:
            # print(os.path.join(path, filename))
            # file_path = (os.path.join(path, filename))
            
            file_type = file_operations.get_file_type(file_path)
            while file_type:
                if file_type == 'yaml':
                    print(keyOne)
                    print(keyTwo)
                    with open(file_path, 'r') as file:
                        file_data = yaml.safe_load(file)
                    print(file_data[keyOne][keyTwo])
                    file.close()
                    return file_data[keyOne][keyTwo]
                elif file_type == 'txt':
                    with open(file_path, 'r') as file:
                        file_data = file.read()
                    file.close()
                    return file_data
                elif file_type == 'json':
                    with open(file_path, 'r') as file:
                        file_data = json.load(file)
                    file.close()
                    return file_data
                else :
                    print()
            
        except Exception as error:
            raise error

    def set_data_to_filedef(self, file_path, keyOne, keyTwo):
        """
        """
        try:
            pass
        except Exception as error:
            raise error
        
    def check_roles_avaibility(self, roles, expected_role):
        '''
        check wheather expected role is present in list of roles
        '''
        try:
            r_flag = roles.__contains__(expected_role)
            if r_flag:
                return  f'The {expected_role} is present in the given list{roles}'
            else:
                return  (f'The {expected_role} is NOT present in the given list {roles}')

        except Exception as error:
            raise error