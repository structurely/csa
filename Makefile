status=dev
OBJS = $(wildcard csa/*.py)

.PHONY: build
build: $(OBJS)
	python setup.py install

.PHONY: clean
clean:
	find . | grep -E "(__pycache__|\.pyc|\.o|\.so|\.pyo$$)" | xargs rm -rf
	rm -rf build/
	rm -rf dist/
	rm -rf pycsa.egg-info/
	rm -rf .cache/
	rm -rf examples/.ipynb_checkpoints/

.PHONY: create-branch
create-branch:
	git checkout -b CSA-$(num) dev
	git push --set-upstream origin CSA-$(num)

.PHONY: delete-branch
delete-branch:
	git push origin --delete CSA-$(num)
	git branch -d CSA-$(num)

.PHONY: force-delete
force-delete:
	git push origin --delete CSA-$(num)
	git branch -D CSA-$(num)

.PHONY: pypi-upload
pypi-upload:
	rm -rf dist/
	python setup.py sdist
	python setup.py bdist_wheel
	twine upload dist/*

.PHONY: help
help:
	@echo "    clean"
	@echo "        Remove python artifacts."
	@echo ""
	@echo "    build"
	@echo "        Build module and install locally."
	@echo ""
	@echo "    create-branch"
	@echo "        Create new branch off of dev and push to GitHub."
	@echo "        Ex: (creates a new branch CSA-17)"
	@echo "        > make create-branch num=17"
	@echo ""
	@echo "    delete-branch"
	@echo "        Delete branch from GitHub and locally."
	@echo "        Ex: (deletes branch CSA-17)"
	@echo "        > make delete-branch num=17"
	@echo ""
	@echo "    force-delete"
	@echo "        Delete branch from GitHub and force delete locally."
	@echo "        Ex: (deletes branch CSA-17)"
	@echo "        > make force-delete num=17"
	@echo ""
	@echo "    pypi-upload"
	@echo "        Upload the package to PyPI."
