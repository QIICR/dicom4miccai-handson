# DICOM for storing analysis results

In this component of the tutorial we will use 3D Slicer to segment DICOM images, calculate segmentation-based measurements, store the results as DICOM objects, and use those DICOM objects to re-load those results.

You must complete the [Prerequisites](/gitbook/prerequisites.md) before proceeding!

## Step 0: 3D Slicer interface

3D Slicer is a versatile platform that has many different capabilities. These capabilities are implemented in Slicer _modules_, and utilize common elements of the Slicer interface:

* **Toolbar** provides you with the active module selector, and shortcuts to the most commonly used modules and functionalities
* **Active module panel** shows the user interface for the module currently selected
* **2D and 3D viewers** are used to visualize 2D reformats of the image data with the various overlays (segmentations, annotations, intersections with models), and the 3D views of the data (volume rendering, model surfaces, annotations), respectively

In this tutorial we will use just 2 modules of 3D Slicer: 
* `DICOM Browser` module to load the DICOM datasets
* `Quantitative Reporting` to perform segmentation and quantitation of the DICOM images

![](/gitbook/assets/slicer-ui.png)


## Step 1: Import DICOM data

As the first step, we need to import the DICOM data that we downloaded in the [Prerequisites](/gitbook/prerequisites.md) into Slicer. To do this, activate the `DICOM Browser` module, click the "Import" button in the DICOM module popup to select the data directory, and click "Import", as shown in the screenshot below. When prompted, choose "Add link" to avoid copying the dataset.

![](/gitbook/assets/dicom-import.png)

If the import operation was successful, you should see the following items in your `DICOM Browser` window.

![](/gitbook/assets/dicom-imported.png)

## Step 2: Load DICOM image

Now that the DICOM images are indexed in the Slicer DICOM database we can open the individual image series. In the `DICOM Browser` window, select the item `QIN-HEADNECK-01-0024` in the patient list, and the only image series with modality `PT` (Positron Emission Tomography, or PET). 

![](/gitbook/assets/pt-load.png)

Once the image is loaded, you should automatically see it in the 2D slice viewers (orange arrows below). This is a PET image that was obtained after injecting the [fluorodeoxyglucose (FDG) radioactive tracer](http://bit.ly/2x1hODX), which is a marker of tissue uptake of glucose, in turn closely correlated with certain types of tissue metabolism. The image you see has been normalized by the patient weight to show [Standardized Uptake Value (SUV)](https://en.wikipedia.org/wiki/Standardized_uptake_value) at each pixel, with the lower values (darker pixels) corresponding to larger SUV values. You can see right away the regions that show increased SUV are brain, heart and bladder (green arrows below).

![](/gitbook/assets/pt-loaded.png)

## Step 3: Segment lesions

We will use the `Quantitative Reporting` for the subsequent steps to annotate the loaded PET SUV image with the segmentations of the lesions, and to calculate segmentation-based measurements.

Select the `Quantitative Reporting` module in the module selector. You can click the magnifying glass icon to the left of the module selector and start typing the module name to quickly locate it. Once the module is selected, choose "Create new Table" in the "Measurement report" selector in the module UI. This will create the top level data structure that will keep pointers to the image and the analysis results in the Slicer application.

![](/gitbook/assets/select-qr.png)

Once the report node is created, you will see selector for the "master volume" - this is the volume we will be segmenting. Click the selector, and choose the only item in the drop-down list named `QIN-HEADNECK-01-0024_1986-08-10_(SUVbw)` that corresponds to the SUV volume we have just loaded.

![](/gitbook/assets/select-master.png)

Now we are ready to do the segmentation! First locate the lesions by scrolling to the level of head in the axial 2D viewer (you can use move the mouse with the right mouse button pressed to zoom in). You will see some areas highlighted below that are darker than the surrounding tissue - we will segment those metabolically active areas using automated segmentation tools.

![](/gitbook/assets/pt-lesion.png)

The overall process of creating a segmentation in the `Quantitative Reporting` module is the following:

1. Create a new Segment that will store the segmentation. A single segment corresponds to a single structure or finding in the image.
2. Describe the segmentation and assign the color to use for displaying segmentation overlay (if necessary)
3. Use one of the segmentation tools to segment the structure/finding.



| Step and relevant UI | Explanation |
| -- | -- |
| **Create a new Segment** <br><br> ![](/gitbook/assets/add-segment.png) | Use the _Add segment_ button to create a new segment. <br>The new segment will appear in the table listing all segments in your segmentation. <br>Mouse over the colored patch in the _Color_ to see the default structured description of the new segment.|
| **Update segment description**| We will be segmenting the primary lesion in the |


## Step 4: Explore and store the analysis results in DICOM

## Step 5: Reload the analysis results from DICOM