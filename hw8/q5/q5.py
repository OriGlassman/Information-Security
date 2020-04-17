import subprocess
import time
import json


with open("example.json") as json_file:
	orig_json = json.load(json_file)

with open("whatever.json", "w") as json_file:
	json.dump(orig_json, json_file)

p = subprocess.Popen(['python', 'run.py', 'whatever.json'])
time.sleep(2)
file = open("whatever.json", "w")
orig_json['command'] = 'echo hacked'
json.dump(orig_json, file)
file.close()

p.wait()
orig_json['command'] = 'echo cool'
with open("whatever.json", "w") as ret_to_orig_state_fp:
	json.dump(orig_json, ret_to_orig_state_fp)