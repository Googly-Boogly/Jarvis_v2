import servicemanager
import socket
import win32serviceutil
import win32service
import win32event
# from main import they_loop

class MyService(win32serviceutil.ServiceFramework):
    _svc_name_ = "MyPythonService"
    _svc_display_name_ = "My Python Service"

    def __init__(self, args):
        win32serviceutil.ServiceFramework.__init__(self, args)
        self.hWaitStop = win32event.CreateEvent(None, 0, 0, None)
        socket.setdefaulttimeout(60*30) #in seconds

    def SvcStop(self):
        self.ReportServiceStatus(win32service.SERVICE_STOP_PENDING)
        win32event.SetEvent(self.hWaitStop)

    def SvcDoRun(self):
        servicemanager.LogMsg(servicemanager.EVENTLOG_INFORMATION_TYPE, servicemanager.PYS_SERVICE_STARTED, (self._svc_name_, ''))
        self.main()

    def main(self):
        # they_loop()
        print('hi')

if __name__ == '__main__':
    servicemanager.Initialize()
    servicemanager.PrepareToHostSingle(MyService)
    servicemanager.StartServiceCtrlDispatcher()
