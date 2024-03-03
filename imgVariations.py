import openai

openai.api_key = open("apikey","r").read()

filePath=input("kindly specify picture location:")

response = openai.Image.create_variation(
    image=open(filePath,"rb"),
    n=5,
    size ="256x256"
)

print(response["data"])

# image_url = response["data"][0]["url"]
# print(f"Image URL: {image_url}")