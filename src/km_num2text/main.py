from km_num2text import utils

def num_normalize(input: str) -> str:
    transformed = utils.transform_km2en(input=input)
    
    nums = utils.get_nums(transformed)
    
    str_nums = utils.nums2texts(nums)
    
    tran_str_nums = utils.en2km(str_nums)
    
    for k, v in tran_str_nums.items():
        # if v comes with ។ -> remove it
        v_norm = v.replace('។', '')
        transformed = transformed.replace(k, v_norm)
       
    
    return transformed # after replace the number 

if __name__ == '__main__':
    print(num_normalize('ឆ្នាំ២០២៦ គឺជាឆ្នាំមួយនៅក្នុងសតវត្សទី២១។'))