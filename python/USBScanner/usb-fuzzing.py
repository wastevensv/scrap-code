#!/usr/bin/python

import usb.core
import usb.util
import sys
 
# find our device
dev = usb.core.find(idVendor=0x0feb, idProduct=0x2015)
 
# was it found?
if dev is None:
    raise ValueError('Device not found')

# Linux kernel sets up a device driver for USB device, which you have
# to detach. Otherwise trying to interact with the device gives a
# 'Resource Busy' error.
try:
  dev.detach_kernel_driver(0)
except Exception, e:
  pass # already unregistered
 
# set the active configuration. With no arguments, the first
# configuration will be the active one
dev.set_configuration()

 
# Lets start by Reading 1 byte from the Device using different Requests
# bRequest is a byte so there are 255 different values
for bRequest in range(2):
    try:
        ret = dev.ctrl_transfer(0xC0, bRequest, 0, 0, 1)
        print "bRequest ",bRequest
        print ret
    except:
        # failed to get data for this request
        pass

print "all done"
