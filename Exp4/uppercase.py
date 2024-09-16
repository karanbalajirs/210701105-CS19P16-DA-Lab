def uppercase(text):
	return text.upper()
if __name__ == "__main__":
	import sys
	for line in sys.stdin:
		line = line.strip()
		result = uppercase(line)
		print(result)
