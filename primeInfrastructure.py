# Add Prime API call here
import base64
import json

import requests

from settings import CONFIG, create_config_vlan_model

'''
API Call to Prime Infrastructure 
Provide the VLAN ID and the target device ID
returns a fail or the Prime UID for the scheduled task
'''


def create_vlan(vlan_id, target_device=CONFIG['TARGET_DEVICE']):
    temp = json.dumps(create_config_vlan_model(vlan_id, target_device))

    userCredentials = CONFIG['PRIME_USERNAME'] + ':' + CONFIG['PRIME_PASSWORD']
    b64Val = base64.b64encode(userCredentials)

    apiHeader = {'Authorization': 'Basic %s' % b64Val, 'Content-Type': 'application/json'}

    resp = requests.put(url=CONFIG['PRIME_URL'] + '/webacs/api/v1/op/cliTemplateConfiguration/deployTemplateThroughJob',
                        data=temp, headers=apiHeader, verify=False)
    if resp.status_code == 200:
        response = 'Success, ticket number'
    else:
        response = 'Fail'
    return response
