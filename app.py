import json
import io

obj = {"name":"Alexander","value":"Y"}
results = json.dumps(obj).encode("utf-8")
byte_results = io.BytesIO(results)
counter = 0 
rk = ""
while counter<10:

	# print(byte_results.read(1).decode("utf-8"))
	rk+=byte_results.read(1).decode("utf-8")
	print(rk)
	counter+=1

# trying using stringio


# find length of the data
y = len(json.dumps(obj))

string_stream = io.StringIO(json.dumps(obj))
# print(string_stream)
string_stream.read(1)
string_counter = 0
while y > string_counter:
	print(string_stream.read(1))
	string_counter+=1
