web: sh -c 'cd ersteops && gunicorn ersteops.wsgi:application'

web: daphne ./ersteops/ersteops.asgi:channel_layer --port 8000 --bind 0.0.0.0 -v2
worker: python ./ersteops/manage.py runworker -v2