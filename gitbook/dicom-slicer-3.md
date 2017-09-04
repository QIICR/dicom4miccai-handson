## Step 3: Segment lesions

**TODO:**
* add overview of the QR interface and segmentation-related part

We will use the `Quantitative Reporting` for the subsequent steps to annotate the loaded PET SUV image with the segmentations of the lesions, and to calculate segmentation-based measurements.

Select the `Quantitative Reporting` module in the module selector. You can click the magnifying glass icon to the left of the module selector and start typing the module name to quickly locate it. Once the module is selected, choose "Create new Table" in the "Measurement report" selector in the module UI. This will create the top level data structure that will keep pointers to the image and the analysis results in the Slicer application.

![](/gitbook/assets/select-qr.png)

Once the report node is created, you will see selector for the "master volume" - this is the volume we will be segmenting. Click the selector, and choose the only item in the drop-down list named `QIN-HEADNECK-01-0024_1986-08-10_(SUVbw)` that corresponds to the SUV volume we have just loaded.

![](/gitbook/assets/select-master.png)

Now we are ready to do the segmentation! First locate the lesions by scrolling to the level of head in the axial 2D viewer (you can use move the mouse with the right mouse button pressed to zoom in). You will see some areas highlighted below that are darker than the surrounding tissue - we will segment those metabolically active areas using automated segmentation tools.

![](/gitbook/assets/pt-lesion.png)

### Create a new Segment 

_A segment_ corresponds to a single structure or finding in the image. Use "Add segment" button to create a new segment. Once the segment is created, you should see a new 

2. Describe the segmentation and assign the color to use for displaying segmentation overlay (if necessary)
3. Use one of the segmentation tools to segment the structure/finding.



| Step and relevant UI | Explanation |
| -- | -- |
| **Create a new Segment** <br><br> ![](/gitbook/assets/add-segment.png) | Use the _Add segment_ button to create a new segment. <br>The new segment will appear in the table listing all segments in your segmentation. <br>Mouse over the colored patch in the _Color_ to see the default structured description of the new segment.|
| **Update segment description**| We will be segmenting the primary lesion in the |