
import re
from km_num2text import num2text
    
km2en = {
    '០': 0,
    '១': 1,
    '២': 2,
    '៣': 3,
    '៤': 4,
    '៥': 5,
    '៦': 6,
    '៧': 7,
    '៨': 8,
    '៩': 9
}

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
        num = num.replace(',', '')
        num = int(float(num)) if float(num).is_integer() else float(num)
        
        output[str(num)] = num2text.num2text(num=num)
    
    return output


if __name__ == '__main__':
    
  transformed = transform_km2en('ឆ្នាំ២០២៦ គឺជាឆ្នាំមួយនៅក្នុងសតវត្សទី២១')
  nums = get_nums(transformed)
  str_nums = nums2texts(nums)
  print(str_nums)
  
