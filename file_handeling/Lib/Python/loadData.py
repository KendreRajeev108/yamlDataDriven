
from yamlData import exractData

file_path = "D:\\Users\\rkendre\\Rajeev\\learning\\previous_projects\\jciExacqPoc\\exacqpoc\\file_handeling\\Lib\\Python\\yamlDataDriver.yml"

read_yaml = exractData.read_yaml_file(file_path)
parsed_yaml_dict = exractData.parse_yaml_file(read_yaml)
sorted_data = exractData.server_to_dict(parsed_yaml_dict)
# print("FINAL DATA IS :- ", mysteryInc.get_whole_data())
# print("MysteryInc", mysteryInc)
print("SERVER DATA :- ", sorted_data.get_server_data('port'))
# print("SERVER DETAILS :-", mysteryInc.get_server_details())
print("SERVER DETAILS :-", sorted_data.get_test_specific_data(1445,12))