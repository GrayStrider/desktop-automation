from util import timestamp
from toolz import pipe

flow = lambda *funcs: lambda data: pipe(data, *funcs)

capitalize_I = lambda t: t.replace(' i ', ' I ')

prettify = flow(
capitalize_I

)

def process(text, commands):
	keys = tuple(commands)
	text = text.lower()

	for key in keys:
		if text.startswith(key):
			rest = text.replace(key, '').strip()
			timestamp(f'Recognized <{key}>\n')()  

			processed = commands[key](rest)

			# walrus
			if processed:
				text = processed
			else:
				text = rest

	return prettify(text)