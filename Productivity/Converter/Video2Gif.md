# Video2Gif

Creating high-quality GIFs from videos can be a useful skill, whether for social media, presentations, or personal projects. In this guide, we'll walk you through the steps to convert a video to a GIF using FFmpeg, covering both GPU-accelerated and non-GPU methods.

## Prerequisites

Before you start, make sure you have FFmpeg installed on your system. You can download it from [FFmpeg's official website](https://ffmpeg.org/download.html).

## Step-by-Step Guide

### Step 1: Convert Video to SRGB Color Space

First, we need to convert the input video to an SRGB color space. This step is crucial to maintain color accuracy in the final GIF. You can do this using NVIDIA's NVENC for hardware acceleration or using CPU processing.

#### **1.1. GPU-Accelerated Version (Using NVENC)**

If you have an NVIDIA GPU, you can use the following command for faster processing:

```bash
ffmpeg -hwaccel cuda -i input.mkv -vf "colorspace=bt709" -c:v h264_nvenc temp_srgb.mp4
```

#### **1.2. Non-Hardware Accelerated Version**

If you don’t have a GPU or prefer to use CPU processing, run this command:

```bash
ffmpeg -i input.mkv -vf "colorspace=bt709" -c:v libx264 temp_srgb.mp4
```

### Step 2: Generate the Color Palette

Next, we need to create a color palette from the video. The palette will help improve the quality of the GIF by optimizing the color mapping.

#### **2.1. Command for Generating the Palette**

Run the following command to generate the palette:

```bash
ffmpeg -i temp_srgb.mp4 -vf "fps=10,scale=1280:-1:flags=lanczos,palettegen" -frames:v 1 palette.png
```

### Step 3: Convert the Video to GIF

Finally, we’ll use the generated palette to convert the video into a GIF.

#### **3.1. GPU-Accelerated Version (Using NVENC)**

Use the following command to create the GIF while applying the color palette:

```bash
ffmpeg -hwaccel cuda -i temp_srgb.mp4 -i palette.png -lavfi "fps=10,scale=1280:-1:flags=lanczos [x]; [x][1:v] paletteuse" output.gif
```

#### **3.2. Non-Hardware Accelerated Version**

For the CPU version, run this command:

```bash
ffmpeg -i temp_srgb.mp4 -i palette.png -lavfi "fps=10,scale=1280:-1:flags=lanczos [x]; [x][1:v] paletteuse" output.gif
```

## Conclusion

By following these steps, you can convert a video to a high-quality GIF using FFmpeg, with options for both GPU-accelerated and CPU-based processing. This approach ensures that your GIFs retain their original color integrity while allowing for customization based on your hardware capabilities.

Feel free to reach out in the comments if you have any questions or run into issues while following this guide. Happy GIF-making!
