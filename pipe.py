import yaml
import re

from num2words import num2words
from deep_translator import GoogleTranslator

with open('conf/en2km.yaml', 'r') as file:
    km2en = yaml.safe_load(file)

def transform_km2en(input: str) -> str:
    """Find the Khmer number and replace with English number
    
    Parameter:
    input: str
        String content that may or may not containing the number
    
    Return: str
        Transform string from the original content
    """
    output = ""
    for char in input:
        if char in km2en:
            output += str(km2en[char])
        else:
            output += char
    
    return output

def get_nums(input: str) -> list:
    """Find the number in the text and return back as the list
    """
    pattern = r'-?\d+(?:,\d+)*(?:\.\d+)?|-?\d+(?:\.\d+)?'
    numbers = re.findall(pattern, input)
     
    return numbers

def nums2texts(nums: list) -> dict:
    output = {}
    for num in nums:
        output[str(num)] = num2words(num.replace(',', '')) # if the number has comma
    
    return output

def en2km(inputs: dict) -> dict:
    outputs = {}
    tranlator = GoogleTranslator(source='en', target='km')
    
    for k, v in inputs.items():
        outputs[k] = tranlator.translate(v)
    
    return outputs


if __name__ == '__main__':
    
  transformed = transform_km2en('ឆ្នាំនេះ២៦ ម៉ែអាតាប៉ែ៩ហើយ 100')
  nums = get_nums(transformed)
  str_nums = nums2texts(nums)
  print(str_nums)
  
  tran_str_nums = en2km(str_nums)
  print(tran_str_nums)
    