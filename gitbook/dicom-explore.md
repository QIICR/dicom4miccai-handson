# Exploration of the analysis results stored in DICOM

In this part of the tutorial we will learn how to work with a relatively large DICOM dataset that includes various image analysis results to enable data exploration.

In this example, we will work with the [QIN-HEADNECK](https://wiki.cancerimagingarchive.net/display/Public/QIN-HEADNECK) dataset publicly available from [The Cancer Imaging Archive (TCIA)](https://www.cancerimagingarchive.net/). The dataset is described in the following paper

> Fedorov A., Clunie D., Ulrich E., Bauer C., Wahle A., Brown B., Onken M., Riesmeier J., Pieper S., Kikinis R., Buatti J., Beichel RR. _DICOM for quantitative imaging biomarker development: a standards based approach to sharing clinical data and structured PET/CT analysis results in head and neck cancer research_. PeerJ 4:e2057, 2016. DOI: [10.7717/peerj.2057](https://dx.doi.org/10.7717/peerj.2057)

We will use [Jupyter Notebook](https://jupyter.org/) that will guide you over the data processing steps. You can use any of the following approaches to work with the notebook.

## nbviewer

Static view using Jupyter [nbviewer](https://nbviewer.jupyter.org/): this view will allow you to explore the dataset, processing steps and interactive plots, but you will not be able to interact with the content by changing the python code and observing the result of your changes. Link: http://nbviewer.jupyter.org/github/QIICR/dicom4miccai-handson/blob/miccai2017/notebooks/headneck.ipynb

## binder

Jupyter [Binder](https://beta.mybinder.org/) view: this view will launch a live hosted instance of the notebook accessible from the browser window. Feel free to change anything, explore and play with it! Whatever you do in the browser should not affect the master representation of the notebook. Link: https://beta.mybinder.org/v2/gh/qiicr/dicom4miccai-handson/miccai2017?filepath=/src/dicom4miccai-handson/notebooks/headneck.ipynb

## Using notebook on your computer

Of course, if you have Jupyter Notebook installed on your laptop, you are welcome to download the notebook file and play with it on your system! The notebook file can be downloaded here: https://github.com/QIICR/dicom4miccai-handson/blob/miccai2017/notebooks/headneck.ipynb

If you don't have Jupyter Notebook installed, you can follow the instructions here to set up your system: http://jupyter.org/install.html.