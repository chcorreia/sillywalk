#-------------------------------------------------------------------------------
# Name:        teste.py
# Purpose:     algum teste idiota, programa é reescrito a cada teste
#
# Author:      Carlos H Correia - chcorreia@gmail.com
#
# Created:     07/08/2012
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#!/usr/bin/env python

import atexit

@atexit.register
def xuxu():
    print "hey"

print "acabou"