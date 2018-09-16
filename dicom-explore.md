# DICOM data wrangling

In this part of the tutorial we will learn how to work with a DICOM dataset spanning different TCIA collections and containing various types of DICOM objects. 

### Hands-on demo notes

* TCIA as a use case
  * [LIDC-IDRI](https://wiki.cancerimagingarchive.net/display/Public/LIDC-IDRI) \(annotations in XML\)
  * [TCGA-GBM](https://wiki.cancerimagingarchive.net/display/Public/TCGA-GBM) \([annotations in NIfTI](https://wiki.cancerimagingarchive.net/display/DOI/Segmentation+Labels+and+Radiomic+Features+for+the+Pre-operative+Scans+of+the+TCGA-GBM+collection)\)
  * [TCGA-LGG](https://wiki.cancerimagingarchive.net/display/Public/TCGA-LGG) \([annotations in NIfTI](https://wiki.cancerimagingarchive.net/display/DOI/Segmentation+Labels+and+Radiomic+Features+for+the+Pre-operative+Scans+of+the+TCGA-LGG+collection)\)
  * [QIN-HEADNECK](https://wiki.cancerimagingarchive.net/display/Public/QIN-HEADNECK)
  * QIN-PROSTATE-Repeatability \(not yet released\)
* discuss the example dataset used in the demo
* steps for handling DICOM data:
  * [dicomsort](https://github.com/pieper/dicomsort)
  * [dcm2niix](https://github.com/rordenlab/dcm2niix) for converting image series into volumes
  * [dcmqi](https://github.com/qiicr/dcmqi) for working with SEG and SR
  * [dcm2tables](https://github.com/QIICR/dcm2tables): conversion into tabular representation for working with metadata
    * "database" [visual schema](https://app.quickdatabasediagrams.com/#/schema/_71V1H1AXEqqKWDnvx4VXw%20)
  * Jupyter Notebook demonstration

This part will be covered in a Jupyter Notebook \(link to be added\).

