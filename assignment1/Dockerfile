FROM  continuumio/miniconda3 as build
#creates and moves to myapp directory
WORKDIR /myapp
#copy files
COPY . /myapp
#create conda environment from env.yml
RUN conda env create -f env.yml && \
    conda install -c conda-forge conda-pack
# Use conda-pack to create a standalone enviornment
# in /venv:
RUN conda-pack -n env-h -o /tmp/env.tar && \
    mkdir /venv && cd /venv && tar xf /tmp/env.tar && \
    rm /tmp/env.tar 
RUN /venv/bin/conda-unpack

FROM python:3.8-slim-buster
#(Copy only neccessary artifacts)/venv,/myapp from the previous stage:
WORKDIR /myapp

COPY --from=build /venv /myapp/venv
COPY   --from=build /myapp/ /myapp/ 
CMD ["/bin/bash"]
SHELL ["/bin/bash", "-c"]
#activate conda environment and run python file and gunicorn 
ENTRYPOINT source venv/bin/activate && \ 
    python score.py
