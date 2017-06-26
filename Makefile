build:
	python setup.py build_ext --inplace

clean:
	find . | grep -E "(__pycache__|\.pyc|\.o|\.so|\.pyo$$)" | xargs rm -rf
	rm -rf build

create-branch:
	git checkout -b CSA-$(num) dev
	git push --set-upstream origin CSA-$(num)

delete-branch:
	git push origin --delete BRN-$(num)
	git branch -d BRN-$(num)

force-delete:
	git push origin --delete BRN-$(num)
	git branch -D BRN-$(num)

.PHONY: clean build create-branch delete-branch force-delete
