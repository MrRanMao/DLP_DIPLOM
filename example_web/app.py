from sanic import Sanic, response

app = Sanic(name='example_web_upload')

@app.route("/", methods=['POST'])
async def home(request):
	return response.text(request.files['data'][0].body.decode())

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=8080, debug=True)
