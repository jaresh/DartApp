dev:
	# Deb install
	apt install python3-pip
	apt-get install cython3 python3-dev
	apt-get install libsdl2-dev libsdl2-ttf-dev libsdl2-image-dev libsdl2-mixer-dev

	# Whl install
	pip3 install pylint
	pip3 install pytest
	pip3 install git+https://github.com/kivy/kivy.git@master
	pip3 install pygame

lint:
	find . -type f -name "*.py" | xargs pylint   

test:
	echo 'Run tests'

clean:
	echo 'Cleanup'
