wget -nc https://www.cms.gov/Medicare/Coding/ICD10/Downloads/2017-ICD10-Code-Descriptions.zip
wget -nc https://www.cms.gov/Medicare/Coding/ICD10/Downloads/2017-ICD10-Code-Tables-Index.zip
wget -nc https://www.cms.gov/Medicare/Coding/ICD10/Downloads/2017-GEM-DC.zip
wget -nc https://www.cms.gov/Medicare/Coding/ICD10/Downloads/2017-ICD-10-CM-Guidelines.pdf

unzip -o -d code_tables_index 2017-ICD10-Code-Tables-Index.zip
unzip -o -d code_descriptions 2017-ICD10-Code-Descriptions.zip
unzip -o -d gems 2017-GEM-DC.zip
