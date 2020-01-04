dev:
	# Deb install
	apt install python3-pip
	apt-get install cython3 python3-dev
	apt-get install libsdl2-dev libsdl2-ttf-dev libsdl2-image-dev libsdl2-mixer-dev

	# Whl install
	pip install -r requirements.txt

lint:
	find . -type f -name "*.py" | xargs pylint --rcfile=pylint.rc

test:
	echo 'Run tests'

clean:
	echo 'Cleanup'
