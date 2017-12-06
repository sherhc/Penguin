# Penguin

## require

## camerashot

修改Lib\site-packages\VideoCapture\ \__init__.py第153行，把fromstring改成frombytes

## compile

修改Lib\site-packages\PIL\ImageFont.py第320行，将return load(os.path.join(dir, filename)) 改成return load_default()