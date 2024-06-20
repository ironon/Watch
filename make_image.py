from PIL import Image
## use command line first arguement as png file name
import sys
image_path = sys.argv[1]
def convert_image_to_rgb565(image_path):
    image = Image.open(image_path)
    image = image.convert('RGB')  # Ensure image is in RGB format
    pixels = image.load()

    width, height = image.size
    rgb565_data = []

    for y in range(height):
        for x in range(width):
            red, green, blue = pixels[x, y]
            # Convert to 5-6-5 format
            rgb565 = (((red & 0xf8)<<8) + ((green & 0xfc)<<3) + (blue>>3))
            rgb565_data.append(rgb565)

    return rgb565_data

# Example usage
rgb565_data = convert_image_to_rgb565(image_path)
print(rgb565_data)
template = """
#ifdef __has_include
#if __has_include("lvgl.h")
#ifndef LV_LVGL_H_INCLUDE_SIMPLE
#define LV_LVGL_H_INCLUDE_SIMPLE
#endif
#endif
#endif

#if defined(LV_LVGL_H_INCLUDE_SIMPLE)
#include "lvgl.h"
#else
#include "lvgl.h"
#endif


#ifndef LV_ATTRIBUTE_MEM_ALIGN
#define LV_ATTRIBUTE_MEM_ALIGN
#endif

#ifndef LV_ATTRIBUTE_IMG_WATCH_IF_5
#define LV_ATTRIBUTE_IMG_WATCH_IF_5
#endif

const LV_ATTRIBUTE_MEM_ALIGN LV_ATTRIBUTE_LARGE_CONST LV_ATTRIBUTE_IMG_WATCH_IF_5 uint8_t watch_if_5_map[] = {
#if LV_COLOR_DEPTH == 16 && LV_COLOR_16_SWAP == 0
    /*Pixel format: Red: 5 bit, Green: 6 bit, Blue: 5 bit*/
    {data}
    #endif
};

const lv_img_dsc_t watch_if_5 = {
    .header.cf = LV_IMG_CF_TRUE_COLOR,
    .header.always_zero = 0,
    .header.reserved = 0,
    .header.w = 240,
    .header.h = 240,
    .data_size = 57600 * LV_COLOR_SIZE / 8,
    .data = watch_if_5_map,
};

"""
