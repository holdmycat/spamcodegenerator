# -*- coding: utf-8 -*-

import random


# 产生一个satrtIndex到endIndex位长度的随机字符串
def getRandomStr(satrtIndex,endIndex):
    numbers = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    # random.choice()从列表中返回一个随机数
    final = (random.choice(numbers))
    # 从(50,100)列表中取出一个随机数
    index = random.randint(satrtIndex, endIndex)
    for i in range(index):
        final += (random.choice(numbers))
    return final


def getRandomWord():
    file_path = 'word.txt'
    try:
        f = open(file_path, 'r+')
        lines = f.readlines()
        return random.choice(lines).strip()
    except Exception as e:
        print(e)

# name = getRandomWord()(50,100)
# word = getRandomWord()
# print(word)


# 生成NSString类
def addNSString():
    line = '- (NSString *)' + getRandomWord() + ':(NSString *)' + getRandomWord() + ' {\n   '
    stringName = getRandomWord()
    string = 'NSString *' + stringName + ' = @"' + getRandomWord() + '";\n   return '+ stringName + ';\n}'
    return line+string + '\n\n'

# 生成NSArray类
def addNSArray():
    line = '- (NSArray *)' + getRandomWord() + ':(NSArray *)' + getRandomWord() + ' {\n   '
    arrayName = getRandomWord()
    arrayString = 'NSArray *' + arrayName + ' = @[\n'
    for i in range(1,15):
        element = '     @"' + getRandomWord() + '",\n'
        arrayString += element
    arrayString += '  ];\n    return ' + arrayName + ';\n}'
    return line + arrayString


# 生成NSData类
def addNSData():
    line = '- (NSData *)' + getRandomWord() + ':(NSString *)' + getRandomWord() + ' {\n   '
    dataName = getRandomWord()
    string = 'NSData *' + dataName + ' = [@"' + getRandomWord() + '"' + ' dataUsingEncoding:NSUTF8StringEncoding]' + ';\n   return '+ dataName + ';\n}'
    return line+string


# 生成NSArray类
def addNSDictionary():
    line = '- (NSDictionary *)' + getRandomWord() + ':(NSArray *)' + getRandomWord() + ' {\n   '
    dictName = getRandomWord()
    dictString = 'NSDictionary *' + dictName + ' = @{\n'
    for i in range(1,10):
        element = '      @"' + getRandomWord() + '" : ' + '@"' + getRandomWord() + '",\n'
        dictString += element

    dictString += '  };\n    return ' + dictName + ';\n}'
    return line + dictString


# 生成UIImage类
def addUIImage():
    line = '- (UIImage *)' + getRandomWord() + ':(UIImage *)' + getRandomWord() + ' {\n   '
    dataName = getRandomWord()
    imageName = getRandomWord()
    string = 'NSData *' + dataName + ' = [@"' + getRandomWord() + '"' + ' dataUsingEncoding:NSUTF8StringEncoding]' + ';\n   '
    string += 'UIImage *' + imageName + ' = [UIImage imageWithData:' + dataName + '];\n   '
    string += 'return '+ imageName + ';\n}'

    return line+string + '\n\n'


# 随机调用(addNSString(),addNSArray(),addNSData(),addNSDictionary(),addUIImage())中的某个函数
def addRandomClass():
    index = random.randint(1, 5)
    if index == 1:
        string = addNSString()
    elif index == 2:
        string = addNSArray()
    elif index == 3:
        string = addNSData()
    elif index == 4:
        string = addNSDictionary()
    else:
        string = addUIImage()
    return string

def addRandomClassDeclaration():
    typeArray = ['(UISwitch*)', '(UIControl*)', '(UIFont*)']
    returnType = random.choice(typeArray)#return type
    funcName = getRandomWord()#func name
    paraNum = random.randint(1, 5)# parameter number
    #for i in paraNum:










