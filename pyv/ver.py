import re


SEPERATOR = '.'
DEFAULT_V_NUM = 0


def normalize(v1, v2):
    difference = abs(v1.number_count - v2.number_count)

    if v1.number_count > v2.number_count:
        v2.resize(difference)
    elif v1.number_count < v2.number_count:
        v1.resize(difference)

    return v1, v2


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

    def resize(self, ls_sp):

        if -ls_sp > self.__number_count:
            raise ValueError("the resizing number is out of accepted range")

        if ls_sp >= 0:
            for index in range(ls_sp):
                self.__version_numbers.append(DEFAULT_V_NUM)
        else:
            # making the number positive to make it easier
            ls_sp_p = -ls_sp
            for index in range(self.number_count-1, self.number_count - ls_sp_p-1, -1):
                self.__version_numbers.pop(index)

        self.__number_count += ls_sp

    def removeRedundant(self, value=0):
        counter = 0

        for index in range(self.__number_count-1, 0, -1):
            if self.__version_numbers[index] != value:
                break
            counter += 1
        self.resize(-counter)

    def isunder(self, version, check_num=1):
        ver_1, ver_2 = normalize(self, version)

        for (v1, v2) in zip(ver_1.version_numbers[: check_num], ver_2.version_numbers[:check_num]):
            if v1 != v2:
                return False
        return True

    def __str__(self):
        version = ""
        for num in self.__version_numbers:
            version += SEPERATOR+str(num)
        return version

    def __eq__(self, version):
        ver_1, ver_2 = normalize(self, version)

        for (v1, v2) in zip(ver_1.version_numbers, ver_2.version_numbers):
            if v1 != v2:
                return False
        return True

    def __ne__(self, version):
        return not self.__eq__(version)

    def __gt__(self, version):
        ver_1, ver_2 = normalize(self, version)

        for (v1, v2) in zip(ver_1.version_numbers, ver_2.version_numbers):
            if v1 > v2:
                return True

            elif v1 < v2:
                return False

    def __ge__(self, version):
        return self.__eq__(version) or self.__gt__(version)

    def __lt__(self, version):
        return not self.__gt__(version)

    def __le__(self, version):
        return self.__eq__(version) or self.__lt__(version)

    def __repr__(self):
        return "PyVersion"+str(tuple(self.version_numbers))



