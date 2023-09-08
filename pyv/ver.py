import re


SEPERATOR = '.'
DEFAULT_V_NUM = 0


def normalize(v1, v2):
    difference = v1.number_count - v2.number_count

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

    def removeRedundant(self, value=0):
        counter = 0

        for index in range(self.__number_count):
            if self.__version_numbers[index] != value:
                break
            counter += 1
        self.resize(-counter)

    def __eq__(self, version):
        ver_1, ver_2 = normalize(self, version)

        for (v1, v2) in zip(ver_1.__version_numbers, ver_2.version_numbers):
            if v1 != v2:
                return False
        return True

    def __ne__(self, version):
        return not self.__eq__(version)



a = PyVersion().fromstr("5.3.3")
b = PyVersion().fromstr("4")
print(a)
print(b)
print(a == b)
print(a, a.number_count)
print(b, b.number_count)
a.removeRedundant()
b.removeRedundant()
print(a, a.number_count)
print(b, b.number_count)



