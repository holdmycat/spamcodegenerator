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
    elif controlName == "UIControl":
        funcstr +=addUIControlAsParam(paraName)
    elif controlName == "UISlider":
        funcstr +=addUISliderAsParam(paraName)
         
    return funcstr
#添加UISWITCH,UILabel, UIButton, UIControl, UISlider
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
    funcstr += AddCheckButtonInst(paraName)
    funcstr += AddBtnTitle(paraName)
    funcstr += AddBtnColor(paraName)
    funcstr += AddBtnFont(paraName)      
    #----------------------
    funcstr += "\t}else{\n\t\t" + paraName + " = [[UIButton alloc] init];\n\t}"
    funcstr += '\n'
    return funcstr

def addUIControlAsParam(paraName):
    funcstr = ""
    #UISwitch begin
    funcstr += '\t if(' + paraName + ' !=nil){\n'
    #------------添加中间属性
    #add onTintColor
    funcstr += AddCheckControlInst(paraName)
    funcstr += AddControlBGColor(paraName)
    funcstr += AddControlAlignment(paraName)
    funcstr += AddControlAlpha(paraName)      
    #----------------------
    funcstr += "\t}else{\n\t\t" + paraName + " = [[UIControl alloc] init];\n\t}"
    funcstr += '\n'
    return funcstr

def addUISliderAsParam(paraName):
    funcstr = ""
    #UISwitch begin
    funcstr += '\t if(' + paraName + ' !=nil){\n'
    #------------添加中间属性
    funcstr += AddCheckSliderInst(paraName)
    funcstr += AddUISliderTag(paraName)
    funcstr += AddControlAlignment(paraName)
    funcstr += AddUISliderMin(paraName)      
    #----------------------
    funcstr += "\t}else{\n\t\t" + paraName + " = [[UISlider alloc] init];\n\t}"
    funcstr += '\n'
    return funcstr


#------------UI返回值处理---------------
def addTheControlAsReturn(controlName, returnValue):
    #print(controlName)
    funcstr = ''
    if controlName == 'UISwitch':
        funcstr +=addUISwitchAsReturn(returnValue)
    elif controlName == 'UIButton':
        funcstr +=addUIButtonAsReturn(returnValue)
    elif controlName == 'UILabel':
        funcstr +=addUILabelAsReturn(returnValue)
    elif controlName == 'UIControl':
        funcstr +=addUIControlAsReturn(returnValue)
    elif controlName == 'UISlider':
        funcstr +=addUISliderAsReturn(returnValue)
    return funcstr

#['(UIButton*)', '(UISwitch*)', '(UILabel*)','(UIControl*)','(UISlider*)']
#return: UISWITCH
def addUISwitchAsReturn(returnValue):
    funcstr = ''
    funcstr += ('\tUISwitch * ' + returnValue + '= [[UISwitch alloc] init];\n')

    #添加中间代码
    funcstr += AddOnTintColor(returnValue)
    funcstr += AddTintColor(returnValue)
    funcstr += AddAlpha(returnValue)
    funcstr += AddUIImage(returnValue)
    funcstr += AddisEnabled(returnValue)
    funcstr += AddisHightLighted(returnValue)
    
    funcstr += ("\treturn " + returnValue + ';')
    funcstr += '\n}'
    return funcstr

#return: UIButton
def addUIButtonAsReturn(returnValue):
    funcstr = ''
    funcstr += ('\tUIButton * ' + returnValue + '= [[UIButton alloc] init];\n')

    #添加中间代码
    funcstr += AddBtnColor(returnValue)
    funcstr += AddBtnTitle(returnValue)
    funcstr += AddBtnFont(returnValue)
    
    
    funcstr += ("\treturn " + returnValue + ';')
    funcstr += '\n}'
    return funcstr

#return: UILabel
def addUILabelAsReturn(returnValue):
    funcstr = ''
    funcstr += ('\tUILabel * ' + returnValue + '= [[UILabel alloc] init];\n')

    #添加中间代码
    funcstr += AddLabelText(returnValue)
    funcstr += AddShadowOffSet(returnValue)
    funcstr += AddHighLightedTextColor(returnValue)
    funcstr += AddLabelFont(returnValue)
    funcstr += AddTextAlignment(returnValue)
    
    
    funcstr += ("\treturn " + returnValue + ';')
    funcstr += '\n}'
    return funcstr

#return UIControl
def addUIControlAsReturn(returnValue):
    funcstr = ''
    funcstr += ('\tUIControl * ' + returnValue + '= [[UIControl alloc] init];\n')

    #添加中间代码
    funcstr += AddControlBGColor(returnValue)
    funcstr += AddControlAlignment(returnValue)
    funcstr += AddControlAlpha(returnValue)
       
    funcstr += ("\treturn " + returnValue + ';')
    funcstr += '\n}'
    return funcstr

#return UISlider
def addUISliderAsReturn(returnValue):
    funcstr = ''
    #开头代码
    funcstr += ('\tUISlider * ' + returnValue + '= [[UISlider alloc] init];\n')

    #添加中间代码
    funcstr += AddUISliderTag(returnValue)
    funcstr += AddUISliderMin(returnValue)
    
    #尾部代码
    funcstr += ("\treturn " + returnValue + ';')
    funcstr += '\n}'
    return funcstr
#--------------------------------------

#--------------属性封装区---------------

#----uislider
def AddCheckSliderInst(paramName):
    funcstr = ''
    funcstr += '\t\tif(' + paramName + ' == nil) {\n'
    funcstr += '\t\t\t' + paramName + ' = [[UISlider alloc] init];\n'
    funcstr += '\t\t}\n'
    return funcstr

def AddUISliderTag (paraName):
    funcstr = ""
    funcstr += '\t\t' + paraName + ".tag = " + str(random.randint(1, 400)) + ";\n"
    return funcstr   

def AddUISliderMin (paraName):
    funcstr = ""
    funcstr += '\t\t' + paraName + ".minimumValue = " + str(random.randint(0, 13)) + ";\n"
    return funcstr 

#----uicontorl
def AddCheckControlInst(paramName):
    funcstr = ''
    funcstr += '\t\tif(' + paramName + ' == nil) {\n'
    funcstr += '\t\t\t' + paramName + ' = [[UIControl alloc] init];\n'
    funcstr += '\t\t}\n'
    return funcstr

def AddControlBGColor(paraName):
    funcstr = ""
    funcstr += '\t\t' + paraName + ".backgroundColor = [UIColor colorWithRed:" + str(random.randint(1, 255)) + \
                "/255.0 green:" + str(random.randint(1, 255)) + "/255.0 blue:" + str(random.randint(1, 255)) + \
                 "/255.0 alpha:1.0];\n"
    return funcstr    

def AddControlAlignment(paraName):
    funcstr = ""
    funcstr += '\t\t' + paraName + ".contentVerticalAlignment = UIControlContentVerticalAlignmentCenter;\n"
    return funcstr   

def AddControlAlpha (paraName):
    funcstr = ""
    funcstr += '\t\t' + paraName + ".alpha = 0." + str(random.randint(0,10)) + ";\n"
    return funcstr  

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
    funcstr += '\t\t[' + paraName + " setTitle:@\"" + addRandomUI.getRandomWord() + "\"" + ' forState:UIControlStateNormal' + '];\n' 
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
