import sys
import os
import subprocess
import importlib

class SensorWrangler:
    
    ##dictionary sensor registry??** databasejson,xml?? bunch of sensor objects?? folder with sensor.py files?** 
    ##sensor address/port ??
    ##server address/port ??
    ##

    PluginFolder = "./plugins"
    MainModule = "__init__"

    def New():
        ''' register a new sensor
        '''
        pass

    def Update():
        ''' request data from a registered sensor
        '''
        pass

    def Status():
        '''request status of all sensors
        '''
        pass

    def getPlugins():
        plugins = []
        possibleplugins = os.listdir(PluginFolder)
        for i in possibleplugins:
            location = os.path.join(PluginFolder, i)
            if not os.path.isdir(location) or not MainModule + ".py" in os.listdir(location):
                continue
            info = imp.find_module(MainModule, [location])
            plugins.append({"name": i, "info": info})
        return plugins

    def loadPlugin(plugin):
        return imp.load_module(MainModule, *plugin["info"])