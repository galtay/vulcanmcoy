import pandas

class CcsFile():
    def __init__(self, target, year=2017):
        fname = '{year}/ccs_dx_icd10{target}_{year}.csv'.format(
            target=target, year=year)
        df = pandas.read_csv(fname)
        df.columns = df.columns.str.replace("'",'')
        for col in [
                'ICD-10-CM CODE', 'CCS CATEGORY', 'MULTI CCS LVL 1',
                'MULTI CCS LVL 2']:
            df[col] = df[col].str.replace("'",'')
        self._df = df


if __name__ == '__main__':

    ccs_file = CcsFile('cm')
