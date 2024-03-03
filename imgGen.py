import openai

openai.api_key = open("apikey","r").read()

inp=input("kindly specify picture details:")

response = openai.Image.create(
    prompt= inp,
    n=1,
    size ="1024x1024"
)

image_url = response["data"][0]["url"]
print(f"Image URL: {image_url}")