# -*- coding: utf-8 -*-
# -*- author: zhaoxuefei -*-
# -*- date: 2020.03.10 -*-


import random
import os
import addRandomUI


# 获取文件中 @end 的总数量
def GetFileEndCount(file_path,old_str):
    #file_data = ""
    #print('filePath------'+file_path)
    Ropen=open(file_path,'r')#读取文件
    flagCount = 0
    for line in Ropen:
        if old_str in line:#如果.h文件中的某一行里包含old_str,则往这一行添加一下语句
            flagCount += 1
    return flagCount   

#.h文件添加废代码
def HFileAddCode(file_path,old_str,endTotalCount):
    # .h文件里属性的类型从这个数组里随机选
    classArray = ['NSString', 'UILabel', 'NSDictionary', 'NSData', 'UIScrollView', 'UIView', 'UITextView',
                  'UITableView', 'UIImageView']
    file_data = ""
    Ropen=open(file_path,'r')
    flagCount = 0
    for line in Ropen:
        #nameStr = addRandomUI.getRandomWord()
        #className = random.choice(classArray)

        if old_str in line:
            flagCount += 1
            if flagCount==endTotalCount:
                #file_data += '\n@property(nonatomic,strong) '+className +' *'+nameStr+';\n'
                file_data += (addRandomUI.addRandomClassDeclaration() + "\n")
            file_data += line
        else:
            file_data += line
    Ropen.close()
    Wopen=open(file_path,'w')
    Wopen.write(file_data)
    Wopen.close()


# .h file: add spam function declearation

#.m文件添加垃圾代码
def MFileAddCode(file_path,old_str,endTotalCount):
    file_data = ""
    #print('filePath------'+file_path)
    Ropen=open(file_path,'r')#读取文件
    flagCount = 0
    for line in Ropen:
        if old_str in line:
            flagCount += 1
            # 在最后一个 '@end' 前面加上垃圾代码
            if flagCount==endTotalCount:
                file_data += addRandomUI.addRandomClass() + '\n\n'
            file_data += line
        else:
            file_data += line
    Ropen.close()
    Wopen=open(file_path,'w')
    Wopen.write(file_data)
    Wopen.close()
    


def AddFunctionHFile(file_path,file_dir, old_str):
    #print("file_dir: " + file_dir)
    file_data = ""
    Ropen=open(file_path,'r')
    flagCount = 0
    fundata = {} 

    hFileNameArray = []#当前文件通目录下的其他.h文件名称数组
    for file_name in os.listdir(file_dir): 
        if '.h' in file_name:
            if file_path.find(file_name) == -1:
                hFileNameArray.append(file_name)
   
             
    hendTotalCount = GetFileEndCount(file_path, old_str)
    for line in Ropen:
        if old_str in line:
            flagCount += 1
            if flagCount==hendTotalCount:
                fundata = addRandomUI.addRandomClassDeclaration()
                file_data += (fundata["fundecla"] + "\n")            
            file_data += line
        else:
            file_data += line
    Ropen.close()
    Wopen=open(file_path,'w')
    Wopen.write(file_data)
    Wopen.close()
    fundata["hFileArray"] = hFileNameArray
    return fundata

def AddFunctionMFile(hfile_path, old_str, funstruc, hFileArray):
    mfiledata = ""
    mfilepath = hfile_path.replace(".h", ".m")   
    flagCount = 0
    headerFlatCount = 0
    headStr = "#import"
    hendTotalCount = GetFileEndCount(mfilepath, old_str)
    finalHFileArray = []#最终真正添加到当前文件的#import头 
    curHFileStr = ""
    #add import header
    try:
        mfopen = open(mfilepath, 'r')
        for line in mfopen:
            if headStr in line:
                curHFileStr+=(line + "\r")
        mfopen.close()
        mfopen = open(mfilepath, 'r')
        for line in mfopen:
            if headStr in line:
                if headerFlatCount == 0 and len(hFileArray) > 1:     
                        randomNum = random.randint(1, len(hFileArray))
                        for i in range(randomNum):
                            if curHFileStr.find(hFileArray[i]) == -1:
                                finalHFileArray.append(hFileArray[i])
                                mfiledata+= ("#import \"" + hFileArray[i] + "\"" + '\n')
                mfiledata += line
                headerFlatCount+=1
            else:
                mfiledata += line
        mfopen.close()
        Wopen=open(mfilepath,'w')
        Wopen.write(mfiledata)
        Wopen.close()     
    except IOError:
        print("File not accessible")
    finally:
        mfopen.close()
    
    #add import function
    mfiledata = ""
    try:
        mfopen = open(mfilepath, 'r')
        for line in mfopen:
            if old_str in line:
                flagCount += 1
                if flagCount==hendTotalCount:
                    mfiledata +=  (addRandomUI.addRandomClassDefinition(funstruc, finalHFileArray) + "\n")            
                mfiledata += line
            else:
                mfiledata += line
        mfopen.close()
        Wopen=open(mfilepath,'w')
        Wopen.write(mfiledata)
        Wopen.close()     
    except IOError:
        print("File not accessible")
    finally:
        mfopen.close()

def addCode(file_path, file_dir):
    global codeCount
    if '.h' in file_path:  # file_dir+'/'+file含义是file_dir文件夹下的file文件
        # 获取文件中 @end 的总数量，在最后一个 @end 前面添加垃圾代码 
        
        for num in range(codeCount):
            #print("file path: " + file_path)
            fundata = AddFunctionHFile(file_path, file_dir, "@end")
            AddFunctionMFile(file_path, "@end", fundata["funstruc"],fundata["hFileArray"])
            #print(file_path)
            
            #print(funcStruc)
    # if '.m' in file_path:
    #     mCount = GetFileEndCount(file_path,"@end")
    #     for num in range(codeCount):
    #         MFileAddCode(file_path, "@end", mCount)



# 循环递归遍历文件夹
def traverse(file_dir):
    fs = os.listdir(file_dir)
    #print(fs)
    for dir in fs:
        tmp_path = os.path.join(file_dir, dir)
        #print("tmp_path:" + tmp_path) 
        if not os.path.isdir(tmp_path):
            addCode(tmp_path, file_dir)    
        else:
            # 是文件夹,则递归调用
            traverse(tmp_path)


def addRubbish():
    global codeCount
    # 每个文件中添加的代码数量
    codeCount = 1
    # 主工程目录
    file_prefix = '../testcode/'
    # 要添加垃圾代码文件所在的文件夹路径
    #file_dirs = ['testcode',"Views","Models"]
    file_dirs = ['testSpamCode']
    for dir in file_dirs:
            file_dir = file_prefix + dir
            traverse(file_dir)
        

def main():
    addRubbish()
    print('add code success')


if __name__ == '__main__':
    main()
