def decodeMorse(morseCode):
    new_word_list=[]
    for word in morseCode.split("   "):
        #'.... . -.--'
        convert_word=''.join([MORSE_CODE[i] for i in word.split(" ")])
        #[HEY]
        new_word_list.append(convert_word)
    return new_word_list
             
MORSE_CODE={'....':'H','.':'E','-.--':'Y','.---':'J','..-':'U','-..':'D'}
print(decodeMorse('.... . -.--   .--- ..- -.. .'))
print("".join([['HEY'],['J','U','D','E']]))

#强烈建议新建另一个文件，这样才有意义！
#还是缺少条理，拿到这道题该怎么解，但总而言之，看别人答案改代码都不能一次成功，而且还改了很久，以后还是自己把题解完吧，仔细想想，其实还是时间花的少了
#比如说 这道题的逻辑其实挺简单的，稍微梳理（当然也要时间），就是先将摩斯码转化为字母没有空格，但是又得知道词和词的缝隙，这是一个挺大的难点
#最后居然通过两次split解决了，很妙，还有 emm 等下次你就会知道了
    