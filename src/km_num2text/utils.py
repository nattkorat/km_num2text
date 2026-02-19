
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
    for k, v in km2en.items():
        input.replace(k, str(v))
    
    return input

def get_nums(input: str) -> list:
    """Find the number in the text and return back as the list
    """
    pattern = r'-?\d+(?:,\d+)*(?:\.\d+)?|-?\d+(?:\.\d+)?'
    numbers = re.findall(pattern, input)
     
    return numbers

def str2num_type(str_n: str):
    return int(float(str_n)) if float(str_n).is_integer() else float(str_n)

def is_trailing_zero(str_num: str):
    return str_num.startswith('0')

def split_long_numbers(text, min_len=8, group=3):
    def repl(match):
        num = match.group()
        return " ".join(
            num[i:i+group] for i in range(0, len(num), group)
        )

    pattern = rf'(?<!\d)\d{{{min_len},}}(?!\d)'
    return re.sub(pattern, repl, text).split()


def nums2texts(nums: list) -> dict:
    """
    Convert a list of numeric strings to their Khmer text equivalents.
    
    Parameters
    ----------
    nums : list
        List of numeric strings, possibly containing commas.
    
    Returns
    -------
    dict
        Mapping from original string to Khmer text.
    """
    output = {}

    for num in nums:
        # Remove commas
        c_num = num.replace(',', '')

        # Convert string to proper numeric type
        numeric_value = str2num_type(c_num)

        # Handle trailing zero numbers with length > 1
        if is_trailing_zero(c_num) and len(c_num) > 1:
            first_digit_text = ''
            rest_text = ''

            if len(c_num) < 3:
                # Simple case: "10" → remove leading '1', convert
                numeric_value = str2num_type(c_num[1:])
                rest_text = num2text.num2text(num=numeric_value)
            else:
                # Complex case: "100000000"
                first_digit_text = num2text.num2text(str2num_type(c_num[0]))
                rest = c_num[1:]

                # If rest is long (>8 digits), split and convert each part
                if len(rest) >= 8:
                    splitted = split_long_numbers(rest)
                    rest_text = ''.join(
                        num2text.num2text(str2num_type(part))
                        for part in splitted
                    )
                else:
                    rest_text = num2text.num2text(str2num_type(rest))

            output[str(num)] = first_digit_text + rest_text
        else:
            # Normal case: convert entire number
            output[str(num)] = num2text.num2text(num=numeric_value)

    return output



if __name__ == '__main__':
    
  transformed = transform_km2en('ឆ្នាំ២០២៦ គឺជាឆ្នាំមួយនៅក្នុងសតវត្សទី២១')
  nums = get_nums(transformed)
  str_nums = nums2texts(nums)
  print(str_nums)
  
