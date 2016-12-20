import json
import string

def process_json(filename):
    with open(filename, 'r') as fp:
        raw_string = fp.read()
        replaced_string = raw_string.replace('}\n{', '},\n{')
        s = "[" + replaced_string + "]"
        streamdata = json.loads(s)
        s1 = streamdata['list']
        #s = str(streamdata)
        all_data = open("json_output.txt", "w")
        all_data.write(s1)
        all_data.close()		
        #for info in streamdata:
            #if ['v'] in streamdata > 1:
        print s1[0]
             #print error

		
if __name__ == "__main__":
    process_json('practice_data.json')
