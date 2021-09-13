FROM continuumio/miniconda3

# activate conda enviorment
RUN /bin/sh -c conda activate base
WORKDIR /g1g_portal
COPY requirements.txt .
RUN pip install -r requirements.txt


ENV CONDA_PACKAGES="\
    anaconda::pyodbc"

RUN conda install $CONDA_PACKAGES

# Flask configurations
ENV FLASK_CONFIG='development'
ENV PATH=$FLASK_CONFIG:$PATH

ENV FLASK_APP=run.py

