#
# name-divination
# 한글 이름 궁합 프로그램
# Author: Ilhwan Hwang (https://github.com/IlhwanHwang/)
# Date: 18.05.11
#


consonent_first = ord('ㄱ')
consonent_last = ord('ㅎ')
vowel_first = ord('ㅏ')
vowel_last = ord('ㅣ')
syllable_first = ord('가')
syllable_last = ord('힣')

list_initial = ['ㄱ','ㄲ','ㄴ','ㄷ','ㄸ','ㄹ','ㅁ','ㅂ','ㅃ','ㅅ','ㅆ','ㅇ','ㅈ','ㅉ','ㅊ','ㅋ','ㅌ','ㅍ','ㅎ']
list_medial = ['ㅏ','ㅐ','ㅑ','ㅒ','ㅓ','ㅔ','ㅕ','ㅖ','ㅗ','ㅘ','ㅙ','ㅚ','ㅛ','ㅜ','ㅝ','ㅞ','ㅟ','ㅠ','ㅡ','ㅢ','ㅣ']
list_final = ['','ㄱ','ㄲ','ㄳ','ㄴ','ㄵ','ㄶ','ㄷ','ㄹ','ㄺ','ㄻ','ㄼ','ㄽ','ㄾ','ㄿ','ㅀ','ㅁ','ㅂ','ㅄ','ㅅ','ㅆ','ㅇ','ㅈ','ㅊ','ㅋ','ㅌ','ㅍ','ㅎ']

map_strokes = {
    '': 0, 
    'ㄱ': 2, 'ㄲ': 4, 'ㄳ': 4, 'ㄴ': 2, 'ㄵ': 5, 'ㄶ': 5, 'ㄷ': 3, 'ㄸ': 6 ,'ㄹ': 5, 'ㄺ': 7, 'ㄻ': 9, 'ㄼ': 9, 'ㄽ': 7, 
    'ㄾ': 9, 'ㄿ': 9, 'ㅀ': 8, 'ㅁ': 4, 'ㅂ': 4, 'ㅃ': 8, 'ㅄ': 6, 'ㅅ': 2, 'ㅆ': 4, 'ㅇ': 1, 'ㅈ': 3, 'ㅉ': 6 ,'ㅊ': 4, 
    'ㅋ': 3, 'ㅌ': 4, 'ㅍ': 4, 'ㅎ': 3,
    'ㅏ': 2, 'ㅐ': 3, 'ㅑ': 3, 'ㅒ': 4, 'ㅓ': 2, 'ㅔ': 3, 'ㅕ': 3, 'ㅖ': 4, 'ㅗ': 2, 'ㅘ': 4, 'ㅙ': 5, 'ㅚ': 3, 'ㅛ': 3, 
    'ㅜ': 2, 'ㅝ': 4, 'ㅞ': 5, 'ㅟ': 3, 'ㅠ': 3, 'ㅡ': 1, 'ㅢ': 2, 'ㅣ': 1
}

def sep(syl):
    uind = ord(syl)

    if uind >= consonent_first and uind <= consonent_last:
        return syl, '', ''

    elif uind >= vowel_first and uind <= vowel_last:
        return '', syl, ''

    elif uind >= syllable_first and uind <= syllable_last:
        ind = ord(syl) - syllable_first
        ind_final = ind % len(list_final)
        ind_medial = (ind // len(list_final)) % len(list_medial)
        ind_initial = (ind // len(list_final)) // len(list_medial)

        return list_initial[ind_initial], list_medial[ind_medial], list_final[ind_final]

    else:   # Not a korean syllable
        return '', '', ''


if __name__ == '__main__':

    from itertools import zip_longest

    name1 = input('첫번째 사람의 이름 >> ')
    name2 = input('두번째 사람의 이름 >> ')

    if abs(len(name1) - len(name2)) == 1:
        if len(name1) < len(name2):
            tmp = name1
            name1 = name2
            name2 = tmp

    if abs(len(name1) - len(name2)) > 1:
        print('궁합을 볼 수 없는 이름 글자 수 입니다.')
        exit()

    sep1 = [sum([map_strokes[s] for s in sep(c)]) % 10 for c in name1]
    sep2 = [sum([map_strokes[s] for s in sep(c)]) % 10 for c in name2]

    score = [s for s in sum(zip_longest(sep1, sep2, fillvalue=None), ()) if s is not None]
    names = [s for s in sum(zip_longest(name1, name2, fillvalue=None), ()) if s is not None]

    print('======================')
    print('  '.join(names))
    spaces = 1

    while True:
        print(' ' * spaces + '   '.join([str(s) for s in score]))

        if len(score) <= 2:
            break

        score_old = score
        score_new = []

        for i in range(len(score) - 1):
            score_new.append((score[i] + score[i + 1]) % 10)

        score = score_new
        spaces += 2

    print('======================')
    print('판정 결과: {}%'.format(score[0] * 10 + score[1]))
    print('======================')
