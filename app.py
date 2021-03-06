import json
import io
import requests
from flask import Flask,render_template
from flask_socketio import SocketIO,emit
from time import sleep

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)


obj = {"name":"Alexander","value":"Y"}

def mock_gemma_mapping():
	results = requests.get("http://genenetwork.org/api/v_pre1/mapping?trait_id=10015&db=BXDPublish&method=gemma&use_loco=true")

	mapping_obj = json.loads(results.content)

	yield mapping_obj


def string_io_converter():
	length = len(json.dumps(obj))
	string_stream = io.StringIO(json.dumps(obj))
	return string_stream,length


@socketio.on('messenger')
def test_connect():

	# string_stream,length = string_io_converter()
	gemma_results = mock_gemma_mapping()

	string_io_data = io.StringIO(gemma_results)
	while True:
		print(string_io_data)
		data = string_io_data.read(1)
		if data =="":
			break

		
		emit("response",{'data':data})
		# sleep(0.1)


	# while length>string_stream.tell():
	# 	data = string_stream.read(1)
	# 	print(data)
	# 	emit("response",{'data':data})
	# 	sleep(0.1)


@socketio.on("gemma")
def gemma():
	print("my name is alexis")

@app.route("/")
def home():
	return render_template("index.html")

if __name__ == '__main__':
	app.run(debug=True)

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


