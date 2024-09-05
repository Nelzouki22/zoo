def is_similar_to_zoo(word):
    # تحقق من أن الكلمة تبدأ بحروف Z ثم حروف O
    if not word.startswith('z'):
        return "No"
    
    # حساب عدد حروف Z و O
    count_z = 0
    count_o = 0
    
    # عد عدد حروف Z
    while count_z < len(word) and word[count_z] == 'z':
        count_z += 1
    
    # عد عدد حروف O
    while count_o < len(word) - count_z and word[count_z + count_o] == 'o':
        count_o += 1
    
    # تحقق من أن كل الأحرف بعد حروف Z هي حروف O فقط
    if count_z + count_o == len(word) and count_o >= count_z:
        return "Yes"
    else:
        return "No"

# قراءة الكلمة المدخلة
word = input().strip()

# طباعة النتيجة
print(is_similar_to_zoo(word))

