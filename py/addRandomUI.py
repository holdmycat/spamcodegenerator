# -*- coding: utf-8 -*-
# -*- author: zhaoxuefei -*-
# -*- date: 2020.03.10 -*-

import random
import addUIControl

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
    funcStruc = {}
    returnType = random.choice(g_typeArray)#return type
    funcName = getRandomWord()#func name
    paraNum = random.randint(1, g_variableNum)# parameter number
    
    paramArray = []
    for i in range(paraNum):
        tmpParamType = random.choice(g_typeArray)
        tmpParamName = getRandomWord()
        paramStru = {
            "type":tmpParamType,
            "name":tmpParamName
        }
        paramArray.append(paramStru)
    #for i in paraNum:
    funcStruc = {
        "returnType":returnType,
        "funcName":funcName,
        "paramNum":paraNum,
        "paramArray": paramArray
    }
   
    #append the function declaration
    funcDecla = '-' + funcStruc["returnType"] + funcStruc["funcName"] + ":"
    # tmpParamType = funcStruc["paramArray"][0]["type"]
    # tmpParamName = funcStruc["paramArray"][0]["name"]
    #funcDecla+= (tmpParamType + tmpParamName + " ")
    for i in range(funcStruc["paramNum"]):
        tmpParamType = funcStruc["paramArray"][i]["type"]
        tmpParamName = funcStruc["paramArray"][i]["name"]
        if i == 0:
            funcDecla += (tmpParamType) + tmpParamName + " "
        else :
            funcDecla += (tmpParamName) + ":" + (tmpParamType) + tmpParamName + " "
    funcDecla += ";"
    print (funcDecla)
    return {
        "fundecla":funcDecla,
        "funstruc": funcStruc
    }

def addRandomClassDefinition(funcstruc, finalHFileArray):
    returnType = funcstruc["returnType"]
    funcName = funcstruc["funcName"]#func name
    paraNum = funcstruc["paramNum"]
    #print(returnType)
    funcstr = '-' + returnType + funcName + ':'
    for i in range(paraNum):
        tmpParamType = funcstruc["paramArray"][i]["type"]
        tmpParamName = funcstruc["paramArray"][i]["name"]
        if i == 0:
            funcstr += (tmpParamType) + tmpParamName + " "
        else :
            funcstr += (tmpParamName) + ":" + (tmpParamType) + tmpParamName + " "
    funcstr += '{\n'

    #--------------------------- add function body

    # 在接口开头添加头文件类的实例化代码
    if len(finalHFileArray) > 1:
        _tmpIndex = random.randint(0, len(finalHFileArray) - 1)
        className = finalHFileArray[_tmpIndex].split('.')[0]
        print(className.split('.')[0])
        tmpParaName = getRandomWord()
        funcstr+= '\t' + className + ' * ' + tmpParaName + \
                ' = [[' + className + '] init];\n'
    
    #对参数进行属性随机设置
    for i in range(paraNum):   
        tmpParamType = funcstruc["paramArray"][i]["type"]
        tmpParamName = funcstruc["paramArray"][i]["name"]
        if tmpParamType == '(UISwitch*)' :
            funcstr+=addUIControl.addTheControlAsParam("UISwitch", tmpParamName)
        elif tmpParamType == '(UILabel*)' :
            funcstr+=addUIControl.addTheControlAsParam("UILabel", tmpParamName)
        elif tmpParamType == '(UIButton*)' :
            funcstr+=addUIControl.addTheControlAsParam("UIButton", tmpParamName)
        elif tmpParamType == '(UIControl*)' :
            funcstr+=addUIControl.addTheControlAsParam("UIControl", tmpParamName) 
        elif tmpParamType == '(UISlider*)' :
            funcstr+=addUIControl.addTheControlAsParam("UISlider", tmpParamName) 
        
    #根据接口返回类型，实例化返回值
    returnValue = getRandomWord()
    if returnType == '(UISwitch*)' :
        funcstr += ('\tUISwitch * ' + returnValue + ';\n')
        funcstr += ("\treturn " + returnValue + ';')
        
    funcstr += '\n}'

    return funcstr


def InitRandomGlobalData ():
    global g_typeArray
    #g_typeArray = ['(UIButton*)', '(UISwitch*)', '(UILabel*)','(UIControl*)']#, UISwitch, UILabel '(UIControl*)', '(UIFont*)'
    g_typeArray = ['(UISlider*)']#, UISwitch, UILabel '(UIControl*)', '(UIFont*)'
    global g_variableNum# 参数最大个数
    g_variableNum = 2


