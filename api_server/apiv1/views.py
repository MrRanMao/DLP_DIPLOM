from django.shortcuts import render
from django.http import JsonResponse
from backend.models import FileHash, User, EventHashLog
from django.views.decorators.csrf import csrf_exempt
import json

def write_event_hash_log(hash):
	event = EventHashLog()
	event.hash = FileHash.objects.get(hash=hash)
	event.save()

@csrf_exempt
def auth_check(request):
	if request.method == 'POST':
		print(request.body)
		data = json.loads(request.body)
		if 'uuid' in data.keys() and 'key' in data.keys():
			if User.objects.filter(uuid=data.get('uuid')).filter(key_phase=data.get('key')).exists():
				return JsonResponse({
					'status': 'success',
					'message': 'You are successfuly authorized.'
				}, status=201)
	return JsonResponse({
		'status': 'error',
		'message': 'You are not authorized'
	}, status=401)


@csrf_exempt
def add_hash_view(request):
	if request.method == 'POST':
		data = json.loads(request.body)
		hash = ''
		if 'hash' in data.keys() and 'uuid' in data.keys() and 'key' in data.keys():
			try:
				if User.objects.filter(uuid=data.get('uuid')).filter(key_phase=data.get('key')).exists():
					if not FileHash.objects.filter(hash=data.get('hash')).exists():
						file_hash = FileHash()
						file_hash.hash = data.get('hash')
						file_hash.save()

						return JsonResponse({
							'status': 'success',
							'message': 'Hash is successfuly added to database.'
						}, status=201)
					return JsonResponse({
						'status': 'error',
						'message': 'Hash is exists in database.'
					}, status=409)
				return JsonResponse({
					'status': 'error',
					'message': 'You are not authorized'
				}, status=401)
			except:
				return JsonResponse({
					'status': 'error',
					'message': 'Bad request'
				}, status=400)

		return JsonResponse({
			'status': 'error',
			'message': 'Bad request'
		}, status=400)
	return JsonResponse({
		'status': 'error',
		'message': f'{request.method} method not allowed'
	}, status=405)

@csrf_exempt
def del_hash_view(request):
	if request.method == 'POST':
		data = json.loads(request.body)
		hash = ''
		if 'hash' in data.keys() and 'uuid' in data.keys() and 'key' in data.keys():
			try:
				if User.objects.filter(uuid=data.get('uuid')).filter(key_phase=data.get('key')).exists():
					if FileHash.objects.filter(hash=data.get('hash')).exists():
						file_hash = FileHash.objects.filter(hash=data.get('hash'))[0]
						file_hash.delete()

						return JsonResponse({
							'status': 'success',
							'message': 'Hash is successfuly removed from database.'
						}, status=201)
					return JsonResponse({
						'status': 'error',
						'message': 'Hash does not exists in database.'
					}, status=409)
				return JsonResponse({
					'status': 'error',
					'message': 'You are not authorized'
				}, status=401)
			except:
				return JsonResponse({
					'status': 'error',
					'message': 'Bad request'
				}, status=400)
		return JsonResponse({
			'status': 'error',
			'message': 'Bad request'
		}, status=400)
	return JsonResponse({
		'status': 'error',
		'message': f'{request.method} method not allowed'
	}, status=405)

@csrf_exempt
def check_hash_view(request, hash=None):
	if request.method == 'GET':
		if hash == None:
			return JsonResponse({
				'status': 'error',
				'message': 'Bad request'
			}, status=400)
		if FileHash.objects.filter(hash=hash).exists():
			write_event_hash_log(hash)
			return JsonResponse({
				'status': 'success',
				'message': 'Hash is exists in database.'
			}, status=200)
		return JsonResponse({
			'status': 'error',
			'message': 'Hash does not in database.'
		}, status=404)
	return JsonResponse({
		'status': 'error',
		'message': f'{request.method} method not allowed'
	}, status=405)

	if request.method == 'POST':
		data = json.loads(request.body)
		hash = ''
		if 'hash' in data.keys() and 'uuid' in data.keys() and 'key' in data.keys():
			try:
				if User.objects.filter(uuid=data.get('uuid')).filter(key_phase=data.get('key')).exists():
					if FileHash.objects.filter(hash=data.get('hash')).exists():
						write_event_hash_log(data.get('hash'), data.get('uuid'))
						return JsonResponse({
							'status': 'success',
							'message': 'Hash is exists in database.'
						}, status=200)
					return JsonResponse({
						'status': 'error',
						'message': 'Hash does not in database.'
					}, status=404)
				return JsonResponse({
					'status': 'error',
					'message': 'You are not authorized'
				}, status=401)
			except:
				return JsonResponse({
					'status': 'error',
					'message': 'Bad request'
				}, status=400)
		return JsonResponse({
			'status': 'error',
			'message': 'Bad request'
		}, status=400)
	return JsonResponse({
		'status': 'error',
		'message': f'{request.method} method not allowed'
	}, status=405)

