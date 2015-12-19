from .partials import *


DEBUG = False

ALLOWED_HOSTS = [
    '*',
]


# Static/Media File Management

DEFAULT_FILE_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
STATICFILES_STORAGE = 'okwarning.storage.S3PipelineManifestStorage'

STATIC_URL = 'https://derlz5b7zq0xp.cloudfront.net/'


# AWS Credentials

AWS_ACCESS_KEY_ID = os.environ["AWS_ACCESS_KEY_ID"]
AWS_SECRET_ACCESS_KEY = os.environ["AWS_SECRET_ACCESS_KEY"]
AWS_STORAGE_BUCKET_NAME = os.environ["AWS_STORAGE_BUCKET_NAME"]
