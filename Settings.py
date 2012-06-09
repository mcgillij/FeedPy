""" Settings class """
import os, glob, pickle

class Settings():
    """ Going to use the settings class to pickle everything and write it to disk """
    def __init__(self):
        self.uri_list = []
        self.refresh_time = 1
        
    def save_settings(self):
        save_file = file("settings.dat", "wb")
        pickle.dump(self, save_file, 2)
        save_file.close()

    def load_settings(self):
        if check_for_save_file():
            load_file = file('settings.dat', "rb")
            settings = pickle.load(load_file)
            self.uri_list = settings.uri_list
            self.refresh_time = settings.refresh_time
            load_file.close()
            return True
        return False
    
def check_for_save_file():
    """ check for the existence of a save """
    path = "./"
    for cur_file in glob.glob(os.path.join(path, "*.dat")):
        return True
    return False
        