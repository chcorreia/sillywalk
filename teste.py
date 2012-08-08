#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Ana Paula
#
# Created:     07/08/2012
# Copyright:   (c) Ana Paula 2012
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#!/usr/bin/env python

import atexit

def xuxu():
    print "hey"

atexit.register(xuxu)
