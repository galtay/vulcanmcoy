import os
import pandas

path_here = os.path.dirname(__file__)

class Icd10cmCodesFile():
    """The ICD-10-CM codes file contains all valid codes and their long
    descriptions.
    """
    COL_NAMES = ['code', 'long_description']
    def __init__(self, year=2017):
        fname=(
            '{path_here}/{year}/code_descriptions/icd10cm_codes_{year}.txt'
            .format(path_here=path_here, year=year))
        self.fname = fname
        self._df = pandas.read_fwf(fname, header=None, names=self.COL_NAMES)
    def return_codes(self):
        return self._df


class Icd10cmOrderFile():
    """The ICD-10-CM order file contains a unique "order number" for each valid
    code or header, a flag distinguishing valid codes from headers, and both
    long and short descriptions.
    """
    COL_NAMES = [
        'order_num', 'code', 'code_flag', 'short_description',
        'long_description']
    def __init__(self, year=2017):
        fname=(
            '{path_here}/{year}/code_descriptions/icd10cm_order_{year}.txt'
            .format(path_here=path_here, year=year))
        self.fname = fname
        self._df = pandas.read_fwf(fname, header=None, names=self.COL_NAMES)
    def return_codes(self):
        bmask = self._df['code_flag']==1
        return self._df.loc[bmask, :]
    def return_headers(self):
        bmask = self._df['code_flag']==0
        return self._df.loc[bmask, :]



if __name__ == '__main__':
    icd10cm_codes_file = Icd10cmCodesFile()
    codes = icd10cm_codes_file.return_codes()

    icd10cm_order_file = Icd10cmOrderFile()
    order_codes = icd10cm_order_file.return_codes()
    order_headers = icd10cm_order_file.return_headers()
