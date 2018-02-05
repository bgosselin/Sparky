CONFIG = {
    'SPARK_URL': 'https://api.ciscospark.com',  # Spark cloud url
    'BOT_ID': '.....',  # Spark Bot ID
    'ROOM_ID': '.....',  # Spark room ID
    'BEARER': '.....',  # Bot token
    'PRIME_URL': '.....',  # Prime Infrastructure URL
    'TARGET_DEVICE': '.....',  # Switch device ID in Prime Infra
    'PRIME_TEMPLATE_NAME': '.....',  # Name of the template to call in Prime
    'PRIME_USERNAME': '.....',  # Username in Prime
    'PRIME_PASSWORD': '.....'  # Password in Prime

}


def create_config_vlan_model(vlan_id, target_device=CONFIG['TARGET_DEVICE']):
    primePayload = {
        "cliTemplateCommand": {
            "targetDevices": {
                "targetDevice": {
                    "targetDeviceID": target_device,
                    "variableValues": {
                        "variableValue": {
                            "name": "vlanid",
                            "value": vlan_id
                        }
                    }
                }
            },
            "templateName": CONFIG['PRIME_TEMPLATE_NAME']
        }
    }
    return primePayload
