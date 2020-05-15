# -*- coding: utf-8 -*-
"""
Created on Fri May 15 19:53:45 2020

@author: Renu
"""
import win32serviceutil
import win32service
import win32event
import servicemanager
import socket

 class AppserverSvc(win32serviceutil.ServiceFramework):
     _svc_name_ = "TestService"
     _svc_display_name = "Test Service"
     
     
def _init_(self):
    win32serviceutil.ServiceFramework._init_(self,args)
    self.hwaitStop = win32event.CreateEvent(None,0,0,None)
    socket.setdefaulttimeout(60)
    
def SvcStop(self):
    self.ReportServiceStatus(win32service.SERVICE_STOP_PENDING)
    win32event.SetEvent(self.hwaitStop)
    
def SvcDoRun(self):
    servicemanager.LogMsg(servicemanager.EVENTLOG_INFORMATION_TYPE,
                          servicemanager.PYS_SERVICE_STARTED,
                          (self._svc_name_,''))
    self.main()

def main(self):
    pass

if _name_ = '_main_':
    win32serviceutil.HandleCommandLine(AppServerSvc)
    
    
    
