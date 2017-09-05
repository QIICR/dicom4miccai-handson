## Step 3: Segment lesions

We will use the `Quantitative Reporting` for the subsequent steps to annotate the loaded PET SUV image with the segmentations of the lesions, and to calculate segmentation-based measurements.

Select the `Quantitative Reporting` module in the module selector. You can click the magnifying glass icon to the left of the module selector and start typing the module name to quickly locate it. 

### `Quantitative Reporting`

`Quantitative Reporting` is a module that supports segmentation and measurements from a DICOM image series.

![](/gitbook/assets/qr-ui.png)

Once the module is selected, choose "Create new Table" in the "Measurement report" selector in the module UI. This will create the top level data structure that will keep pointers to the image and the analysis results in the Slicer application.

![](/gitbook/assets/select-qr.png)

Once the report node is created, you will see selector for the "master volume" - this is the volume we will be segmenting. Click the selector, and choose the only item in the drop-down list named `QIN-HEADNECK-01-0024_1986-08-10_(SUVbw)` that corresponds to the SUV volume we have just loaded.

![](/gitbook/assets/select-master.png)

Now we are ready to do the segmentation! First locate the lesions in the dataset downloaded in the [Prerequisites](/gitbook/prerequisites.md). Scroll to the level of head in the axial 2D viewer (you can use move the mouse with the right mouse button pressed to zoom in). You will see some areas highlighted below that are darker than the surrounding tissue - we will segment those metabolically active areas using automated segmentation tools.

![](/gitbook/assets/pt-lesion.png)

### Create and initialize a new Segment 

_A segment_ corresponds to a single structure or finding in the image. Use "Add segment" button to create a new segment. Once the segment is created, you should see a new entry in the segments list. The segment itself is empty (no image voxels have been segmented yet), but it has a default color and metadata. You can see the latter in the tooltip by placing your mouse over the square color patch.

![](/gitbook/assets/new-segment.png)

Next we will initialize this metadata to the values meaningful in our situation. Double-click the colored patch to open the segmentation terminology window. This window allows to select segment the following structured attributes for each segment:

* **Category**: overall category of the segmentation.
* **Type**: more specific description of the segmentation.
* **Anatomic region**: where applicable, location of the segmented structure.

![](/gitbook/assets/context-window.png)

"Anatomic region" selector will be disabled when it is not applicable (e.g., when segmentation category is "Anatomic structure"). "Type" and "Anatomic region" have modifier selectors, which are applicable to some items. These can be used to differentiate between left and right organs, for example.

Content of the lists is defined by the segmentation and anatomic contexts, or lexicons. 3D Slicer includes the lexicons of terms commonly used in 3D Slicer, and also those that are included in the DICOM standard. However, they can also be defined by the user or application developer (you can read more in [this article](https://qiicr.gitbooks.io/dcmqi-guide/user_guide/coding_schemes.html) from the [dcmqi user guide](https://qiicr.gitbooks.io/dcmqi-guide)).

In our case, we will select the lexicon defined specifically for describing the structures relevant in segmenting PET images for head and neck cancer:

![](/gitbook/assets/hnc-contexts.png)

We will first be segmenting primary lesion (Segmentation type: "Neoplasm, Primary"), which belongs to the "Morphologically Altered Structure" category. "Anatomic region" selector contains locations where head and neck cancer lesions are commonly encountered. After you confirmed the selection of metadata for the new segment, you should see it in the tooltip as shown below.

![](/gitbook/assets/segment-initialized.png)

### Segment the lesion

Various segmentation tools are available, from basic manual contouring, to thresholding and more advanced automated tools.

For segmenting the lesion in PET, we will use a specialized automated tool presented by Beichel et al in [this manuscript](http://dx.doi.org/10.1118/1.4948679).

To segment a PET lesion using this tool, first enable it from the list of segmentation tools, and then click within the primary lesion region in the axial slice.


|![](/gitbook/assets/pt-lesion.png)|![](/gitbook/assets/pet-effect.png)|![](/gitbook/assets/pet-segmented.png)|
|-|-|

**Try it yourself: Repeat the same sequence of steps to segment the Secondary lesion!**
