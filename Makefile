dep-deb:
	# Deb install
	apt update
	apt install python3-pip
	apt install cython3 python3-dev
	apt install libsdl2-dev libsdl2-ttf-dev libsdl2-image-dev libsdl2-mixer-dev

dep-py:
	# Whl install
	python3 -m pip install --upgrade pip
	pip3 install -r requirements.txt

dev: dep-deb dep-py
	echo 'Installed!'

lint:
	find . -type f -name "*.py" | xargs pylint --rcfile=pylint.rc

test:
	echo 'Run tests'

clean:
	echo 'Cleanup'
