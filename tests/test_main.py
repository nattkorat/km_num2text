from km_num2text import num_normalize


text = """
    ខ្ញុំ+ជា+student !!! Facebook@@ 2024
    នេះ​គឺ​ជា+example+text@@@ មានលេខ 12345 និង symbols ###$$$
    I+love+Cambodia 🇰🇭!!! ឆ្នាំ2023 ?​។៕ ""!@#$%^&*()_-+={[]}:;""''<.,?/៖៖៖៖  “ ”“ ”
    Google@@AI កំពុង+develop+technology...
    Hello+World!!! ខ្មែរ+english+mix
    សាកល្បង+test+data@@ with@@@noise@@@
    លេខ+១០០+and+100 mixed!!!
    TikTok@@@ YouTube### Facebook!!!
    កាលពីថ្ងៃទី ០២ ខែកក្កដា ឆ្នាំ ២០២៤
    ១​​ ២​ ៣ ៤ ៥ ៦ ៧ ៨ ៩​ ០
    ១២៣
    ០៤ ១០៤៤
    ១២៣៤៥៦៧៨៩០
    012543876
    012 543 876
    ២០២៤
    ថ្ងៃទី ២៣ ខែមិថុនា បានបង្ហោះសារយ៉ាងដូច្នេះថា៖ «Thanks y'all for 600K views and Trending #1 on YouTube »។
"""

res = []
for t in text.split('\n'):
    res.append(num_normalize(t))

with open("result.txt", "w", encoding="utf-8") as file:
    file.write("\n".join(res))