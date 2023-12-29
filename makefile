
setup: requirements.txt
	pip install -r requirements.txt

run:
	python3 main.py

install:
	sudo apt-get update
	sudo apt-get install python3

clean:
	rm -rf app/src/actions/__pycache__
	rm -rf app/src/enums/__pycache__
	rm -rf app/src/models/__pycache__
	rm -rf app/src/tests/__pycache__
	rm output.txt


