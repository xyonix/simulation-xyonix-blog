BUILD_DIR := $(shell pwd)/build
XYONIX_KERNEL=xyonix-text-simulation
VENV_DIR := ${BUILD_DIR}/venv/${XYONIX_KERNEL}

all: clean install run-jupyter

install-venv: ${VENV_DIR}/bin/activate

${VENV_DIR}/bin/activate: requirements.txt
	test -d "${VENV_DIR}" || python3 -m venv ${VENV_DIR}
	. ${VENV_DIR}/bin/activate; pip install -Ur requirements.txt
	@touch ${VENV_DIR}/bin/activate

clean:
	@rm -rf ${BUILD_DIR} __pycache__
	@rm -f nbeats-pytorch

install: install-venv

jupyter-kernel: install-venv
	${VENV_DIR}/bin/ipython kernel install --user --name=${XYONIX_KERNEL}

run-jupyter: jupyter-kernel
	${VENV_DIR}/bin/jupyter notebook simulation-xyonix-blog.ipynb

lint:
	${VENV_DIR}/bin/pylint *.py


