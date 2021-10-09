# AgiTest
This is a repository with data analysis and programming tests.

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

## Programming Test
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

## Data Analysis Test
The second test is related to exploring financial inclusion data from Africa. You can access it by opening `financial_incusion_africa.ipynb` or by going to the following link:
 - https://colab.research.google.com/drive/1qGBj2B4z3yQqteYGUQFgmF12N7kCRJki?usp=sharing