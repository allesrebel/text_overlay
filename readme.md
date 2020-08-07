# Requirements
```
python3 -m pip install -r requirements.txt
```
or
```
python -m pip install  -r requirements.txt
```

# Usage
```
python3 text_overlay_util.py < header > < footer > <font_path> <font_size>
```
input stream contains formatted image data, what Pillow supports
ouput stream will be image data, png

Example usage on Windows with MinGW:

```
echo "123456" | \
xargs -I % bash -c \
'echo % | \
qr --error-correction=H "{\"name\":\"Payload_%\",\"transport\":\"softap\"}" | \
python text_overlay_util.py "%" "footer" "Roboto/Roboto-Black.ttf" 45 \
> %.png'
```

Example Usage MacOS:
```
echo "123456" | \
xargs -I % bash -c \
'echo % | \
qr --error-correction=H "{\"name\":\"Payload_%\",\"transport\":\"softap\"}" | \
python3 text_overlay_util.py "%" "footer" "Roboto/Roboto-Black.ttf" 45 \
> %.png'
```

Generates QR Code for gateway ending in 123456, with header of GW name and footer 

# Credits
Thanks to [Google](https://fonts.google.com) for allowing us to use awesome fonts!
