# Image Generation in deltaV using Text Descriptions

In the context of deltaV, we've integrated an agent that leverages AI to generate images directly from text inputs. This agent uses the `stabilityai/stable-diffusion-xl-base-1.0` API for image generation and `imgbb` for temporary image storage.

## API Setup

To interact with the APIs, set up the necessary URLs and keys:

```python
API_URL = "https://api-inference.huggingface.co/models/stabilityai/stable-diffusion-xl-base-1.0"
IMG_BB_API_URL = "https://api.imgbb.com/1/upload"
IMG_BB_API_KEY = "your_imgbb_api_key_here"  # Replace with your actual ImgBB API key
headers = {"Authorization": "Bearer your_huggingface_api_key_here"}  # Replace with your actual Hugging Face API key
```

## Agent Configuration

Configure the agent responsible for image generation:

```python
GetImage=Agent(name="GetImage",
               seed="alice recovery phrase",
               mailbox="your_mailbox_id@https://agentverse.ai",  # Replace with your actual mailbox ID
)
```

## Sample Images

Below are fields that display a range of images generated by our agent:

- **Image 1**: ![Optional_description](https://github.com/Pixathon-Saavyas/InCapables/blob/main/files/image1.jpg)
- **Image 2**: ![Optional_description](https://github.com/Pixathon-Saavyas/InCapables/blob/main/files/image2.jpg)
- **Image 3**: ![Optional_description](https://github.com/Pixathon-Saavyas/InCapables/blob/main/files/image3.jpg)
- **Image 4**: ![Optional_description](https://github.com/Pixathon-Saavyas/InCapables/blob/main/files/image4.jpg)

## Output on deltaV

The generated images are displayed with the following fields:

- **Image URL**: Direct link to the generated image
- **Generation Parameters**: Text description used, model settings, etc.
- **Temporary Storage Link**: Link to the image stored temporarily on ImgBB

(Note: Include actual outputs or mockups of the output fields.)
