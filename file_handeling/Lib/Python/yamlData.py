from dataclasses import dataclass
from typing import Any, Dict, List

import yaml


@dataclass
class ServerDetails:
      ip_address: str
      tc_id: int
      port: int
      username: str
      password: str
      additional_data: str
      server_type: str
      u_id: int


@dataclass
class Server:
    working_server: List[ServerDetails]
    def __post_init__(self):
        try:
            server_data = []
            for tc in self.working_server:
                server_data.append(ServerDetails(**tc))
            self.emp = server_data
        except Exception as error:
            raise error

@dataclass
class Addserver():
    '''
    '''
    test_case: List[Server]
    def __post_init__(self) -> Server:
        try:
            test_case_data = []
            for tc in self.test_case:
                test_case_data.append(Server(**tc))
            self.test_case = test_case_data
        except Exception as error:
            raise error


@dataclass()
class Main_class():
    '''
    '''
    add_server_data: List[Addserver]
    def __post_init__(self) -> Addserver:
        try:
            test_data = []
            for tc in self.add_server_data:
                test_data.append(Addserver(**tc))
            self.add_server_data = test_data
            print(test_data)
        except Exception as error:
            raise error
    def get_whole_data(self) -> List:
        '''
        '''        
        try:
            list_of_data = []
            print(len(self.add_server_data))
            for cmp in self.add_server_data:
                for em in cmp.test_case:
                    for dm in em.working_server:
                        for key, value in dm.items():
                            ky = key,value
                            list_of_data.append(ky)
            return list_of_data
        except Exception as error:
            raise error

    def get_server_data(self, attribute_name:str) -> List:
        '''
        '''
        try:
            server_data = []
            print(len(self.add_server_data))
            for cmp in self.add_server_data:
                for em in cmp.test_case:
                    for dm in em.working_server:
                        for key, value in dm.items(): 
                            if key == attribute_name:
                                server_data.append(key)
                                server_data.append(value)

            return server_data
        except Exception as error:
            raise error

    def get_server_details(self) -> List:
        '''
        '''
        try:
            server_details = []
            print(len(self.add_server_data))
            for cmp in self.add_server_data:
                for em in cmp.test_case:
                    for dm in em.working_server:
                        for key, value in  dm.items(): 
                                server_details.append(key)
                                server_details.append(value)

            return server_details
        except Exception as error:
            raise error
    
    def get_test_specific_data(self, tc_param_a, tc_param_b=None) -> List:
        '''
        '''
        try:

            test_specific_details = []
            print(len(self.add_server_data))
            for cmp in self.add_server_data:
                for em in cmp.test_case:
                    for dm in em.working_server:
                        for key, value in  dm.items():
                            if value == tc_param_a:
                                    for data in em.working_server:
                                        for km, val in data.items():
                                            tup = km, val
                                            test_specific_details.append(tup)

            return test_specific_details
        except Exception as error:
            raise error

class exractData():
# step 1: Read the file. Since file is small, we are doing a whole read.
    def read_yaml_file(file_path):
        with open(file_path) as load_yaml_file:
            return load_yaml_file.read()


    # step 2: Parse the yaml file into a dictionary
    def parse_yaml_file(yaml_string: str) -> Dict[Any, Any]:
        return yaml.safe_load(yaml_string)


    # step 3: Change dictionary into data class
    def server_to_dict(parsed_yaml: Dict[Any, Any]) -> Main_class:
        return Main_class(**parsed_yaml)
    
file_path = "D:\\Users\\rkendre\\Rajeev\\learning\\previous_projects\\jciExacqPoc\\exacqpoc\\file_handeling\\Lib\\Python\\yamlDataDriver.yml"

read_yaml = exractData.read_yaml_file(file_path)
parsed_yaml_dict = exractData.parse_yaml_file(read_yaml)
sorted_data = exractData.server_to_dict(parsed_yaml_dict)
# print("FINAL DATA IS :- ", mysteryInc.get_whole_data())
# print("MysteryInc", mysteryInc)
print("SERVER DATA :- ", sorted_data.get_server_data('port'))
# print("SERVER DETAILS :-", mysteryInc.get_server_details())
print("SERVER DETAILS :-", sorted_data.get_test_specific_data(1445,12))