#!/usr/bin/python3
#
# main.py
#
# central launcher that processes commandline arguments and selects interface.
#
# Here's your stinkin' licence: http://unlicense.org/
#
# - l0k1
#
# Contact details for l0k1
# steemit.com - https://steemit.com/@l0k1
# bitmessage - BM-2cXWxTVaXJbNyMxv5tAjNg87xS98hrAg8P
# torchat - xq6xcvqc2vy34qtx
# email - l0k1@null.net

"""
Main interface that works with the commandline interface, imports the 
user selected interface module, and launches the core module
"""

debugflag = True

import sys, os, argparse

"""
Commandline argument parsing

Commandline defines which frontend and which config backends are used by
the app

TODO: Add the ability to select these by the name of this script
"""

if __name__ == "__main__":
    """
    Load core module and begin application
    """
    parser = argparse.ArgumentParser()
    parser.add_argument ('frontend', 
        metavar='FRONTEND', type=str, nargs="?",
        default="gtk3", 
        help="Interface frontend library to use, defaults to gtk3")
    parser.add_argument ('config', metavar='CONFIG', type=str, nargs="?",
        default="dconf", 
        help="Configuration backend library to use, defaults to dconf")
    args = parser.parse_args()

    frontend_obj = __import__ (args.frontend)
    globals () [args.frontend] = frontend_obj
    config_obj = __import__ (args.config)
    globals () [args.config] = config_obj  
    
    coremodule_obj = __import__ ("core")
    globals () ["core"] = coremodule_obj

    coremodule_obj.steemportal (frontend_obj, config_obj)
