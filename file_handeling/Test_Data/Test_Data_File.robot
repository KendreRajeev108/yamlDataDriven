*** Settings ***
Documentation    Test Data file 

*** Variables ***


${browser}      Chrome
# ${link}         http://google.com

# input data
${list}

# login details
# ${link}     http://esmdemo.exacq.com
${link}     http://127.0.0.1/
# ${Username}    altimetrik
# ${Password}    @Met3K#!
${Username}    admin
${Password}    Iasys@128

# ${folderPath}     C:/Program Files/exacqVision/EnterpriseManager/EnterpriseSystemManager/logs
${fileName}       log_settings.yaml
${expectedDateFormat}    %d/%b/%Y %H:%M:%S
${formatters_standard_format_value}    [%(asctime)s] %(levelname)s [%(processName)s:%(process)d,%(threadName)s:%(thread)d,%(filename)s:%(lineno)s] %(message)s

${advanced_options}    advanced_options
${formatters_standard_datefmt}    formatters_standard_datefmt
${formatters_standard_format}    formatters_standard_format
