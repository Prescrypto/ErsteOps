web: sh -c 'cd ersteops && daphne ersteops.asgi:application --port $PORT --bind 0.0.0.0 -v2'
worker: python ./ersteops/manage.py runworker channels -v 2
