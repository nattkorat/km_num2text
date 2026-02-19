from km_num2text import utils

import re

def num_normalize(input: str) -> str:
    transformed = utils.transform_km2en(input=input)
    
    nums = utils.get_nums(transformed)
    
    str_nums = utils.nums2texts(nums)

    
    for k, v in str_nums.items():
        v_norm = v.replace('។', '')
        pattern = rf'(?<!\d){re.escape(k)}(?!\d)'
        transformed = re.sub(pattern, v_norm, transformed)
       
    
    return transformed # after replace the number 

if __name__ == '__main__':
    print(num_normalize('ឆ្នាំ២០២៦ គឺជាឆ្នាំមួយនៅក្នុងសតវត្សទី២១។'))