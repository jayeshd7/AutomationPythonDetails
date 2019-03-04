import json

value  = json.dumps({'4': 5, '6': 7}, sort_keys=True,
                indent=4, separators=(',', ': '))

print(value)