# custom_storages.py
from django.conf import settings
#from storages.backends.s3boto import S3BotoStorage
from storages.backends.s3boto3 import S3Boto3Storage

# class StaticStorage(S3BotoStorage):
#     location = settings.STATICFILES_LOCATION

class MediaStorage(S3BotoStorage):
        location = settings.MEDIAFILES_LOCATION