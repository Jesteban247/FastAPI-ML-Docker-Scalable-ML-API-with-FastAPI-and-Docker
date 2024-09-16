from PIL import Image
from transformers import BlipProcessor, BlipForConditionalGeneration

# Load the BLIP model and processor
processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-large")
model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-large")

def model_pipeline(image: Image):
    """
    Generate an unconditional caption for the given image using the BLIP model.

    Args:
        image (Image): The input image.

    Returns:
        str: The generated caption.
    """
    # Unconditional image captioning
    inputs = processor(image, return_tensors="pt")
    
    # Generate caption
    out = model.generate(**inputs)
    caption = processor.decode(out[0], skip_special_tokens=True)

    return caption
