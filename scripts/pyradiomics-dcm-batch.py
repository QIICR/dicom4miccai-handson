'''
Input:
 - directory organized with dicomsort
 - modality-specific configuration files
Output:
 - DICOM SR objects with the pyradiomics features
'''

import sys, os, pydicom, argparse, shutil
from subprocess import call

def main():
  parser = argparse.ArgumentParser(usage="%(prog)s --input-dir <dir> --output-dir <dir>")

  parser.add_argument('--input-dir', dest="inputDICOMDir", metavar='Input DICOM image directory',  help="Directory with the input DICOM series. Should be organized following PatientID/StudyUID/SeriesUID/InstanceUID.dcm convention first!")
  parser.add_argument('--output-dir', dest="outputDir", metavar='Output directory',  help="Directory to store the resulting DICOM files produced in the process of computation.")

  args = parser.parse_args()

  segFound = 0
  matchingImagesFound = 0

  for dirName,subdirList,fileList in os.walk(args.inputDICOMDir):
    for f in fileList:
      fname = os.path.join(args.inputDICOMDir,dirName,f)
      try:
        dcm = pydicom.read_file(fname)
      except:
       continue

      patientID = dcm.PatientID
      studyUID = dcm.StudyInstanceUID


      if dcm.SOPClassUID == '1.2.840.10008.5.1.4.1.1.66.4':
        print("Found SEG: "+fname)
        segFound = segFound+1
        if hasattr(dcm,'ReferencedSeriesSequence'):
          imageSeriesUID = dcm.ReferencedSeriesSequence[0].SeriesInstanceUID
          segmentationSeriesUID = dcm.SeriesInstanceUID
          segmentationInstanceUID = dcm.SOPInstanceUID

          imageDirectory = os.path.join(args.inputDICOMDir,patientID,studyUID,imageSeriesUID)
          segmentationFile = os.path.join(args.inputDICOMDir,patientID,studyUID,segmentationSeriesUID,segmentationInstanceUID+'.dcm')

          print("Image: "+imageDirectory)
          print("Segmentation: "+segmentationFile)
          matchingImagesFound = matchingImagesFound+1
          call(["python","dicom2dicom.py","--output-dir", args.outputDir, "--input-image",imageDirectory,"--input-seg",segmentationFile,"--temp-dir","TempDirBatch","--features-dict","featuresDict.tsv"])
          shutil.rmtree("TempDirBatch")
          os.mkdir("TempDirBatch")

  print("Total SEG objects found: "+str(segFound))
  print("Total matching SEG objects found: "+str(matchingImagesFound))

if __name__ == "__main__":
  main()
