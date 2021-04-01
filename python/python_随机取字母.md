## 1、思路：随机生成一位字母

参考文档**string - 常用字符串操作**[string](https://link.zhihu.com/?target=http%3A//python.usyiyi.cn/translate/python_352/library/string.html%23module-string)

> string.ascii_letters
>
> 与此级联（即包含）的 [ascii_lowercase](https://link.zhihu.com/?target=http%3A//python.usyiyi.cn/documents/python_352/library/string.html%23string.ascii_lowercase) 和 [ascii_uppercase](https://link.zhihu.com/?target=http%3A//python.usyiyi.cn/documents/python_352/library/string.html%23string.ascii_uppercase) 描述见下文。该值不依赖于本地设置。
>
> string.ascii_lowercase
>
> 小写字母 'abcdefghijklmnopqrstuvwxyz'.该值不依赖于本地设置以及不会被修改。
>
> string.ascii_uppercase
>
> 大写字母 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'.该值不依赖于本地设置以及不会被修改。

## 2、具体操作（利用string和random）

```python
>>> import string
>>> string.ascii_letters
'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
>>> import random
>>> random.choice(string.ascii_uppercase)
'G'
```

参考[Generate a random letter in Python](https://link.zhihu.com/?target=http%3A//stackoverflow.com/questions/2823316/generate-a-random-letter-in-python)

首先生成52位大写及小写字母，再利用random提取其中一位便成为随即字母。

```python
import string
import random
from PIL import Image, ImageDraw, ImageFont, ImageFilter

#captcha size
size = (240, 60)

#random chars
def gen_random():
    charlist = [random.choice(string.ascii_uppercase) for i in range(4)]
    chars = ''.join(charlist)
    return chars

def random_color():
    return (random.randint(0, 255), random.randint(0, 255), \
            random.randint(0, 255))


def gen_captcha():
    im = Image.new('RGBA', size, color = 0)
    draw = ImageDraw.Draw(im)

    #background   
    for w in range(size[0]):
        for h in range(size[1]):
            draw.point((w, h), random_color())

    #draw text
    chars = gen_random()
    #font and size
    fnt = ImageFont.truetype('arial.ttf', int(size[1] * 0.8))
    x = 0
    y = size[1] * 0.1

    for i in range(4):
        x += size[0] * 0.2
        draw.text((x, y), chars[i], font = fnt, fill = random_color())

    #blur
    im = im.filter(ImageFilter.BLUR)
    im.save('captchar.jpg')
    im.show()
    
if __name__ == '__main__':
    gen_captcha()
```

更多解法：

```python
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import random

def rndChar():
    return chr(random.randint(65, 90))

def rndColor(type):
    if type == 1:
        return (random.randint(0, 125), random.randint(0, 125), random.randint(0, 125))
    elif type == 2:
        return (random.randint(126, 255), random.randint(126, 255), random.randint(126, 255))

fontSize = 25
width = int(fontSize * 1.2 * 4)
height = int(fontSize * 1.2)

# 创建图像
image = Image.new('RGB', (width, height), (255, 255, 255))
# 创建字体，本地字体存放位置
font = ImageFont.truetype("C:\Windows\Fonts\Arial.ttf", 20)

draw = ImageDraw.Draw(image)

# 填满整个画面
for x in range(width):
    for y in range(height):
        draw.point((x, y), fill = rndColor(1))

# 输出字母
for t in range(4):
    draw.text((t * height + fontSize * 0.2, fontSize * 0.2), rndChar(), font = font, fill = rndColor(2))

if __name__ == '__main__':
    image.show()
```