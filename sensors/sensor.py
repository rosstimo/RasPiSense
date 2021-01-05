
class sensor:
    #def __init__(self):
    #    pass

    def read():
        return {"ValueName":123, "thing":1}

    #def set():
    #    pass

if __name__ == '__main__' :
    r = sensor.read()
    print(r["ValueName"])
    print(sensor.read()["thing"])