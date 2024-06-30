all:
	python setup.py develop --user
	#python setup.py build_ext --inplace
clean:
	rm *.so pypowspec/*so pypowspec/src/pypowspec.c
