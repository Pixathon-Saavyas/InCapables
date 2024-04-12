from uagents import Agent, Context, Protocol, Model, Bureau
from pydantic import Field
from ai_engine import UAgentResponse, UAgentResponseType
import requests

API_URL = "https://api-inference.huggingface.co/models/stabilityai/stable-diffusion-xl-base-1.0"
IMG_BB_API_URL = "https://api.imgbb.com/1/upload"
IMG_BB_API_KEY = "fc7ab5d3266f57af3386855f4d93bac7"  # Replace with your actual ImgBB API key
headers = {"Authorization": "Bearer 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"}
GetImage=Agent(name="GetImage",
                seed="alice recovery phrase",
                mailbox=f"ad6de0c7-17dc-4979-8988-ead663cd9213@https://agentverse.ai",
)
def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.content
def upload_image_to_imgbb(image_bytes):
    """Uploads image to ImgBB and returns the URL of the uploaded image."""
    response = requests.post(
        IMG_BB_API_URL,
        files={'image': image_bytes},
        data={'key': IMG_BB_API_KEY}
    )
    return response.json()['data']['url']

class GetImage(Model):
    prompt: str = Field(description="the prompt which is used to create the image identify it from the user")

Get_Image_protocol = Protocol("GetImage")

@Get_Image_protocol.on_message(model=GetImage, replies={UAgentResponse})
async def Get_image(ctx: Context, sender: str, msg: GetImage):
    image_bytes = query({"inputs": f"{msg.prompt}",})

    image_url = upload_image_to_imgbb(image_bytes)
    await ctx.send(
        sender, UAgentResponse(message=f"Generated image link:<a href={image_url}> Image Link </a>", type=UAgentResponseType.FINAL)
    )
GetImage.include(Get_Image_protocol, publish_manifest=True)
GetImage.run()

