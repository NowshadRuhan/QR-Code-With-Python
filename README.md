# QR-Code-With-Python
## Generate your QR code using python.

![MyQR-Code](https://github.com/NowshadRuhan/QR-Code-With-Python/blob/main/mycode.png?raw=true) 

#### Install 
```
pip install pyqrcode
```
```
pip install pypng
```

### Run this code
```
import pyqrcode
import png
from pyqrcode import QRCode
from PIL import Image

s = "Nowshad Ruhani Chowdhury, Lead Software Engineer."

url = pyqrcode.create(s)

url.svg("mycode.svg", scale = 8)

url.png("mycode.png", scale = 6)

img = Image.open(r"C:\Users\HP\Desktop\Python Project\mycode.png") 
 
img.show()

display(img)
```

![G.your-QR-Code](https://github.com/NowshadRuhan/QR-Code-With-Python/blob/main/QRCode1.png?raw=true) 

