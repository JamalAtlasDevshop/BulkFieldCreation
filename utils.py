import os
import re
import pandas as pd

def createDirIfNotExists(dirpath):
    if not os.path.exists(dirpath):
        os.makedirs(dirpath)

def getObjectPath(objectApiName):
    dirpath = r'force-app\main\default\objects\\'+objectApiName+r'\fields'
    createDirIfNotExists(dirpath)
    return dirpath


def validateAPIName(APIName):
    pattern = r'^[a-zA-Z0-9_]+$'
    if re.match(pattern, APIName):
        return True
    else:
        return False


def validateFieldDetails(fieldDetails):
    if pd.isna(fieldDetails.get('Label')):
        return 'Label is required'
    if pd.isna(fieldDetails.get('Name')):
        return 'Name is required'
    if not validateAPIName(fieldDetails.get('Name')):
        return 'Name should contain only [A-Z, a-z, 0-9, _]'
    if pd.isna(fieldDetails.get('Object Api Name')):
        return 'Object Api Name is required'
    if pd.isna(fieldDetails.get('Type')):
        return 'Type is required'
    if fieldDetails.get('Type') == 'Text':
        if not str(fieldDetails.get('Length')).isdigit() :
            return 'Length should be a number'
        if int(fieldDetails.get('Length')) > 255:
            return 'Length should be less than or equal to 255'
    if fieldDetails.get('Type') == 'Number':
        if not str(fieldDetails.get('Scale')).isdigit():
            return 'Scale should be a number'
    return 'Valid'


def BoolToStr(value):
    if value in ['true', 'True', 'TRUE', True, '1', 1,'yes','Yes','YES']:
        return 'TRUE'
    else:
        return 'FALSE'

def setFieldDetailsDefaultValues(fieldDetails):
    if pd.isna(fieldDetails.get('External Id')):
        fieldDetails['External Id'] = 'FALSE'
    if pd.isna(fieldDetails.get('Required')):
        fieldDetails['Required'] = 'FALSE'
    if pd.isna(fieldDetails.get('Unique')):
        fieldDetails['Unique'] = 'FALSE'
    if pd.isna(fieldDetails.get('Help Text')):
        fieldDetails['Help Text'] = ''
    if pd.isna(fieldDetails.get('Description')):
        fieldDetails['Description'] = ''
    if pd.isna(fieldDetails.get('Length')):
        fieldDetails['Length'] = '255'
    if pd.isna(fieldDetails.get('Scale')):
        fieldDetails['Scale'] = '2'
    else:
        fieldDetails['Scale'] = str(int(fieldDetails.get('Scale')))
    return fieldDetails
