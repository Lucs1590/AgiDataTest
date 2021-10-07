# AgiTest
This is a repository with data analysis and data science tests.

## Prerequisites
As a prerequisite for the execution of this project, the following are cited:
  - Python >= 3

Thus, the installation of prerequisites can be performed from the command:
```bash
pip install -r requirements.txt
```
Or through a conda environment, running:
```bash
count env create -f environment.yml
```

## Data Science Test
This test is related to the validation of the response rate of a given list composed of groups that supposedly were hired or not in a company.

To run the unit tests for this exercise, run:

```bash
python -m unittest tests/test_main.py
```

To check the functions documentation, run:
```bash
python -m pydoc src/main.py
```

Finally, to view the script execution, run:
```bash
python src/main.py
```