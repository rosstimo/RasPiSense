#testing class implementation for multiple sensors

class sensor(object):
    """docstring for sensor."""
        #name = ?
        #data = ?
        #dataUnits =
        # What is returned? (Name, data, ?)
        #set continueous Boolean. needs continuoues interval and Duration
        #shutdown command

    def __init__(self, recData):
        self.recData = recData
        print recData
# class dummySensor(sensor):
#     """docstring for ."""
#
#     def __init__(self, command):
#         #super(, self).__init__()
#         self.arg = arg

dsensor = dummySensor('hello')

dsensor.name = 'dummy'
dsensor.data = 'data'
