.PHONY: all run_notebook run_data_py run_dzn_py
all: run_notebook run_data_py run_dzn_py
run_notebook:
	jupyter nbconvert --to notebook --execute Untitled.ipynb
run_data_py:
	python3 Data/txt_files/data.py
run_dzn_py:
	python3 Data/dzn.py
