from PIL import Image, ImageFont, ImageDraw
import exifread
import os

root_dir = 'C:\\Users\\asjxw\\Desktop\\1117'
dir_list = os.listdir(root_dir)
dir_url_list = [os.path.join(root_dir, directory) for directory in dir_list]

for dir_url in dir_url_list:
    images_list = os.listdir(dir_url)
    images_url_list = [os.path.join(dir_url, file) for file in images_list]
    image_dict = dict(zip(images_list, images_url_list))
    for image, image_url in image_dict.items():

        img = open(image_url, 'rb')
        exif = exifread.process_file(img)

        ISOSpeedRatings = exif['EXIF ISOSpeedRatings'].printable
        ExposureTime = exif['EXIF ExposureTime'].printable
        FNumber = str(eval(exif['EXIF FNumber'].printable))
        FocalLength = exif['EXIF FocalLength'].printable
        Time = exif['Image DateTime'].printable.split(' ')[0].replace(':', '.')
        Location = '奥林匹克森林公园'

        img.close()

        img = Image.open(image_url)
        width, height = img.size
        catagory = dir_url.split('\\')[-1]
        new_img = os.path.join('C:\\Users\\asjxw\\Desktop\\extended2', catagory, image_url.split('\\')[-1])

        # Set Font
        f_font_url = 'C:\\Users\\asjxw\\Desktop\\timesi.ttf'
        title_font_url = 'C:\\Users\\asjxw\\Desktop\\PingFang_normal.ttf'
        text_font_url = 'C:\\Users\\asjxw\\Desktop\\PingFang_Light.ttf'

        f_font = ImageFont.truetype(f_font_url, int(width/40))
        title_font = ImageFont.truetype(title_font_url, int(width/40))
        text_font = ImageFont.truetype(text_font_url, int(width/40))
        color = '#000'

        # img = img.crop((0, 0, width, height * 1.1))
        extended_img = Image.new('RGB', (width, int(height * 1.15)), '#FFF')
        extended_img.paste(img, (0, 0))
        draw = ImageDraw.Draw(extended_img)
        filename = image.split('.')[0]
        title = filename + ' / ' + catagory + '     ' + Time + ' / ' + Location
        draw.text((width/20, height * 1.012), title, fill='#000', font=title_font)
        draw.text((width/20, height * 1.07),
                  'SONY ILCE-6300, E16-50mm@' + FocalLength + 'mm; ' +
                  ExposureTime + 's; f/' + FNumber + '; ISO-' + ISOSpeedRatings,
                  fill='#000', font=f_font)
        extended_img.save(new_img)
