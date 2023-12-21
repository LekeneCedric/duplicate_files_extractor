MAIN_FILE_PATH = app/src

setup: requirements.txt
	pip install -r requirements.txt

run:
	python3 $(MAIN_FILE_PATH)/main.py

install:
	sudo apt-get update
	sudo apt-get install python3

clean:
	rm $(MAIN_FILE_PATH)/output.txt


