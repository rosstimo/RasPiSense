import os#, imp
import imp #ortlib

PluginFolder = os.path.abspath("plugins")
MainModule = "__init__"

def getPlugins():
    plugins = []
    possibleplugins = os.listdir(PluginFolder)
    for i in possibleplugins:
        location = os.path.join(PluginFolder, i)
        if not os.path.isdir(location) or not MainModule + ".py" in os.listdir(location):
            print(f'{i} is {True}')
            continue
        info = imp.find_module(MainModule, [location])
        #info = imp.find_module(MainModule, i)
        print(f'name: {i} info: {info}')
        plugins.append({"name": i, "info": info})
    print(plugins)
    return plugins

def loadPlugin(plugin):
    return imp.load_module(MainModule, *plugin["info"])

for i in getPlugins():
    print("Loading plugin " + i["name"])
    plugin = loadPlugin(i)
    plugin.run()