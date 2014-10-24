import easygui

#消息框
user_response = easygui.msgbox("Hello world!")
print(user_response)

#按钮框
flavor = easygui.buttonbox("What is you favorite icecream flavor?", choices = ['icecream1', 'ice2', 'ice3'])
easygui.msgbox("You picked " + flavor)

#选择框
flavor = easygui.choicebox("What is you favorite icecream flavor?", choices = ['icecream1', 'ice2', 'ice3'])
easygui.msgbox("You picked " + flavor)

#输入框
flavor = easygui.enterbox("What is you favorite icecream flavor?", default='auto')
easygui.msgbox("You picked " + flavor)

#整数框
easygui.