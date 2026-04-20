all: install test

install:
	pip install -r requirements.txt

test:
	python3 auto_brew.py --test-mode

clean:
	rm -rf __pycache__
	rm -f audit_log.txt
