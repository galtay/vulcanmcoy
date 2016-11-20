import os
import pandas

path_here = os.path.dirname(__file__)

class CcsFile():
    def __init__(self, target, year=2017):
        if target not in ['cm', 'pcs']:
            raise ValueError('target must be one of ["cm", "pcs"]')
        fname = '{path_here}/{year}/ccs_dx_icd10{target}_{year}.csv'.format(
            path_here=path_here, target=target, year=year)
        df = pandas.read_csv(fname)
        df.columns = df.columns.str.replace("'",'')
        for col in [
                'ICD-10-CM CODE', 'CCS CATEGORY', 'MULTI CCS LVL 1',
                'MULTI CCS LVL 2']:
            df[col] = df[col].str.replace("'",'')
        self._df = df
    def return_codes(self):
        return self._df

if __name__ == '__main__':

    ccs_file = CcsFile('cm')
