import json, base64

with open('out.json') as f:
    frames = json.loads(json.load(f))

for i, frame in enumerate(frames):
    data = base64.b64decode(frame.split(',')[1])
    with open('frame-%05d.jpg' % i, 'wb') as f:
        f.write(data)

import os
os.system('convert -delay 2 frame-*.jpg out.gif; rm frame-*.jpg')
