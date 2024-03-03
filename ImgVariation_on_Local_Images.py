import openai
from io import BytesIO
from PIL import Image

openai.api_key = open("apikey","r").read()
filePath=input("kindly specify picture location:")

image= Image.open(filePath)
width,height = 256,256
image = image.resize((width,height))

# .resize((width,height))
byte_stream = BytesIO()
image.save(byte_stream, format='PNG')
byte_array = byte_stream.getvalue()

response = openai.Image.create_variation(
    image=byte_array,
    n=2,
    size="256x256"
)



# -------------------------------------------
#
# response = openai.Image.create_variation(
#     image=open(filePath,"rb"),
#     n=2,
#     size ="256x256"
# )

print(response["data"])
