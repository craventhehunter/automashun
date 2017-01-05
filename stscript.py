import json
import string

def process_json(filename):
    with open(filename, 'r') as fp:
        raw_string = fp.read()
        mtu_dicts = {}
        for line in raw_string.splitlines():
         if ':"mtu"' in line:
          mtu_values = json.loads(line).get("v")
          print mtu_values
         if '"server_mtu"' in line:
          smtu_values = json.loads(line).get("v")
          print smtu_values


if __name__ == "__main__":
    process_json('practice_data.json')
