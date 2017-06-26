build:
	python setup.py build_ext --inplace

clean:
	find . | grep -E "(__pycache__|\.pyc|\.o|\.so|\.pyo$$)" | xargs rm -rf
	rm -rf build

.PHONY: clean build
