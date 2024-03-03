import openai

openai.api_key = open("apikey","r").read()

file_path = input("File path please:")
mask_path = input("Mask file path please:")
masking=input("kindly specify masking details:")

response = openai.Image.create_edit(
    image=open(file_path,"rb"),
    mask = open(mask_path,"rb"),
    prompt= masking,
    n=2,
    size ="256x256"
)

print(response["data"])
