# Prerequisites

In this tutorial we will use several open source software tools, and publicly available datasets. 

Many of the tools we install here will be helpful to you in the future when you work with DICOM, so think about this as setting up your lab space for the future work!

We prepared packages with the binaries of those tools for each of the platforms, that are provided on this page together with the platform-specific installation instructions. The list of the tools we will be using is provided in the Details section. 

## Step 1: Download the software package for your platform

**If you are attending the tutorial in-person**: we will be providing USB drives with the software. Copy the package for your platform to your computer.

**If you are preparing for the tutorial beforehand, or are following it on your own**: use the links below to download the package (all packages are for 64-bit operating systems):
* [Windows](https://github.com/qiicr/dicom4miccai-handson/releases/download/QIN-HEADNECK_tables/DICOM4MICCAI-Win64.zip)
* [macOS](https://github.com/qiicr/dicom4miccai-handson/releases/download/QIN-HEADNECK_tables/DICOM4MICCAI-macOS.zip)
* [Linux](https://github.com/qiicr/dicom4miccai-handson/releases/download/QIN-HEADNECK_tables/DICOM4MICCAI-Linux.zip)

## Step 2: Install the software

First, extract the package you downloaded. We will further refer to the location of the extracted folder as `DICOM4MICCAI_ROOT`.

Next, install the software tools that require installation (3D Slicer and Atom editor), following the platform-specific instructions below.

Note, that if you have an older version of 3D Slicer, you will need to install the one we provide! Although we use a standard 3D Slicer package, we will be using functionality introduced relatively recently.

### Windows

Double-click the installers for 3D Slicer and Atom editor to install these tools.

### macOS

Open the 3D Slicer package (`.dmg` file), then **drag the 3D Slicer icon in the opened volume to your Applications folder** (if you don't do this, Slicer will not function properly!).

To install Atom editor, unzip the Atom.zip file, and drag the Atom icon to your Applications folder.

### Linux

Extract the 3D Slicer application from the `Slicer-4.7.0-2017-08-30-linux-amd64.tar.gz` file.

Install Atom using the `.deb` or `.rpm` package.

## Step 3: Configure the software

### Install 3D Slicer extensions

Launch the 3D Slicer application. Start 3D Slicer and open Extension Manager by clicking this button in the toolbar:

![](https://qiicr.gitbooks.io/quantitativereporting-guide/docs/screenshots/extension_manager.png)

Next, click the "wrench" icon in the upper right corner of the Extension Manager window, and click the "Install Extension from File..."

One by one, install each of the files that are located in the SlicerExtensions folder in `DICOM4MICCAI_ROOT`.

### Install dicom-dump Atom package

Windows: go to menu item `File > Settings > Install`

Mac: go to menu item `Atom > Preferences > Install`

Linux: go to menu item `File > Settings > Install`

Search for `dicom-dump` package, click "Install" button when found.

Once installed, click `dicom-dump` "Settings" button, locate the entry with the name "Path to DCMTK installation", and set this path to point to the `bin` directory in the `DICOM4MICCAI_ROOT`/dcmtk/bin.

## Step 4: Download the datasets

To keep the data that we will use in the tutorial, make a sub-folder `Data` in the `DICOM-tutorial` folder we created earlier.

Download the file from this location, and extract its contents: 
* [data package](https://github.com/QIICR/dicom4miccai-handson/releases/download/QIN-HEADNECK_tables/DICOM4MICCAI-Data.zip)

The zip file contains the following items:
* Single DICOM PET series for subject 24 from the [TCIA QIN-HEADNECK collection](https://wiki.cancerimagingarchive.net/display/Public/QIN-HEADNECK)
* Single DICOM CT series for subject 314 from the [TCIA LIDC-IDRI collection](https://wiki.cancerimagingarchive.net/display/Public/LIDC-IDRI)
* segmentation of a lung nodule from the CT series above done using 3D Slicer [Chest Imaging Platform](https://chestimagingplatform.org/) extension "Lung lesion analyzer" module, stored in NRRD format

## Details on the software used

Software|Information|Home page
-|-|-
3D Slicer|Free open source software platform for medical image informatics, image processing, and three-dimensional visualization.|https://slicer.org
DCMTK|DCMTK is a free open source collection of libraries and applications implementing large parts the DICOM standard.| http://dcmtk.org
dcmqi|Free open source library that implements conversion of the data stored in commonly used research formats into the standard DICOM representation.|https://github.com/qiicr/dcmqi
Atom|A hackable text editor for the 21st Century|https://atom.io
dicom-dump|An Atom package that simplifies examining the content of DICOM files| https://atom.io/packages/dicom-dump