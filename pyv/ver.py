import re


SEPERATOR = '.'
DEFAULT_V_NUM = 0


class PyVersion:
    __number_count: int = 0
    __version_numbers: list = None

    def __init__(self, *version_numbers):
        self.__number_count = len(version_numbers)
        self.__version_numbers = self.__convertInt(list(version_numbers))

    @property
    def number_count(self):
        return self.__number_count

    @property
    def version_numbers(self):
        return self.__version_numbers

    @staticmethod
    def __convertInt(arr: list):
        for index in range(len(arr)):
            arr[index] = int(arr[index])
        return arr

    @classmethod
    def fromstr(cls, version: str, sep: str = SEPERATOR):
        num_ls = version.split(sep)
        try:
            while True:
                num_ls.remove('')
        except ValueError:
            ...
        return cls(*num_ls)

    def __str__(self):
        version = ""
        for num in self.__version_numbers:
            version += SEPERATOR+str(num)
        return version

    def resize(self, ls_sp):

        if -ls_sp > self.__number_count:
            raise ValueError("the resizing number is out of accepted range")

        self.__number_count += ls_sp
        if ls_sp >= 0:
            for index in range(ls_sp):
                self.__version_numbers.insert(index, DEFAULT_V_NUM)
        else:
            for index in range(-ls_sp):
                self.__version_numbers.pop(DEFAULT_V_NUM)

    def __eq__(self, version):
        difference = self.__number_count - version.number_count

        if self.__number_count > version.number_count:
            version.resize(difference)
        elif self.__number_count < version.number_count:
            self.resize(difference)

        for (v1, v2) in zip(self.__version_numbers, version.version_numbers):
            if v1 != v2:
                return False
        return True

    def __ne__(self, version):
        return not self.__eq__(version)


