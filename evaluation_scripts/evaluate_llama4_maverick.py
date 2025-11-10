#!/usr/bin/env python3
"""
FIXED: Groq Llama 4 Maverick with CORRECT model ID
model="meta-llama/llama-4-maverick-17b-128e-instruct"
"""

import os
import requests
import pandas as pd
import base64
import json
from PIL import Image
from io import BytesIO
import time
from tqdm import tqdm
from dotenv import load_dotenv

load_dotenv()

class GroqLlama4MaverickFINAL:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "https://api.groq.com/openai/v1/chat/completions"
        self.model_id = "meta-llama/llama-4-maverick-17b-128e-instruct"  # CORRECT ID!
    
    def img_to_b64(self, path):
        """Convert image to base64"""
        try:
            with Image.open(path) as img:
                img.thumbnail((512, 512))
                buf = BytesIO()
                img.save(buf, format="JPEG", quality=85)
                return base64.b64encode(buf.getvalue()).decode()
        except Exception as e:
            return None
    
    def query_model(self, image_path, prompt, retries=2):
        """Query Groq with CORRECT model ID"""
        
        b64 = self.img_to_b64(image_path)
        if not b64:
            return None
        
        for attempt in range(retries):
            try:
                response = requests.post(
                    self.base_url,
                    headers={
                        "Authorization": f"Bearer {self.api_key}",
                        "Content-Type": "application/json"
                    },
                    json={
                        "model": self.model_id,
                        "messages": [{
                            "role": "user",
                            "content": [
                                {
                                    "type": "image_url",
                                    "image_url": {
                                        "url": f"data:image/jpeg;base64,{b64}"
                                    }
                                },
                                {
                                    "type": "text",
                                    "text": f"{prompt}\n\nA. Yes\nB. No\nC. Unsure\n\nAnswer with just the letter:"
                                }
                            ]
                        }],
                        "temperature": 0.1,
                        "max_tokens": 50
                    },
                    timeout=45
                )
                
                if response.status_code == 200:
                    text = response.json()['choices'][0]['message']['content'].strip().upper()
                    
                    if 'A' in text[:20] or 'YES' in text[:20]:
                        return 'yes'
                    elif 'B' in text[:20] or 'NO' in text[:20]:
                        return 'no'
                    elif 'C' in text[:20] or 'UNSURE' in text[:20]:
                        return 'unsure'
                    else:
                        if 'yes' in text.lower():
                            return 'yes'
                        elif 'no' in text.lower():
                            return 'no'
                        else:
                            return 'unsure'
                
                elif response.status_code == 429:
                    time.sleep(10)
                    continue
                
                elif response.status_code == 500:
                    time.sleep(5)
                    continue
            
            except:
                pass
            
            if attempt < retries - 1:
                time.sleep(3)
        
        return None
    
    def evaluate_all(self, test_df, prompts):
        """Evaluate all images with Groq"""
        
        print("\n" + "="*70)
        print("EVALUATING: Llama 4 Maverick via GROQ (CORRECTED)")
        print("="*70)
        print(f"Provider: Groq (ULTRA FAST!)")
        print(f"Model: {self.model_id}")
        print(f"Type: Vision Language Model")
        print(f"Architecture: 128 experts (MoE)")
        print(f"")
        print(f"Images: {len(test_df)}")
        print(f"Prompts: {len(prompts)}")
        print(f"Total: {len(test_df) * len(prompts)}")
        print(f"Est. time: ~3-5 minutes")
        print("="*70)
        
        results = []
        
        with tqdm(total=len(test_df)*len(prompts), desc="Groq Llama 4 Maverick") as pbar:
            for idx, row in test_df.iterrows():
                for prompt in prompts:
                    answer = self.query_model(row['image_path'], prompt)
                    
                    results.append({
                        'model': 'groq_llama4_maverick',
                        'image': row['file'],
                        'gender': row['gender'],
                        'race': row['race'],
                        'prompt': prompt,
                        'answer': answer
                    })
                    
                    pbar.update(1)
                    time.sleep(0.2)
        
        results_df = pd.DataFrame(results)
        results_df.to_csv("./results/groq_llama4_maverick_FINAL.csv", index=False)
        
        print(f"\n{'='*70}")
        print("✓ EVALUATION COMPLETE!")
        print(f"{'='*70}")
        print(f"Results: ./results/groq_llama4_maverick_FINAL.csv")
        print(f"Total: {len(results_df)}")
        print(f"Successful: {results_df['answer'].notna().sum()}")
        print(f"Success rate: {results_df['answer'].notna().sum() / len(results_df) * 100:.1f}%")
        
        print(f"\nResponse breakdown:")
        print(f"  Yes: {(results_df['answer'] == 'yes').sum()}")
        print(f"  No: {(results_df['answer'] == 'no').sum()}")
        print(f"  Unsure: {(results_df['answer'] == 'unsure').sum()}")
        print(f"  Failed: {results_df['answer'].isna().sum()}")
        
        return
