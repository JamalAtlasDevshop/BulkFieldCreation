import pandas as pd
import xml.etree.ElementTree as ET
from datetime import datetime
from generateXML import *




file_path = r'C:\Users\pc\Atlas Devshop Dropbox\Client Documents\Respectability\Piscatway - Temp\familyfields.csv'
df = pd.read_csv(file_path)

# add a column to store the creation status in the success and failure dataframes
df['Creation Status'] = ''
df_failure = pd.DataFrame(columns=df.columns)
df_success = pd.DataFrame(columns=df.columns)


for index, row in df.iterrows():
    fieldDetails = row.to_dict()
    creationStatus = generateXml(fieldDetails)
    row['Creation Status'] = creationStatus
    if creationStatus == 'Created Successfully':
        df_success = pd.concat([df_success, pd.DataFrame([row])], ignore_index=True)
    else:
        df_failure = pd.concat([df_failure, pd.DataFrame([row])], ignore_index=True)




createDirIfNotExists('BulkFieldCreationResult')
df_failure.to_csv('BulkFieldCreationResult/error_'+datetime.now().strftime("%Y-%m-%d_%H-%M-%S")+'.csv', index=False)
df_success.to_csv('BulkFieldCreationResult/success_'+datetime.now().strftime("%Y-%m-%d_%H-%M-%S")+'.csv', index=False)



