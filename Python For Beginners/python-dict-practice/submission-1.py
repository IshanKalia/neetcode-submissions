from typing import Dict # this adds type hinting for Dict

def count_characters(word: str) -> Dict[str, int]:
    dict_count = {}
    for i in word: 
        if i not in dict_count:
            dict_count[i] = 0
        dict_count[i] += 1
    return dict_count
    


# don't modify below this line
print(count_characters("hello"))
print(count_characters("world"))
print(count_characters("hello world"))
print(count_characters("this is a longer sentence"))
