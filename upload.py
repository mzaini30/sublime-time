import time, os

git = """git status
git add -A .
git commit -m "oke"
git push"""

while True:
	os.system(git)
	print
	time.sleep(180)