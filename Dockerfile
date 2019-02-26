#Sample Notebook
FROM jupyter/minimal-notebook:7f1482f5a136
RUN pip install git+https://github.com/grading/gradememaybe.git
RUN pip install --no-cache-dir vdom==0.5
