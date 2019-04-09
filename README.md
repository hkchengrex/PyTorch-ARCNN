# PyTorch-ARCNN
This a unofficial *testing only* script written for ARCNN. It loads pretrained weights (.m) and execute them in PyTorch. There is absolutely no training functionality.

For details, please refer to the paper author's website: [Deep Convolution Networks for Compression
Artifacts Reduction](http://mmlab.ie.cuhk.edu.hk/projects/ARCNN.html).

This can act as a pre-processing step to other image processing algorithm like the [ESRGAN](https://github.com/xinntao/ESRGAN) which [suffers](https://github.com/xinntao/ESRGAN/issues/5) from jpeg artifact.

## Usage
`
python run.py --dir [Folder for input images] --output [Output directory] --batch_size [Batch size] --quality [Quality of JPEG images used to train: 10/20/30/40]
`

All of these parameters are optional. By default, it will read images in `test_imgs/` and output to `results/`.

If you encountered out of memory, please lower the batch size. If the input images are of different resolutions, they cannot be batched and batch size 1 should be used.

GPU will be used if one is present.

## Performance
Speedwise, tt can process a 224*224 image within 5ms with a GTX 1080Ti.

In terms of quality, it has almost the exact same output as the author's Matlab testing code. You can use the script in the `compare/` folder to verify this. Maximum absolute error is `1` and mean absolute error is `2e-3`.

| Original | Author's matlab code | Our result |
| -------- | --------- | --------- |
|![Original](/test_imgs/147.jpg)|![matlab](/compare/gt.bmp)|![ours](/compare/147.png)|

## Acknowledgment
The network structure and pretrained weights are provided in the [said project](http://mmlab.ie.cuhk.edu.hk/projects/ARCNN.html). The pretrained weights are uploaded here for convenience.