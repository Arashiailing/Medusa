#!/usr/bin/env python
# _*_ coding: utf-8 _*_
from Cms.AfterLogicWebMail import AfterLogicWebMailArbitraryFileContains
import time
def Main(ThreadPool,Url,Values,ProxyIp):
    ThreadPool.Append(AfterLogicWebMailArbitraryFileContains.medusa, Url, Values, ProxyIp)
    print("\033[1;40;32m[ + ] AfterLogicWebMail component payload successfully loaded\033[0m")
    time.sleep(0.5)