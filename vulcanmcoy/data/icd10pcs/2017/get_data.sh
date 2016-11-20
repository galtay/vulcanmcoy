wget -nc https://www.cms.gov/Medicare/Coding/ICD10/Downloads/2017-New-Procedure-Codes.zip
wget -nc https://www.cms.gov/Medicare/Coding/ICD10/Downloads/2017-PCS-Long-Abbrev-Titles.zip
wget -nc https://www.cms.gov/Medicare/Coding/ICD10/Downloads/2017-PCS-Code-Tables.zip
wget -nc https://www.cms.gov/Medicare/Coding/ICD10/Downloads/2017-GEM-PCS.zip
wget -nc https://www.cms.gov/Medicare/Coding/ICD10/Downloads/2017-Official-ICD-10-PCS-Coding-Guidelines.pdf

unzip -o -d code_descriptions 2017-New-Procedure-Codes.zip
unzip -o -d code_descriptions 2017-PCS-Long-Abbrev-Titles.zip
unzip -o -d code_tables_index 2017-PCS-Code-Tables.zip
unzip -o -d gems 2017-GEM-PCS.zip
