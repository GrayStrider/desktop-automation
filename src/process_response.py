from util import timestamp

def process(text, commands):
    keys = tuple(commands)

    for key in keys:
        if text.startswith(key):
            rest = text.replace(key, '').strip()
            timestamp(f'Recognized <{key}>')()
            commands[key](rest)
            return rest

    return text