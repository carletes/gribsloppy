all: pyflakes pep8

pyflakes:
	pyflakes gribsloppy

pep8:
	pep8 gribsloppy

pylint:
	pylint gribsloppy 2>&1 | tee pylint.log

TESTS=

check: all
	nosetests \
		--with-coverage \
		--cover-package=gribsloppy \
		--cover-branch \
		--cover-tests \
		--cover-inclusive \
		--cover-erase \
		--cover-html \
		--cover-html-dir=coverage-html \
		$(TESTS)

clean:
	-git clean -dXf
