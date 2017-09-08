FROM jupyter/datascience-notebook:16e6d72cbff3

MAINTAINER https://github.com/qiicr

USER root

USER $NB_USER

RUN mkdir -p ${HOME}/data
RUN cd ${HOME}/data && wget https://github.com/QIICR/dicom4miccai-handson/releases/download/miccai2017/QIN-HEADNECK-Tables.tgz && tar zxf QIN-HEADNECK-Tables.tgz

RUN mkdir ${HOME}/src
RUN cd ${HOME}/src && git clone https://github.com/qiicr/dicom4miccai-handson && cd dicom4miccai-handson && git checkout miccai2017
