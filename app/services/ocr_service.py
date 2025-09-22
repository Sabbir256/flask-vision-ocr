from google.cloud import vision
import logging
import time
from typing import Dict

logger = logging.getLogger(__name__)

class OCRService:
    def __init__(self):
        try:
            self.client = vision.ImageAnnotatorClient()
        except Exception as e:
            logger.error(f"Failed to initialize Google Vision client: {str(e)}")
            raise Exception("Could not initialize Google Cloud Vision API client.")
        
    def extract_text_from_image(self, file) -> Dict:
            try:
                file.seek(0)
                image_content = file.read()
                
                image = vision.Image(content=image_content) # vision api image object
                
                start_time = time.perf_counter()
                response = self.client.text_detection(image=image)
                end_time = time.perf_counter()
                
                if response.error.message:
                    raise Exception(f"Vision API error: {response.error.message}")
                
                processing_time_ms = (end_time - start_time) * 1000
                
                result = {
                    "full_text": "",
                    "confidence_score": 0.0,
                    "processing_time_ms": round(processing_time_ms, 2)
                }
                
                texts = response.text_annotations
                if texts:
                    result["full_text"] = texts[0].description # first annotation contains the entire detected text
                
                if result["full_text"]:
                    result["confidence_score"] = 0.95 # vision api does not return confidence for text detection
                    
                return result
            except Exception as e:
                logger.error(f"OCR extraction failed: {str(e)}")
                raise Exception("Failed to extract text from image.")
                
                
    