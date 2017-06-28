status=dev

build:
	python setup.py build_ext --inplace

clean:
	find . | grep -E "(__pycache__|\.pyc|\.o|\.so|\.pyo$$)" | xargs rm -rf
	rm -rf build/
	rm -rf dist/

create-branch:
	git checkout -b CSA-$(num) dev
	git push --set-upstream origin CSA-$(num)

delete-branch:
	git push origin --delete CSA-$(num)
	git branch -d CSA-$(num)

force-delete:
	git push origin --delete CSA-$(num)
	git branch -D CSA-$(num)

pypi-upload:
	rm -rf dist/
	python setup.py bdist_wheel
	twine upload dist/*

.PHONY: clean build create-branch delete-branch force-delete pypi-upload
