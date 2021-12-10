# Salary Prediction App On Docker

To run locally using Docker:
`docker run -it salary-predictor python3 predict_salary.py`

To run model API using Docker:
`docker run -p 5000:5000 -it salary-predictor python3 app.py`