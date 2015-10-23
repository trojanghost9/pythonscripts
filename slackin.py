import requests
import json
	
payload = {'payload': json.dumps({
        'channel': '#queue_bot_test',
        'username': 'somecoolusername',
        'text': "this is a test",
    })
}

requests.post("https://hooks.slack.com/services/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", data=payload)
