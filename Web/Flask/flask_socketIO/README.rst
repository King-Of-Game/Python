# run
python main.py

gunicorn -b 0.0.0.0:8888 -k eventlet --workers=1 main:app