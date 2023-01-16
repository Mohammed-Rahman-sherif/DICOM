import pydicom as dicom
import matplotlib.pylab as plt

# specify your image path
image_path = 'C:\\Users\\smart\\Documents\\Datasets\\Metosis_Trainingset\\0e56fd11a762be0983f0.dcm'
ds = dicom.dcmread(image_path)

plt.imshow(ds.pixel_array, cmap=plt.cm.bone_r)
plt.show()