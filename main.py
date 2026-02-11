import pipe

def num_normalize(input: str) -> str:
    transformed = pipe.transform_km2en(input=input)
    
    nums = pipe.get_nums(transformed)
    
    str_nums = pipe.nums2texts(nums)
    
    tran_str_nums = pipe.en2km(str_nums)
    
    for k, v in tran_str_nums.items():
        transformed = transformed.replace(k, v)
       
    
    return transformed # after replace the number 

if __name__ == '__main__':
    print(num_normalize('ឆ្នាំនេះ២,០២៦ ម៉ែអាតាប៉ែ៩ហើយ។'))