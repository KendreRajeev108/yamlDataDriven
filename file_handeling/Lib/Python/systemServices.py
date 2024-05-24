import psutil
import os
import subprocess as sb
import wmi

class systemServices(object):
    '''
    This class contains system seevice operations.
    '''
    def getService(self, serviceName):
        '''
        This function will return the state of the service name provided.
        Arguments:
            serviceName - Name of the service.
        '''
        service = None
        try:
            service = psutil.win_service_get(serviceName)
            service = service.as_dict()
        except Exception as ex:
            print(str(ex))
        return service

    def serviceOperation(self, serviceName, operation):
        '''
        This function will return the state of the service name provided.
        Arguments:
            serviceName - Name of the service.
        '''
        service = None
        try:
            if operation == 'start':
                service = psutil.win_service_get(serviceName)
                service = service.as_dict()
                service['name'].start()
            if operation == 'stop':
                service = psutil.win_service_get(serviceName)
                service = service.as_dict()
                service['name'].stop()
            if operation == 'suspend':
                service = psutil.win_service_get(serviceName)
                service = service.as_dict()
                service['name'].suspend()
            if operation == 'resume':
                service = psutil.win_service_get(serviceName)
                service = service.as_dict()
                service['name'].resume()
            else:
                pass
            
        except Exception as error:
            raise error
        return service

    def checkServiceStatus(self, getService):
        '''
        This function check whether service is runing or not.
        '''

        try:
            if getService:
                print("service found")
            else:
                print("service not found")
            if getService and getService['status'] == 'running':
                print("service is running")
            else:
                print("service is not running")
        except Exception as error:
            raise error


    def stopProcess(self, pid):
        '''
        This function will perfowm the operation for specified process.
        Arguments:
            pid - process id
            Note - like  stopProcess(8260)

        '''
        try:
            print(psutil.Process.is_running(pid))
            ps = psutil.Process(pid).kill()
            # ps.suspend()
            print('after suspend !!!')
            # print(psutil.Process.is_running(serviceName))
        except Exception as error:
            # print(str(error))
            raise error


    def getAllServices():
        '''
        This function will give all the services present on system.
        Note verified for windows
        '''
        try:
            services = []
            for winService in wmi.WMI().Win32_Service():
                services.append(winService)
            return services
        except Exception as error:
            raise error


    def stopServiceOS(self, serviceName, operation):
        '''
        This function will perfoem the operation for secified service.
        Arguments:
            serviceName - Name of the service
            operation - operation to perform( start, stop and resume )
        ''' 
        try:
            for winService in wmi.WMI().Win32_Service(): 
                # if services.Name == serviceName:
                if operation == 'start' and winService.Name == serviceName:
                    print(winService.Name)
                    winService.StartService()
                    break
                if operation == 'stop' and winService.Name == serviceName:
                    print(winService.Name)
                    winService.StopService()
                    break
                if operation == 'resume' and winService.Name == serviceName:
                    print(winService.Name)
                    winService.ResumeService()
                    break
                else:
                    pass
                
        except Exception as error:
            raise error