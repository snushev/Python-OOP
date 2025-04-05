from abc import ABC, abstractmethod
########################
@staticmethod
def _find_object_by_name(lst, name):
    return next((obj for obj in lst if obj.name == name), None)

##########################################
@property
def name(self):
    return self.__name


@name.setter
def name(self, value):
    if value.strip() == "":
        raise ValueError()
    self.__name = value
##################################