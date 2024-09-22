.PHONY: all run_notebook run_data_py run_dzn_py

# Tüm adımları çalıştıran kural
all: run_notebook run_data_py run_dzn_py

# Jupyter notebook'u çalıştıran kural
run_notebook:
	jupyter nbconvert --to notebook --execute Untitled.ipynb

# data.py'yi çalıştıran kural
run_data_py:
	python3 Data/txt_files/data.py

# dzn.py'yi çalıştıran kural
run_dzn_py:
	python3 Data/dzn.py

