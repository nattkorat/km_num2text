# Khmer Number to Text
A Python library for normalizing and converting Khmer numbers to text, with built-in support for translation.

## Features
- Number Normalization: Clean and standardize Khmer digit strings (១០ -> ដប់).

## Installation
Install the package via pip:

```Bash
pip install km-num2text
```

## Quick Start
The num_normalize function cleans up input strings to ensure they are in a standard format (all numbers are converted to text-based).

```python
from km_num2text import num_normalize

input = "ឆ្នាំ២០២៦ គឺជាឆ្នាំមួយនៅក្នុងសតវត្សទី២១។"

normalized = num_normalize(input)

# ឆ្នាំពីរពាន់ម្ភៃប្រាំមួយ គឺជាឆ្នាំមួយនៅក្នុងសតវត្សទីម្ភៃមួយ។
```