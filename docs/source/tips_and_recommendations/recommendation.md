## Recommendations

### Process of experimentation

When you work with satellite imagery you usually work with multi/hyperspectral image data. Which means you have a lot of channels available to you which are to an extent related to each other. Such that network architectures that work well with RGB images might not work well with multi/hyperspectral images or there are likely better alternatives. Such that the process of experimentation is very important and differs from RGB processing.

1. Use simple pretrained model attach the required decoder onto it
    - Make sure the that the model can generalize well on the data
    - Use PCA to reduce the number of channels to 3 
2. Move away from the PCA approach and work with pure HSI Data
3. Adapt model architecture to fit the HSI data
    - Take advantage of the spectral information (depth wise processing)

>**Note:** The Main point is to go from simple to complex, it is easier to identify issues that way.
    

### Resources

**Models:**
- Huggingface library
- Both PyTorch and Tensorflow has pretrained backbones available

**Datasets:**
- DeepGlobe Land Cover Classification Challenge (RGB landcover dataset)
- Sentinel-2 dataset (MSI dataset)
- WHU-OHS dataset (HSI Landcover dataset)
- EnMAP (HSI dataset, has to be requested)