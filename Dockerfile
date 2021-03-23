 FROM python:3

 ADD src /src

 #CMD [ "python", "./src/CalculatorTests.py"]

 CMD [ "python", "./src/CSVTests.py"]