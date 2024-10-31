from PIL import Image
import os
from pixelmatch.contrib.PIL import pixelmatch
import pathlib


# script_directory = os.path.dirname(__file__)
# folder_path = os.path.abspath(os.path.join(script_directory, '..', "dummyWork"))

# print(folder_path)

# new_list = []
# for x in os.listdir(folder_path):
#     if x.lower().endswith(('.png')):
#         print(x)        
#         file_p = os.path.join(folder_path, x)
#         file_p = pathlib.Path(file_p)
#         new_list.append(file_p)

# print(new_list)

# img_a = Image.open(new_list[0])
# img_b = Image.open(new_list[1])
# img_diff = Image.new("RGBA", img_a.size)


# # note how there is no need to specify dimensions
# mismatch = pixelmatch(img_a, img_b, img_diff, includeAA=True,threshold = 1.1)

# img_diff.save("diff.png")

server_detail = ['Serial', 'Mac', 'Server Platform','Version','Operating System','Mother Board','Bios','Processors','Memory']
connection_detail = ['Address','Port','Server Connection Type','Connection Heartbeat']
server_setting = ['Group','Username','Desired Oldest Content','Password Strengthening','Live Streaming']
var_ls = 'server_detail'
def getServerDetails():
    try:
        # list_of_element = Util.webDriverObj.find_elements(By.XPATH, self.serverPath)
        element_ls = ['', 'Status: Connected', '', 'Oldest Content: 526 days', 'Address:', 'hybrid.exacq.com', 'Port:', '22609', 'Hostname:', 'Server Connection Type:', 'Inbound', 'Connection Heartbeat:', '30', 'Serial:', 'ER2050025125', 'Mac:', 'A8-A1-59-04-36-7A', 'Server Platform:', 'Windows 64-bit', 'Version:', '24.03.4.0', 'Operating System:', 'Microsoft Windows Server 2019 Standard 64-bit 10.0.17763', 'Mother Board:', 'ASRockRack / C236M WS', 'Bios:', 'American Megatrends Inc. / L2.70D 05/22/2020', 'Processors:', 'Intel(R) Core(TM) i7-7700 CPU @ 3.60GHz', 'Memory:', '16.00GB', 'Group:', 'Username:', 'Dave.Ratliff', 'Desired Oldest Content:', '0 days', 'Password Strengthening:', 'Disabled', 'Live Streaming:', 'Enabled']
        remove_items_ls = ['','Hostname:','Group:']
        for rm in remove_items_ls:
            element_ls.remove(rm)
        # items will be removed from the list
        main_list = []
        for x in element_ls:
            if x.__contains__(': '):
                    nl = x.split(':')
                    for z in nl:
                        m = z.strip()
                        main_list.append(m)
        # 
        for el in element_ls:
            if el.endswith(':'):
                y = el.removesuffix(':')
                main_list.append(y)
            elif  (':' not in el):
                main_list.append(el)
        return main_list
    except Exception as error:
        raise error

def get_specific_server_details(server_detail):
    '''
    argument type :-
    server_detail - for server details
    connection_detail - for connection details
    server_setting - for server setting details
    '''
    detail_ls = []
    list_of_elements = getServerDetails()
    for x in server_detail:
        loop_ls = []
        if list_of_elements.__contains__(x):
            loop_ls.append(x)
            loop_ls.append(list_of_elements[(list_of_elements.index(x) + 1)])
            detail_ls.append(loop_ls)
    return detail_ls


def get_specific_server_details(var_ls):
    '''
    argument type :-
    server_detail - for server details
    connection_detail - for connection details
    server_setting - for server setting details
    '''
    server_detail = ['Serial', 'Mac', 'Server Platform','Version','Operating System','Mother Board','Bios','Processors','Memory']
    connection_detail = ['Address','Port','Server Connection Type','Connection Heartbeat']
    server_setting = ['Group','Username','Desired Oldest Content','Password Strengthening','Live Streaming']
    md = {'server_detail':server_detail, 'connection_detail':connection_detail, 'server_setting':server_setting}
    print(md[var_ls])
    # print(dd)



get_specific_server_details(var_ls)
# print(get_specific_server_details(server_detail))




from PIL import Image
import os
from pixelmatch.contrib.PIL import pixelmatch
import pathlib
from robot.api import logger

def compare_two_images(image_a, Image_b):
    try:
        script_directory = os.path.dirname(__file__)
        folder_path = os.path.abspath(os.path.join(script_directory, '..', "Reports","Screenshots"))
        image_a_path = os.path.join(folder_path, image_a)
        Image_b_path = os.path.join(folder_path, Image_b)
        print(image_a_path)
        print(Image_b_path)

        new_list = []
        for x in os.listdir(folder_path):
            if x.lower().endswith(('.png')):
                print(x)
                file_p = os.path.join(folder_path, x)
                file_p = pathlib.Path(file_p)
                new_list.append(file_p)
            # if new_list.__contains__
        img_a = Image.open(new_list[0])
        img_b = Image.open(new_list[3])
        img_diff = Image.new("RGBA", img_a.size)
        mismatch = pixelmatch(img_a, img_b, img_diff, includeAA=True,threshold = 1.1)
        logger.info(mismatch)
        # logger.console(mismatch)
        img_diff.save("diff.png")
        return  True
    except ValueError  as error:
        logger.info(error)
        return False
        # logger.console(error)

compare_two_images('pic.png', 'pic_two.png')

#  in base page 