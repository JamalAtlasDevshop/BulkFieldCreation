import xml.etree.ElementTree as ET
from utils import *

def generateXml(fieldDetails):
    fieldDetails = setFieldDetailsDefaultValues(fieldDetails)
    if validateFieldDetails(fieldDetails) != 'Valid':
        return validateFieldDetails(fieldDetails)
    if fieldDetails.get('Type').lower() == 'text':
        return generateTextFieldXml(fieldDetails)
    elif fieldDetails.get('Type').lower() == 'date':
        return generateDateFieldXml(fieldDetails)
    elif fieldDetails.get('Type').lower() == 'number':
        return generateNumberFieldXml(fieldDetails)
    elif fieldDetails.get('Type').lower() == 'checkbox':
        return generateCheckboxFieldXml(fieldDetails)
    return 'Unsupported Field Type'



def generateTextFieldXml(fieldDetails):
    with open(r'.\XMLTemplates\Text.template.xml', 'r') as file:
        template_xml = file.read()

    template_xml = template_xml.replace('{{fullName}}', str(fieldDetails.get('Name')+'__c'))
    template_xml = template_xml.replace('{{externalId}}', str(fieldDetails.get('External Id')))
    template_xml = template_xml.replace('{{label}}', str(fieldDetails.get('Label')))
    template_xml = template_xml.replace('{{length}}', str(fieldDetails.get('Length')))
    template_xml = template_xml.replace('{{required}}', BoolToStr(fieldDetails.get('Required')))
    template_xml = template_xml.replace('{{unique}}', BoolToStr(fieldDetails.get('Unique')))
    template_xml = template_xml.replace('{{description}}', fieldDetails.get('Description'))
    template_xml = template_xml.replace('{{inlineHelpText}}', str(fieldDetails.get('Help Text')))



    with open(getObjectPath(fieldDetails.get('Object Api Name'))+'/'+fieldDetails.get('Name')+'__c.field-meta.xml', 'w') as file:
        file.write(template_xml)
    return 'Created Successfully'

def generateDateFieldXml(fieldDetails):
    with open(r'C:\Users\pc\Desktop\Python\XMLTemplates\Date.template.xml', 'r') as file:
        template_xml = file.read()

    template_xml = template_xml.replace('{{fullName}}', str(fieldDetails.get('Name')+'__c'))
    template_xml = template_xml.replace('{{label}}', str(fieldDetails.get('Label')))
    template_xml = template_xml.replace('{{required}}', BoolToStr(fieldDetails.get('Required')))
    template_xml = template_xml.replace('{{description}}', str(fieldDetails.get('Description')))
    template_xml = template_xml.replace('{{inlineHelpText}}', str(fieldDetails.get('Help Text')))

    with open(getObjectPath(fieldDetails.get('Object Api Name'))+'/'+fieldDetails.get('Name')+'__c.field-meta.xml', 'w') as file:
        file.write(template_xml)
    return 'Created Successfully'

def generateNumberFieldXml(fieldDetails):
    with open(r'C:\Users\pc\Desktop\Python\XMLTemplates\Number.template.xml', 'r') as file:
        template_xml = file.read()

    template_xml = template_xml.replace('{{fullName}}', str(fieldDetails.get('Name')+'__c'))
    template_xml = template_xml.replace('{{description}}', str(fieldDetails.get('Description')))
    template_xml = template_xml.replace('{{externalId}}', BoolToStr(fieldDetails.get('External Id')))
    template_xml = template_xml.replace('{{inlineHelpText}}', str(fieldDetails.get('Help Text')))
    template_xml = template_xml.replace('{{label}}', str(fieldDetails.get('Label')))
    template_xml = template_xml.replace('{{required}}', BoolToStr(fieldDetails.get('Required')))
    template_xml = template_xml.replace('{{scale}}', str(fieldDetails.get('Scale')))
    template_xml = template_xml.replace('{{unique}}', BoolToStr(fieldDetails.get('Unique')))

    with open(getObjectPath(fieldDetails.get('Object Api Name'))+'/'+fieldDetails.get('Name')+'__c.field-meta.xml', 'w') as file:
        file.write(template_xml)
    return 'Created Successfully'


def generateCheckboxFieldXml(fieldDetails):
    with open(r'C:\Users\pc\Desktop\Python\XMLTemplates\Checkbox.template.xml', 'r') as file:
        template_xml = file.read()

    template_xml = template_xml.replace('{{fullName}}', str(fieldDetails.get('Name')+'__c'))
    template_xml = template_xml.replace('{{description}}', str(fieldDetails.get('Description')))
    template_xml = template_xml.replace('{{inlineHelpText}}', str(fieldDetails.get('Help Text')))
    template_xml = template_xml.replace('{{label}}', str(fieldDetails.get('Label')))
    template_xml = template_xml.replace('{{required}}', BoolToStr(fieldDetails.get('Required')))

    with open(getObjectPath(fieldDetails.get('Object Api Name'))+'/'+fieldDetails.get('Name')+'__c.field-meta.xml', 'w') as file:
        file.write(template_xml)
    return 'Created Successfully'