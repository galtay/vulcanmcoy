from bs4 import BeautifulSoup
fname = '2017/code_tables_index/icd10cm_tabular_2017.xml'
with open(fname, 'r') as fp:
    soup = BeautifulSoup(fp, 'lxml')
