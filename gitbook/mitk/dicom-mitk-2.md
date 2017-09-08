## Step 2: Load DICOM image

Now that the DICOM images are indexed in the MITK DICOM database we can open the individual image series. In the `DICOM Browser` window, select the item `QIN-HEADNECK-01-0024` in the patient list, and the only image series with modality `PT` (Positron Emission Tomography, or PET). To load an image double click on it or select it and press the `View` button.

![](/gitbook/assets/MITK/mitk-pt-load.png)

The image will be loaded and appear in the `Data Manager` on the left side. A prompt might appear if there are multiple readers available. Just use the reader selected by default and hit `OK`. Once the image is loaded, you should automatically see it in the 2D render windows and the 3D render window. If not right click on the image in the `Data Manager` and select `Global Reinit`.

![](/gitbook/assets/MITK/mitk-pt-loaded.png)
