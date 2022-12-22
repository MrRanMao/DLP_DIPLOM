from django.db import models
from uuid import uuid4
import random
import string

def random_phase():
	return ''.join(random.choice(string.ascii_lowercase + string.ascii_uppercase + '1234567890') for i in range(8))

class FileHash(models.Model):
	uuid = models.UUIDField(default=uuid4)
	hash = models.CharField(max_length=64)

	def __str__(self):
		return str(self.uuid)

class User(models.Model):
	uuid = models.UUIDField(default=uuid4)
	key_phase = models.CharField(max_length=8, default=random_phase)

	def __str__(self):
		return str(self.uuid)

class EventHashLog(models.Model):
	uuid = models.UUIDField(default=uuid4)
	hash = models.ForeignKey(FileHash, on_delete=models.CASCADE)

	time = models.DateTimeField(auto_now=True)

	def __str__(self):
		return str(self.uuid)
