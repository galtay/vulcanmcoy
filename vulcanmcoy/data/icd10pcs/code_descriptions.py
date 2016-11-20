import pandas


class Icd10pcsCodesFile():
    """The ICD-10-PCS codes file contains all valid codes and their long
    descriptions.
    """
    COL_NAMES = ['code', 'long_description']
    def __init__(self, fname='2017/code_descriptions/icd10pcs_codes_2017.txt'):
        self.fname = fname
        self._df = pandas.read_fwf(fname, header=None, names=self.COL_NAMES)
    def return_codes(self):
        return self._df


class Icd10pcsOrderFile():
    """The ICD-10-PCS order file contains a unique "order number" for each valid
    code or header, a flag distinguishing valid codes from headers, and both
    long and short descriptions.
    """
    COL_NAMES = [
        'order_num', 'code', 'code_flag', 'short_description',
        'long_description']

    def __init__(self, fname='2017/code_descriptions/icd10pcs_order_2017.txt'):
        self.fname = fname
        self._df = pandas.read_fwf(fname, header=None, names=self.COL_NAMES)
    def return_codes(self):
        bmask = self._df['code_flag']==1
        return self._df.loc[bmask, :]
    def return_headers(self):
        bmask = self._df['code_flag']==0
        return self._df.loc[bmask, :]



if __name__ == '__main__':
    icd10pcs_codes_file = Icd10pcsCodesFile()
    codes = icd10pcs_codes_file.return_codes()

    icd10pcs_order_file = Icd10pcsOrderFile()
    order_codes = icd10pcs_order_file.return_codes()
    order_headers = icd10pcs_order_file.return_headers()
