from datetime import datetime

timestamp = lambda t: \
lambda:\
print(f'[{datetime.now().strftime("%H:%M:%S")}] {t}')