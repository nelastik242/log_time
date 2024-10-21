import datetime
import time

while True:
	time_log = datetime.datetime.now()

	with open("log.txt", "w") as file:
		file.write(f"time now is {time_log}\n")

	with open("log.txt", "r") as file:
		print(file.read())
	time.sleep(2)
