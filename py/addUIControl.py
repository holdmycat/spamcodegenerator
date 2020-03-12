import random
import addRandomUI
#------------控件作为参数--------------
def addTheControlAsParam(controlName, paraName):
    #print(controlName)
    funcstr = ''
    if controlName == 'UISwitch':
        funcstr +=addUISwitchAsParam(paraName)
    return funcstr
#添加UISWITCH
def addUISwitchAsParam(paraName):
    funcstr = ""
    print("addUISwitchAsParam: " + paraName)
    #UISwitch begin
    funcstr += '\t if(' + paraName + ' !=nil){\n'
    #------------添加中间属性
    #add onTintColor
    if CheckIsTrue() == True:
        funcstr += AddOnTintColor(paraName)
    if CheckIsTrue() == True:
        funcstr += AddTintColor(paraName)
    if CheckIsTrue() == True:
        funcstr += AddAlpha(paraName)
    if CheckIsTrue() == True:
        funcstr += AddUIImage(paraName)
    #----------------------
    funcstr += "\t}else{\n\t\t" + paraName + " = [[UISwitch alloc] init];\n\t}"
    funcstr += '\n'
    return funcstr



#------------UI返回值处理---------------
def addTheControlAsReturn(controlName):
    #print(controlName)
    if controlName == 'UISwitch':
        addUISwitchAsReturn()

#添加UISWITCH
def addUISwitchAsReturn():
    print("addUISwitchAsParam")
#--------------------------------------




#--------------属性封装区---------------
def AddOnTintColor(paraName):
    funcstr = ""
    funcstr += '\t\t' + paraName + ".onTintColor = [UIColor colorWithRed:" + str(random.randint(1, 255)) + \
                "/255.0 green:" + str(random.randint(1, 255)) + "/255.0 blue:" + str(random.randint(1, 255)) + \
                 "/255.0 alpha:1.0];\n"
    return funcstr

def AddTintColor(paraName):
    funcstr = ""
    funcstr += '\t\t' + paraName + ".tintColor = [UIColor colorWithRed:" + str(random.randint(1, 255)) + \
                "/255.0 green:" + str(random.randint(1, 255)) + "/255.0 blue:" + str(random.randint(1, 255)) + \
                 "/255.0 alpha:1.0];\n"
    return funcstr

def AddAlpha (paramName):
    funcstr = ""
    funcstr +=  '\t\t' + paramName + ".alpha = 0.1;\n"
    return funcstr       

def AddUIImage (paramName):
    funcstr = ""
    #UIImage *img = [UIImage imageNamed:@"anyImageName”];
    imagename = addRandomUI.getRandomWord()
    imagename2 = addRandomUI.getRandomWord()
    funcstr +=  '\t\t' + 'UIImage *' + imagename + ' = [UIImage imageNamed:@'+ "\"" + imagename2 + "\"" + "];\n"
    funcstr +=  '\t\t' + paramName + ".onImage = " + imagename + ";\n"
    return funcstr    

def CheckIsTrue():
    _tmpRandom = random.randint(0, 1)

    if _tmpRandom == 0:
        return True
    else:
        return False
#-------------------------------------
