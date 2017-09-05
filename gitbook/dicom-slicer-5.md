## Step 5: Reload the analysis results from DICOM

You can close the 3D Slicer application and open it again to start fresh.

To reload the analysis results you created in the previous steps, simply open the "DICOM Browser", select the SR series for the subject QIN-HEADNECK-01-0024, and load it.

After you click "Load" in the "DICOM Browser", you will be prompted about loading the referenced series. The measurements report references both the original PET series, and the SUV. Uncheck the PET series to load just the SUV-corrected volume.

![](/gitbook/assets/sr-reload.png)

Next, switch to the `QuantitativeReporting` module. You should be able to select the loaded measurement report item in the selector, upon which the segmentations and measurements table should appear as it was at the time you saved the results of your work.

![](/gitbook/assets/sr-reloaded.png)