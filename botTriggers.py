BOT_DICTIONARY = {
    'triggers': [
        {
            'trigger': ['add vlan'],
            'action': 'ADD VLAN',
            'response': 'Adding VLAN...'

        },
        {
            'trigger': ['add ap', 'create ap', 'mac'],
            'action': 'ADD AP',
            'response': 'Adding AP...'

        },
        {
            'trigger': ['hi', 'hello', 'how are you'],
            'action': 'none',
            'response': 'Hi there!'

        },
        {
            'trigger': ['are you hungry'],
            'action': 'none',
            'response': 'I never eat nor sleep, I just sit here waiting to talk to you'

        }
    ],

    'defaults': {
        'action': 'none',
        'response': 'Sorry, I do not understand your request'
    }
}
