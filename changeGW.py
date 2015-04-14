#coding:utf-8

import wmi
from Tkinter import *



def Qgw():
    wmiService=wmi.WMI()
    colNicConfigs=wmiService.Win32_NetworkAdapterConfiguration(IPEnabled=True)
    gw=colNicConfigs[0].DefaultIPGateway[0]
    if "192.168.199.1" in gw:
        return "中国电信ADSL20Mb"
    elif "192.168.199.250" in gw:
        return "中国电信静态光纤10Mb"
    elif "192.168.199.2" in gw:
        return "中国联通ADSL30Mb"
    else:
        return "未知线路"

def changeIP(gw=[]):
    dns=['192.168.199.230','8.8.8.8']
    wmiService=wmi.WMI()
    colNicConfigs=wmiService.Win32_NetworkAdapterConfiguration(IPEnabled=True)
    objNicConfig=colNicConfigs[0]
    intReboot=0
    objNicConfig.SetDNSServerSearchOrder(dns)
    returnValue=objNicConfig.SetGateways(DefaultIPGateway=gw,GatewayCostMetric=[1])
    if returnValue[0]==0 or returnValue[0]==1 :
        msg['text']="恭喜！你已经切换成为"+"<"+str(Qgw())+">"
    else:
        msg['text']="网络切换失败,请尝试用系统管理员权限运行程序。"

tel=['192.168.199.1']
uni=['192.168.199.2']
root=Tk()
root.wm_title("万金网络切换程序")
msg=Label(root,text="你当前使用的是"+"<"+str(Qgw())+">",font="bold 16")
msg.grid(row=0,sticky=E)
tel_b=Button(root,text="点击切换为<中国联通>",command=lambda:changeIP(uni))
tel_b.grid(row=1,sticky=W)
uni_b=Button(root,text="点击切换为<中国电信>",command=lambda:changeIP(tel))
uni_b.grid(row=1,column=1,sticky=W)
Button(root,text="退出程序",command=root.quit).grid(row=3,sticky=W)

root.mainloop()
