# DICOM for storing analysis results

In this component of the tutorial we will use 3D Slicer to segment DICOM images, calculate segmentation-based measurements, store the results as DICOM objects, and use those DICOM objects to re-load those results.

You must complete the [Prerequisites](/gitbook/prerequisites.md) before proceeding!

## Step 0: 3D Slicer interface

3D Slicer is a versatile platform that has many different capabilities. These capabilities are implemented in Slicer _modules_, and utilize common elements of the Slicer interface:

* **Toolbar** provides you with the active module selector, and shortcuts to the most commonly used modules and functionalities
* **Active module panel** shows the user interface for the module currently selected
* **2D and 3D viewers** are used to visualize 2D reformats of the image data with the various overlays (segmentations, annotations, intersections with models), and the 3D views of the data (volume rendering, model surfaces, annotations), respectively

In this tutorial we will use just 2 modules of 3D Slicer: 
* `DICOM` module to load the DICOM datasets
* `Quantitative Reporting` to perform segmentation and quantitation of the DICOM images

![](/assets/slicer-ui.png)


## Step 1: Import DICOM data

As the first step, we need to import the DICOM data that we downloaded in the [Prerequisites](/gitbook/prerequisites.md) into Slicer. To do this, activate the `DICOM` module, click the "Import" button in the DICOM module popup to select the data directory, and click "Import", as shown in the screenshot below. When prompted, choose "Add link" to avoid copying the dataset.

![](/assets/dicom-import.png)

## Step 2: Load DICOM image

## Step 3: Segment lesions

## Step 4: Explore and store the analysis results in DICOM

## Step 5: Reload the analysis results from DICOM