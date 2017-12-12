web: sh -c 'cd ersteops && daphne ersteops.asgi:channel_layer --port $PORT --bind 0.0.0.0 -v2'
worker: python ./ersteops/manage.py runworker -v2
