from mitmproxy import http
from mitmproxy import ctx
import mitmproxy
import hashlib
import requests

class FileHandler:
	API_CHECK_HASH = 'http://127.0.0.1:8000/api/v1/hash/check/'

	def request(self, flow: http.HTTPFlow) -> None:
		if flow.request.method == "POST":
			data = flow.request.content.decode()
			if 'filename=' in data:
				data = data.split('filename="')[1]
				data = data.split("\r\n\r\n")[1]
				data = data.split("\r\n--------")[0]
				print(f"Hash: {hashlib.sha256(data.encode()).hexdigest()}")
			else:
				print(f"Hash: {hashlib.sha256(data.encode()).hexdigest()}")

			response = requests.get(self.API_CHECK_HASH + hashlib.sha256(data.encode()).hexdigest())
			if response.status_code == 200:
				print(f"Data blocked: {hashlib.sha256(data.encode()).hexdigest()}")
				banner = "########################################################\n"
				banner += "########################################################\n"
				banner += "#####                                              #####\n"
				banner += "#####          CONTENT IS BLOCKED BY DLP           #####\n"
				banner += "#####                                              #####\n"
				banner += "########################################################\n"
				banner += "########################################################\n"
				full_data = flow.request.content.decode()
				full_data = full_data.replace(data, banner)
				flow.request.content = full_data.encode()
			else:
				print(f"Data passed: {hashlib.sha256(data.encode()).hexdigest()}")

	def response(self, flow: http.HTTPFlow) -> None:
		pass

addons = [FileHandler()]
