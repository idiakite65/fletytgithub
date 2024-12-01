from flet import *
def main(page:Page):
    ########window pro======
    page.title=("Ismail")
    page.window.height = 740
    page.window.width= 390
    page.window.top = 10
    page.window.left = 960
    page.vertical_alignment="center"
    page.horizontal_alignment="center"
    ####### appbar star ##########
    page.appbar = AppBar(
        bgcolor=colors.RED,
        title= Text("Ismail Diakite"),
        center_title= True,
        leading=Icon(icons.HOME),
        leading_width=40,
        actions=[
            IconButton(icons.NOTIFICATIONS),
            PopupMenuButton(
                items=[
                    PopupMenuItem(text='الملف الشخصي'),
                    PopupMenuItem(text='اعدادات التطبيق'),
                    PopupMenuItem(text='من نحن'),
                    PopupMenuItem(),
                    PopupMenuItem(text='اغلاق التطبيق'),
                ]
            )
        ]
    )
    ####### appbar end ###########

    ######### Tools #######
    def show(e):
        v1 = on1.value #ismail
        v2 = on2.value #23011965
        if v1 == 'ismail' and v2 == '23011965':
            alert1 = AlertDialog(
                title= Text("Welcom admin", size=18, color='green')                
            )
            page.overlay.append(alert1)
            alert1.open =True
            page.update()
        else:
            alert1 = AlertDialog(
                title= Text("Date Error", size=18, color='red')                
            )
            page.overlay.append(alert1)
            alert1.open =True
            page.update()

    image = Image(src="alfarouk.png", width=170)
    text = Text("لوحة تسجيل الدخول", color="black", size=20)
    
    on1 = TextField(label='Email(البريد الالكتروني)', icon=icons.EMAIL)
    on2 = TextField(label='Password(كلمة المرور)', icon=icons.PASSWORD, password=True, can_reveal_password=True)
    btn1 = ElevatedButton('Login - الدخول للحساب', on_click=show)

    page.add(image, text, on1, on2, btn1)
    ###### ButtonBar ########
    page.navigation_bar = CupertinoNavigationBar(
        bgcolor=colors.RED,
        inactive_color=colors.BLACK,
        destinations=[
            NavigationBarDestination(icon=icons.CALL, label='اتصال'), 
            NavigationBarDestination(icon=icons.CAMERA, label='كامسرا'),
            NavigationBarDestination(icon=icons.CONTACT_PHONE, label='جهات الاتصال')
        ]
    )
    #########################

    page.update()
app(main)
