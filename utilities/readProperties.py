import configparser

# object creation
config = configparser.RawConfigParser()
config.read("Configurations/config.ini")

# 5.2 of Documentation
class ReadConfig:
    # static methods so that we can call methods directly using class name without creating object
    @staticmethod
    def getApplicaionURL():
        return config.get("common info", "baseURL")

    @staticmethod
    def getUsername():
        return config.get("common info", "username")

    @staticmethod
    def getPassword():
        return config.get("common info", "password")
