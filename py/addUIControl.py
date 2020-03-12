import random
import addRandomUI
#------------控件作为参数--------------
def addTheControlAsParam(controlName, paraName):
    #print(controlName)
    funcstr = ''
    if controlName == 'UISwitch':
        funcstr +=addUISwitchAsParam(paraName)
    elif controlName == "UILabel":
        funcstr +=addUILabelAsParam(paraName)
    elif controlName == "UIButton":
        funcstr +=addUIButtonAsParam(paraName)
        
    return funcstr
#添加UISWITCH
def addUISwitchAsParam(paraName):
    funcstr = ""
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
    if CheckIsTrue() == True:
        funcstr += AddisEnabled(paraName)
    if CheckIsTrue() == True:
        funcstr += AddisHightLighted(paraName)
       
    #----------------------
    funcstr += "\t}else{\n\t\t" + paraName + " = [[UISwitch alloc] init];\n\t}"
    funcstr += '\n'
    return funcstr

def addUILabelAsParam(paraName):
    funcstr = ""
    if CheckIsTrue() == True:
        funcstr += AddCheckLabelInst(paraName)
    if CheckIsTrue() == True:
        funcstr += AddLabelText(paraName)
    if CheckIsTrue() == True:
        funcstr += AddShadowOffSet(paraName)
    if CheckIsTrue() == True:
        funcstr += AddHighLightedTextColor(paraName)
    if CheckIsTrue() == True:
        funcstr += AddLabelFont(paraName)
    if CheckIsTrue() == True:
        funcstr += AddTextAlignment(paraName)
    return funcstr

def addUIButtonAsParam(paraName):
    funcstr = ""
    #UISwitch begin
    funcstr += '\t if(' + paraName + ' !=nil){\n'
    #------------添加中间属性
    #add onTintColor
    if CheckIsTrue() == True:
        funcstr += AddCheckButtonInst(paraName)
    if CheckIsTrue() == True:
        funcstr += AddBtnTitle(paraName)
    funcstr += AddBtnColor(paraName)
    funcstr += AddBtnFont(paraName)      
    #----------------------
    funcstr += "\t}else{\n\t\t" + paraName + " = [[UIButton alloc] init];\n\t}"
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

#----uibutton
def AddCheckButtonInst(paramName):
    funcstr = ''
    funcstr += '\t\tif(' + paramName + ' == nil) {\n'
    funcstr += '\t\t\t' + paramName + ' = [[UIButton alloc] init];\n'
    funcstr += '\t\t}\n'
    return funcstr

def AddBtnColor (paraName):
    funcstr = ""
    funcstr += '\t\t[' + paraName + " setTitleColor : [UIColor colorWithRed:" + str(random.randint(1, 255)) + \
                "/255.0 green:" + str(random.randint(1, 255)) + "/255.0 blue:" + str(random.randint(1, 255)) + \
                 "/255.0 alpha:1.0] forState:UIControlStateNormal];\n"
    return funcstr

def AddBtnTitle(paraName):
    funcstr = ""
    funcstr += '\t\t[' + paraName + "setTitle:@\"" + addRandomUI.getRandomWord() + "\"" + ' forState:UIControlStateNormal' + '];\n' 
    return funcstr   

def AddBtnFont (paraName):
    funcstr = ""
    funcstr += '\t\t' + paraName + ".titleLabel.font = [UIFont systemFontOfSize:" + str(random.randint(10,40)) + '];\n' 
    return funcstr   

#----uiswitch
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

def AddisEnabled (paramName):
    funcstr = ""
    funcstr +=  '\t\tif(!' + paramName + ".isEnabled){\n"
    funcstr +=  '\t\t}\n'
    return funcstr    

def AddisHightLighted(paramName):
    funcstr = ""
    funcstr +=  '\t\tif(!' + paramName + ".isHighlighted){\n"
    funcstr +=  '\t\t}\n'
    return funcstr  
#----label
def AddCheckLabelInst(paramName):
    funcstr = ''
    funcstr += '\t\tif(' + paramName + ' == nil) {\n'
    funcstr += '\t\t\t' + paramName + ' = [[UILabel alloc] init];\n'
    funcstr += '\t\t}\n'
    return funcstr

def AddLabelText (paramName):
   
    funcstr = ""
    funcstr +=  '\t\t' + paramName + ".text = @" + "\"" +addRandomUI.getRandomWord() + "\"" +";\n"
    return funcstr      

def AddShadowOffSet (paramName):
    funcstr = ""
    funcstr =  '\t\t' + paramName + ".shadowOffset = CGSizeMake(" + str(random.randint(10,20)) + "," + str(random.randint(25,50)) +");\n" 
    return funcstr   

def AddHighLightedTextColor(paramName):
    funcstr = ""
    funcstr =  '\t\t' + paramName + ".highlightedTextColor = [UIColor colorWithRed:" + str(random.randint(1, 255)) + \
                "/255.0 green:" + str(random.randint(1, 255)) + "/255.0 blue:" + str(random.randint(1, 255)) + \
                 "/255.0 alpha:1.0];\n"
    return funcstr  

def AddLabelFont (paramName):
    funcstr = ""
    funcstr += '\t\t[' + paramName + ' setFont:[UIFont systemFontOfSize:' + str(random.randint(2,22)) + ']];\n'
    return funcstr   

def AddTextAlignment (paramName):
    funcstr = ""
    funcstr += '\t\t[' + paramName + ' setTextAlignment:UITextAlignmentCenter];\n'
    return funcstr   

def CheckIsTrue():
    _tmpRandom = random.randint(0, 1)

    if _tmpRandom == 0:
        return True
    else:
        return False
#-------------------------------------
