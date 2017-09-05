## Step 4: Explore and store the analysis results in DICOM

Enable crosshairs. Try clicking on any of the segments, or any of the rows in the measurement table to synchronize the 2D viewers. Note how metadata about the segmentations and measurements is populated and shows up in the tooltip.

|![](/gitbook/assets/segmented-segments.png)|![](/gitbook/assets/segmented-measurements.png)|
|-|-|

Click "Complete Report" button to finalize your work.

Open the "DICOM Browser" window, as we did in the beginning to load the image. Note 3 more series are now included in the study that had just the PET series before.

![](/gitbook/assets/qr-exported.png)

The new series you see are the following:

* **RWV**: Real-world value DICOM object storing the Standardized Uptake Value (SUV) normalization information for the PET series we loaded. It was created automatically when you loaded the PET series.
* **SEG**: Segmentation DICOM object storing the results of the segmentation and metadata for the individual segments.
* **SR**: DICOM Structured report that follows template TID 1500 recording the measurements calculated from the SUV-normalized PET image for the image regions defined by the segmentations.