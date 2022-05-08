#Importing the library
import datetime as time
from tkinter import Canvas
import sqlite3
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
# set up
w,h = 1000,700
# splash window
splash_win = Tk()
startimage= PhotoImage(file="image\mainprogram\startimage.png")
startlogo= PhotoImage(file="image\mainprogram\logo_app.png")
splash_win.title("Splash Screen")
x = splash_win.winfo_screenwidth()/2 - 400/2
y = splash_win.winfo_screenheight()/2 - 250/2
splash_win.geometry("%dx%d+%d+%d"%(400,250,x,y))
splash_win.overrideredirect(True)
splash_win.configure(bg='#FFFFFF')
image = Label(splash_win,image=startimage)
image.place(x=-2,y=-2)
# def start program
def Startprogram():
    splash_win.destroy()
    root= Tk()
    root.title("BOOKAQ APPLICATION")
    x = root.winfo_screenwidth()/2 - w/2
    y = root.winfo_screenheight()/2 - h/2
    root.geometry("%dx%d+%d+%d"%(w,h,x,y))
    root.resizable(FALSE,False)
    root.option_add('*font',"Calibri 20")
    # photo
    def photoimage_inloginpage() : # รูปทั้งหมด
        global main_picture
        def main_picture() :
            global signinpage_pic1 ,logoapp , searchbar1 , searchbar2, photobutton_hotel , photobutton_resta , photobutton_dessert , text_cate , text_sugg , button_home_activate , button_q_not , picbutton_search ,button_wallet_not , button_fav_not , quit_button , button_home_not , button_q_activate , button_wallet_activate , button_fav_activate,admin_login,yayoishop_header,yayoishop_logo,admin_yayoi_frame_1,admin_yayoi_frame_2,admin_yayoi_table,admin_yayoi_table_1,admin_yayoi_table_2,admin_yayoi_table_3,admin_yayoi_table_4,admin_yayoi_table_5,button_yellow,teble_green_act,teble_green_not,teble_red_act,teble_red_not,teble_yellow_act,teble_yellow_not,frameshop_yyo,frameshop_aty,queue_yayoi,amountpeople,amountpeople_1,yayoishop_whiteframe_1,yayoishop_whiteframe_2,yayoishop_but_orders,yayoishop_but_staff,yayoishop_cate_frame_1,yayoishop_cate_frame_2,yayoishop_but_menu,yayoishop_mart_photo,yayoishop_payment_1,yayoishop_payment_2,yayoishop_payment_3,yayoishop_confirm,yayoishop_menuset_1,yayoishop_menuset_2,yayoishop_menuset_3,yayoishop_menuset_4,yayoishop_menuset_5,yayoishop_menuset_6,yayoishop_menuset_7,yayoishop_menuset_8,yayoishop_menuset_9,yayoishop_menuset_10,yayoishop_menuset_11,yayoishop_menuset_12,yayoishop_menuset_13,yayoishop_menuset_14,yayoishop_menuset_15,yayoishop_menuset_16,yayoishop_menuset_17,yayoishop_menuset_18,yayoishop_menuset_19,yayoishop_menuset_20,yayoishop_menuset_21,yayoishop_menuset_22,yayoishop_menuset_23,yayoishop_menuset_24,yayoishop_menuset_25,yayoishop_menuset_26,yayoishop_menuset_27,yayoishop_menuset_28,yayoishop_menuset_29,yayoishop_menuset_30,yayoishop_menuset_31,yayoishop_menuset_32,yayoishop_menuset_33,yayoishop_menuset_34,yayoishop_menuset_35,yayoishop_menuset_36,yayoishop_menuset_37,yayoishop_menuset_38,yayoishop_menuset_39,yayoishop_menuset_41,yayoishop_menuset_42,yayoishop_menuset_43,yayoishop_menuset_44,yayoishop_menuset_45,yayoishop_menuset_46,yayoishop_menuset_47,yayoishop_menuset_48,yayoishop_menuset_49,yayoishop_menuset_50,yayoishop_red_status,yayoishop_yellow_status,yayoishop_green_status,yayoishop_yayoishop_payout,staff_cal,queue_frame,frameshop_okj,frameshop_afteryum,frameshop_kyo , frameshop_code,frameshop_shin,registop,regisbel
            #
            registop = PhotoImage(file="image/mainprogram/registop.png")
            regisbel = PhotoImage(file="image/mainprogram/regisbelow.png")
            #
            signinpage_pic1 = PhotoImage(file="image/mainprogram/loginpage.png")
            admin_login = PhotoImage(file="image/mainprogram/adminloginpage.png")
            logoapp = PhotoImage(file="image/mainprogram/logo_app.png")
            searchbar1 = PhotoImage(file="image/mainprogram/searchbar.png")
            searchbar2 = PhotoImage(file="image/mainprogram/searchbar2.png")
            photobutton_hotel = PhotoImage(file="image/mainprogram/button_hotel.png")
            photobutton_resta = PhotoImage(file="image/mainprogram/button_resta.png")
            photobutton_dessert = PhotoImage(file="image/mainprogram/button-dessert.png")
            text_cate = PhotoImage(file="image/mainprogram/text_Category.png")
            text_sugg = PhotoImage(file="image/mainprogram/text_suggest.png")
            picbutton_search = PhotoImage(file="image/mainprogram/button-search.png")
            quit_button = PhotoImage(file="image/mainprogram/button_quit.png")
            # shopframe food
            frameshop_yyo = PhotoImage(file="image/mainprogram/shop-yayoi.png") # finish
            frameshop_shin = PhotoImage(file="image/mainprogram/shop-shin.png")
            # shopframe dess
            frameshop_aty = PhotoImage(file="image/mainprogram/shop-afteryou.png") # finish
            frameshop_kyo = PhotoImage(file="image/mainprogram/shop-kyo.png") # finish
            frameshop_code = PhotoImage(file="image/mainprogram/shop-code.png") # finish
            frameshop_okj = PhotoImage(file="image/mainprogram/shop-ohkaju.png") 
            frameshop_afteryum = PhotoImage(file="image/mainprogram/shop-afteryum.png")
            queue_frame = PhotoImage(file="image/mainprogram/queue_frame.png")
            # act
            button_home_activate = PhotoImage(file="image/mainprogram/button_home.png").subsample(1,1)
            button_q_activate = PhotoImage(file="image/mainprogram/button_q_1.png").subsample(1,1)
            button_wallet_activate = PhotoImage(file="image/mainprogram/button_wallet_1.png").subsample(1,1)
            button_fav_activate = PhotoImage(file="image/mainprogram/button_fav_1.png").subsample(1,1)
            # not act
            button_home_not = PhotoImage(file="image/mainprogram/button_home_1.png").subsample(1,1)
            button_wallet_not = PhotoImage(file="image/mainprogram/button_wallet.png").subsample(1,1)
            button_q_not = PhotoImage(file="image/mainprogram/button_q.png").subsample(1,1)
            button_fav_not = PhotoImage(file="image/mainprogram/button_fav.png").subsample(1,1)
            # yayoi
            staff_cal = PhotoImage(file="image/mainprogram/staffcall.png").subsample(2,2)
            queue_yayoi = PhotoImage(file="image/mainprogram/queue_yayoi.png").subsample(1,1)
            teble_green_act = PhotoImage(file="image/mainprogram/table-green-act.png").subsample(1,1)
            teble_green_not = PhotoImage(file="image/mainprogram/table-green-not.png").subsample(1,1)
            teble_red_act = PhotoImage(file="image/mainprogram/table-red-act.png").subsample(1,1)
            teble_red_not = PhotoImage(file="image/mainprogram/table-red-not.png").subsample(1,1)
            teble_yellow_act = PhotoImage(file="image/mainprogram/table-yellow-act.png").subsample(1,1)
            teble_yellow_not = PhotoImage(file="image/mainprogram/table-yellow-not.png").subsample(1,1)
            # YAYOI SHOP
            amountpeople = PhotoImage(file="image/mainprogram/amountpeople.png").subsample(1,1) 
            amountpeople_1 = PhotoImage(file="image/mainprogram/amountpeople_1.png").subsample(1,1) 
            yayoishop_header = PhotoImage(file="image/Yayoi-shop/header.png").subsample(1,1)
            yayoishop_logo = PhotoImage(file="image/Yayoi-shop/logo-yayoi.png").subsample(1,1)
            button_yellow = PhotoImage(file="image/mainprogram/admin-menubar.png").subsample(1,1)
            yayoishop_whiteframe_1 = PhotoImage(file="image/Yayoi-shop/whiteframe-1.png").subsample(1,1)
            yayoishop_whiteframe_2 = PhotoImage(file="image/Yayoi-shop/whiteframe-2.png").subsample(1,1)
            yayoishop_but_orders = PhotoImage(file="image/Yayoi-shop/button_orders.png").subsample(1,1)
            yayoishop_but_staff = PhotoImage(file="image/Yayoi-shop/button_staffcall.png").subsample(1,1)
            yayoishop_cate_frame_1 = PhotoImage(file="image/Yayoi-shop/categagory_frame.png").subsample(1,1)
            yayoishop_cate_frame_2 = PhotoImage(file="image/Yayoi-shop/categagory_frame_1.png").subsample(1,1)
            yayoishop_but_menu = PhotoImage(file="image/Yayoi-shop/button_menu.png").subsample(1,1)
            yayoishop_mart_photo = PhotoImage(file="image/Yayoi-shop/martphoto.png")
            yayoishop_payment_1 = PhotoImage(file="image/Yayoi-shop/payment_frame.png")
            yayoishop_payment_2 = PhotoImage(file="image/Yayoi-shop/payment_frame_2.png")
            yayoishop_payment_3 = PhotoImage(file="image/Yayoi-shop/payment_frame_3.png")
            yayoishop_confirm = PhotoImage(file="image/Yayoi-shop/Confirm.png")
            yayoishop_menuset_1 = PhotoImage(file="image/Yayoi-shop/menuset_1.png")
            yayoishop_menuset_2 = PhotoImage(file="image/Yayoi-shop/menuset_2.png")
            yayoishop_menuset_3 = PhotoImage(file="image/Yayoi-shop/menuset_3.png")
            yayoishop_menuset_4 = PhotoImage(file="image/Yayoi-shop/menuset_4.png")
            yayoishop_menuset_5 = PhotoImage(file="image/Yayoi-shop/menuset_5.png")
            yayoishop_menuset_6 = PhotoImage(file="image/Yayoi-shop/menuset_6.png")
            yayoishop_menuset_7 = PhotoImage(file="image/Yayoi-shop/menuset_7.png")
            yayoishop_menuset_8 = PhotoImage(file="image/Yayoi-shop/menuset_8.png")
            yayoishop_menuset_9 = PhotoImage(file="image/Yayoi-shop/menuset_9.png")
            yayoishop_menuset_10 = PhotoImage(file="image/Yayoi-shop/menuset_10.png")
            yayoishop_menuset_11 = PhotoImage(file="image/Yayoi-shop/menuset_11.png")
            yayoishop_menuset_12 = PhotoImage(file="image/Yayoi-shop/menuset_12.png")
            yayoishop_menuset_13 = PhotoImage(file="image/Yayoi-shop/menuset_13.png")
            yayoishop_menuset_14 = PhotoImage(file="image/Yayoi-shop/menuset_14.png")
            yayoishop_menuset_15 = PhotoImage(file="image/Yayoi-shop/menuset_15.png")
            yayoishop_menuset_16 = PhotoImage(file="image/Yayoi-shop/menuset_16.png")
            yayoishop_menuset_17 = PhotoImage(file="image/Yayoi-shop/menuset_17.png")
            yayoishop_menuset_18 = PhotoImage(file="image/Yayoi-shop/menuset_18.png")
            yayoishop_menuset_19 = PhotoImage(file="image/Yayoi-shop/menuset_19.png")
            yayoishop_menuset_20 = PhotoImage(file="image/Yayoi-shop/menuset_20.png")
            yayoishop_menuset_21 = PhotoImage(file="image/Yayoi-shop/menuset_21.png")
            yayoishop_menuset_22 = PhotoImage(file="image/Yayoi-shop/menuset_22.png")
            yayoishop_menuset_23 = PhotoImage(file="image/Yayoi-shop/menuset_23.png")
            yayoishop_menuset_24 = PhotoImage(file="image/Yayoi-shop/menuset_24.png")
            yayoishop_menuset_25 = PhotoImage(file="image/Yayoi-shop/menuset_25.png")
            yayoishop_menuset_26 = PhotoImage(file="image/Yayoi-shop/menuset_26.png")
            yayoishop_menuset_27 = PhotoImage(file="image/Yayoi-shop/menuset_27.png")
            yayoishop_menuset_28 = PhotoImage(file="image/Yayoi-shop/menuset_28.png")
            yayoishop_menuset_29 = PhotoImage(file="image/Yayoi-shop/menuset_29.png")
            yayoishop_menuset_30 = PhotoImage(file="image/Yayoi-shop/menuset_30.png")
            yayoishop_menuset_31 = PhotoImage(file="image/Yayoi-shop/menuset_31.png")
            yayoishop_menuset_32 = PhotoImage(file="image/Yayoi-shop/menuset_32.png")
            yayoishop_menuset_33 = PhotoImage(file="image/Yayoi-shop/menuset_33.png")
            yayoishop_menuset_34 = PhotoImage(file="image/Yayoi-shop/menuset_34.png")
            yayoishop_menuset_35 = PhotoImage(file="image/Yayoi-shop/menuset_35.png")
            yayoishop_menuset_36 = PhotoImage(file="image/Yayoi-shop/menuset_36.png")
            yayoishop_menuset_37 = PhotoImage(file="image/Yayoi-shop/menuset_37.png")
            yayoishop_menuset_38 = PhotoImage(file="image/Yayoi-shop/menuset_38.png")
            yayoishop_menuset_39 = PhotoImage(file="image/Yayoi-shop/menuset_39.png")
            yayoishop_menuset_41 = PhotoImage(file="image/Yayoi-shop/menuset_41.png")
            yayoishop_menuset_42 = PhotoImage(file="image/Yayoi-shop/menuset_42.png")
            yayoishop_menuset_43 = PhotoImage(file="image/Yayoi-shop/menuset_43.png")
            yayoishop_menuset_44 = PhotoImage(file="image/Yayoi-shop/menuset_44.png")
            yayoishop_menuset_45 = PhotoImage(file="image/Yayoi-shop/menuset_45.png")
            yayoishop_menuset_46 = PhotoImage(file="image/Yayoi-shop/menuset_46.png")
            yayoishop_menuset_47 = PhotoImage(file="image/Yayoi-shop/menuset_47.png")
            yayoishop_menuset_48 = PhotoImage(file="image/Yayoi-shop/menuset_48.png")
            yayoishop_menuset_49 = PhotoImage(file="image/Yayoi-shop/menuset_49.png")
            yayoishop_menuset_50 = PhotoImage(file="image/Yayoi-shop/menuset_50.png")
            yayoishop_red_status  = PhotoImage(file="image/Yayoi-shop/red-status.png")
            yayoishop_yellow_status = PhotoImage(file="image/Yayoi-shop/yellow-status.png")
            yayoishop_green_status  = PhotoImage(file="image/Yayoi-shop/green-status.png")
            yayoishop_yayoishop_payout = PhotoImage(file="image/Yayoi-shop/payout.png")
            # admin
            admin_yayoi_frame_1 = PhotoImage(file="image/mainprogram/admin-frame1.png")
            admin_yayoi_frame_2 = PhotoImage(file="image/mainprogram/admin-frame2.png")
            admin_yayoi_table = PhotoImage(file="image/mainprogram/admin-text-table.png")
            admin_yayoi_table_1 = PhotoImage(file="image/mainprogram/admin-text-table-1.png")
            admin_yayoi_table_2 = PhotoImage(file="image/mainprogram/admin-text-table-2.png")
            admin_yayoi_table_3 = PhotoImage(file="image/mainprogram/admin-text-table-3.png")
            admin_yayoi_table_4 = PhotoImage(file="image/mainprogram/admin-text-table-4.png")
            admin_yayoi_table_5 = PhotoImage(file="image/mainprogram/admin-text-table-5.png")
            # afteryou
            global afteryou_queuepic,afteryou_logo,afteryou_header
            #
            afteryou_queuepic = PhotoImage(file="image/Afteryou-shop/quepicture.png")
            afteryou_logo = PhotoImage(file="image/Afteryou-shop/logo-afteryou.png")
            afteryou_header = PhotoImage(file="image/Afteryou-shop/edge.png")
            # kyo
            global kyo_queuepic , kyo_logo , kyo_header
            kyo_queuepic = PhotoImage(file="image/Kyo-shop/quepicture.png")
            kyo_logo = PhotoImage(file="image/Kyo-shop/logo-kyo.png")
            kyo_header = PhotoImage(file="image/Kyo-shop/edge.png")
            # code
            global code_queuepic,code_logo,code_header
            code_queuepic = PhotoImage(file="image/Code-shop/quepicture.png")
            code_logo = PhotoImage(file="image/Code-shop/logo-code.png")
            code_header = PhotoImage(file="image/Code-shop/edge.png")
            # shin
            global shin_queuepic ,shin_header,shin_logo
            shin_queuepic = PhotoImage(file="image/Shinkanzen-shop/quepicture.png")
            shin_logo = PhotoImage(file="image/Shinkanzen-shop/logo-shin.png")
            shin_header = PhotoImage(file="image/Shinkanzen-shop/edge.png")
            # ohk
            global ohk_queuepic,ohk_logo,ohk_header
            ohk_queuepic = PhotoImage(file="image/Ohkajhu-shop/quepicture.png")
            ohk_logo = PhotoImage(file="image/Ohkajhu-shop/logo-ohk.png")
            ohk_header = PhotoImage(file="image/Ohkajhu-shop/edge.png")
            #
            global addtofav_not,addtofav_act
            addtofav_not = PhotoImage(file="image/mainprogram/Group 1183.png")
            addtofav_act = PhotoImage(file="image/mainprogram/Group 73 (1).png")
            # HOTEL
            global hotel_frame,hotel_text_1
            hotel_frame = PhotoImage(file="image/mainprogram/hotelframe.png")
            hotel_text_1 = PhotoImage(file="image/mainprogram/text_hotel1.png")
            #
            global hotel_shop1,hotel_shop2,hotel_shop3,hotel_1_info,hotel_2_info,hotel_3_info,bookhotel,hotel_confirm,hotel_1_bg,hotel_paymnet,hotel_2_bg,hotel_3_bg,hotel_search,hotel_checkbook
            #
            hotel_shop1 = PhotoImage(file="image/mainprogram/hotel_shop1.png")
            hotel_shop2 = PhotoImage(file="image/mainprogram/hotel_shop2.png")
            hotel_shop3 = PhotoImage(file="image/mainprogram/hotel_shop3.png")
            bookhotel = PhotoImage(file="image/mainprogram/bookhotel.png")
            hotel_1_info = PhotoImage(file="image/mainprogram/hotel_shop1_info.png")
            hotel_2_info = PhotoImage(file="image/mainprogram/hotel_shop2_info.png")
            hotel_3_info = PhotoImage(file="image/mainprogram/hotel_shop3_info.png")
            hotel_confirm = PhotoImage(file="image/mainprogram/hotelconfirm.png")
            hotel_paymnet = PhotoImage(file="image/mainprogram/hotelpayment.png")
            hotel_1_bg = PhotoImage(file="image/mainprogram/hotel_shop1_bg.png")
            hotel_2_bg = PhotoImage(file="image/mainprogram/hotel_shop2_bg.png")
            hotel_3_bg = PhotoImage(file="image/mainprogram/hotel_shop3_bg.png")
            hotel_search = PhotoImage(file="image/mainprogram/hotel_search.png")
            hotel_checkbook = PhotoImage(file="image/mainprogram/checkbooking.png")
            # boy girl
            global boy_image,girl_image,button_manage,button_change,button_cf,button_topup,frame_point,frame_money,button_exc,button_money,pic_item_1,pic_item_2,pic_item_3
            #
            boy_image = PhotoImage(file="image/mainprogram/hahaboy.png").subsample(6,6)
            girl_image = PhotoImage(file="image/mainprogram/hahagirl.png").subsample(6,6)
            button_manage = PhotoImage(file="image/Yayoi-shop/yellow-manage.png")
            button_change = PhotoImage(file="image/Yayoi-shop/yellow-change.png")
            button_cf = PhotoImage(file="image/Yayoi-shop/yellow-confirm.png")
            button_topup = PhotoImage(file="image/Yayoi-shop/topuppount.png")
            frame_point = PhotoImage(file="image/Yayoi-shop/framepoint.png")
            frame_money = PhotoImage(file="image/Yayoi-shop/framemoney.png")
            button_exc = PhotoImage(file="image/Yayoi-shop/yellow-exc.png")
            button_money = PhotoImage(file="image/Yayoi-shop/yellow-topup.png")
            pic_item_1 = PhotoImage(file="image/mainprogram/item_1.png")
            pic_item_2 = PhotoImage(file="image/mainprogram/item_2.png")
            pic_item_3 = PhotoImage(file="image/mainprogram/item_3.png")
    # def 1 login customer/admin
    def allfunctionin_loginpage() : # all function about login
        global customerlogin , customerregister , adminlogin , entry_username_admin_spy , entry_password_admin_spy
        # Spy login
        entry_username_customerlogin_spy = StringVar()
        entry_password_customerlogin_spy = StringVar()
        # Spy register
        entry_regusername_customerlogin_spy = StringVar() #
        entry_regfullname_customerlogin_spy = StringVar() #
        # special spy
        split_fname = StringVar()
        split_lname = StringVar()
        #
        entry_regtelephone_customerlogin_spy = StringVar()
        entry_reggender_customerlogin_spy = StringVar()
        entry_regpassword_customerlogin_spy = StringVar()
        entry_regcfpassword_customerlogin_spy = StringVar()
        # admin
        entry_username_admin_spy = StringVar()
        entry_password_admin_spy = StringVar()
        # customer login page
        def customerlogin() : # login page for customer
            # function
            def entry_username_customerlogin_click(e) :
                if entry_username_customerlogin_spy.get() == "Username   " :
                    entry_username_customerlogin_spy.set("")
                    entry_username_customerlogin["fg"] = "Black"
                if  entry_password_customerlogin_spy.get() == "" :
                    entry_password_customerlogin_spy.set("Password   ")
                    entry_password_customerlogin["fg"] = "#AAAAAA"
                    entry_password_customerlogin["show"] = ""
            def entry_password_customerlogin_click(e) :
                if entry_password_customerlogin_spy.get() == "Password   " :
                    entry_password_customerlogin_spy.set("")
                    entry_password_customerlogin["fg"] = "Black"
                    entry_password_customerlogin["show"] = "*"
                if  entry_username_customerlogin_spy.get() == "" :
                    entry_username_customerlogin_spy.set("Username   ")
                    entry_username_customerlogin["fg"] = "#AAAAAA"
            def button_signin_customerlogin_click(e) :
                if entry_username_customerlogin_spy.get() != "" and entry_username_customerlogin_spy.get() != "Username   ":
                    if entry_password_customerlogin_spy.get() != "" and entry_password_customerlogin_spy.get() != "Password   ":
                        # connect db
                        conn = sqlite3.connect("projectdb.db")
                        cursor = conn.cursor()
                        # sql command
                        sql = """
                                SELECT * FROM customer_login WHERE username_customer=? and password_customer=?
                                """
                        cursor.execute(sql,[entry_username_customerlogin_spy.get(),entry_password_customerlogin_spy.get()])
                        result = cursor.fetchone()
                        if result :
                            messagebox.showinfo("Admin","Login successfully")
                            customermainpage(result[0])
                        else :
                            messagebox.showwarning("Admin","Username or Password is Incorrect")
                    else :
                        messagebox.showwarning("Admin","Please enter Password")
                        if  entry_password_customerlogin_spy.get() == "" :
                            entry_password_customerlogin_spy.set("Password   ")
                            entry_password_customerlogin["fg"] = "#AAAAAA"
                else :
                    messagebox.showwarning("Admin","Please enter Username")
                    if  entry_username_customerlogin_spy.get() == "" :
                        entry_username_customerlogin_spy.set("Username   ")
                        entry_username_customerlogin["fg"] = "#AAAAAA"
                    if  entry_password_customerlogin_spy.get() == "" :
                        entry_password_customerlogin_spy.set("Password   ")
                        entry_password_customerlogin["fg"] = "#AAAAAA"
            # Spy set
            entry_username_customerlogin_spy.set("Username   ")
            entry_password_customerlogin_spy.set("Password   ")
            # frame setting
            frame_customerlogin = Frame(root,bg="#FFFFFF")
            frame_customerlogin.place(x=0,y=0,w=w,h=h)
            # Canvas
            canv = Canvas(frame_customerlogin, width=w, height=h,bg="white")
            canv.pack()
            canv.create_rectangle(635, 255, 885, 258, fill="black", outline = 'black')
            canv.create_rectangle(635, 355, 885, 358, fill="black", outline = 'black')
            # widget
            # photo
            photo_1 = Label(frame_customerlogin,image=signinpage_pic1,bg="white")
            photo_1.place(x=-2,y=-1)
            # text = signin
            text_signin_customerlogin = Label(frame_customerlogin,text="Sign in",fg="#7D92BE",bg="white",font="Calibri 42 bold")
            text_signin_customerlogin.place(x=685,y=100)
            # entry = username
            entry_username_customerlogin = Entry(frame_customerlogin,text="",bg="#FFFFFF",fg="#AAAAAA",font="Calibri 18 bold",textvariable=entry_username_customerlogin_spy,border=0,width=20)
            entry_username_customerlogin.place(x=640,y=220)
            # entry = password
            entry_password_customerlogin = Entry(frame_customerlogin,text="",bg="#FFFFFF",fg="#AAAAAA",font="Calibri 18 bold",textvariable=entry_password_customerlogin_spy,border=0,width=20)
            entry_password_customerlogin.place(x=640,y=320)
            # button = signin
            button_signin_customerlogin = Button(frame_customerlogin,text="Sign in",width=18,height=1,bg="#7D92BE",fg="white",font="Calibri 18 bold",border=2,activebackground="white")
            button_signin_customerlogin.place(x=640,y=420)
            # text = Don't have an account ?
            text_Donthave_customerlogin =Label(frame_customerlogin,text="Don't have an account ?",fg="#000000",bg="#FFFFFF",font="Calibri 12 bold")
            text_Donthave_customerlogin.place(x=645,y=480)
            # button = sign up
            button_signup_customerlogin = Button(frame_customerlogin,text="Sign up",width=6,border=0,height=1,bg="#FFFFFF",fg="#7D92BE",font="Calibri 12 bold",command=customerregister,activebackground="white",activeforeground="purple")
            button_signup_customerlogin.place(x=822,y=477)
            # bind
            if entry_username_customerlogin_spy.get() == "Username   " :
                entry_username_customerlogin.bind("<Button-1>",entry_username_customerlogin_click)
            if entry_password_customerlogin_spy.get() == "Password   " :
                entry_password_customerlogin.bind("<Button-1>",entry_password_customerlogin_click)
            button_signin_customerlogin.bind("<Button-1>",button_signin_customerlogin_click)
            button_adminlogin = Button(frame_customerlogin,text="For Admin",font="Calibri 12 underline",border=0,bg="white",activebackground="white",command=adminlogin)
            button_adminlogin.place(x=w-80,y=h-35)
        # customer register page
        def customerregister() : # register page for customer
            global frame_customerregister
            # Frame
            frame_customerregister = Frame(root,bg="#FFFFFF")
            frame_customerregister.place(x=0,y=0,w=w,h=h)
            # Spy set
            # function
            def button_confirm_customerlogin_click(e) :
                if entry_regusername_customerlogin_spy.get() == "" : # 
                    entry_regusername_customerlogin_spy.set("Username   ")
                    entry_register_username["fg"] = "#AAAAAA"
                if  entry_regfullname_customerlogin_spy.get() == "" :
                    entry_regfullname_customerlogin_spy.set("Fullname   ") #
                    entry_register_fullname["fg"] = "#AAAAAA"
                if  entry_reggender_customerlogin_spy.get() == "-" : #
                    entry_reggender_customerlogin_spy.set("Gender   ")
                    entry_register_gender["fg"] = "#AAAAAA"
                    combobox_reggender_customerlogin.place(relx=-50,y=-100)
                if  entry_regpassword_customerlogin_spy.get() == "" : #
                    entry_regpassword_customerlogin_spy.set("Password   ")
                    entry_register_password["fg"] = "#AAAAAA"
                if  entry_regcfpassword_customerlogin_spy.get() == "" :
                    entry_regcfpassword_customerlogin_spy.set("Confirm Password   ")
                    entry_register_cfpassword["fg"] = "#AAAAAA"
                if  entry_regtelephone_customerlogin_spy.get() == "" :
                    entry_regtelephone_customerlogin_spy.set("Telephone number   ")
                    entry_register_tele["fg"] = "#AAAAAA"
                if entry_regusername_customerlogin_spy.get() != "" and entry_regusername_customerlogin_spy.get() != "Username   " :
                    if len(entry_regusername_customerlogin_spy.get()) >= 5 :
                        if entry_regfullname_customerlogin_spy.get() != "" and entry_regfullname_customerlogin_spy.get() != "Fullname   " :
                            amount = 0
                            indentinname = 0
                            for i in entry_regfullname_customerlogin_spy.get() :
                                if i == " " :
                                    indentinname += 1
                                amount += 1
                            if indentinname == 1 and amount != 2 :
                                value = entry_regfullname_customerlogin_spy.get().split(" ")
                                if value[1] != "" :
                                    split_fname.set(value[0])
                                    split_lname.set(value[1])
                                    if entry_reggender_customerlogin_spy.get() == "Male" or entry_reggender_customerlogin_spy.get() == "Female" or entry_reggender_customerlogin_spy.get() == "Other" :
                                        if entry_regpassword_customerlogin_spy.get() != "" and entry_regpassword_customerlogin_spy.get() != "Password   " :
                                            if len(entry_regpassword_customerlogin_spy.get()) >= 8 :
                                                if entry_regcfpassword_customerlogin_spy.get() != "" and entry_regcfpassword_customerlogin_spy.get() != "Confirm Password   " :
                                                    if entry_regpassword_customerlogin_spy.get() == entry_regcfpassword_customerlogin_spy.get():
                                                        if entry_regtelephone_customerlogin_spy.get() != "" and entry_regtelephone_customerlogin_spy.get() != "Telephone number   " :
                                                            conn = sqlite3.connect("projectdb.db")
                                                            cursor = conn.cursor()
                                                            sqlchk = """
                                                                    SELECT * FROM customer_information
                                                                    WHERE tel_customer=? """
                                                            cursor.execute(sqlchk,[entry_regtelephone_customerlogin_spy.get()])
                                                            result = cursor.fetchone()
                                                            if result :
                                                                messagebox.showwarning("Admin","This phone number has been registed\nPlease use another number")
                                                            else :
                                                                count_1 = 0
                                                                for i in (entry_regusername_customerlogin_spy.get()) :
                                                                    count_1 = count_1 + 1
                                                                idcus = entry_regusername_customerlogin_spy.get()[0:4]+entry_regpassword_customerlogin_spy.get()[0:2]+"-"+entry_reggender_customerlogin_spy.get()+str(count_1)
                                                                #
                                                                conn = sqlite3.connect("projectdb.db")
                                                                cursor = conn.cursor()
                                                                sql = """
                                                                        INSERT INTO customer_login (id_customer, username_customer, password_customer)
                                                                        values (?,?,?)"""
                                                                cursor.execute(sql,[idcus,entry_regusername_customerlogin_spy.get(),entry_regpassword_customerlogin_spy.get()])
                                                                #
                                                                member = "None"
                                                                point = "0"
                                                                money = "0"
                                                                favshop = "-"
                                                                sqlinsertx = """
                                                                        INSERT INTO customer_information (id_customer, firstname_customer, lastname_customer, tel_customer, gender_customer, member_customer, point_customer, money_customer, fav_shop) 
                                                                        values (?,?,?,?,?,?,?,?,?) """
                                                                cursor.execute(sqlinsertx, [idcus,split_fname.get(),split_lname.get(),entry_regtelephone_customerlogin_spy.get(),entry_reggender_customerlogin_spy.get(),member,point,money,favshop])
                                                                conn.commit()
                                                                conn.close()
                                                                messagebox.showinfo("Admin","Register successfully")
                                                                regisgotologin()    
                                                        else :
                                                            messagebox.showwarning("Admin","Please enter Telephone number")
                                                    else :
                                                        messagebox.showwarning("Admin","Password and Confirm Password doesn't match \nPlease try again.") 
                                                else :
                                                    messagebox.showwarning("Admin","Please enter Confirm Password") 
                                            else :
                                                messagebox.showwarning("Admin","Please set a password of 8 characters or more") 
                                        else :
                                            messagebox.showwarning("Admin","Please enter Password")
                                    else :
                                        messagebox.showwarning("Admin","Please choose gender")
                                else :
                                    messagebox.showwarning("Admin","Please fill in exactly the format provided")
                            else :
                                messagebox.showwarning("Admin","Please fill fullname in exactly the format provided")
                        else :
                            messagebox.showwarning("Admin","Please enter Full name")
                    else :
                        messagebox.showwarning("Admin","Username must be at least 5 characters.")
                else :
                    messagebox.showwarning("Admin","Please enter Username")
            def entry_gender_customerlogin_click(e) :
                global combobox_reggender_customerlogin
                global text_hine_user,text_hine_regis,text_hine_pass,text_hine_cfpass,text_hine_tel
                gender = ["-","Male","Female","Other"]
                combobox_reggender_customerlogin = ttk.Combobox(frame_customerregister,value=gender,textvariable=entry_reggender_customerlogin_spy)
                combobox_reggender_customerlogin.set("-")
                combobox_reggender_customerlogin.place(relx=0.6825,y=280)
                if entry_regusername_customerlogin_spy.get() == "" : # 
                    entry_regusername_customerlogin_spy.set("Username   ")
                    entry_register_username["fg"] = "#AAAAAA"
                    #
                text_hine_user["fg"] = "white"
                    #
                if  entry_regfullname_customerlogin_spy.get() == "" :
                    entry_regfullname_customerlogin_spy.set("Fullname   ") #
                    entry_register_fullname["fg"] = "#AAAAAA"
                    #
                text_hine_regis["fg"] = "white"
                    #
                if  entry_reggender_customerlogin_spy.get() == "Male" or "Female" or "Other" : #
                    entry_register_gender["fg"] = "black"
                if  entry_regpassword_customerlogin_spy.get() == "" : #
                    entry_regpassword_customerlogin_spy.set("Password   ")
                    entry_register_password["fg"] = "#AAAAAA"
                    #
                text_hine_pass["fg"] = "white"
                    #
                if  entry_regcfpassword_customerlogin_spy.get() == "" :
                    entry_regcfpassword_customerlogin_spy.set("Confirm Password   ")
                    entry_register_cfpassword["fg"] = "#AAAAAA"
                    #
                text_hine_cfpass["fg"] = "white"
                    #
                if  entry_regtelephone_customerlogin_spy.get() == "" :
                    entry_regtelephone_customerlogin_spy.set("Telephone number   ")
                    entry_register_tele["fg"] = "#AAAAAA"
                    #
                text_hine_tel["fg"] = "white"
            def entry_username_customerlogin_click(e) :
                global text_hine_user,text_hine_regis,text_hine_pass,text_hine_cfpass,text_hine_tel
                if entry_regusername_customerlogin_spy.get() == "Username   " : 
                    entry_regusername_customerlogin_spy.set("")
                    entry_register_username["fg"] = "Black"
                    #
                text_hine_user["fg"] = "red"
                    #
                if  entry_regfullname_customerlogin_spy.get() == "" :
                    entry_regfullname_customerlogin_spy.set("Fullname   ") 
                    entry_register_fullname["fg"] = "#AAAAAA"
                    #
                text_hine_regis["fg"] = "white"
                    #
                if  entry_reggender_customerlogin_spy.get() == "-" : #
                    entry_reggender_customerlogin_spy.set("Gender   ")
                    entry_register_gender["fg"] = "#AAAAAA"
                    #
                    #
                    combobox_reggender_customerlogin.place(relx=-50,y=-100)
                if  entry_regpassword_customerlogin_spy.get() == "" : #
                    entry_regpassword_customerlogin_spy.set("Password   ")
                    entry_register_password["fg"] = "#AAAAAA"
                    #
                text_hine_pass["fg"] = "white"
                    #
                if  entry_regcfpassword_customerlogin_spy.get() == "" :
                    entry_regcfpassword_customerlogin_spy.set("Confirm Password   ")
                    entry_register_cfpassword["fg"] = "#AAAAAA"
                    #
                text_hine_cfpass["fg"] = "white"
                    #
                if  entry_regtelephone_customerlogin_spy.get() == "" :
                    entry_regtelephone_customerlogin_spy.set("Telephone number   ")
                    entry_register_tele["fg"] = "#AAAAAA"
                    #
                text_hine_tel["fg"] = "white"
            def entry_fullname_customerlogin_click(e) : 
                global text_hine_user,text_hine_regis,text_hine_pass,text_hine_cfpass,text_hine_tel
                if entry_regusername_customerlogin_spy.get() == "" : # 
                    entry_regusername_customerlogin_spy.set("Username   ")
                    entry_register_username["fg"] = "#AAAAAA"
                    #
                text_hine_user["fg"] = "white"
                    #
                if  entry_regfullname_customerlogin_spy.get() == "Fullname   " :
                    entry_regfullname_customerlogin_spy.set("") #
                    entry_register_fullname["fg"] = "Black"
                    #
                text_hine_regis["fg"] = "red"
                    #
                if  entry_reggender_customerlogin_spy.get() == "-" : #
                    entry_reggender_customerlogin_spy.set("Gender   ")
                    entry_register_gender["fg"] = "#AAAAAA"
                    combobox_reggender_customerlogin.place(relx=-50,y=-100)
                if  entry_regpassword_customerlogin_spy.get() == "" : #
                    entry_regpassword_customerlogin_spy.set("Password   ")
                    entry_register_password["fg"] = "#AAAAAA"
                    #
                text_hine_pass["fg"] = "white"
                    #
                if  entry_regcfpassword_customerlogin_spy.get() == "" :
                    entry_regcfpassword_customerlogin_spy.set("Confirm Password   ")
                    entry_register_cfpassword["fg"] = "#AAAAAA"
                    #
                text_hine_cfpass["fg"] = "white"
                    #
                if  entry_regtelephone_customerlogin_spy.get() == "" :
                    entry_regtelephone_customerlogin_spy.set("Telephone number   ")
                    entry_register_tele["fg"] = "#AAAAAA"   
                    #
                text_hine_tel["fg"] = "white"    
            def entry_password_customerlogin_click(e) : 
                global text_hine_user,text_hine_regis,text_hine_pass,text_hine_cfpass,text_hine_tel
                if entry_regusername_customerlogin_spy.get() == "" : # 
                    entry_regusername_customerlogin_spy.set("Username   ")
                    entry_register_username["fg"] = "#AAAAAA"
                    #
                text_hine_user["fg"] = "white"
                    #
                if  entry_regfullname_customerlogin_spy.get() == "" :
                    entry_regfullname_customerlogin_spy.set("Fullname   ") #
                    entry_register_fullname["fg"] = "#AAAAAA"
                    #
                text_hine_regis["fg"] = "white"
                    #
                if  entry_reggender_customerlogin_spy.get() == "-" : #
                    entry_reggender_customerlogin_spy.set("Gender   ")
                    entry_register_gender["fg"] = "#AAAAAA"
                    combobox_reggender_customerlogin.place(relx=-50,y=-100)
                if  entry_regpassword_customerlogin_spy.get() == "Password   " : #
                    entry_regpassword_customerlogin_spy.set("")
                    entry_register_password["fg"] = "Black"
                    #
                text_hine_pass["fg"] = "red"
                    #
                if  entry_regcfpassword_customerlogin_spy.get() == "" :
                    entry_regcfpassword_customerlogin_spy.set("Confirm Password   ")
                    entry_register_cfpassword["fg"] = "#AAAAAA"
                    #
                text_hine_cfpass["fg"] = "white"
                    #
                if  entry_regtelephone_customerlogin_spy.get() == "" :
                    entry_regtelephone_customerlogin_spy.set("Telephone number   ")
                    entry_register_tele["fg"] = "#AAAAAA"
                    #
                text_hine_tel["fg"] = "white"
            def entry_cfpassword_customerlogin_click(e) : 
                global text_hine_user,text_hine_regis,text_hine_pass,text_hine_cfpass,text_hine_tel
                if entry_regusername_customerlogin_spy.get() == "" : # 
                    entry_regusername_customerlogin_spy.set("Username   ")
                    entry_register_username["fg"] = "#AAAAAA"
                    #
                text_hine_user["fg"] = "white"
                    #
                if  entry_regfullname_customerlogin_spy.get() == "" :
                    entry_regfullname_customerlogin_spy.set("Fullname   ") #
                    entry_register_fullname["fg"] = "#AAAAAA"
                    #
                text_hine_regis["fg"] = "white"
                    #
                if  entry_reggender_customerlogin_spy.get() == "-" : #
                    entry_reggender_customerlogin_spy.set("Gender   ")
                    entry_register_gender["fg"] = "#AAAAAA"
                    combobox_reggender_customerlogin.place(relx=-50,y=-100)
                if  entry_regpassword_customerlogin_spy.get() == "" : #
                    entry_regpassword_customerlogin_spy.set("Password   ")
                    entry_register_password["fg"] = "#AAAAAA"
                    #
                text_hine_pass["fg"] = "white"
                    #
                if  entry_regcfpassword_customerlogin_spy.get() == "Confirm Password   " :
                    entry_regcfpassword_customerlogin_spy.set("")
                    entry_register_cfpassword["fg"] = "black"
                    #
                text_hine_cfpass["fg"] = "red"
                    #
                if  entry_regtelephone_customerlogin_spy.get() == "" :
                    entry_regtelephone_customerlogin_spy.set("Telephone number   ")
                    entry_register_tele["fg"] = "#AAAAAA"
                    #
                text_hine_tel["fg"] = "white"
            def entry_tele_customerlogin_click(e) : 
                global text_hine_user,text_hine_regis,text_hine_pass,text_hine_cfpass,text_hine_tel
                if entry_regusername_customerlogin_spy.get() == "" : # 
                    entry_regusername_customerlogin_spy.set("Username   ")
                    entry_register_username["fg"] = "#AAAAAA"
                    #
                text_hine_user["fg"] = "white"
                    #
                if  entry_regfullname_customerlogin_spy.get() == "" :
                    entry_regfullname_customerlogin_spy.set("Fullname   ") #
                    entry_register_fullname["fg"] = "#AAAAAA"
                    #
                text_hine_regis["fg"] = "white"
                    #
                if  entry_reggender_customerlogin_spy.get() == "-" : #
                    entry_reggender_customerlogin_spy.set("Gender   ")
                    entry_register_gender["fg"] = "#AAAAAA"
                    combobox_reggender_customerlogin.place(relx=-50,y=-100)
                if  entry_regpassword_customerlogin_spy.get() == "" : #
                    entry_regpassword_customerlogin_spy.set("Password   ")
                    entry_register_password["fg"] = "#AAAAAA"
                    #
                text_hine_pass["fg"] = "white"
                    #
                if  entry_regcfpassword_customerlogin_spy.get() == "" :
                    entry_regcfpassword_customerlogin_spy.set("Confirm Password   ")
                    entry_register_cfpassword["fg"] = "#AAAAAA"
                    #
                text_hine_cfpass["fg"] = "white"
                    #
                if  entry_regtelephone_customerlogin_spy.get() == "Telephone number   " :
                    entry_regtelephone_customerlogin_spy.set("")
                    entry_register_tele["fg"] = "black"
                    #
                text_hine_tel["fg"] = "red"

            # canvas
            canv = Canvas(frame_customerregister, width=w, height=h,bg="white")
            canv.pack()
            canv.create_rectangle(360, 195, 671, 198, fill="black", outline = 'black')
            canv.create_rectangle(360, 255, 671, 258, fill="black", outline = 'black')
            canv.create_rectangle(360, 315, 671, 318, fill="black", outline = 'black')
            canv.create_rectangle(360, 375, 671, 378, fill="black", outline = 'black')
            canv.create_rectangle(360, 435, 671, 438, fill="black", outline = 'black')
            canv.create_rectangle(360, 495, 671, 498, fill="black", outline = 'black')
            #
            pictop = Label(frame_customerregister,image=registop,bg="#FFFFFF").place(x=w-275,y=0)
            picbel = Label(frame_customerregister,image=regisbel,bg="#FFFFFF").place(x=-5,y=h-240)
            # text sign up
            text_signup_customerlogin = Label(frame_customerregister,text="Sign up",bg="#FFFFFF",fg="#7D92BE",font="Calibri 42 bold")
            text_signup_customerlogin.place(relx=0.425,y=50)
            global text_hine_user,text_hine_regis,text_hine_pass,text_hine_cfpass,text_hine_tel
            # username
            entry_regusername_customerlogin_spy.set("Username   ")
            entry_register_username = Entry(frame_customerregister,text="",bg="#FFFFFF",fg="#AAAAAA",font="Calibri 18 bold",textvariable=entry_regusername_customerlogin_spy,width=25,border=0)
            entry_register_username.place(relx=0.365,y=160)
            #
            text_hine_user = Label(frame_customerregister,text="Username must be more than 5 characters",fg="white",font="Calibri 12",bg="white")
            text_hine_user.place(relx=0.685,y=170)
            # name
            entry_regfullname_customerlogin_spy.set("Fullname   ")
            entry_register_fullname = Entry(frame_customerregister,text="",bg="#FFFFFF",fg="#AAAAAA",font="Calibri 18 bold",textvariable=entry_regfullname_customerlogin_spy,width=25,border=0)
            entry_register_fullname.place(relx=0.365,y=220)
            #
            text_hine_regis = Label(frame_customerregister,text="Must have firstname and lastname\nExample Melanie Evadill",fg="white",font="Calibri 12",bg="white")
            text_hine_regis.place(relx=0.685,y=230)
            # gender
            entry_reggender_customerlogin_spy.set("Gender   ")
            entry_register_gender = Entry(frame_customerregister,text="",bg="#FFFFFF",fg="#AAAAAA",font="Calibri 18 bold",textvariable=entry_reggender_customerlogin_spy,width=25,border=0)
            entry_register_gender.place(relx=0.365,y=280)
            # password
            entry_regpassword_customerlogin_spy.set("Password   ")
            entry_register_password = Entry(frame_customerregister,text="",bg="#FFFFFF",fg="#AAAAAA",font="Calibri 18 bold",textvariable=entry_regpassword_customerlogin_spy,width=25,border=0)
            entry_register_password.place(relx=0.365,y=340)
            #
            text_hine_pass = Label(frame_customerregister,text="Create your Password",fg="white",font="Calibri 12",bg="white")
            text_hine_pass.place(relx=0.685,y=345)
            # repassword
            entry_regcfpassword_customerlogin_spy.set("Confirm Password   ")
            entry_register_cfpassword = Entry(frame_customerregister,text="",bg="#FFFFFF",fg="#AAAAAA",font="Calibri 18 bold",textvariable=entry_regcfpassword_customerlogin_spy,width=25,border=0)
            entry_register_cfpassword.place(relx=0.365,y=400)
            #
            text_hine_cfpass = Label(frame_customerregister,text="Confirm Password must be\nthe same as Password",fg="white",font="Calibri 12",bg="white")
            text_hine_cfpass.place(relx=0.685,y=405)
            # telephone num
            entry_regtelephone_customerlogin_spy.set("Telephone number   ")
            entry_register_tele = Entry(frame_customerregister,text="",bg="#FFFFFF",fg="#AAAAAA",font="Calibri 18 bold",textvariable=entry_regtelephone_customerlogin_spy,width=25,border=0)
            entry_register_tele.place(relx=0.365,y=460)
            #
            text_hine_tel = Label(frame_customerregister,text="Please enter your Telephone number",fg="white",font="Calibri 12",bg="white")
            text_hine_tel.place(relx=0.685,y=465)
            # button = Confirm
            button_confirm_customerlogin = Button(frame_customerregister,text="Confirm",bg="#7D92BE",fg="#FFFFFF",font="Calibri 18 bold",width=20)
            button_confirm_customerlogin.place(relx=0.38,y=570)
            # button = Exit
            button_exit_customerlogin = Button(frame_customerregister,text="< Back",bg="#FFFFFF",fg="#485188",font="Calibri 18 bold",width=5,command=regisgotologin,border=0,activebackground="white",activeforeground="purple")
            button_exit_customerlogin.place(x=15,y=15)
            # bind
            button_confirm_customerlogin.bind("<Button-1>",button_confirm_customerlogin_click)
            # 
            entry_register_username.bind("<Button-1>",entry_username_customerlogin_click)
            entry_register_fullname.bind("<Button-1>",entry_fullname_customerlogin_click)
            entry_register_gender.bind("<Button-1>",entry_gender_customerlogin_click)
            entry_register_password.bind("<Button-1>",entry_password_customerlogin_click)
            entry_register_cfpassword.bind("<Button-1>",entry_cfpassword_customerlogin_click)
            entry_register_tele.bind("<Button-1>",entry_tele_customerlogin_click)
        # admin login page
        def adminlogin() : # login page for admin
            def exitx() :
                admin.destroy()
            def entry_username_admin_click(e) :
                if entry_username_admin_spy.get() == "Username   " :
                    entry_username_admin_spy.set("")
                    entry_username_admin["fg"] = "white"
                if  entry_password_admin_spy.get() == "" :
                    entry_password_admin_spy.set("Password   ")
                    entry_password_admin["fg"] = "#AAAAAA"
                    entry_password_admin["show"] = ""
            def entry_password_admin_click(e) :
                if entry_password_admin_spy.get() == "Password   " :
                    entry_password_admin_spy.set("")
                    entry_password_admin["fg"] = "white"
                    entry_password_admin["show"] = "*"
                if  entry_username_admin_spy.get() == "" :
                    entry_username_admin_spy.set("Username   ")
                    entry_username_admin["fg"] = "#AAAAAA"
            def button_signin_admin_click(e) :
                if entry_username_admin_spy.get() != "" and entry_username_admin_spy.get() != "Username   ":
                    if entry_password_admin_spy.get() != "" and entry_password_admin_spy.get() != "Password   ":
                        # connect db
                        conn = sqlite3.connect("projectdb.db")
                        cursor = conn.cursor()
                        # sql command
                        sql = """
                                SELECT * FROM admin_login WHERE username_admin=? and password_admin=?
                                """
                        cursor.execute(sql,[entry_username_admin_spy.get(),entry_password_admin_spy.get()])
                        result = cursor.fetchone()
                        if result :
                            messagebox.showinfo("Admin","Login successfully")
                            # YAYOI
                            if result[3] == "YAYOI" :
                                frame_adminlogin.destroy()
                                yayoi_admin_frame = Frame(admin,bg="white")
                                yayoi_admin_frame.place(x=0,y=0,w=w,h=h)
                                # frame
                                def yayoi_queue() :
                                    global yayoi_queue
                                    def queueinfomation(number) :
                                        def yayoi_addtostore(namecus,numbergroup) :
                                            ans = messagebox.askquestion("Admin","Add customer to table %s"%(numbergroup))   
                                            if ans == "yes" :
                                                if numbergroup == 1 or numbergroup == 2 or numbergroup == 3:
                                                    people = "1-2"
                                                elif numbergroup == 4 or numbergroup == 5 or numbergroup == 6:
                                                    people = "3-4"
                                                elif numbergroup == 7 or numbergroup == 8:
                                                    people = "3-4"
                                                #
                                                sql = """
                                                        UPDATE shop_yayoi_table
                                                        SET name=?,amount=?,staffcall=?
                                                        WHERE table_no=? """
                                                cursor.execute(sql,[namecus,people,"no",numbergroup])
                                                conn.commit()
                                                #
                                                sql = """
                                                        UPDATE shop_yayoi_table
                                                        SET status=?
                                                        WHERE table_no=? """
                                                cursor.execute(sql,["default",numbergroup])
                                                conn.commit()
                                                #
                                                sql = """
                                                        UPDATE shop_yayoi_queue
                                                        SET q_status=?
                                                        WHERE q_name=?"""
                                                cursor.execute(sql,["ready",namecus])   
                                                conn.commit()     
                                                conn.close()
                                            else :
                                                pass
                                        Label(yayoi_queue,image=queue_frame,bg="#FFE296").place(x=645,y=5)
                                        Label(yayoi_queue,text="Table %s"%(number),font="Calibri 24 bold",bg='#FFE296').place(x=670,y=20)
                                        Label(yayoi_queue,text="No.",font="Calibri 18",bg='#FFE296').place(x=660,y=70)
                                        Label(yayoi_queue,text="Name",font="Calibri 18",bg='#FFE296').place(x=860,y=70)
                                        conn = sqlite3.connect("projectdb.db")
                                        cursor = conn.cursor()
                                        if number == 1 or number == 2 or number == 3:
                                            sql = """
                                                    SELECT * FROM shop_yayoi_queue
                                                    WHERE q_amount=? and q_status=?"""
                                            cursor.execute(sql,["1-2","wait"])
                                            result = cursor.fetchall()
                                            yasix = 120
                                            for i,data in enumerate(result) :
                                                Label(yayoi_queue,text=data[0],bg="#FFE296").place(x=660,y=yasix)
                                                Label(yayoi_queue,text=data[1],bg="#FFE296").place(x=860,y=yasix)
                                                yasix = yasix +70
                                                yayoi1_2 = Button(yayoi_queue,text="bookatble",font="Calibri 18",bg='green',border=0,fg="white",command=lambda:yayoi_addtostore(result[0][1],number))
                                                yayoi1_2.place(x=660,y=470)
                                        elif number == 4 or number == 5 or number == 6:
                                            sql = """
                                                    SELECT * FROM shop_yayoi_queue
                                                    WHERE q_amount=? and q_status=?"""
                                            cursor.execute(sql,["3-4","wait"])
                                            result = cursor.fetchall()
                                            yasix = 120
                                            for i,data in enumerate(result) :
                                                Label(yayoi_queue,text=data[0],bg="#FFE296").place(x=660,y=yasix)
                                                Label(yayoi_queue,text=data[1],bg="#FFE296").place(x=860,y=yasix)
                                                yasix = yasix +70
                                                yayoi1_2 = Button(yayoi_queue,text="bookatble",font="Calibri 18",bg='green',border=0,fg="white",command=lambda:yayoi_addtostore(result[0][1],number))
                                                yayoi1_2.place(x=660,y=470)
                                        elif number == 7 or number == 8:
                                            sql = """
                                                    SELECT * FROM shop_yayoi_queue
                                                    WHERE q_amount=? and q_status=? """
                                            cursor.execute(sql,["5-6","wait"])
                                            result = cursor.fetchall()
                                            yasix = 120
                                            for i,data in enumerate(result) :
                                                Label(yayoi_queue,text=data[0],bg="#FFE296").place(x=660,y=yasix)
                                                Label(yayoi_queue,text=data[1],bg="#FFE296").place(x=860,y=yasix)
                                                yasix = yasix +70
                                                yayoi1_2 = Button(yayoi_queue,text="bookatble",font="Calibri 18",bg='green',border=0,fg="white",command=lambda:yayoi_addtostore(result[0][1],number))
                                                yayoi1_2.place(x=660,y=470)
                                    queuebut["state"] = "disabled"
                                    tablebut["state"] = "active"
                                    showtext["text"] = "Queue"
                                    yayoi_table_frame.destroy()
                                    yayoi_queue = Frame(yayoi_admin_frame,bg="white")
                                    yayoi_queue.place(x=0,y=160,w=w,h=h-140)
                                    Label(yayoi_queue,image=admin_yayoi_frame_1,bg="#FFFFFF").place(x=25,y=5)
                                    Label(yayoi_queue,image=queue_frame,bg="#FFFFFF").place(x=645,y=5)
                                    Label(yayoi_queue,image=admin_yayoi_table,bg="#FFDDEB").place(x=40,y=25)
                                    Label(yayoi_queue,text="1-2 People",bg="#FFDDEB",font="Calibri 18").place(x=40,y=65)
                                    Label(yayoi_queue,text="3-4 People",bg="#FFDDEB",font="Calibri 18").place(x=40,y=215)
                                    Label(yayoi_queue,text="5-6 People",bg="#FFDDEB",font="Calibri 18").place(x=40,y=365)
                                    # conn
                                    conn = sqlite3.connect("projectdb.db")
                                    cursor = conn.cursor()
                                    sql = """
                                            SELECT * FROM shop_yayoi_table """
                                    cursor.execute(sql)
                                    result = cursor.fetchall()
                                    # 1
                                    if result[0][1] == "free" :
                                        table_1 = Button(yayoi_queue,image=teble_green_act,bg="#FFDDEB",font="Calibri 22 bold",border=0,activebackground="#FFDDEB",text="1",compound="center",fg="white",command=lambda:queueinfomation(1))
                                        table_1.place(x=50,y=120)
                                    else :
                                        table_1 = Button(yayoi_queue,image=teble_green_act,bg="#FFDDEB",font="Calibri 22 bold",border=0,activebackground="#FFDDEB",text="1",compound="center",fg="white",command=lambda:queueinfomation(1),state="disabled")
                                        table_1.place(x=50,y=120)
                                    # 2
                                    if result[1][1] == "free" :
                                        table_2 = Button(yayoi_queue,image=teble_green_act,bg="#FFDDEB",font="Calibri 22 bold",border=0,activebackground="#FFDDEB",text="2",compound="center",fg="white",command=lambda:queueinfomation(2))
                                        table_2.place(x=140,y=120)
                                    else :
                                        table_2 = Button(yayoi_queue,image=teble_green_act,bg="#FFDDEB",font="Calibri 22 bold",border=0,activebackground="#FFDDEB",text="2",compound="center",fg="white",command=lambda:queueinfomation(2),state="disabled")
                                        table_2.place(x=140,y=120)
                                    # 3
                                    if result[2][1] == "free" :
                                        table_3 = Button(yayoi_queue,image=teble_green_act,bg="#FFDDEB",font="Calibri 22 bold",border=0,activebackground="#FFDDEB",text="3",compound="center",fg="white",command=lambda:queueinfomation(3))
                                        table_3.place(x=230,y=120)
                                    else :
                                        table_3 = Button(yayoi_queue,image=teble_green_act,bg="#FFDDEB",font="Calibri 22 bold",border=0,activebackground="#FFDDEB",text="3",compound="center",fg="white",command=lambda:queueinfomation(3),state="disabled")
                                        table_3.place(x=230,y=120)
                                    # 4
                                    if result[3][1] == "free" :
                                        table_4 = Button(yayoi_queue,image=teble_yellow_act,bg="#FFDDEB",font="Calibri 22 bold",border=0,activebackground="#FFDDEB",text="4",compound="center",fg="white",command=lambda:queueinfomation(4))
                                        table_4.place(x=50,y=270)
                                    else :
                                        table_4 = Button(yayoi_queue,image=teble_yellow_act,bg="#FFDDEB",font="Calibri 22 bold",border=0,activebackground="#FFDDEB",text="4",compound="center",fg="white",command=lambda:queueinfomation(4),state="disabled")
                                        table_4.place(x=50,y=270)
                                    # 5
                                    if result[4][1] == "free" :
                                        table_5 = Button(yayoi_queue,image=teble_yellow_act,bg="#FFDDEB",font="Calibri 22 bold",border=0,activebackground="#FFDDEB",text="5",compound="center",fg="white",command=lambda:queueinfomation(5))
                                        table_5.place(x=140,y=270)
                                    else :
                                        table_5 = Button(yayoi_queue,image=teble_yellow_act,bg="#FFDDEB",font="Calibri 22 bold",border=0,activebackground="#FFDDEB",text="5",compound="center",fg="white",command=lambda:queueinfomation(5),state="disabled")
                                        table_5.place(x=140,y=270)
                                    # 6
                                    if result[5][1] == "free" :
                                        table_6 = Button(yayoi_queue,image=teble_yellow_act,bg="#FFDDEB",font="Calibri 22 bold",border=0,activebackground="#FFDDEB",text="6",compound="center",fg="white",command=lambda:queueinfomation(6))
                                        table_6.place(x=230,y=270)
                                    else :
                                        table_6 = Button(yayoi_queue,image=teble_yellow_act,bg="#FFDDEB",font="Calibri 22 bold",border=0,activebackground="#FFDDEB",text="6",compound="center",fg="white",command=lambda:queueinfomation(6),state="disabled")
                                        table_6.place(x=230,y=270)
                                    # 7
                                    if result[6][1] == "free" :
                                        table_7 = Button(yayoi_queue,image=teble_red_act,bg="#FFDDEB",font="Calibri 22 bold",border=0,activebackground="#FFDDEB",text="7",compound="center",fg="white",command=lambda:queueinfomation(7))
                                        table_7.place(x=50,y=420)
                                    else :
                                        table_7 = Button(yayoi_queue,image=teble_red_act,bg="#FFDDEB",font="Calibri 22 bold",border=0,activebackground="#FFDDEB",text="7",compound="center",fg="white",command=lambda:queueinfomation(7),state="disabled")
                                        table_7.place(x=50,y=420)
                                    # 8
                                    if result[7][1] == "free" :
                                        table_8 = Button(yayoi_queue,image=teble_red_act,bg="#FFDDEB",font="Calibri 22 bold",border=0,activebackground="#FFDDEB",text="8",compound="center",fg="white",command=lambda:queueinfomation(8))
                                        table_8.place(x=140,y=420)
                                    else :
                                        table_8 = Button(yayoi_queue,image=teble_red_act,bg="#FFDDEB",font="Calibri 22 bold",border=0,activebackground="#FFDDEB",text="8",compound="center",fg="white",command=lambda:queueinfomation(8),state="disabled")
                                        table_8.place(x=140,y=420)
                                    conn.close()
                                def yayoi_table() :
                                    global yayoi_table_frame
                                    # def
                                    def tableinfomation(no):
                                        def yayoi_confirmorder() :
                                            ans = messagebox.askquestion("Admin","Confirm order") 
                                            if ans == "yes" :
                                                if result :
                                                    for i,data in enumerate(result) :
                                                        sql = """
                                                                    UPDATE shop_yayoi_orderprocess
                                                                    SET status=? WHERE menu_name =? """
                                                        cursor.execute(sql,["F",data[1]])
                                                        conn.commit()
                                                else :
                                                    yayoicon["state"] = "disabled"
                                                    yayoicon["fg"] = "white"
                                                conn.close()
                                            else :
                                                pass
                                        Label(yayoi_table_frame,image=admin_yayoi_frame_2,bg="#FFFFFF").place(x=645,y=5)
                                        Label(yayoi_table_frame,text="Table %s"%(no),font="Calibri 24 bold",bg='#DFDCED').place(x=670,y=20)
                                        Label(yayoi_table_frame,text="Menu",font="Calibri 18",bg='#DFDCED').place(x=660,y=70)
                                        Label(yayoi_table_frame,text="Amount",font="Calibri 18",bg='#DFDCED').place(x=860,y=70)
                                        conn = sqlite3.connect("projectdb.db")
                                        cursor = conn.cursor()
                                        sql = """
                                                SELECT * FROM shop_yayoi_orderprocess 
                                                WHERE table_index=? and status=?"""
                                        cursor.execute(sql,[no,"NF"])
                                        result = cursor.fetchall()
                                        indexy = 120
                                        for i,data in enumerate(result) :
                                            if i<6 :
                                                Label(yayoi_table_frame,text=data[1][0:17],font="Calibri 18",bg='#DFDCED').place(x=660,y=indexy)
                                                Label(yayoi_table_frame,text=data[3][0:17],font="Calibri 18",bg='#DFDCED').place(x=890,y=indexy)
                                            else :
                                                pass
                                            indexy = indexy + 50
                                        yayoicon = Button(yayoi_table_frame,text="Confirm Order",font="Calibri 18",bg='green',border=0,fg="white",command=yayoi_confirmorder)
                                        yayoicon.place(x=660,y=460)
                                    #
                                    tablebut["state"] = "disabled"
                                    queuebut["state"] = "active"
                                    showtext["text"] = "Table info"
                                    yayoi_table_frame = Frame(yayoi_admin_frame,bg="white")
                                    yayoi_table_frame.place(x=0,y=160,w=w,h=h-140)
                                    Label(yayoi_table_frame,image=admin_yayoi_frame_1,bg="#FFFFFF").place(x=25,y=5)
                                    Label(yayoi_table_frame,image=admin_yayoi_frame_2,bg="#FFFFFF").place(x=645,y=5)
                                    Label(yayoi_table_frame,image=admin_yayoi_table,bg="#FFDDEB").place(x=40,y=25)
                                    Label(yayoi_table_frame,text="1-2 People",bg="#FFDDEB",font="Calibri 18").place(x=40,y=65)
                                    Label(yayoi_table_frame,text="3-4 People",bg="#FFDDEB",font="Calibri 18").place(x=40,y=215)
                                    Label(yayoi_table_frame,text="5-6 People",bg="#FFDDEB",font="Calibri 18").place(x=40,y=365)
                                    # conn
                                    conn = sqlite3.connect("projectdb.db")
                                    cursor = conn.cursor()
                                    sql = """
                                            SELECT * FROM shop_yayoi_table """
                                    cursor.execute(sql)
                                    result = cursor.fetchall()
                                    conn.close()
                                    # 1
                                    if result[0][1] == "default" :
                                        table_1 = Button(yayoi_table_frame,image=teble_green_act,bg="#FFDDEB",font="Calibri 22 bold",border=0,activebackground="#FFDDEB",text="1",compound="center",fg="white",command=lambda:tableinfomation(1))
                                        table_1.place(x=50,y=120)
                                        def staff_1() :
                                            conn = sqlite3.connect("projectdb.db")
                                            cursor = conn.cursor()
                                            sql = """
                                                    UPDATE shop_yayoi_table
                                                    SET staffcall=?
                                                    WHERE table_no=? """
                                            cursor.execute(sql,["no","1"])
                                            conn.commit()
                                        if result[0][4] == "yes" :
                                            Button(yayoi_table_frame,image=staff_cal,border=0,bg="#62943B",command=staff_1).place(x=100,y=125)
                                        else :
                                            pass
                                    else :
                                        table_1 = Button(yayoi_table_frame,image=teble_green_act,bg="#FFDDEB",font="Calibri 22 bold",border=0,activebackground="#FFDDEB",text="1",compound="center",fg="white",command=lambda:tableinfomation(1),state="disabled")
                                        table_1.place(x=50,y=120)
                                    # 2
                                    if result[1][1] == "default" :
                                        table_2 = Button(yayoi_table_frame,image=teble_green_act,bg="#FFDDEB",font="Calibri 22 bold",border=0,activebackground="#FFDDEB",text="2",compound="center",fg="white",command=lambda:tableinfomation(2))
                                        table_2.place(x=140,y=120)
                                        def staff_2() :
                                            conn = sqlite3.connect("projectdb.db")
                                            cursor = conn.cursor()
                                            sql = """
                                                    UPDATE shop_yayoi_table
                                                    SET staffcall=?
                                                    WHERE table_no=? """
                                            cursor.execute(sql,["no","2"])
                                            conn.commit()
                                        if result[1][4] == "yes" :
                                            Button(yayoi_table_frame,image=staff_cal,border=0,bg="#62943B",command=staff_2).place(x=190,y=125)
                                        else :
                                            pass
                                    else :
                                        table_2 = Button(yayoi_table_frame,image=teble_green_act,bg="#FFDDEB",font="Calibri 22 bold",border=0,activebackground="#FFDDEB",text="2",compound="center",fg="white",command=lambda:tableinfomation(2),state="disabled")
                                        table_2.place(x=140,y=120)
                                    # 3
                                    if result[2][1] == "default" :
                                        table_3 = Button(yayoi_table_frame,image=teble_green_act,bg="#FFDDEB",font="Calibri 22 bold",border=0,activebackground="#FFDDEB",text="3",compound="center",fg="white",command=lambda:tableinfomation(3))
                                        table_3.place(x=230,y=120)
                                        def staff_3() :
                                            conn = sqlite3.connect("projectdb.db")
                                            cursor = conn.cursor()
                                            sql = """
                                                    UPDATE shop_yayoi_table
                                                    SET staffcall=?
                                                    WHERE table_no=? """
                                            cursor.execute(sql,["no","3"])
                                            conn.commit()
                                        if result[2][4] == "yes" :
                                            Button(yayoi_table_frame,image=staff_cal,border=0,bg="#62943B",command=staff_3).place(x=280,y=125)
                                        else :
                                            pass
                                    else :
                                        table_3 = Button(yayoi_table_frame,image=teble_green_act,bg="#FFDDEB",font="Calibri 22 bold",border=0,activebackground="#FFDDEB",text="3",compound="center",fg="white",command=lambda:tableinfomation(3),state="disabled")
                                        table_3.place(x=230,y=120)
                                    # 4
                                    if result[3][1] == "default" :
                                        table_4 = Button(yayoi_table_frame,image=teble_yellow_act,bg="#FFDDEB",font="Calibri 22 bold",border=0,activebackground="#FFDDEB",text="4",compound="center",fg="white",command=lambda:tableinfomation(4))
                                        table_4.place(x=50,y=270)
                                        def staff_4() :
                                            conn = sqlite3.connect("projectdb.db")
                                            cursor = conn.cursor()
                                            sql = """
                                                    UPDATE shop_yayoi_table
                                                    SET staffcall=?
                                                    WHERE table_no=? """
                                            cursor.execute(sql,["no","4"])
                                            conn.commit()
                                        if result[3][4] == "yes" :
                                            Button(yayoi_table_frame,image=staff_cal,border=0,bg="#62943B",command=staff_4).place(x=100,y=275)
                                        else :
                                            pass
                                    else :
                                        table_4 = Button(yayoi_table_frame,image=teble_yellow_act,bg="#FFDDEB",font="Calibri 22 bold",border=0,activebackground="#FFDDEB",text="4",compound="center",fg="white",command=lambda:tableinfomation(4),state="disabled")
                                        table_4.place(x=50,y=270)
                                    # 5
                                    if result[4][1] == "default" :
                                        table_5 = Button(yayoi_table_frame,image=teble_yellow_act,bg="#FFDDEB",font="Calibri 22 bold",border=0,activebackground="#FFDDEB",text="5",compound="center",fg="white",command=lambda:tableinfomation(5))
                                        table_5.place(x=140,y=270)
                                        def staff_5() :
                                            conn = sqlite3.connect("projectdb.db")
                                            cursor = conn.cursor()
                                            sql = """
                                                    UPDATE shop_yayoi_table
                                                    SET staffcall=?
                                                    WHERE table_no=? """
                                            cursor.execute(sql,["no","5"])
                                            conn.commit()
                                        if result[4][4] == "yes" :
                                            Button(yayoi_table_frame,image=staff_cal,border=0,bg="#62943B",command=staff_5).place(x=190,y=275)
                                        else :
                                            pass
                                    else :
                                        table_5 = Button(yayoi_table_frame,image=teble_yellow_act,bg="#FFDDEB",font="Calibri 22 bold",border=0,activebackground="#FFDDEB",text="5",compound="center",fg="white",command=lambda:tableinfomation(5),state="disabled")
                                        table_5.place(x=140,y=270)
                                    # 6
                                    if result[5][1] == "default" :
                                        table_6 = Button(yayoi_table_frame,image=teble_yellow_act,bg="#FFDDEB",font="Calibri 22 bold",border=0,activebackground="#FFDDEB",text="6",compound="center",fg="white",command=lambda:tableinfomation(6))
                                        table_6.place(x=230,y=270)
                                        def staff_6() :
                                            conn = sqlite3.connect("projectdb.db")
                                            cursor = conn.cursor()
                                            sql = """
                                                    UPDATE shop_yayoi_table
                                                    SET staffcall=?
                                                    WHERE table_no=? """
                                            cursor.execute(sql,["no","5"])
                                            conn.commit()
                                        if result[5][4] == "yes" :
                                            Button(yayoi_table_frame,image=staff_cal,border=0,bg="#62943B",command=staff_6).place(x=280,y=275)
                                        else :
                                            pass
                                    else :
                                        table_6 = Button(yayoi_table_frame,image=teble_yellow_act,bg="#FFDDEB",font="Calibri 22 bold",border=0,activebackground="#FFDDEB",text="6",compound="center",fg="white",command=lambda:tableinfomation(6),state="disabled")
                                        table_6.place(x=230,y=270)
                                    # 7
                                    if result[6][1] == "default" :
                                        def staff_7() :
                                            conn = sqlite3.connect("projectdb.db")
                                            cursor = conn.cursor()
                                            sql = """
                                                    UPDATE shop_yayoi_table
                                                    SET staffcall=?
                                                    WHERE table_no=? """
                                            cursor.execute(sql,["no","5"])
                                            conn.commit()
                                        table_7 = Button(yayoi_table_frame,image=teble_red_act,bg="#FFDDEB",font="Calibri 22 bold",border=0,activebackground="#FFDDEB",text="7",compound="center",fg="white",command=lambda:tableinfomation(7))
                                        table_7.place(x=50,y=420)
                                        if result[6][4] == "yes" :
                                            Button(yayoi_table_frame,image=staff_cal,border=0,bg="#62943B",command=staff_7).place(x=100,y=425)
                                        else :
                                            pass
                                    else :
                                        table_7 = Button(yayoi_table_frame,image=teble_red_act,bg="#FFDDEB",font="Calibri 22 bold",border=0,activebackground="#FFDDEB",text="7",compound="center",fg="white",command=lambda:tableinfomation(7),state="disabled")
                                        table_7.place(x=50,y=420)
                                    # 8
                                    if result[7][1] == "default" :
                                        table_8 = Button(yayoi_table_frame,image=teble_red_act,bg="#FFDDEB",font="Calibri 22 bold",border=0,activebackground="#FFDDEB",text="8",compound="center",fg="white",command=lambda:tableinfomation(8))
                                        table_8.place(x=140,y=420)
                                        def staff_8() :
                                            conn = sqlite3.connect("projectdb.db")
                                            cursor = conn.cursor()
                                            sql = """
                                                    UPDATE shop_yayoi_table
                                                    SET staffcall=?
                                                    WHERE table_no=? """
                                            cursor.execute(sql,["no","5"])
                                            conn.commit()
                                        if result[7][4] == "yes" :
                                            Button(yayoi_table_frame,image=staff_cal,border=0,bg="#62943B",command=staff_8).place(x=190,y=425)
                                        else :
                                            pass
                                    else :
                                        table_8 = Button(yayoi_table_frame,image=teble_red_act,bg="#FFDDEB",font="Calibri 22 bold",border=0,activebackground="#FFDDEB",text="8",compound="center",fg="white",command=lambda:tableinfomation(8),state="disabled")
                                        table_8.place(x=140,y=420)
                                    conn.close()
                                # Start             
                                Label(yayoi_admin_frame,image=yayoishop_header,bg="#FFFFFF").place(x=-2,y=-35)
                                Label(yayoi_admin_frame,image=yayoishop_logo,bg="#FFFFFF").place(x=40,y=0)
                                tablebut = Button(yayoi_admin_frame,image=button_yellow,border=0,activebackground="white",activeforeground="white",bg="white",text="Table",compound="center",font="Calibri 16",command=yayoi_table)
                                tablebut.place(x=880,y=112)
                                queuebut = Button(yayoi_admin_frame,image=button_yellow,border=0,activebackground="white",activeforeground="white",bg="white",text="Queue",compound="center",font="Calibri 16",command=yayoi_queue)
                                queuebut.place(x=780,y=112)
                                showtext = Label(yayoi_admin_frame,text="",font="Calibri 24 bold",bg="#FFA1C9")
                                showtext.place(x=250,y=30)
                                yayoi_table()
                            # AFTERYOU
                            elif result[3] == "AFTERYOU" :
                                frame_adminlogin.destroy()
                                afteryou_admin_frame = Frame(admin,bg="#FFFBEA")
                                afteryou_admin_frame.place(x=0,y=0,w=w,h=h)
                                # frame
                                def afteryou_queue() :
                                    global afteryou_queue
                                    def queueinfomation(number) :
                                        def afteryou_addtostore(namecus,numbergroup) :
                                            ans = messagebox.askquestion("Admin","Add customer to table %s"%(numbergroup))
                                            if ans == "yes" :
                                                if numbergroup == 1 or numbergroup == 2 or numbergroup == 3:
                                                    people = "1-2"
                                                elif numbergroup == 4 or numbergroup == 5 or numbergroup == 6:
                                                    people = "3-4"
                                                elif numbergroup == 7 or numbergroup == 8:
                                                    people = "3-4"
                                                #
                                                sql = """
                                                        UPDATE shop_afteryou_table
                                                        SET name=?,amount=?,staffcall=?
                                                        WHERE table_no=? """
                                                cursor.execute(sql,[namecus,people,"no",numbergroup])
                                                conn.commit()
                                                #
                                                sql = """
                                                        UPDATE shop_afteryou_table
                                                        SET status=?
                                                        WHERE table_no=? """
                                                cursor.execute(sql,["default",numbergroup])
                                                conn.commit()
                                                #
                                                sql = """
                                                        UPDATE shop_afteryou_queue
                                                        SET q_status=?
                                                        WHERE q_name=?"""
                                                cursor.execute(sql,["ready",namecus])   
                                                conn.commit()     
                                                conn.close()
                                            else :
                                                pass
                                        Label(afteryou_queue,image=queue_frame,bg="#FFE296").place(x=645,y=5)
                                        Label(afteryou_queue,text="Table %s"%(number),font="Calibri 24 bold",bg='#FFE296').place(x=670,y=20)
                                        Label(afteryou_queue,text="No.",font="Calibri 18",bg='#FFE296').place(x=660,y=70)
                                        Label(afteryou_queue,text="Name",font="Calibri 18",bg='#FFE296').place(x=860,y=70)
                                        conn = sqlite3.connect("projectdb.db")
                                        cursor = conn.cursor()
                                        if number == 1 or number == 2 or number == 3:
                                            sql = """
                                                    SELECT * FROM shop_afteryou_queue
                                                    WHERE q_amount=? and q_status=?"""
                                            cursor.execute(sql,["1-2","wait"])
                                            result = cursor.fetchall()
                                            
                                            yasix = 120
                                            for i,data in enumerate(result) :
                                                Label(afteryou_queue,text=data[0],bg="#FFE296").place(x=660,y=yasix)
                                                Label(afteryou_queue,text=data[1],bg="#FFE296").place(x=860,y=yasix)
                                                yasix = yasix +70
                                                afteryou1_2 = Button(afteryou_queue,text="bookatble",font="Calibri 18",bg='green',border=0,fg="white",command=lambda:afteryou_addtostore(result[0][1],number))
                                                afteryou1_2.place(x=660,y=470)
                                        elif number == 4 or number == 5 or number == 6:
                                            sql = """
                                                    SELECT * FROM shop_afteryou_queue
                                                    WHERE q_amount=? and q_status=?"""
                                            cursor.execute(sql,["3-4","wait"])
                                            result = cursor.fetchall()
                                            
                                            yasix = 120
                                            for i,data in enumerate(result) :
                                                Label(afteryou_queue,text=data[0],bg="#FFE296").place(x=660,y=yasix)
                                                Label(afteryou_queue,text=data[1],bg="#FFE296").place(x=860,y=yasix)
                                                yasix = yasix +70
                                                afteryou1_2 = Button(afteryou_queue,text="bookatble",font="Calibri 18",bg='green',border=0,fg="white",command=lambda:afteryou_addtostore(result[0][1],number))
                                                afteryou1_2.place(x=660,y=470)
                                        elif number == 7 or number == 8:
                                            sql = """
                                                    SELECT * FROM shop_afteryou_queue
                                                    WHERE q_amount=? and q_status=? """
                                            cursor.execute(sql,["5-6","wait"])
                                            result = cursor.fetchall()
                                            
                                            yasix = 120
                                            for i,data in enumerate(result) :
                                                Label(afteryou_queue,text=data[0],bg="#FFE296").place(x=660,y=yasix)
                                                Label(afteryou_queue,text=data[1],bg="#FFE296").place(x=860,y=yasix)
                                                yasix = yasix +70
                                                afteryou1_2 = Button(afteryou_queue,text="bookatble",font="Calibri 18",bg='green',border=0,fg="white",command=lambda:afteryou_addtostore(result[0][1],number))
                                                afteryou1_2.place(x=660,y=470)
                                    queuebut["state"] = "disabled"
                                    tablebut["state"] = "active"
                                    showtext["text"] = "Queue"
                                    afteryou_table_frame.destroy()
                                    afteryou_queue = Frame(afteryou_admin_frame,bg="#FFFBEA")
                                    afteryou_queue.place(x=0,y=160,w=w,h=h-140)
                                    Label(afteryou_queue,image=admin_yayoi_frame_1,bg="#FEF9E8").place(x=25,y=5)
                                    Label(afteryou_queue,image=queue_frame,bg="#FEF9E8").place(x=645,y=5)
                                    Label(afteryou_queue,image=admin_yayoi_table,bg="#FFDDEB").place(x=40,y=25)
                                    Label(afteryou_queue,text="1-2 People",bg="#FFDDEB",font="Calibri 18").place(x=40,y=65)
                                    Label(afteryou_queue,text="3-4 People",bg="#FFDDEB",font="Calibri 18").place(x=40,y=215)
                                    Label(afteryou_queue,text="5-6 People",bg="#FFDDEB",font="Calibri 18").place(x=40,y=365)
                                    # conn
                                    conn = sqlite3.connect("projectdb.db")
                                    cursor = conn.cursor()
                                    sql = """
                                            SELECT * FROM shop_afteryou_table """
                                    cursor.execute(sql)
                                    result = cursor.fetchall()
                                    # 1
                                    if result[0][1] == "free" :
                                        table_1 = Button(afteryou_queue,image=teble_green_act,bg="#FFDDEB",font="Calibri 22 bold",border=0,activebackground="#FFDDEB",text="1",compound="center",fg="white",command=lambda:queueinfomation(1))
                                        table_1.place(x=50,y=120)
                                    else :
                                        table_1 = Button(afteryou_queue,image=teble_green_act,bg="#FFDDEB",font="Calibri 22 bold",border=0,activebackground="#FFDDEB",text="1",compound="center",fg="white",command=lambda:queueinfomation(1),state="disabled")
                                        table_1.place(x=50,y=120)
                                    # 2
                                    if result[1][1] == "free" :
                                        table_2 = Button(afteryou_queue,image=teble_green_act,bg="#FFDDEB",font="Calibri 22 bold",border=0,activebackground="#FFDDEB",text="2",compound="center",fg="white",command=lambda:queueinfomation(2))
                                        table_2.place(x=140,y=120)
                                    else :
                                        table_2 = Button(afteryou_queue,image=teble_green_act,bg="#FFDDEB",font="Calibri 22 bold",border=0,activebackground="#FFDDEB",text="2",compound="center",fg="white",command=lambda:queueinfomation(2),state="disabled")
                                        table_2.place(x=140,y=120)
                                    # 3
                                    if result[2][1] == "free" :
                                        table_3 = Button(afteryou_queue,image=teble_green_act,bg="#FFDDEB",font="Calibri 22 bold",border=0,activebackground="#FFDDEB",text="3",compound="center",fg="white",command=lambda:queueinfomation(3))
                                        table_3.place(x=230,y=120)
                                    else :
                                        table_3 = Button(afteryou_queue,image=teble_green_act,bg="#FFDDEB",font="Calibri 22 bold",border=0,activebackground="#FFDDEB",text="3",compound="center",fg="white",command=lambda:queueinfomation(3),state="disabled")
                                        table_3.place(x=230,y=120)
                                    # 4
                                    if result[3][1] == "free" :
                                        table_4 = Button(afteryou_queue,image=teble_yellow_act,bg="#FFDDEB",font="Calibri 22 bold",border=0,activebackground="#FFDDEB",text="4",compound="center",fg="white",command=lambda:queueinfomation(4))
                                        table_4.place(x=50,y=270)
                                    else :
                                        table_4 = Button(afteryou_queue,image=teble_yellow_act,bg="#FFDDEB",font="Calibri 22 bold",border=0,activebackground="#FFDDEB",text="4",compound="center",fg="white",command=lambda:queueinfomation(4),state="disabled")
                                        table_4.place(x=50,y=270)
                                    # 5
                                    if result[4][1] == "free" :
                                        table_5 = Button(afteryou_queue,image=teble_yellow_act,bg="#FFDDEB",font="Calibri 22 bold",border=0,activebackground="#FFDDEB",text="5",compound="center",fg="white",command=lambda:queueinfomation(5))
                                        table_5.place(x=140,y=270)
                                    else :
                                        table_5 = Button(afteryou_queue,image=teble_yellow_act,bg="#FFDDEB",font="Calibri 22 bold",border=0,activebackground="#FFDDEB",text="5",compound="center",fg="white",command=lambda:queueinfomation(5),state="disabled")
                                        table_5.place(x=140,y=270)
                                    # 6
                                    if result[5][1] == "free" :
                                        table_6 = Button(afteryou_queue,image=teble_yellow_act,bg="#FFDDEB",font="Calibri 22 bold",border=0,activebackground="#FFDDEB",text="6",compound="center",fg="white",command=lambda:queueinfomation(6))
                                        table_6.place(x=230,y=270)
                                    else :
                                        table_6 = Button(afteryou_queue,image=teble_yellow_act,bg="#FFDDEB",font="Calibri 22 bold",border=0,activebackground="#FFDDEB",text="6",compound="center",fg="white",command=lambda:queueinfomation(6),state="disabled")
                                        table_6.place(x=230,y=270)
                                    # 7
                                    if result[6][1] == "free" :
                                        table_7 = Button(afteryou_queue,image=teble_red_act,bg="#FFDDEB",font="Calibri 22 bold",border=0,activebackground="#FFDDEB",text="7",compound="center",fg="white",command=lambda:queueinfomation(7))
                                        table_7.place(x=50,y=420)
                                    else :
                                        table_7 = Button(afteryou_queue,image=teble_red_act,bg="#FFDDEB",font="Calibri 22 bold",border=0,activebackground="#FFDDEB",text="7",compound="center",fg="white",command=lambda:queueinfomation(7),state="disabled")
                                        table_7.place(x=50,y=420)
                                    # 8
                                    if result[7][1] == "free" :
                                        table_8 = Button(afteryou_queue,image=teble_red_act,bg="#FFDDEB",font="Calibri 22 bold",border=0,activebackground="#FFDDEB",text="8",compound="center",fg="white",command=lambda:queueinfomation(8))
                                        table_8.place(x=140,y=420)
                                    else :
                                        table_8 = Button(afteryou_queue,image=teble_red_act,bg="#FFDDEB",font="Calibri 22 bold",border=0,activebackground="#FFDDEB",text="8",compound="center",fg="white",command=lambda:queueinfomation(8),state="disabled")
                                        table_8.place(x=140,y=420)
                                    conn.close()
                                def afteryou_table() :
                                    global afteryou_table_frame
                                    # def
                                    def tableinfomation(no):
                                        def afteryou_confirmorder() :
                                            ans = messagebox.askquestion("Admin","Confirm order") 
                                            if ans == "yes" :
                                                if result :
                                                    for i,data in enumerate(result) :
                                                        sql = """
                                                                    UPDATE shop_afteryou_orderprocess
                                                                    SET status=? WHERE menu_name =? """
                                                        cursor.execute(sql,["F",data[1]])
                                                        conn.commit()
                                                else :
                                                    afteryoucon["state"] = "disabled"
                                                    afteryoucon["fg"] = "white"
                                                conn.close()
                                            else :
                                                pass
                                        Label(afteryou_table_frame,image=admin_yayoi_frame_2,bg="#FEF9E8").place(x=645,y=5)
                                        Label(afteryou_table_frame,text="Table %s"%(no),font="Calibri 24 bold",bg='#DFDCED').place(x=670,y=20)
                                        Label(afteryou_table_frame,text="Menu",font="Calibri 18",bg='#DFDCED').place(x=660,y=70)
                                        Label(afteryou_table_frame,text="Amount",font="Calibri 18",bg='#DFDCED').place(x=860,y=70)
                                        conn = sqlite3.connect("projectdb.db")
                                        cursor = conn.cursor()
                                        sql = """
                                                SELECT * FROM shop_afteryou_orderprocess 
                                                WHERE table_index=? and status=?"""
                                        cursor.execute(sql,[no,"NF"])
                                        result = cursor.fetchall()
                                        indexy = 120
                                        for i,data in enumerate(result) :
                                            if i<6 :
                                                Label(afteryou_table_frame,text=data[1][0:17],font="Calibri 18",bg='#DFDCED').place(x=660,y=indexy)
                                                Label(afteryou_table_frame,text=data[3][0:17],font="Calibri 18",bg='#DFDCED').place(x=890,y=indexy)
                                            else :
                                                pass
                                            indexy = indexy + 50
                                        afteryoucon = Button(afteryou_table_frame,text="Confirm Order",font="Calibri 18",bg='green',border=0,fg="white",command=afteryou_confirmorder)
                                        afteryoucon.place(x=660,y=460)
                                    #
                                    tablebut["state"] = "disabled"
                                    queuebut["state"] = "active"
                                    showtext["text"] = "Table info"
                                    afteryou_table_frame = Frame(afteryou_admin_frame,bg="#FFFBEA")
                                    afteryou_table_frame.place(x=0,y=160,w=w,h=h-140)
                                    Label(afteryou_table_frame,image=admin_yayoi_frame_1,bg="#FEF9E8").place(x=25,y=5)
                                    Label(afteryou_table_frame,image=admin_yayoi_frame_2,bg="#FEF9E8").place(x=645,y=5)
                                    Label(afteryou_table_frame,image=admin_yayoi_table,bg="#FFDDEB").place(x=40,y=25)
                                    Label(afteryou_table_frame,text="1-2 People",bg="#FFDDEB",font="Calibri 18").place(x=40,y=65)
                                    Label(afteryou_table_frame,text="3-4 People",bg="#FFDDEB",font="Calibri 18").place(x=40,y=215)
                                    Label(afteryou_table_frame,text="5-6 People",bg="#FFDDEB",font="Calibri 18").place(x=40,y=365)
                                    # conn
                                    conn = sqlite3.connect("projectdb.db")
                                    cursor = conn.cursor()
                                    sql = """
                                            SELECT * FROM shop_afteryou_table """
                                    cursor.execute(sql)
                                    result = cursor.fetchall()
                                    conn.close()
                                    # 1
                                    if result[0][1] == "default" :
                                        table_1 = Button(afteryou_table_frame,image=teble_green_act,bg="#FFDDEB",font="Calibri 22 bold",border=0,activebackground="#FFDDEB",text="1",compound="center",fg="white",command=lambda:tableinfomation(1))
                                        table_1.place(x=50,y=120)
                                        def staff_1() :
                                            conn = sqlite3.connect("projectdb.db")
                                            cursor = conn.cursor()
                                            sql = """
                                                    UPDATE shop_afteryou_table
                                                    SET staffcall=?
                                                    WHERE table_no=? """
                                            cursor.execute(sql,["no","1"])
                                            conn.commit()
                                        if result[0][4] == "yes" :
                                            Button(afteryou_table_frame,image=staff_cal,border=0,bg="#62943B",command=staff_1).place(x=100,y=125)
                                        else :
                                            pass
                                    else :
                                        table_1 = Button(afteryou_table_frame,image=teble_green_act,bg="#FFDDEB",font="Calibri 22 bold",border=0,activebackground="#FFDDEB",text="1",compound="center",fg="white",command=lambda:tableinfomation(1),state="disabled")
                                        table_1.place(x=50,y=120)
                                    # 2
                                    if result[1][1] == "default" :
                                        table_2 = Button(afteryou_table_frame,image=teble_green_act,bg="#FFDDEB",font="Calibri 22 bold",border=0,activebackground="#FFDDEB",text="2",compound="center",fg="white",command=lambda:tableinfomation(2))
                                        table_2.place(x=140,y=120)
                                        def staff_2() :
                                            conn = sqlite3.connect("projectdb.db")
                                            cursor = conn.cursor()
                                            sql = """
                                                    UPDATE shop_afteryou_table
                                                    SET staffcall=?
                                                    WHERE table_no=? """
                                            cursor.execute(sql,["no","2"])
                                            conn.commit()
                                        if result[1][4] == "yes" :
                                            Button(afteryou_table_frame,image=staff_cal,border=0,bg="#62943B",command=staff_2).place(x=190,y=125)
                                        else :
                                            pass
                                    else :
                                        table_2 = Button(afteryou_table_frame,image=teble_green_act,bg="#FFDDEB",font="Calibri 22 bold",border=0,activebackground="#FFDDEB",text="2",compound="center",fg="white",command=lambda:tableinfomation(2),state="disabled")
                                        table_2.place(x=140,y=120)
                                    # 3
                                    if result[2][1] == "default" :
                                        table_3 = Button(afteryou_table_frame,image=teble_green_act,bg="#FFDDEB",font="Calibri 22 bold",border=0,activebackground="#FFDDEB",text="3",compound="center",fg="white",command=lambda:tableinfomation(3))
                                        table_3.place(x=230,y=120)
                                        def staff_3() :
                                            conn = sqlite3.connect("projectdb.db")
                                            cursor = conn.cursor()
                                            sql = """
                                                    UPDATE shop_afteryou_table
                                                    SET staffcall=?
                                                    WHERE table_no=? """
                                            cursor.execute(sql,["no","3"])
                                            conn.commit()
                                        if result[2][4] == "yes" :
                                            Button(afteryou_table_frame,image=staff_cal,border=0,bg="#62943B",command=staff_3).place(x=280,y=125)
                                        else :
                                            pass
                                    else :
                                        table_3 = Button(afteryou_table_frame,image=teble_green_act,bg="#FFDDEB",font="Calibri 22 bold",border=0,activebackground="#FFDDEB",text="3",compound="center",fg="white",command=lambda:tableinfomation(3),state="disabled")
                                        table_3.place(x=230,y=120)
                                    # 4
                                    if result[3][1] == "default" :
                                        table_4 = Button(afteryou_table_frame,image=teble_yellow_act,bg="#FFDDEB",font="Calibri 22 bold",border=0,activebackground="#FFDDEB",text="4",compound="center",fg="white",command=lambda:tableinfomation(4))
                                        table_4.place(x=50,y=270)
                                        def staff_4() :
                                            conn = sqlite3.connect("projectdb.db")
                                            cursor = conn.cursor()
                                            sql = """
                                                    UPDATE shop_afteryou_table
                                                    SET staffcall=?
                                                    WHERE table_no=? """
                                            cursor.execute(sql,["no","4"])
                                            conn.commit()
                                        if result[3][4] == "yes" :
                                            Button(afteryou_table_frame,image=staff_cal,border=0,bg="#62943B",command=staff_4).place(x=100,y=275)
                                        else :
                                            pass
                                    else :
                                        table_4 = Button(afteryou_table_frame,image=teble_yellow_act,bg="#FFDDEB",font="Calibri 22 bold",border=0,activebackground="#FFDDEB",text="4",compound="center",fg="white",command=lambda:tableinfomation(4),state="disabled")
                                        table_4.place(x=50,y=270)
                                    # 5
                                    if result[4][1] == "default" :
                                        table_5 = Button(afteryou_table_frame,image=teble_yellow_act,bg="#FFDDEB",font="Calibri 22 bold",border=0,activebackground="#FFDDEB",text="5",compound="center",fg="white",command=lambda:tableinfomation(5))
                                        table_5.place(x=140,y=270)
                                        def staff_5() :
                                            conn = sqlite3.connect("projectdb.db")
                                            cursor = conn.cursor()
                                            sql = """
                                                    UPDATE shop_afteryou_table
                                                    SET staffcall=?
                                                    WHERE table_no=? """
                                            cursor.execute(sql,["no","5"])
                                            conn.commit()
                                        if result[4][4] == "yes" :
                                            Button(afteryou_table_frame,image=staff_cal,border=0,bg="#62943B",command=staff_5).place(x=190,y=275)
                                        else :
                                            pass
                                    else :
                                        table_5 = Button(afteryou_table_frame,image=teble_yellow_act,bg="#FFDDEB",font="Calibri 22 bold",border=0,activebackground="#FFDDEB",text="5",compound="center",fg="white",command=lambda:tableinfomation(5),state="disabled")
                                        table_5.place(x=140,y=270)
                                    # 6
                                    if result[5][1] == "default" :
                                        table_6 = Button(afteryou_table_frame,image=teble_yellow_act,bg="#FFDDEB",font="Calibri 22 bold",border=0,activebackground="#FFDDEB",text="6",compound="center",fg="white",command=lambda:tableinfomation(6))
                                        table_6.place(x=230,y=270)
                                        def staff_6() :
                                            conn = sqlite3.connect("projectdb.db")
                                            cursor = conn.cursor()
                                            sql = """
                                                    UPDATE shop_afteryou_table
                                                    SET staffcall=?
                                                    WHERE table_no=? """
                                            cursor.execute(sql,["no","5"])
                                            conn.commit()
                                        if result[5][4] == "yes" :
                                            Button(afteryou_table_frame,image=staff_cal,border=0,bg="#62943B",command=staff_6).place(x=280,y=275)
                                        else :
                                            pass
                                    else :
                                        table_6 = Button(afteryou_table_frame,image=teble_yellow_act,bg="#FFDDEB",font="Calibri 22 bold",border=0,activebackground="#FFDDEB",text="6",compound="center",fg="white",command=lambda:tableinfomation(6),state="disabled")
                                        table_6.place(x=230,y=270)
                                    # 7
                                    if result[6][1] == "default" :
                                        def staff_7() :
                                            conn = sqlite3.connect("projectdb.db")
                                            cursor = conn.cursor()
                                            sql = """
                                                    UPDATE shop_afteryou_table
                                                    SET staffcall=?
                                                    WHERE table_no=? """
                                            cursor.execute(sql,["no","5"])
                                            conn.commit()
                                        table_7 = Button(afteryou_table_frame,image=teble_red_act,bg="#FFDDEB",font="Calibri 22 bold",border=0,activebackground="#FFDDEB",text="7",compound="center",fg="white",command=lambda:tableinfomation(7))
                                        table_7.place(x=50,y=420)
                                        if result[6][4] == "yes" :
                                            Button(afteryou_table_frame,image=staff_cal,border=0,bg="#62943B",command=staff_7).place(x=100,y=425)
                                        else :
                                            pass
                                    else :
                                        table_7 = Button(afteryou_table_frame,image=teble_red_act,bg="#FFDDEB",font="Calibri 22 bold",border=0,activebackground="#FFDDEB",text="7",compound="center",fg="white",command=lambda:tableinfomation(7),state="disabled")
                                        table_7.place(x=50,y=420)
                                    # 8
                                    if result[7][1] == "default" :
                                        table_8 = Button(afteryou_table_frame,image=teble_red_act,bg="#FFDDEB",font="Calibri 22 bold",border=0,activebackground="#FFDDEB",text="8",compound="center",fg="white",command=lambda:tableinfomation(8))
                                        table_8.place(x=140,y=420)
                                        def staff_8() :
                                            conn = sqlite3.connect("projectdb.db")
                                            cursor = conn.cursor()
                                            sql = """
                                                    UPDATE shop_afteryou_table
                                                    SET staffcall=?
                                                    WHERE table_no=? """
                                            cursor.execute(sql,["no","5"])
                                            conn.commit()
                                        if result[7][4] == "yes" :
                                            Button(afteryou_table_frame,image=staff_cal,border=0,bg="#62943B",command=staff_8).place(x=190,y=425)
                                        else :
                                            pass
                                    else :
                                        table_8 = Button(afteryou_table_frame,image=teble_red_act,bg="#FFDDEB",font="Calibri 22 bold",border=0,activebackground="#FFDDEB",text="8",compound="center",fg="white",command=lambda:tableinfomation(8),state="disabled")
                                        table_8.place(x=140,y=420)
                                    conn.close()
                                # Start             
                                Label(afteryou_admin_frame,image=afteryou_header,bg="#FFFBEA").place(x=-2,y=-15)
                                Label(afteryou_admin_frame,image=afteryou_logo,bg="#FFFBEA").place(x=40,y=0)
                                tablebut = Button(afteryou_admin_frame,image=button_yellow,border=0,activebackground="white",activeforeground="white",bg="#FFFBEA",text="Table",compound="center",font="Calibri 16",command=afteryou_table)
                                tablebut.place(x=880,y=112)
                                queuebut = Button(afteryou_admin_frame,image=button_yellow,border=0,activebackground="white",activeforeground="white",bg="#FFFBEA",text="Queue",compound="center",font="Calibri 16",command=afteryou_queue)
                                queuebut.place(x=780,y=112)
                                showtext = Label(afteryou_admin_frame,text="",font="Calibri 24 bold",bg="#DCC6AE")
                                showtext.place(x=250,y=30)
                                afteryou_table()
                            # KYO
                            elif result[3] == "KYO" :
                                frame_adminlogin.destroy()
                                kyo_admin_frame = Frame(admin,bg="#FFFBEA")
                                kyo_admin_frame.place(x=0,y=0,w=w,h=h)
                                # frame
                                def kyo_queue() :
                                    global kyo_queue
                                    def queueinfomation(number) :
                                        def kyo_addtostore(namecus,numbergroup) :
                                            ans = messagebox.askquestion("Admin","Add customer to table %s"%(numbergroup))
                                            if ans == "yes" :
                                                if numbergroup == 1 or numbergroup == 2 or numbergroup == 3:
                                                    people = "1-2"
                                                elif numbergroup == 4 or numbergroup == 5 or numbergroup == 6:
                                                    people = "3-4"
                                                elif numbergroup == 7 or numbergroup == 8:
                                                    people = "3-4"
                                                #
                                                sql = """
                                                        UPDATE shop_kyo_table
                                                        SET name=?,amount=?,staffcall=?
                                                        WHERE table_no=? """
                                                cursor.execute(sql,[namecus,people,"no",numbergroup])
                                                conn.commit()
                                                #
                                                sql = """
                                                        UPDATE shop_kyo_table
                                                        SET status=?
                                                        WHERE table_no=? """
                                                cursor.execute(sql,["default",numbergroup])
                                                conn.commit()
                                                #
                                                sql = """
                                                        UPDATE shop_kyo_queue
                                                        SET q_status=?
                                                        WHERE q_name=?"""
                                                cursor.execute(sql,["ready",namecus])   
                                                conn.commit()     
                                                conn.close()
                                            else:
                                                pass
                                        Label(kyo_queue,image=queue_frame,bg="#FFE296").place(x=645,y=5)
                                        Label(kyo_queue,text="Table %s"%(number),font="Calibri 24 bold",bg='#FFE296').place(x=670,y=20)
                                        Label(kyo_queue,text="No.",font="Calibri 18",bg='#FFE296').place(x=660,y=70)
                                        Label(kyo_queue,text="Name",font="Calibri 18",bg='#FFE296').place(x=860,y=70)
                                        conn = sqlite3.connect("projectdb.db")
                                        cursor = conn.cursor()
                                        if number == 1 or number == 2 or number == 3:
                                            sql = """
                                                    SELECT * FROM shop_kyo_queue
                                                    WHERE q_amount=? and q_status=?"""
                                            cursor.execute(sql,["1-2","wait"])
                                            result = cursor.fetchall()
                                            
                                            yasix = 120
                                            for i,data in enumerate(result) :
                                                Label(kyo_queue,text=data[0],bg="#FFE296").place(x=660,y=yasix)
                                                Label(kyo_queue,text=data[1],bg="#FFE296").place(x=860,y=yasix)
                                                yasix = yasix +70
                                                kyo1_2 = Button(kyo_queue,text="bookatble",font="Calibri 18",bg='green',border=0,fg="white",command=lambda:kyo_addtostore(result[0][1],number))
                                                kyo1_2.place(x=660,y=470)
                                        elif number == 4 or number == 5 or number == 6:
                                            
                                            sql = """
                                                    SELECT * FROM shop_kyo_queue
                                                    WHERE q_amount=? and q_status=?"""
                                            cursor.execute(sql,["3-4","wait"])
                                            result = cursor.fetchall()
                                            
                                            yasix = 120
                                            for i,data in enumerate(result) :
                                                Label(kyo_queue,text=data[0],bg="#FFE296").place(x=660,y=yasix)
                                                Label(kyo_queue,text=data[1],bg="#FFE296").place(x=860,y=yasix)
                                                yasix = yasix +70
                                                kyo1_2 = Button(kyo_queue,text="bookatble",font="Calibri 18",bg='green',border=0,fg="white",command=lambda:kyo_addtostore(result[0][1],number))
                                                kyo1_2.place(x=660,y=470)
                                        elif number == 7 or number == 8:
                                            
                                            sql = """
                                                    SELECT * FROM shop_kyo_queue
                                                    WHERE q_amount=? and q_status=? """
                                            cursor.execute(sql,["5-6","wait"])
                                            result = cursor.fetchall()
                                            
                                            yasix = 120
                                            for i,data in enumerate(result) :
                                                Label(kyo_queue,text=data[0],bg="#FFE296").place(x=660,y=yasix)
                                                Label(kyo_queue,text=data[1],bg="#FFE296").place(x=860,y=yasix)
                                                yasix = yasix +70
                                                kyo1_2 = Button(kyo_queue,text="bookatble",font="Calibri 18",bg='green',border=0,fg="white",command=lambda:kyo_addtostore(result[0][1],number))
                                                kyo1_2.place(x=660,y=470)
                                    queuebut["state"] = "disabled"
                                    tablebut["state"] = "active"
                                    showtext["text"] = "Queue"
                                    kyo_table_frame.destroy()
                                    kyo_queue = Frame(kyo_admin_frame,bg="#FFFBEA")
                                    kyo_queue.place(x=0,y=160,w=w,h=h-140)
                                    Label(kyo_queue,image=admin_yayoi_frame_1,bg="#FEF9E8").place(x=25,y=5)
                                    Label(kyo_queue,image=queue_frame,bg="#FEF9E8").place(x=645,y=5)
                                    Label(kyo_queue,image=admin_yayoi_table,bg="#FFDDEB").place(x=40,y=25)
                                    Label(kyo_queue,text="1-2 People",bg="#FFDDEB",font="Calibri 18").place(x=40,y=65)
                                    Label(kyo_queue,text="3-4 People",bg="#FFDDEB",font="Calibri 18").place(x=40,y=215)
                                    Label(kyo_queue,text="5-6 People",bg="#FFDDEB",font="Calibri 18").place(x=40,y=365)
                                    # conn
                                    conn = sqlite3.connect("projectdb.db")
                                    cursor = conn.cursor()
                                    sql = """
                                            SELECT * FROM shop_kyo_table """
                                    cursor.execute(sql)
                                    result = cursor.fetchall()
                                    # 1
                                    if result[0][1] == "free" :
                                        table_1 = Button(kyo_queue,image=teble_green_act,bg="#FFDDEB",font="Calibri 22 bold",border=0,activebackground="#FFDDEB",text="1",compound="center",fg="white",command=lambda:queueinfomation(1))
                                        table_1.place(x=50,y=120)
                                    else :
                                        table_1 = Button(kyo_queue,image=teble_green_act,bg="#FFDDEB",font="Calibri 22 bold",border=0,activebackground="#FFDDEB",text="1",compound="center",fg="white",command=lambda:queueinfomation(1),state="disabled")
                                        table_1.place(x=50,y=120)
                                    # 2
                                    if result[1][1] == "free" :
                                        table_2 = Button(kyo_queue,image=teble_green_act,bg="#FFDDEB",font="Calibri 22 bold",border=0,activebackground="#FFDDEB",text="2",compound="center",fg="white",command=lambda:queueinfomation(2))
                                        table_2.place(x=140,y=120)
                                    else :
                                        table_2 = Button(kyo_queue,image=teble_green_act,bg="#FFDDEB",font="Calibri 22 bold",border=0,activebackground="#FFDDEB",text="2",compound="center",fg="white",command=lambda:queueinfomation(2),state="disabled")
                                        table_2.place(x=140,y=120)
                                    # 3
                                    if result[2][1] == "free" :
                                        table_3 = Button(kyo_queue,image=teble_green_act,bg="#FFDDEB",font="Calibri 22 bold",border=0,activebackground="#FFDDEB",text="3",compound="center",fg="white",command=lambda:queueinfomation(3))
                                        table_3.place(x=230,y=120)
                                    else :
                                        table_3 = Button(kyo_queue,image=teble_green_act,bg="#FFDDEB",font="Calibri 22 bold",border=0,activebackground="#FFDDEB",text="3",compound="center",fg="white",command=lambda:queueinfomation(3),state="disabled")
                                        table_3.place(x=230,y=120)
                                    # 4
                                    if result[3][1] == "free" :
                                        table_4 = Button(kyo_queue,image=teble_yellow_act,bg="#FFDDEB",font="Calibri 22 bold",border=0,activebackground="#FFDDEB",text="4",compound="center",fg="white",command=lambda:queueinfomation(4))
                                        table_4.place(x=50,y=270)
                                    else :
                                        table_4 = Button(kyo_queue,image=teble_yellow_act,bg="#FFDDEB",font="Calibri 22 bold",border=0,activebackground="#FFDDEB",text="4",compound="center",fg="white",command=lambda:queueinfomation(4),state="disabled")
                                        table_4.place(x=50,y=270)
                                    # 5
                                    if result[4][1] == "free" :
                                        table_5 = Button(kyo_queue,image=teble_yellow_act,bg="#FFDDEB",font="Calibri 22 bold",border=0,activebackground="#FFDDEB",text="5",compound="center",fg="white",command=lambda:queueinfomation(5))
                                        table_5.place(x=140,y=270)
                                    else :
                                        table_5 = Button(kyo_queue,image=teble_yellow_act,bg="#FFDDEB",font="Calibri 22 bold",border=0,activebackground="#FFDDEB",text="5",compound="center",fg="white",command=lambda:queueinfomation(5),state="disabled")
                                        table_5.place(x=140,y=270)
                                    # 6
                                    if result[5][1] == "free" :
                                        table_6 = Button(kyo_queue,image=teble_yellow_act,bg="#FFDDEB",font="Calibri 22 bold",border=0,activebackground="#FFDDEB",text="6",compound="center",fg="white",command=lambda:queueinfomation(6))
                                        table_6.place(x=230,y=270)
                                    else :
                                        table_6 = Button(kyo_queue,image=teble_yellow_act,bg="#FFDDEB",font="Calibri 22 bold",border=0,activebackground="#FFDDEB",text="6",compound="center",fg="white",command=lambda:queueinfomation(6),state="disabled")
                                        table_6.place(x=230,y=270)
                                    # 7
                                    if result[6][1] == "free" :
                                        table_7 = Button(kyo_queue,image=teble_red_act,bg="#FFDDEB",font="Calibri 22 bold",border=0,activebackground="#FFDDEB",text="7",compound="center",fg="white",command=lambda:queueinfomation(7))
                                        table_7.place(x=50,y=420)
                                    else :
                                        table_7 = Button(kyo_queue,image=teble_red_act,bg="#FFDDEB",font="Calibri 22 bold",border=0,activebackground="#FFDDEB",text="7",compound="center",fg="white",command=lambda:queueinfomation(7),state="disabled")
                                        table_7.place(x=50,y=420)
                                    # 8
                                    if result[7][1] == "free" :
                                        table_8 = Button(kyo_queue,image=teble_red_act,bg="#FFDDEB",font="Calibri 22 bold",border=0,activebackground="#FFDDEB",text="8",compound="center",fg="white",command=lambda:queueinfomation(8))
                                        table_8.place(x=140,y=420)
                                    else :
                                        table_8 = Button(kyo_queue,image=teble_red_act,bg="#FFDDEB",font="Calibri 22 bold",border=0,activebackground="#FFDDEB",text="8",compound="center",fg="white",command=lambda:queueinfomation(8),state="disabled")
                                        table_8.place(x=140,y=420)
                                    conn.close()
                                def kyo_table() :
                                    global kyo_table_frame
                                    # def
                                    def tableinfomation(no):
                                        def kyo_confirmorder() :
                                            ans = messagebox.askquestion("Admin","Confirm order") 
                                            if ans == "yes" :
                                                if result :
                                                    for i,data in enumerate(result) :
                                                        sql = """
                                                                    UPDATE shop_kyo_orderprocess
                                                                    SET status=? WHERE menu_name =? """
                                                        cursor.execute(sql,["F",data[1]])
                                                        conn.commit()
                                                else :
                                                    kyocon["state"] = "disabled"
                                                    kyocon["fg"] = "white"
                                                conn.close()
                                            else :
                                                pass
                                        Label(kyo_table_frame,image=admin_yayoi_frame_2,bg="#FFFFFF").place(x=645,y=5)
                                        Label(kyo_table_frame,text="Table %s"%(no),font="Calibri 24 bold",bg='#DFDCED').place(x=670,y=20)
                                        Label(kyo_table_frame,text="Menu",font="Calibri 18",bg='#DFDCED').place(x=660,y=70)
                                        Label(kyo_table_frame,text="Amount",font="Calibri 18",bg='#DFDCED').place(x=860,y=70)
                                        conn = sqlite3.connect("projectdb.db")
                                        cursor = conn.cursor()
                                        sql = """
                                                SELECT * FROM shop_kyo_orderprocess 
                                                WHERE table_index=? and status=?"""
                                        cursor.execute(sql,[no,"NF"])
                                        result = cursor.fetchall()
                                        indexy = 120
                                        for i,data in enumerate(result) :
                                            if i<6 :
                                                Label(kyo_table_frame,text=data[1][0:17],font="Calibri 18",bg='#DFDCED').place(x=660,y=indexy)
                                                Label(kyo_table_frame,text=data[3][0:17],font="Calibri 18",bg='#DFDCED').place(x=890,y=indexy)
                                            else :
                                                pass
                                            indexy = indexy + 50
                                        kyocon = Button(kyo_table_frame,text="Confirm Order",font="Calibri 18",bg='green',border=0,fg="white",command=kyo_confirmorder)
                                        kyocon.place(x=660,y=460)
                                    #
                                    tablebut["state"] = "disabled"
                                    queuebut["state"] = "active"
                                    showtext["text"] = "Table info"
                                    kyo_table_frame = Frame(kyo_admin_frame,bg="#FFFBEA")
                                    kyo_table_frame.place(x=0,y=160,w=w,h=h-140)
                                    Label(kyo_table_frame,image=admin_yayoi_frame_1,bg="#FEF9E8").place(x=25,y=5)
                                    Label(kyo_table_frame,image=admin_yayoi_frame_2,bg="#FEF9E8").place(x=645,y=5)
                                    Label(kyo_table_frame,image=admin_yayoi_table,bg="#FFDDEB").place(x=40,y=25)
                                    Label(kyo_table_frame,text="1-2 People",bg="#FFDDEB",font="Calibri 18").place(x=40,y=65)
                                    Label(kyo_table_frame,text="3-4 People",bg="#FFDDEB",font="Calibri 18").place(x=40,y=215)
                                    Label(kyo_table_frame,text="5-6 People",bg="#FFDDEB",font="Calibri 18").place(x=40,y=365)
                                    # conn
                                    conn = sqlite3.connect("projectdb.db")
                                    cursor = conn.cursor()
                                    sql = """
                                            SELECT * FROM shop_kyo_table """
                                    cursor.execute(sql)
                                    result = cursor.fetchall()
                                    conn.close()
                                    # 1
                                    if result[0][1] == "default" :
                                        table_1 = Button(kyo_table_frame,image=teble_green_act,bg="#FFDDEB",font="Calibri 22 bold",border=0,activebackground="#FFDDEB",text="1",compound="center",fg="white",command=lambda:tableinfomation(1))
                                        table_1.place(x=50,y=120)
                                        def staff_1() :
                                            conn = sqlite3.connect("projectdb.db")
                                            cursor = conn.cursor()
                                            sql = """
                                                    UPDATE shop_kyo_table
                                                    SET staffcall=?
                                                    WHERE table_no=? """
                                            cursor.execute(sql,["no","1"])
                                            conn.commit()
                                        if result[0][4] == "yes" :
                                            Button(kyo_table_frame,image=staff_cal,border=0,bg="#62943B",command=staff_1).place(x=100,y=125)
                                        else :
                                            pass
                                    else :
                                        table_1 = Button(kyo_table_frame,image=teble_green_act,bg="#FFDDEB",font="Calibri 22 bold",border=0,activebackground="#FFDDEB",text="1",compound="center",fg="white",command=lambda:tableinfomation(1),state="disabled")
                                        table_1.place(x=50,y=120)
                                    # 2
                                    if result[1][1] == "default" :
                                        table_2 = Button(kyo_table_frame,image=teble_green_act,bg="#FFDDEB",font="Calibri 22 bold",border=0,activebackground="#FFDDEB",text="2",compound="center",fg="white",command=lambda:tableinfomation(2))
                                        table_2.place(x=140,y=120)
                                        def staff_2() :
                                            conn = sqlite3.connect("projectdb.db")
                                            cursor = conn.cursor()
                                            sql = """
                                                    UPDATE shop_kyo_table
                                                    SET staffcall=?
                                                    WHERE table_no=? """
                                            cursor.execute(sql,["no","2"])
                                            conn.commit()
                                        if result[1][4] == "yes" :
                                            Button(kyo_table_frame,image=staff_cal,border=0,bg="#62943B",command=staff_2).place(x=190,y=125)
                                        else :
                                            pass
                                    else :
                                        table_2 = Button(kyo_table_frame,image=teble_green_act,bg="#FFDDEB",font="Calibri 22 bold",border=0,activebackground="#FFDDEB",text="2",compound="center",fg="white",command=lambda:tableinfomation(2),state="disabled")
                                        table_2.place(x=140,y=120)
                                    # 3
                                    if result[2][1] == "default" :
                                        table_3 = Button(kyo_table_frame,image=teble_green_act,bg="#FFDDEB",font="Calibri 22 bold",border=0,activebackground="#FFDDEB",text="3",compound="center",fg="white",command=lambda:tableinfomation(3))
                                        table_3.place(x=230,y=120)
                                        def staff_3() :
                                            conn = sqlite3.connect("projectdb.db")
                                            cursor = conn.cursor()
                                            sql = """
                                                    UPDATE shop_kyo_table
                                                    SET staffcall=?
                                                    WHERE table_no=? """
                                            cursor.execute(sql,["no","3"])
                                            conn.commit()
                                        if result[2][4] == "yes" :
                                            Button(kyo_table_frame,image=staff_cal,border=0,bg="#62943B",command=staff_3).place(x=280,y=125)
                                        else :
                                            pass
                                    else :
                                        table_3 = Button(kyo_table_frame,image=teble_green_act,bg="#FFDDEB",font="Calibri 22 bold",border=0,activebackground="#FFDDEB",text="3",compound="center",fg="white",command=lambda:tableinfomation(3),state="disabled")
                                        table_3.place(x=230,y=120)
                                    # 4
                                    if result[3][1] == "default" :
                                        table_4 = Button(kyo_table_frame,image=teble_yellow_act,bg="#FFDDEB",font="Calibri 22 bold",border=0,activebackground="#FFDDEB",text="4",compound="center",fg="white",command=lambda:tableinfomation(4))
                                        table_4.place(x=50,y=270)
                                        def staff_4() :
                                            conn = sqlite3.connect("projectdb.db")
                                            cursor = conn.cursor()
                                            sql = """
                                                    UPDATE shop_kyo_table
                                                    SET staffcall=?
                                                    WHERE table_no=? """
                                            cursor.execute(sql,["no","4"])
                                            conn.commit()
                                        if result[3][4] == "yes" :
                                            Button(kyo_table_frame,image=staff_cal,border=0,bg="#62943B",command=staff_4).place(x=100,y=275)
                                        else :
                                            pass
                                    else :
                                        table_4 = Button(kyo_table_frame,image=teble_yellow_act,bg="#FFDDEB",font="Calibri 22 bold",border=0,activebackground="#FFDDEB",text="4",compound="center",fg="white",command=lambda:tableinfomation(4),state="disabled")
                                        table_4.place(x=50,y=270)
                                    # 5
                                    if result[4][1] == "default" :
                                        table_5 = Button(kyo_table_frame,image=teble_yellow_act,bg="#FFDDEB",font="Calibri 22 bold",border=0,activebackground="#FFDDEB",text="5",compound="center",fg="white",command=lambda:tableinfomation(5))
                                        table_5.place(x=140,y=270)
                                        def staff_5() :
                                            conn = sqlite3.connect("projectdb.db")
                                            cursor = conn.cursor()
                                            sql = """
                                                    UPDATE shop_kyo_table
                                                    SET staffcall=?
                                                    WHERE table_no=? """
                                            cursor.execute(sql,["no","5"])
                                            conn.commit()
                                        if result[4][4] == "yes" :
                                            Button(kyo_table_frame,image=staff_cal,border=0,bg="#62943B",command=staff_5).place(x=190,y=275)
                                        else :
                                            pass
                                    else :
                                        table_5 = Button(kyo_table_frame,image=teble_yellow_act,bg="#FFDDEB",font="Calibri 22 bold",border=0,activebackground="#FFDDEB",text="5",compound="center",fg="white",command=lambda:tableinfomation(5),state="disabled")
                                        table_5.place(x=140,y=270)
                                    # 6
                                    if result[5][1] == "default" :
                                        table_6 = Button(kyo_table_frame,image=teble_yellow_act,bg="#FFDDEB",font="Calibri 22 bold",border=0,activebackground="#FFDDEB",text="6",compound="center",fg="white",command=lambda:tableinfomation(6))
                                        table_6.place(x=230,y=270)
                                        def staff_6() :
                                            conn = sqlite3.connect("projectdb.db")
                                            cursor = conn.cursor()
                                            sql = """
                                                    UPDATE shop_kyo_table
                                                    SET staffcall=?
                                                    WHERE table_no=? """
                                            cursor.execute(sql,["no","5"])
                                            conn.commit()
                                        if result[5][4] == "yes" :
                                            Button(kyo_table_frame,image=staff_cal,border=0,bg="#62943B",command=staff_6).place(x=280,y=275)
                                        else :
                                            pass
                                    else :
                                        table_6 = Button(kyo_table_frame,image=teble_yellow_act,bg="#FFDDEB",font="Calibri 22 bold",border=0,activebackground="#FFDDEB",text="6",compound="center",fg="white",command=lambda:tableinfomation(6),state="disabled")
                                        table_6.place(x=230,y=270)
                                    # 7
                                    if result[6][1] == "default" :
                                        def staff_7() :
                                            conn = sqlite3.connect("projectdb.db")
                                            cursor = conn.cursor()
                                            sql = """
                                                    UPDATE shop_kyo_table
                                                    SET staffcall=?
                                                    WHERE table_no=? """
                                            cursor.execute(sql,["no","5"])
                                            conn.commit()
                                        table_7 = Button(kyo_table_frame,image=teble_red_act,bg="#FFDDEB",font="Calibri 22 bold",border=0,activebackground="#FFDDEB",text="7",compound="center",fg="white",command=lambda:tableinfomation(7))
                                        table_7.place(x=50,y=420)
                                        if result[6][4] == "yes" :
                                            Button(kyo_table_frame,image=staff_cal,border=0,bg="#62943B",command=staff_7).place(x=100,y=425)
                                        else :
                                            pass
                                    else :
                                        table_7 = Button(kyo_table_frame,image=teble_red_act,bg="#FFDDEB",font="Calibri 22 bold",border=0,activebackground="#FFDDEB",text="7",compound="center",fg="white",command=lambda:tableinfomation(7),state="disabled")
                                        table_7.place(x=50,y=420)
                                    # 8
                                    if result[7][1] == "default" :
                                        table_8 = Button(kyo_table_frame,image=teble_red_act,bg="#FFDDEB",font="Calibri 22 bold",border=0,activebackground="#FFDDEB",text="8",compound="center",fg="white",command=lambda:tableinfomation(8))
                                        table_8.place(x=140,y=420)
                                        def staff_8() :
                                            conn = sqlite3.connect("projectdb.db")
                                            cursor = conn.cursor()
                                            sql = """
                                                    UPDATE shop_kyo_table
                                                    SET staffcall=?
                                                    WHERE table_no=? """
                                            cursor.execute(sql,["no","5"])
                                            conn.commit()
                                        if result[7][4] == "yes" :
                                            Button(kyo_table_frame,image=staff_cal,border=0,bg="#62943B",command=staff_8).place(x=190,y=425)
                                        else :
                                            pass
                                    else :
                                        table_8 = Button(kyo_table_frame,image=teble_red_act,bg="#FFDDEB",font="Calibri 22 bold",border=0,activebackground="#FFDDEB",text="8",compound="center",fg="white",command=lambda:tableinfomation(8),state="disabled")
                                        table_8.place(x=140,y=420)
                                    conn.close()
                                # Start             
                                Label(kyo_admin_frame,image=kyo_header,bg="#FFFBEA").place(x=-2,y=-15)
                                Label(kyo_admin_frame,image=kyo_logo,bg="#FFFBEA").place(x=40,y=0)
                                tablebut = Button(kyo_admin_frame,image=button_yellow,border=0,activebackground="white",activeforeground="white",bg="white",text="Table",compound="center",font="Calibri 16",command=kyo_table)
                                tablebut.place(x=880,y=112)
                                queuebut = Button(kyo_admin_frame,image=button_yellow,border=0,activebackground="white",activeforeground="white",bg="white",text="Queue",compound="center",font="Calibri 16",command=kyo_queue)
                                queuebut.place(x=780,y=112)
                                showtext = Label(kyo_admin_frame,text="",font="Calibri 24 bold",bg="#B1A698")
                                showtext.place(x=250,y=30)
                                kyo_table()
                            # CODE
                            elif result[3] == "CODE" :
                                frame_adminlogin.destroy()
                                code_admin_frame = Frame(admin,bg="#FFFBEA")
                                code_admin_frame.place(x=0,y=0,w=w,h=h)
                                # frame
                                def code_queue() :
                                    global code_queue
                                    def queueinfomation(number) :
                                        def code_addtostore(namecus,numbergroup) :
                                            ans = messagebox.askquestion("Admin","Add customer to table %s"%(numbergroup))
                                            if ans == "yes" :
                                                if numbergroup == 1 or numbergroup == 2 or numbergroup == 3:
                                                    people = "1-2"
                                                elif numbergroup == 4 or numbergroup == 5 or numbergroup == 6:
                                                    people = "3-4"
                                                elif numbergroup == 7 or numbergroup == 8:
                                                    people = "3-4"
                                                #
                                                sql = """
                                                        UPDATE shop_code_table
                                                        SET name=?,amount=?,staffcall=?
                                                        WHERE table_no=? """
                                                cursor.execute(sql,[namecus,people,"no",numbergroup])
                                                conn.commit()
                                                #
                                                sql = """
                                                        UPDATE shop_code_table
                                                        SET status=?
                                                        WHERE table_no=? """
                                                cursor.execute(sql,["default",numbergroup])
                                                conn.commit()
                                                #
                                                sql = """
                                                        UPDATE shop_code_queue
                                                        SET q_status=?
                                                        WHERE q_name=?"""
                                                cursor.execute(sql,["ready",namecus])   
                                                conn.commit()     
                                                conn.close()
                                            else :
                                                pass
                                        Label(code_queue,image=queue_frame,bg="#FFE296").place(x=645,y=5)
                                        Label(code_queue,text="Table %s"%(number),font="Calibri 24 bold",bg='#FFE296').place(x=670,y=20)
                                        Label(code_queue,text="No.",font="Calibri 18",bg='#FFE296').place(x=660,y=70)
                                        Label(code_queue,text="Name",font="Calibri 18",bg='#FFE296').place(x=860,y=70)
                                        conn = sqlite3.connect("projectdb.db")
                                        cursor = conn.cursor()
                                        if number == 1 or number == 2 or number == 3:
                                            sql = """
                                                    SELECT * FROM shop_code_queue
                                                    WHERE q_amount=? and q_status=?"""
                                            cursor.execute(sql,["1-2","wait"])
                                            result = cursor.fetchall()
                                            
                                            yasix = 120
                                            for i,data in enumerate(result) :
                                                Label(code_queue,text=data[0],bg="#FFE296").place(x=660,y=yasix)
                                                Label(code_queue,text=data[1],bg="#FFE296").place(x=860,y=yasix)
                                                yasix = yasix +70
                                                code1_2 = Button(code_queue,text="bookatble",font="Calibri 18",bg='green',border=0,fg="white",command=lambda:code_addtostore(result[0][1],number))
                                                code1_2.place(x=660,y=470)
                                        elif number == 4 or number == 5 or number == 6:
                                            
                                            sql = """
                                                    SELECT * FROM shop_code_queue
                                                    WHERE q_amount=? and q_status=?"""
                                            cursor.execute(sql,["3-4","wait"])
                                            result = cursor.fetchall()
                                            
                                            yasix = 120
                                            for i,data in enumerate(result) :
                                                Label(code_queue,text=data[0],bg="#FFE296").place(x=660,y=yasix)
                                                Label(code_queue,text=data[1],bg="#FFE296").place(x=860,y=yasix)
                                                yasix = yasix +70
                                                code1_2 = Button(code_queue,text="bookatble",font="Calibri 18",bg='green',border=0,fg="white",command=lambda:code_addtostore(result[0][1],number))
                                                code1_2.place(x=660,y=470)
                                        elif number == 7 or number == 8:
                                            
                                            sql = """
                                                    SELECT * FROM shop_code_queue
                                                    WHERE q_amount=? and q_status=? """
                                            cursor.execute(sql,["5-6","wait"])
                                            result = cursor.fetchall()
                                            
                                            yasix = 120
                                            for i,data in enumerate(result) :
                                                Label(code_queue,text=data[0],bg="#FFE296").place(x=660,y=yasix)
                                                Label(code_queue,text=data[1],bg="#FFE296").place(x=860,y=yasix)
                                                yasix = yasix +70
                                                code1_2 = Button(code_queue,text="bookatble",font="Calibri 18",bg='green',border=0,fg="white",command=lambda:code_addtostore(result[0][1],number))
                                                code1_2.place(x=660,y=470)
                                    queuebut["state"] = "disabled"
                                    tablebut["state"] = "active"
                                    showtext["text"] = "Queue"
                                    code_table_frame.destroy()
                                    code_queue = Frame(code_admin_frame,bg="#FFFBEA")
                                    code_queue.place(x=0,y=160,w=w,h=h-140)
                                    Label(code_queue,image=admin_yayoi_frame_1,bg="#FFFBEA").place(x=25,y=5)
                                    Label(code_queue,image=queue_frame,bg="#FFFBEA").place(x=645,y=5)
                                    Label(code_queue,image=admin_yayoi_table,bg="#FFDDEB").place(x=40,y=25)
                                    Label(code_queue,text="1-2 People",bg="#FFDDEB",font="Calibri 18").place(x=40,y=65)
                                    Label(code_queue,text="3-4 People",bg="#FFDDEB",font="Calibri 18").place(x=40,y=215)
                                    Label(code_queue,text="5-6 People",bg="#FFDDEB",font="Calibri 18").place(x=40,y=365)
                                    # conn
                                    conn = sqlite3.connect("projectdb.db")
                                    cursor = conn.cursor()
                                    sql = """
                                            SELECT * FROM shop_code_table """
                                    cursor.execute(sql)
                                    result = cursor.fetchall()
                                    # 1
                                    if result[0][1] == "free" :
                                        table_1 = Button(code_queue,image=teble_green_act,bg="#FFDDEB",font="Calibri 22 bold",border=0,activebackground="#FFDDEB",text="1",compound="center",fg="white",command=lambda:queueinfomation(1))
                                        table_1.place(x=50,y=120)
                                    else :
                                        table_1 = Button(code_queue,image=teble_green_act,bg="#FFDDEB",font="Calibri 22 bold",border=0,activebackground="#FFDDEB",text="1",compound="center",fg="white",command=lambda:queueinfomation(1),state="disabled")
                                        table_1.place(x=50,y=120)
                                    # 2
                                    if result[1][1] == "free" :
                                        table_2 = Button(code_queue,image=teble_green_act,bg="#FFDDEB",font="Calibri 22 bold",border=0,activebackground="#FFDDEB",text="2",compound="center",fg="white",command=lambda:queueinfomation(2))
                                        table_2.place(x=140,y=120)
                                    else :
                                        table_2 = Button(code_queue,image=teble_green_act,bg="#FFDDEB",font="Calibri 22 bold",border=0,activebackground="#FFDDEB",text="2",compound="center",fg="white",command=lambda:queueinfomation(2),state="disabled")
                                        table_2.place(x=140,y=120)
                                    # 3
                                    if result[2][1] == "free" :
                                        table_3 = Button(code_queue,image=teble_green_act,bg="#FFDDEB",font="Calibri 22 bold",border=0,activebackground="#FFDDEB",text="3",compound="center",fg="white",command=lambda:queueinfomation(3))
                                        table_3.place(x=230,y=120)
                                    else :
                                        table_3 = Button(code_queue,image=teble_green_act,bg="#FFDDEB",font="Calibri 22 bold",border=0,activebackground="#FFDDEB",text="3",compound="center",fg="white",command=lambda:queueinfomation(3),state="disabled")
                                        table_3.place(x=230,y=120)
                                    # 4
                                    if result[3][1] == "free" :
                                        table_4 = Button(code_queue,image=teble_yellow_act,bg="#FFDDEB",font="Calibri 22 bold",border=0,activebackground="#FFDDEB",text="4",compound="center",fg="white",command=lambda:queueinfomation(4))
                                        table_4.place(x=50,y=270)
                                    else :
                                        table_4 = Button(code_queue,image=teble_yellow_act,bg="#FFDDEB",font="Calibri 22 bold",border=0,activebackground="#FFDDEB",text="4",compound="center",fg="white",command=lambda:queueinfomation(4),state="disabled")
                                        table_4.place(x=50,y=270)
                                    # 5
                                    if result[4][1] == "free" :
                                        table_5 = Button(code_queue,image=teble_yellow_act,bg="#FFDDEB",font="Calibri 22 bold",border=0,activebackground="#FFDDEB",text="5",compound="center",fg="white",command=lambda:queueinfomation(5))
                                        table_5.place(x=140,y=270)
                                    else :
                                        table_5 = Button(code_queue,image=teble_yellow_act,bg="#FFDDEB",font="Calibri 22 bold",border=0,activebackground="#FFDDEB",text="5",compound="center",fg="white",command=lambda:queueinfomation(5),state="disabled")
                                        table_5.place(x=140,y=270)
                                    # 6
                                    if result[5][1] == "free" :
                                        table_6 = Button(code_queue,image=teble_yellow_act,bg="#FFDDEB",font="Calibri 22 bold",border=0,activebackground="#FFDDEB",text="6",compound="center",fg="white",command=lambda:queueinfomation(6))
                                        table_6.place(x=230,y=270)
                                    else :
                                        table_6 = Button(code_queue,image=teble_yellow_act,bg="#FFDDEB",font="Calibri 22 bold",border=0,activebackground="#FFDDEB",text="6",compound="center",fg="white",command=lambda:queueinfomation(6),state="disabled")
                                        table_6.place(x=230,y=270)
                                    # 7
                                    if result[6][1] == "free" :
                                        table_7 = Button(code_queue,image=teble_red_act,bg="#FFDDEB",font="Calibri 22 bold",border=0,activebackground="#FFDDEB",text="7",compound="center",fg="white",command=lambda:queueinfomation(7))
                                        table_7.place(x=50,y=420)
                                    else :
                                        table_7 = Button(code_queue,image=teble_red_act,bg="#FFDDEB",font="Calibri 22 bold",border=0,activebackground="#FFDDEB",text="7",compound="center",fg="white",command=lambda:queueinfomation(7),state="disabled")
                                        table_7.place(x=50,y=420)
                                    # 8
                                    if result[7][1] == "free" :
                                        table_8 = Button(code_queue,image=teble_red_act,bg="#FFDDEB",font="Calibri 22 bold",border=0,activebackground="#FFDDEB",text="8",compound="center",fg="white",command=lambda:queueinfomation(8))
                                        table_8.place(x=140,y=420)
                                    else :
                                        table_8 = Button(code_queue,image=teble_red_act,bg="#FFDDEB",font="Calibri 22 bold",border=0,activebackground="#FFDDEB",text="8",compound="center",fg="white",command=lambda:queueinfomation(8),state="disabled")
                                        table_8.place(x=140,y=420)
                                    conn.close()
                                def code_table() :
                                    global code_table_frame
                                    # def
                                    def tableinfomation(no):
                                        def code_confirmorder() :
                                            ans = messagebox.askquestion("Admin","Confirm order") 
                                            if ans == "yes" :
                                                if result :
                                                    for i,data in enumerate(result) :
                                                        sql = """
                                                                    UPDATE shop_code_orderprocess
                                                                    SET status=? WHERE menu_name =? """
                                                        cursor.execute(sql,["F",data[1]])
                                                        conn.commit()
                                                else :
                                                    codecon["state"] = "disabled"
                                                    codecon["fg"] = "white"
                                                conn.close()
                                            else :
                                                pass
                                        Label(code_table_frame,image=admin_yayoi_frame_2,bg="#FFFFFF").place(x=645,y=5)
                                        Label(code_table_frame,text="Table %s"%(no),font="Calibri 24 bold",bg='#DFDCED').place(x=670,y=20)
                                        Label(code_table_frame,text="Menu",font="Calibri 18",bg='#DFDCED').place(x=660,y=70)
                                        Label(code_table_frame,text="Amount",font="Calibri 18",bg='#DFDCED').place(x=860,y=70)
                                        conn = sqlite3.connect("projectdb.db")
                                        cursor = conn.cursor()
                                        sql = """
                                                SELECT * FROM shop_code_orderprocess 
                                                WHERE table_index=? and status=?"""
                                        cursor.execute(sql,[no,"NF"])
                                        result = cursor.fetchall()
                                        indexy = 120
                                        for i,data in enumerate(result) :
                                            if i<6 :
                                                Label(code_table_frame,text=data[1][0:17],font="Calibri 18",bg='#DFDCED').place(x=660,y=indexy)
                                                Label(code_table_frame,text=data[3][0:17],font="Calibri 18",bg='#DFDCED').place(x=890,y=indexy)
                                            else :
                                                pass
                                            indexy = indexy + 50
                                        codecon = Button(code_table_frame,text="Confirm Order",font="Calibri 18",bg='green',border=0,fg="white",command=code_confirmorder)
                                        codecon.place(x=660,y=460)
                                    #
                                    tablebut["state"] = "disabled"
                                    queuebut["state"] = "active"
                                    showtext["text"] = "Table info"
                                    code_table_frame = Frame(code_admin_frame,bg="#FFFBEA")
                                    code_table_frame.place(x=0,y=160,w=w,h=h-140)
                                    Label(code_table_frame,image=admin_yayoi_frame_1,bg="#FFFBEA").place(x=25,y=5)
                                    Label(code_table_frame,image=admin_yayoi_frame_2,bg="#FFFBEA").place(x=645,y=5)
                                    Label(code_table_frame,image=admin_yayoi_table,bg="#FFDDEB").place(x=40,y=25)
                                    Label(code_table_frame,text="1-2 People",bg="#FFDDEB",font="Calibri 18").place(x=40,y=65)
                                    Label(code_table_frame,text="3-4 People",bg="#FFDDEB",font="Calibri 18").place(x=40,y=215)
                                    Label(code_table_frame,text="5-6 People",bg="#FFDDEB",font="Calibri 18").place(x=40,y=365)
                                    # conn
                                    conn = sqlite3.connect("projectdb.db")
                                    cursor = conn.cursor()
                                    sql = """
                                            SELECT * FROM shop_code_table """
                                    cursor.execute(sql)
                                    result = cursor.fetchall()
                                    conn.close()
                                    # 1
                                    if result[0][1] == "default" :
                                        table_1 = Button(code_table_frame,image=teble_green_act,bg="#FFDDEB",font="Calibri 22 bold",border=0,activebackground="#FFDDEB",text="1",compound="center",fg="white",command=lambda:tableinfomation(1))
                                        table_1.place(x=50,y=120)
                                        def staff_1() :
                                            conn = sqlite3.connect("projectdb.db")
                                            cursor = conn.cursor()
                                            sql = """
                                                    UPDATE shop_code_table
                                                    SET staffcall=?
                                                    WHERE table_no=? """
                                            cursor.execute(sql,["no","1"])
                                            conn.commit()
                                        if result[0][4] == "yes" :
                                            Button(code_table_frame,image=staff_cal,border=0,bg="#62943B",command=staff_1).place(x=100,y=125)
                                        else :
                                            pass
                                    else :
                                        table_1 = Button(code_table_frame,image=teble_green_act,bg="#FFDDEB",font="Calibri 22 bold",border=0,activebackground="#FFDDEB",text="1",compound="center",fg="white",command=lambda:tableinfomation(1),state="disabled")
                                        table_1.place(x=50,y=120)
                                    # 2
                                    if result[1][1] == "default" :
                                        table_2 = Button(code_table_frame,image=teble_green_act,bg="#FFDDEB",font="Calibri 22 bold",border=0,activebackground="#FFDDEB",text="2",compound="center",fg="white",command=lambda:tableinfomation(2))
                                        table_2.place(x=140,y=120)
                                        def staff_2() :
                                            conn = sqlite3.connect("projectdb.db")
                                            cursor = conn.cursor()
                                            sql = """
                                                    UPDATE shop_code_table
                                                    SET staffcall=?
                                                    WHERE table_no=? """
                                            cursor.execute(sql,["no","2"])
                                            conn.commit()
                                        if result[1][4] == "yes" :
                                            Button(code_table_frame,image=staff_cal,border=0,bg="#62943B",command=staff_2).place(x=190,y=125)
                                        else :
                                            pass
                                    else :
                                        table_2 = Button(code_table_frame,image=teble_green_act,bg="#FFDDEB",font="Calibri 22 bold",border=0,activebackground="#FFDDEB",text="2",compound="center",fg="white",command=lambda:tableinfomation(2),state="disabled")
                                        table_2.place(x=140,y=120)
                                    # 3
                                    if result[2][1] == "default" :
                                        table_3 = Button(code_table_frame,image=teble_green_act,bg="#FFDDEB",font="Calibri 22 bold",border=0,activebackground="#FFDDEB",text="3",compound="center",fg="white",command=lambda:tableinfomation(3))
                                        table_3.place(x=230,y=120)
                                        def staff_3() :
                                            conn = sqlite3.connect("projectdb.db")
                                            cursor = conn.cursor()
                                            sql = """
                                                    UPDATE shop_code_table
                                                    SET staffcall=?
                                                    WHERE table_no=? """
                                            cursor.execute(sql,["no","3"])
                                            conn.commit()
                                        if result[2][4] == "yes" :
                                            Button(code_table_frame,image=staff_cal,border=0,bg="#62943B",command=staff_3).place(x=280,y=125)
                                        else :
                                            pass
                                    else :
                                        table_3 = Button(code_table_frame,image=teble_green_act,bg="#FFDDEB",font="Calibri 22 bold",border=0,activebackground="#FFDDEB",text="3",compound="center",fg="white",command=lambda:tableinfomation(3),state="disabled")
                                        table_3.place(x=230,y=120)
                                    # 4
                                    if result[3][1] == "default" :
                                        table_4 = Button(code_table_frame,image=teble_yellow_act,bg="#FFDDEB",font="Calibri 22 bold",border=0,activebackground="#FFDDEB",text="4",compound="center",fg="white",command=lambda:tableinfomation(4))
                                        table_4.place(x=50,y=270)
                                        def staff_4() :
                                            conn = sqlite3.connect("projectdb.db")
                                            cursor = conn.cursor()
                                            sql = """
                                                    UPDATE shop_code_table
                                                    SET staffcall=?
                                                    WHERE table_no=? """
                                            cursor.execute(sql,["no","4"])
                                            conn.commit()
                                        if result[3][4] == "yes" :
                                            Button(code_table_frame,image=staff_cal,border=0,bg="#62943B",command=staff_4).place(x=100,y=275)
                                        else :
                                            pass
                                    else :
                                        table_4 = Button(code_table_frame,image=teble_yellow_act,bg="#FFDDEB",font="Calibri 22 bold",border=0,activebackground="#FFDDEB",text="4",compound="center",fg="white",command=lambda:tableinfomation(4),state="disabled")
                                        table_4.place(x=50,y=270)
                                    # 5
                                    if result[4][1] == "default" :
                                        table_5 = Button(code_table_frame,image=teble_yellow_act,bg="#FFDDEB",font="Calibri 22 bold",border=0,activebackground="#FFDDEB",text="5",compound="center",fg="white",command=lambda:tableinfomation(5))
                                        table_5.place(x=140,y=270)
                                        def staff_5() :
                                            conn = sqlite3.connect("projectdb.db")
                                            cursor = conn.cursor()
                                            sql = """
                                                    UPDATE shop_code_table
                                                    SET staffcall=?
                                                    WHERE table_no=? """
                                            cursor.execute(sql,["no","5"])
                                            conn.commit()
                                        if result[4][4] == "yes" :
                                            Button(code_table_frame,image=staff_cal,border=0,bg="#62943B",command=staff_5).place(x=190,y=275)
                                        else :
                                            pass
                                    else :
                                        table_5 = Button(code_table_frame,image=teble_yellow_act,bg="#FFDDEB",font="Calibri 22 bold",border=0,activebackground="#FFDDEB",text="5",compound="center",fg="white",command=lambda:tableinfomation(5),state="disabled")
                                        table_5.place(x=140,y=270)
                                    # 6
                                    if result[5][1] == "default" :
                                        table_6 = Button(code_table_frame,image=teble_yellow_act,bg="#FFDDEB",font="Calibri 22 bold",border=0,activebackground="#FFDDEB",text="6",compound="center",fg="white",command=lambda:tableinfomation(6))
                                        table_6.place(x=230,y=270)
                                        def staff_6() :
                                            conn = sqlite3.connect("projectdb.db")
                                            cursor = conn.cursor()
                                            sql = """
                                                    UPDATE shop_code_table
                                                    SET staffcall=?
                                                    WHERE table_no=? """
                                            cursor.execute(sql,["no","5"])
                                            conn.commit()
                                        if result[5][4] == "yes" :
                                            Button(code_table_frame,image=staff_cal,border=0,bg="#62943B",command=staff_6).place(x=280,y=275)
                                        else :
                                            pass
                                    else :
                                        table_6 = Button(code_table_frame,image=teble_yellow_act,bg="#FFDDEB",font="Calibri 22 bold",border=0,activebackground="#FFDDEB",text="6",compound="center",fg="white",command=lambda:tableinfomation(6),state="disabled")
                                        table_6.place(x=230,y=270)
                                    # 7
                                    if result[6][1] == "default" :
                                        def staff_7() :
                                            conn = sqlite3.connect("projectdb.db")
                                            cursor = conn.cursor()
                                            sql = """
                                                    UPDATE shop_code_table
                                                    SET staffcall=?
                                                    WHERE table_no=? """
                                            cursor.execute(sql,["no","5"])
                                            conn.commit()
                                        table_7 = Button(code_table_frame,image=teble_red_act,bg="#FFDDEB",font="Calibri 22 bold",border=0,activebackground="#FFDDEB",text="7",compound="center",fg="white",command=lambda:tableinfomation(7))
                                        table_7.place(x=50,y=420)
                                        if result[6][4] == "yes" :
                                            Button(code_table_frame,image=staff_cal,border=0,bg="#62943B",command=staff_7).place(x=100,y=425)
                                        else :
                                            pass
                                    else :
                                        table_7 = Button(code_table_frame,image=teble_red_act,bg="#FFDDEB",font="Calibri 22 bold",border=0,activebackground="#FFDDEB",text="7",compound="center",fg="white",command=lambda:tableinfomation(7),state="disabled")
                                        table_7.place(x=50,y=420)
                                    # 8
                                    if result[7][1] == "default" :
                                        table_8 = Button(code_table_frame,image=teble_red_act,bg="#FFDDEB",font="Calibri 22 bold",border=0,activebackground="#FFDDEB",text="8",compound="center",fg="white",command=lambda:tableinfomation(8))
                                        table_8.place(x=140,y=420)
                                        def staff_8() :
                                            conn = sqlite3.connect("projectdb.db")
                                            cursor = conn.cursor()
                                            sql = """
                                                    UPDATE shop_code_table
                                                    SET staffcall=?
                                                    WHERE table_no=? """
                                            cursor.execute(sql,["no","5"])
                                            conn.commit()
                                        if result[7][4] == "yes" :
                                            Button(code_table_frame,image=staff_cal,border=0,bg="#62943B",command=staff_8).place(x=190,y=425)
                                        else :
                                            pass
                                    else :
                                        table_8 = Button(code_table_frame,image=teble_red_act,bg="#FFDDEB",font="Calibri 22 bold",border=0,activebackground="#FFDDEB",text="8",compound="center",fg="white",command=lambda:tableinfomation(8),state="disabled")
                                        table_8.place(x=140,y=420)
                                    conn.close()
                                # Start             
                                Label(code_admin_frame,image=code_header,bg="#FFFBEA").place(x=-2,y=-15)
                                Label(code_admin_frame,image=code_logo,bg="#FFFBEA").place(x=40,y=0)
                                tablebut = Button(code_admin_frame,image=button_yellow,border=0,activebackground="white",activeforeground="white",bg="white",text="Table",compound="center",font="Calibri 16",command=code_table)
                                tablebut.place(x=880,y=112)
                                queuebut = Button(code_admin_frame,image=button_yellow,border=0,activebackground="white",activeforeground="white",bg="white",text="Queue",compound="center",font="Calibri 16",command=code_queue)
                                queuebut.place(x=780,y=112)
                                showtext = Label(code_admin_frame,text="",font="Calibri 24 bold",bg="#F8B4B9")
                                showtext.place(x=250,y=30)
                                code_table()
                            # SHIN
                            elif result[3] == "SHIN" :
                                frame_adminlogin.destroy()
                                shin_admin_frame = Frame(admin,bg="#FFFBEA")
                                shin_admin_frame.place(x=0,y=0,w=w,h=h)
                                # frame
                                def shin_queue() :
                                    global shin_queue
                                    def queueinfomation(number) :
                                        def shin_addtostore(namecus,numbergroup) :
                                            ans = messagebox.askquestion("Admin","Add customer to table %s"%(numbergroup))
                                            if ans == "yes" :
                                                if numbergroup == 1 or numbergroup == 2 or numbergroup == 3:
                                                    people = "1-2"
                                                elif numbergroup == 4 or numbergroup == 5 or numbergroup == 6:
                                                    people = "3-4"
                                                elif numbergroup == 7 or numbergroup == 8:
                                                    people = "3-4"
                                                #
                                                sql = """
                                                        UPDATE shop_shin_table
                                                        SET name=?,amount=?,staffcall=?
                                                        WHERE table_no=? """
                                                cursor.execute(sql,[namecus,people,"no",numbergroup])
                                                conn.commit()
                                                #
                                                sql = """
                                                        UPDATE shop_shin_table
                                                        SET status=?
                                                        WHERE table_no=? """
                                                cursor.execute(sql,["default",numbergroup])
                                                conn.commit()
                                                #
                                                sql = """
                                                        UPDATE shop_shin_queue
                                                        SET q_status=?
                                                        WHERE q_name=?"""
                                                cursor.execute(sql,["ready",namecus])   
                                                conn.commit()     
                                                conn.close()
                                            else :
                                                pass
                                        Label(shin_queue,image=queue_frame,bg="#FFE296").place(x=645,y=5)
                                        Label(shin_queue,text="Table %s"%(number),font="Calibri 24 bold",bg='#FFE296').place(x=670,y=20)
                                        Label(shin_queue,text="No.",font="Calibri 18",bg='#FFE296').place(x=660,y=70)
                                        Label(shin_queue,text="Name",font="Calibri 18",bg='#FFE296').place(x=860,y=70)
                                        conn = sqlite3.connect("projectdb.db")
                                        cursor = conn.cursor()
                                        if number == 1 or number == 2 or number == 3:
                                            sql = """
                                                    SELECT * FROM shop_shin_queue
                                                    WHERE q_amount=? and q_status=?"""
                                            cursor.execute(sql,["1-2","wait"])
                                            result = cursor.fetchall()
                                            
                                            yasix = 120
                                            for i,data in enumerate(result) :
                                                Label(shin_queue,text=data[0],bg="#FFE296").place(x=660,y=yasix)
                                                Label(shin_queue,text=data[1],bg="#FFE296").place(x=860,y=yasix)
                                                yasix = yasix +70
                                                shin1_2 = Button(shin_queue,text="bookatble",font="Calibri 18",bg='green',border=0,fg="white",command=lambda:shin_addtostore(result[0][1],number))
                                                shin1_2.place(x=660,y=470)
                                        elif number == 4 or number == 5 or number == 6:
                                            
                                            sql = """
                                                    SELECT * FROM shop_shin_queue
                                                    WHERE q_amount=? and q_status=?"""
                                            cursor.execute(sql,["3-4","wait"])
                                            result = cursor.fetchall()
                                            
                                            yasix = 120
                                            for i,data in enumerate(result) :
                                                Label(shin_queue,text=data[0],bg="#FFE296").place(x=660,y=yasix)
                                                Label(shin_queue,text=data[1],bg="#FFE296").place(x=860,y=yasix)
                                                yasix = yasix +70
                                                shin1_2 = Button(shin_queue,text="bookatble",font="Calibri 18",bg='green',border=0,fg="white",command=lambda:shin_addtostore(result[0][1],number))
                                                shin1_2.place(x=660,y=470)
                                        elif number == 7 or number == 8:
                                            
                                            sql = """
                                                    SELECT * FROM shop_shin_queue
                                                    WHERE q_amount=? and q_status=? """
                                            cursor.execute(sql,["5-6","wait"])
                                            result = cursor.fetchall()
                                            
                                            yasix = 120
                                            for i,data in enumerate(result) :
                                                Label(shin_queue,text=data[0],bg="#FFE296").place(x=660,y=yasix)
                                                Label(shin_queue,text=data[1],bg="#FFE296").place(x=860,y=yasix)
                                                yasix = yasix +70
                                                shin1_2 = Button(shin_queue,text="bookatble",font="Calibri 18",bg='green',border=0,fg="white",command=lambda:shin_addtostore(result[0][1],number))
                                                shin1_2.place(x=660,y=470)
                                    queuebut["state"] = "disabled"
                                    tablebut["state"] = "active"
                                    showtext["text"] = "Queue"
                                    shin_table_frame.destroy()
                                    shin_queue = Frame(shin_admin_frame,bg="#FFFBEA")
                                    shin_queue.place(x=0,y=160,w=w,h=h-140)
                                    Label(shin_queue,image=admin_yayoi_frame_1,bg="#FFFFFF").place(x=25,y=5)
                                    Label(shin_queue,image=queue_frame,bg="#FFFFFF").place(x=645,y=5)
                                    Label(shin_queue,image=admin_yayoi_table,bg="#FFDDEB").place(x=40,y=25)
                                    Label(shin_queue,text="1-2 People",bg="#FFDDEB",font="Calibri 18").place(x=40,y=65)
                                    Label(shin_queue,text="3-4 People",bg="#FFDDEB",font="Calibri 18").place(x=40,y=215)
                                    Label(shin_queue,text="5-6 People",bg="#FFDDEB",font="Calibri 18").place(x=40,y=365)
                                    # conn
                                    conn = sqlite3.connect("projectdb.db")
                                    cursor = conn.cursor()
                                    sql = """
                                            SELECT * FROM shop_shin_table """
                                    cursor.execute(sql)
                                    result = cursor.fetchall()
                                    # 1
                                    if result[0][1] == "free" :
                                        table_1 = Button(shin_queue,image=teble_green_act,bg="#FFDDEB",font="Calibri 22 bold",border=0,activebackground="#FFDDEB",text="1",compound="center",fg="white",command=lambda:queueinfomation(1))
                                        table_1.place(x=50,y=120)
                                    else :
                                        table_1 = Button(shin_queue,image=teble_green_act,bg="#FFDDEB",font="Calibri 22 bold",border=0,activebackground="#FFDDEB",text="1",compound="center",fg="white",command=lambda:queueinfomation(1),state="disabled")
                                        table_1.place(x=50,y=120)
                                    # 2
                                    if result[1][1] == "free" :
                                        table_2 = Button(shin_queue,image=teble_green_act,bg="#FFDDEB",font="Calibri 22 bold",border=0,activebackground="#FFDDEB",text="2",compound="center",fg="white",command=lambda:queueinfomation(2))
                                        table_2.place(x=140,y=120)
                                    else :
                                        table_2 = Button(shin_queue,image=teble_green_act,bg="#FFDDEB",font="Calibri 22 bold",border=0,activebackground="#FFDDEB",text="2",compound="center",fg="white",command=lambda:queueinfomation(2),state="disabled")
                                        table_2.place(x=140,y=120)
                                    # 3
                                    if result[2][1] == "free" :
                                        table_3 = Button(shin_queue,image=teble_green_act,bg="#FFDDEB",font="Calibri 22 bold",border=0,activebackground="#FFDDEB",text="3",compound="center",fg="white",command=lambda:queueinfomation(3))
                                        table_3.place(x=230,y=120)
                                    else :
                                        table_3 = Button(shin_queue,image=teble_green_act,bg="#FFDDEB",font="Calibri 22 bold",border=0,activebackground="#FFDDEB",text="3",compound="center",fg="white",command=lambda:queueinfomation(3),state="disabled")
                                        table_3.place(x=230,y=120)
                                    # 4
                                    if result[3][1] == "free" :
                                        table_4 = Button(shin_queue,image=teble_yellow_act,bg="#FFDDEB",font="Calibri 22 bold",border=0,activebackground="#FFDDEB",text="4",compound="center",fg="white",command=lambda:queueinfomation(4))
                                        table_4.place(x=50,y=270)
                                    else :
                                        table_4 = Button(shin_queue,image=teble_yellow_act,bg="#FFDDEB",font="Calibri 22 bold",border=0,activebackground="#FFDDEB",text="4",compound="center",fg="white",command=lambda:queueinfomation(4),state="disabled")
                                        table_4.place(x=50,y=270)
                                    # 5
                                    if result[4][1] == "free" :
                                        table_5 = Button(shin_queue,image=teble_yellow_act,bg="#FFDDEB",font="Calibri 22 bold",border=0,activebackground="#FFDDEB",text="5",compound="center",fg="white",command=lambda:queueinfomation(5))
                                        table_5.place(x=140,y=270)
                                    else :
                                        table_5 = Button(shin_queue,image=teble_yellow_act,bg="#FFDDEB",font="Calibri 22 bold",border=0,activebackground="#FFDDEB",text="5",compound="center",fg="white",command=lambda:queueinfomation(5),state="disabled")
                                        table_5.place(x=140,y=270)
                                    # 6
                                    if result[5][1] == "free" :
                                        table_6 = Button(shin_queue,image=teble_yellow_act,bg="#FFDDEB",font="Calibri 22 bold",border=0,activebackground="#FFDDEB",text="6",compound="center",fg="white",command=lambda:queueinfomation(6))
                                        table_6.place(x=230,y=270)
                                    else :
                                        table_6 = Button(shin_queue,image=teble_yellow_act,bg="#FFDDEB",font="Calibri 22 bold",border=0,activebackground="#FFDDEB",text="6",compound="center",fg="white",command=lambda:queueinfomation(6),state="disabled")
                                        table_6.place(x=230,y=270)
                                    # 7
                                    if result[6][1] == "free" :
                                        table_7 = Button(shin_queue,image=teble_red_act,bg="#FFDDEB",font="Calibri 22 bold",border=0,activebackground="#FFDDEB",text="7",compound="center",fg="white",command=lambda:queueinfomation(7))
                                        table_7.place(x=50,y=420)
                                    else :
                                        table_7 = Button(shin_queue,image=teble_red_act,bg="#FFDDEB",font="Calibri 22 bold",border=0,activebackground="#FFDDEB",text="7",compound="center",fg="white",command=lambda:queueinfomation(7),state="disabled")
                                        table_7.place(x=50,y=420)
                                    # 8
                                    if result[7][1] == "free" :
                                        table_8 = Button(shin_queue,image=teble_red_act,bg="#FFDDEB",font="Calibri 22 bold",border=0,activebackground="#FFDDEB",text="8",compound="center",fg="white",command=lambda:queueinfomation(8))
                                        table_8.place(x=140,y=420)
                                    else :
                                        table_8 = Button(shin_queue,image=teble_red_act,bg="#FFDDEB",font="Calibri 22 bold",border=0,activebackground="#FFDDEB",text="8",compound="center",fg="white",command=lambda:queueinfomation(8),state="disabled")
                                        table_8.place(x=140,y=420)
                                    conn.close()
                                def shin_table() :
                                    global shin_table_frame
                                    # def
                                    def tableinfomation(no):
                                        def shin_confirmorder() :
                                            ans = messagebox.askquestion("Admin","Confirm order") 
                                            if ans == "yes" :
                                                if result :
                                                    for i,data in enumerate(result) :
                                                        sql = """
                                                                    UPDATE shop_shin_orderprocess
                                                                    SET status=? WHERE menu_name =? """
                                                        cursor.execute(sql,["F",data[1]])
                                                        conn.commit()
                                                else :
                                                    shincon["state"] = "disabled"
                                                    shincon["fg"] = "white"
                                                conn.close()
                                            else :
                                                pass
                                        Label(shin_table_frame,image=admin_yayoi_frame_2,bg="#FFFFFF").place(x=645,y=5)
                                        Label(shin_table_frame,text="Table %s"%(no),font="Calibri 24 bold",bg='#DFDCED').place(x=670,y=20)
                                        Label(shin_table_frame,text="Menu",font="Calibri 18",bg='#DFDCED').place(x=660,y=70)
                                        Label(shin_table_frame,text="Amount",font="Calibri 18",bg='#DFDCED').place(x=860,y=70)
                                        conn = sqlite3.connect("projectdb.db")
                                        cursor = conn.cursor()
                                        sql = """
                                                SELECT * FROM shop_shin_orderprocess 
                                                WHERE table_index=? and status=?"""
                                        cursor.execute(sql,[no,"NF"])
                                        result = cursor.fetchall()
                                        indexy = 120
                                        for i,data in enumerate(result) :
                                            if i<6 :
                                                Label(shin_table_frame,text=data[1][0:17],font="Calibri 18",bg='#DFDCED').place(x=660,y=indexy)
                                                Label(shin_table_frame,text=data[3][0:17],font="Calibri 18",bg='#DFDCED').place(x=890,y=indexy)
                                            else :
                                                pass
                                            indexy = indexy + 50
                                        shincon = Button(shin_table_frame,text="Confirm Order",font="Calibri 18",bg='green',border=0,fg="white",command=shin_confirmorder)
                                        shincon.place(x=660,y=460)
                                    #
                                    tablebut["state"] = "disabled"
                                    queuebut["state"] = "active"
                                    showtext["text"] = "Table info"
                                    shin_table_frame = Frame(shin_admin_frame,bg="#FFFBEA")
                                    shin_table_frame.place(x=0,y=160,w=w,h=h-140)
                                    Label(shin_table_frame,image=admin_yayoi_frame_1,bg="#FFFFFF").place(x=25,y=5)
                                    Label(shin_table_frame,image=admin_yayoi_frame_2,bg="#FFFFFF").place(x=645,y=5)
                                    Label(shin_table_frame,image=admin_yayoi_table,bg="#FFDDEB").place(x=40,y=25)
                                    Label(shin_table_frame,text="1-2 People",bg="#FFDDEB",font="Calibri 18").place(x=40,y=65)
                                    Label(shin_table_frame,text="3-4 People",bg="#FFDDEB",font="Calibri 18").place(x=40,y=215)
                                    Label(shin_table_frame,text="5-6 People",bg="#FFDDEB",font="Calibri 18").place(x=40,y=365)
                                    # conn
                                    conn = sqlite3.connect("projectdb.db")
                                    cursor = conn.cursor()
                                    sql = """
                                            SELECT * FROM shop_shin_table """
                                    cursor.execute(sql)
                                    result = cursor.fetchall()
                                    conn.close()
                                    # 1
                                    if result[0][1] == "default" :
                                        table_1 = Button(shin_table_frame,image=teble_green_act,bg="#FFDDEB",font="Calibri 22 bold",border=0,activebackground="#FFDDEB",text="1",compound="center",fg="white",command=lambda:tableinfomation(1))
                                        table_1.place(x=50,y=120)
                                        def staff_1() :
                                            conn = sqlite3.connect("projectdb.db")
                                            cursor = conn.cursor()
                                            sql = """
                                                    UPDATE shop_shin_table
                                                    SET staffcall=?
                                                    WHERE table_no=? """
                                            cursor.execute(sql,["no","1"])
                                            conn.commit()
                                        if result[0][4] == "yes" :
                                            Button(shin_table_frame,image=staff_cal,border=0,bg="#62943B",command=staff_1).place(x=100,y=125)
                                        else :
                                            pass
                                    else :
                                        table_1 = Button(shin_table_frame,image=teble_green_act,bg="#FFDDEB",font="Calibri 22 bold",border=0,activebackground="#FFDDEB",text="1",compound="center",fg="white",command=lambda:tableinfomation(1),state="disabled")
                                        table_1.place(x=50,y=120)
                                    # 2
                                    if result[1][1] == "default" :
                                        table_2 = Button(shin_table_frame,image=teble_green_act,bg="#FFDDEB",font="Calibri 22 bold",border=0,activebackground="#FFDDEB",text="2",compound="center",fg="white",command=lambda:tableinfomation(2))
                                        table_2.place(x=140,y=120)
                                        def staff_2() :
                                            conn = sqlite3.connect("projectdb.db")
                                            cursor = conn.cursor()
                                            sql = """
                                                    UPDATE shop_shin_table
                                                    SET staffcall=?
                                                    WHERE table_no=? """
                                            cursor.execute(sql,["no","2"])
                                            conn.commit()
                                        if result[1][4] == "yes" :
                                            Button(shin_table_frame,image=staff_cal,border=0,bg="#62943B",command=staff_2).place(x=190,y=125)
                                        else :
                                            pass
                                    else :
                                        table_2 = Button(shin_table_frame,image=teble_green_act,bg="#FFDDEB",font="Calibri 22 bold",border=0,activebackground="#FFDDEB",text="2",compound="center",fg="white",command=lambda:tableinfomation(2),state="disabled")
                                        table_2.place(x=140,y=120)
                                    # 3
                                    if result[2][1] == "default" :
                                        table_3 = Button(shin_table_frame,image=teble_green_act,bg="#FFDDEB",font="Calibri 22 bold",border=0,activebackground="#FFDDEB",text="3",compound="center",fg="white",command=lambda:tableinfomation(3))
                                        table_3.place(x=230,y=120)
                                        def staff_3() :
                                            conn = sqlite3.connect("projectdb.db")
                                            cursor = conn.cursor()
                                            sql = """
                                                    UPDATE shop_shin_table
                                                    SET staffcall=?
                                                    WHERE table_no=? """
                                            cursor.execute(sql,["no","3"])
                                            conn.commit()
                                        if result[2][4] == "yes" :
                                            Button(shin_table_frame,image=staff_cal,border=0,bg="#62943B",command=staff_3).place(x=280,y=125)
                                        else :
                                            pass
                                    else :
                                        table_3 = Button(shin_table_frame,image=teble_green_act,bg="#FFDDEB",font="Calibri 22 bold",border=0,activebackground="#FFDDEB",text="3",compound="center",fg="white",command=lambda:tableinfomation(3),state="disabled")
                                        table_3.place(x=230,y=120)
                                    # 4
                                    if result[3][1] == "default" :
                                        table_4 = Button(shin_table_frame,image=teble_yellow_act,bg="#FFDDEB",font="Calibri 22 bold",border=0,activebackground="#FFDDEB",text="4",compound="center",fg="white",command=lambda:tableinfomation(4))
                                        table_4.place(x=50,y=270)
                                        def staff_4() :
                                            conn = sqlite3.connect("projectdb.db")
                                            cursor = conn.cursor()
                                            sql = """
                                                    UPDATE shop_shin_table
                                                    SET staffcall=?
                                                    WHERE table_no=? """
                                            cursor.execute(sql,["no","4"])
                                            conn.commit()
                                        if result[3][4] == "yes" :
                                            Button(shin_table_frame,image=staff_cal,border=0,bg="#62943B",command=staff_4).place(x=100,y=275)
                                        else :
                                            pass
                                    else :
                                        table_4 = Button(shin_table_frame,image=teble_yellow_act,bg="#FFDDEB",font="Calibri 22 bold",border=0,activebackground="#FFDDEB",text="4",compound="center",fg="white",command=lambda:tableinfomation(4),state="disabled")
                                        table_4.place(x=50,y=270)
                                    # 5
                                    if result[4][1] == "default" :
                                        table_5 = Button(shin_table_frame,image=teble_yellow_act,bg="#FFDDEB",font="Calibri 22 bold",border=0,activebackground="#FFDDEB",text="5",compound="center",fg="white",command=lambda:tableinfomation(5))
                                        table_5.place(x=140,y=270)
                                        def staff_5() :
                                            conn = sqlite3.connect("projectdb.db")
                                            cursor = conn.cursor()
                                            sql = """
                                                    UPDATE shop_shin_table
                                                    SET staffcall=?
                                                    WHERE table_no=? """
                                            cursor.execute(sql,["no","5"])
                                            conn.commit()
                                        if result[4][4] == "yes" :
                                            Button(shin_table_frame,image=staff_cal,border=0,bg="#62943B",command=staff_5).place(x=190,y=275)
                                        else :
                                            pass
                                    else :
                                        table_5 = Button(shin_table_frame,image=teble_yellow_act,bg="#FFDDEB",font="Calibri 22 bold",border=0,activebackground="#FFDDEB",text="5",compound="center",fg="white",command=lambda:tableinfomation(5),state="disabled")
                                        table_5.place(x=140,y=270)
                                    # 6
                                    if result[5][1] == "default" :
                                        table_6 = Button(shin_table_frame,image=teble_yellow_act,bg="#FFDDEB",font="Calibri 22 bold",border=0,activebackground="#FFDDEB",text="6",compound="center",fg="white",command=lambda:tableinfomation(6))
                                        table_6.place(x=230,y=270)
                                        def staff_6() :
                                            conn = sqlite3.connect("projectdb.db")
                                            cursor = conn.cursor()
                                            sql = """
                                                    UPDATE shop_shin_table
                                                    SET staffcall=?
                                                    WHERE table_no=? """
                                            cursor.execute(sql,["no","5"])
                                            conn.commit()
                                        if result[5][4] == "yes" :
                                            Button(shin_table_frame,image=staff_cal,border=0,bg="#62943B",command=staff_6).place(x=280,y=275)
                                        else :
                                            pass
                                    else :
                                        table_6 = Button(shin_table_frame,image=teble_yellow_act,bg="#FFDDEB",font="Calibri 22 bold",border=0,activebackground="#FFDDEB",text="6",compound="center",fg="white",command=lambda:tableinfomation(6),state="disabled")
                                        table_6.place(x=230,y=270)
                                    # 7
                                    if result[6][1] == "default" :
                                        def staff_7() :
                                            conn = sqlite3.connect("projectdb.db")
                                            cursor = conn.cursor()
                                            sql = """
                                                    UPDATE shop_shin_table
                                                    SET staffcall=?
                                                    WHERE table_no=? """
                                            cursor.execute(sql,["no","5"])
                                            conn.commit()
                                        table_7 = Button(shin_table_frame,image=teble_red_act,bg="#FFDDEB",font="Calibri 22 bold",border=0,activebackground="#FFDDEB",text="7",compound="center",fg="white",command=lambda:tableinfomation(7))
                                        table_7.place(x=50,y=420)
                                        if result[6][4] == "yes" :
                                            Button(shin_table_frame,image=staff_cal,border=0,bg="#62943B",command=staff_7).place(x=100,y=425)
                                        else :
                                            pass
                                    else :
                                        table_7 = Button(shin_table_frame,image=teble_red_act,bg="#FFDDEB",font="Calibri 22 bold",border=0,activebackground="#FFDDEB",text="7",compound="center",fg="white",command=lambda:tableinfomation(7),state="disabled")
                                        table_7.place(x=50,y=420)
                                    # 8
                                    if result[7][1] == "default" :
                                        table_8 = Button(shin_table_frame,image=teble_red_act,bg="#FFDDEB",font="Calibri 22 bold",border=0,activebackground="#FFDDEB",text="8",compound="center",fg="white",command=lambda:tableinfomation(8))
                                        table_8.place(x=140,y=420)
                                        def staff_8() :
                                            conn = sqlite3.connect("projectdb.db")
                                            cursor = conn.cursor()
                                            sql = """
                                                    UPDATE shop_shin_table
                                                    SET staffcall=?
                                                    WHERE table_no=? """
                                            cursor.execute(sql,["no","5"])
                                            conn.commit()
                                        if result[7][4] == "yes" :
                                            Button(shin_table_frame,image=staff_cal,border=0,bg="#62943B",command=staff_8).place(x=190,y=425)
                                        else :
                                            pass
                                    else :
                                        table_8 = Button(shin_table_frame,image=teble_red_act,bg="#FFDDEB",font="Calibri 22 bold",border=0,activebackground="#FFDDEB",text="8",compound="center",fg="white",command=lambda:tableinfomation(8),state="disabled")
                                        table_8.place(x=140,y=420)
                                    conn.close()
                                # Start             
                                Label(shin_admin_frame,image=shin_header,bg="#FFFBEA").place(x=-2,y=-15)
                                Label(shin_admin_frame,image=shin_logo,bg="#FFFBEA").place(x=40,y=0)
                                tablebut = Button(shin_admin_frame,image=button_yellow,border=0,activebackground="white",activeforeground="white",bg="white",text="Table",compound="center",font="Calibri 16",command=shin_table)
                                tablebut.place(x=880,y=112)
                                queuebut = Button(shin_admin_frame,image=button_yellow,border=0,activebackground="white",activeforeground="white",bg="white",text="Queue",compound="center",font="Calibri 16",command=shin_queue)
                                queuebut.place(x=780,y=112)
                                showtext = Label(shin_admin_frame,text="",font="Calibri 24 bold",bg="#EADDCD")
                                showtext.place(x=250,y=30)
                                shin_table()           
                            # OHK
                            elif result[3] == "OHK" :
                                frame_adminlogin.destroy()
                                ohk_admin_frame = Frame(admin,bg="#FFFBEA")
                                ohk_admin_frame.place(x=0,y=0,w=w,h=h)
                                # frame
                                def ohk_queue() :
                                    global ohk_queue
                                    def queueinfomation(number) :
                                        def ohk_addtostore(namecus,numbergroup) :
                                            ans = messagebox.askquestion("Admin","Add customer to table %s"%(numbergroup))
                                            if ans == "yes" :
                                                if numbergroup == 1 or numbergroup == 2 or numbergroup == 3:
                                                    people = "1-2"
                                                elif numbergroup == 4 or numbergroup == 5 or numbergroup == 6:
                                                    people = "3-4"
                                                elif numbergroup == 7 or numbergroup == 8:
                                                    people = "3-4"
                                                #
                                                sql = """
                                                        UPDATE shop_ohk_table
                                                        SET name=?,amount=?,staffcall=?
                                                        WHERE table_no=? """
                                                cursor.execute(sql,[namecus,people,"no",numbergroup])
                                                conn.commit()
                                                #
                                                sql = """
                                                        UPDATE shop_ohk_table
                                                        SET status=?
                                                        WHERE table_no=? """
                                                cursor.execute(sql,["default",numbergroup])
                                                conn.commit()
                                                #
                                                sql = """
                                                        UPDATE shop_ohk_queue
                                                        SET q_status=?
                                                        WHERE q_name=?"""
                                                cursor.execute(sql,["ready",namecus])   
                                                conn.commit()     
                                                conn.close()
                                            else :
                                                pass
                                        Label(ohk_queue,image=queue_frame,bg="#FFE296").place(x=645,y=5)
                                        Label(ohk_queue,text="Table %s"%(number),font="Calibri 24 bold",bg='#FFE296').place(x=670,y=20)
                                        Label(ohk_queue,text="No.",font="Calibri 18",bg='#FFE296').place(x=660,y=70)
                                        Label(ohk_queue,text="Name",font="Calibri 18",bg='#FFE296').place(x=860,y=70)
                                        conn = sqlite3.connect("projectdb.db")
                                        cursor = conn.cursor()
                                        if number == 1 or number == 2 or number == 3:
                                            sql = """
                                                    SELECT * FROM shop_ohk_queue
                                                    WHERE q_amount=? and q_status=?"""
                                            cursor.execute(sql,["1-2","wait"])
                                            result = cursor.fetchall()
                                            
                                            yasix = 120
                                            for i,data in enumerate(result) :
                                                Label(ohk_queue,text=data[0],bg="#FFE296").place(x=660,y=yasix)
                                                Label(ohk_queue,text=data[1],bg="#FFE296").place(x=860,y=yasix)
                                                yasix = yasix +70
                                                ohk1_2 = Button(ohk_queue,text="bookatble",font="Calibri 18",bg='green',border=0,fg="white",command=lambda:ohk_addtostore(result[0][1],number))
                                                ohk1_2.place(x=660,y=470)
                                        elif number == 4 or number == 5 or number == 6:
                                            
                                            sql = """
                                                    SELECT * FROM shop_ohk_queue
                                                    WHERE q_amount=? and q_status=?"""
                                            cursor.execute(sql,["3-4","wait"])
                                            result = cursor.fetchall()
                                            
                                            yasix = 120
                                            for i,data in enumerate(result) :
                                                Label(ohk_queue,text=data[0],bg="#FFE296").place(x=660,y=yasix)
                                                Label(ohk_queue,text=data[1],bg="#FFE296").place(x=860,y=yasix)
                                                yasix = yasix +70
                                                ohk1_2 = Button(ohk_queue,text="bookatble",font="Calibri 18",bg='green',border=0,fg="white",command=lambda:ohk_addtostore(result[0][1],number))
                                                ohk1_2.place(x=660,y=470)
                                        elif number == 7 or number == 8:
                                            
                                            sql = """
                                                    SELECT * FROM shop_ohk_queue
                                                    WHERE q_amount=? and q_status=? """
                                            cursor.execute(sql,["5-6","wait"])
                                            result = cursor.fetchall()
                                            
                                            yasix = 120
                                            for i,data in enumerate(result) :
                                                Label(ohk_queue,text=data[0],bg="#FFE296").place(x=660,y=yasix)
                                                Label(ohk_queue,text=data[1],bg="#FFE296").place(x=860,y=yasix)
                                                yasix = yasix +70
                                                ohk1_2 = Button(ohk_queue,text="bookatble",font="Calibri 18",bg='green',border=0,fg="white",command=lambda:ohk_addtostore(result[0][1],number))
                                                ohk1_2.place(x=660,y=470)
                                    queuebut["state"] = "disabled"
                                    tablebut["state"] = "active"
                                    showtext["text"] = "Queue"
                                    ohk_table_frame.destroy()
                                    ohk_queue = Frame(ohk_admin_frame,bg="#FFFBEA")
                                    ohk_queue.place(x=0,y=160,w=w,h=h-140)
                                    Label(ohk_queue,image=admin_yayoi_frame_1,bg="#FBF0E3").place(x=25,y=5)
                                    Label(ohk_queue,image=queue_frame,bg="#FBF0E3").place(x=645,y=5)
                                    Label(ohk_queue,image=admin_yayoi_table,bg="#FFDDEB").place(x=40,y=25)
                                    Label(ohk_queue,text="1-2 People",bg="#FFDDEB",font="Calibri 18").place(x=40,y=65)
                                    Label(ohk_queue,text="3-4 People",bg="#FFDDEB",font="Calibri 18").place(x=40,y=215)
                                    Label(ohk_queue,text="5-6 People",bg="#FFDDEB",font="Calibri 18").place(x=40,y=365)
                                    # conn
                                    conn = sqlite3.connect("projectdb.db")
                                    cursor = conn.cursor()
                                    sql = """
                                            SELECT * FROM shop_ohk_table """
                                    cursor.execute(sql)
                                    result = cursor.fetchall()
                                    # 1
                                    if result[0][1] == "free" :
                                        table_1 = Button(ohk_queue,image=teble_green_act,bg="#FFDDEB",font="Calibri 22 bold",border=0,activebackground="#FFDDEB",text="1",compound="center",fg="white",command=lambda:queueinfomation(1))
                                        table_1.place(x=50,y=120)
                                    else :
                                        table_1 = Button(ohk_queue,image=teble_green_act,bg="#FFDDEB",font="Calibri 22 bold",border=0,activebackground="#FFDDEB",text="1",compound="center",fg="white",command=lambda:queueinfomation(1),state="disabled")
                                        table_1.place(x=50,y=120)
                                    # 2
                                    if result[1][1] == "free" :
                                        table_2 = Button(ohk_queue,image=teble_green_act,bg="#FFDDEB",font="Calibri 22 bold",border=0,activebackground="#FFDDEB",text="2",compound="center",fg="white",command=lambda:queueinfomation(2))
                                        table_2.place(x=140,y=120)
                                    else :
                                        table_2 = Button(ohk_queue,image=teble_green_act,bg="#FFDDEB",font="Calibri 22 bold",border=0,activebackground="#FFDDEB",text="2",compound="center",fg="white",command=lambda:queueinfomation(2),state="disabled")
                                        table_2.place(x=140,y=120)
                                    # 3
                                    if result[2][1] == "free" :
                                        table_3 = Button(ohk_queue,image=teble_green_act,bg="#FFDDEB",font="Calibri 22 bold",border=0,activebackground="#FFDDEB",text="3",compound="center",fg="white",command=lambda:queueinfomation(3))
                                        table_3.place(x=230,y=120)
                                    else :
                                        table_3 = Button(ohk_queue,image=teble_green_act,bg="#FFDDEB",font="Calibri 22 bold",border=0,activebackground="#FFDDEB",text="3",compound="center",fg="white",command=lambda:queueinfomation(3),state="disabled")
                                        table_3.place(x=230,y=120)
                                    # 4
                                    if result[3][1] == "free" :
                                        table_4 = Button(ohk_queue,image=teble_yellow_act,bg="#FFDDEB",font="Calibri 22 bold",border=0,activebackground="#FFDDEB",text="4",compound="center",fg="white",command=lambda:queueinfomation(4))
                                        table_4.place(x=50,y=270)
                                    else :
                                        table_4 = Button(ohk_queue,image=teble_yellow_act,bg="#FFDDEB",font="Calibri 22 bold",border=0,activebackground="#FFDDEB",text="4",compound="center",fg="white",command=lambda:queueinfomation(4),state="disabled")
                                        table_4.place(x=50,y=270)
                                    # 5
                                    if result[4][1] == "free" :
                                        table_5 = Button(ohk_queue,image=teble_yellow_act,bg="#FFDDEB",font="Calibri 22 bold",border=0,activebackground="#FFDDEB",text="5",compound="center",fg="white",command=lambda:queueinfomation(5))
                                        table_5.place(x=140,y=270)
                                    else :
                                        table_5 = Button(ohk_queue,image=teble_yellow_act,bg="#FFDDEB",font="Calibri 22 bold",border=0,activebackground="#FFDDEB",text="5",compound="center",fg="white",command=lambda:queueinfomation(5),state="disabled")
                                        table_5.place(x=140,y=270)
                                    # 6
                                    if result[5][1] == "free" :
                                        table_6 = Button(ohk_queue,image=teble_yellow_act,bg="#FFDDEB",font="Calibri 22 bold",border=0,activebackground="#FFDDEB",text="6",compound="center",fg="white",command=lambda:queueinfomation(6))
                                        table_6.place(x=230,y=270)
                                    else :
                                        table_6 = Button(ohk_queue,image=teble_yellow_act,bg="#FFDDEB",font="Calibri 22 bold",border=0,activebackground="#FFDDEB",text="6",compound="center",fg="white",command=lambda:queueinfomation(6),state="disabled")
                                        table_6.place(x=230,y=270)
                                    # 7
                                    if result[6][1] == "free" :
                                        table_7 = Button(ohk_queue,image=teble_red_act,bg="#FFDDEB",font="Calibri 22 bold",border=0,activebackground="#FFDDEB",text="7",compound="center",fg="white",command=lambda:queueinfomation(7))
                                        table_7.place(x=50,y=420)
                                    else :
                                        table_7 = Button(ohk_queue,image=teble_red_act,bg="#FFDDEB",font="Calibri 22 bold",border=0,activebackground="#FFDDEB",text="7",compound="center",fg="white",command=lambda:queueinfomation(7),state="disabled")
                                        table_7.place(x=50,y=420)
                                    # 8
                                    if result[7][1] == "free" :
                                        table_8 = Button(ohk_queue,image=teble_red_act,bg="#FFDDEB",font="Calibri 22 bold",border=0,activebackground="#FFDDEB",text="8",compound="center",fg="white",command=lambda:queueinfomation(8))
                                        table_8.place(x=140,y=420)
                                    else :
                                        table_8 = Button(ohk_queue,image=teble_red_act,bg="#FFDDEB",font="Calibri 22 bold",border=0,activebackground="#FFDDEB",text="8",compound="center",fg="white",command=lambda:queueinfomation(8),state="disabled")
                                        table_8.place(x=140,y=420)
                                    conn.close()
                                def ohk_table() :
                                    global ohk_table_frame
                                    # def
                                    def tableinfomation(no):
                                        def ohk_confirmorder() :
                                            ans = messagebox.askquestion("Admin","Confirm order") 
                                            if ans == "yes" :
                                                if result :
                                                    for i,data in enumerate(result) :
                                                        sql = """
                                                                    UPDATE shop_ohk_orderprocess
                                                                    SET status=? WHERE menu_name =? """
                                                        cursor.execute(sql,["F",data[1]])
                                                        conn.commit()
                                                else :
                                                    ohkcon["state"] = "disabled"
                                                    ohkcon["fg"] = "white"
                                                conn.close()
                                            else :
                                                pass
                                        Label(ohk_table_frame,image=admin_yayoi_frame_2,bg="#FFFFFF").place(x=645,y=5)
                                        Label(ohk_table_frame,text="Table %s"%(no),font="Calibri 24 bold",bg='#DFDCED').place(x=670,y=20)
                                        Label(ohk_table_frame,text="Menu",font="Calibri 18",bg='#DFDCED').place(x=660,y=70)
                                        Label(ohk_table_frame,text="Amount",font="Calibri 18",bg='#DFDCED').place(x=860,y=70)
                                        conn = sqlite3.connect("projectdb.db")
                                        cursor = conn.cursor()
                                        sql = """
                                                SELECT * FROM shop_ohk_orderprocess 
                                                WHERE table_index=? and status=?"""
                                        cursor.execute(sql,[no,"NF"])
                                        result = cursor.fetchall()
                                        indexy = 120
                                        for i,data in enumerate(result) :
                                            if i<6 :
                                                Label(ohk_table_frame,text=data[1][0:17],font="Calibri 18",bg='#DFDCED').place(x=660,y=indexy)
                                                Label(ohk_table_frame,text=data[3][0:17],font="Calibri 18",bg='#DFDCED').place(x=890,y=indexy)
                                            else :
                                                pass
                                            indexy = indexy + 50
                                        ohkcon = Button(ohk_table_frame,text="Confirm Order",font="Calibri 18",bg='green',border=0,fg="white",command=ohk_confirmorder)
                                        ohkcon.place(x=660,y=460)
                                    #
                                    tablebut["state"] = "disabled"
                                    queuebut["state"] = "active"
                                    showtext["text"] = "Table info"
                                    ohk_table_frame = Frame(ohk_admin_frame,bg="#FFFBEA")
                                    ohk_table_frame.place(x=0,y=160,w=w,h=h-140)
                                    Label(ohk_table_frame,image=admin_yayoi_frame_1,bg="#FBF0E3").place(x=25,y=5)
                                    Label(ohk_table_frame,image=admin_yayoi_frame_2,bg="#FBF0E3").place(x=645,y=5)
                                    Label(ohk_table_frame,image=admin_yayoi_table,bg="#FFDDEB").place(x=40,y=25)
                                    Label(ohk_table_frame,text="1-2 People",bg="#FFDDEB",font="Calibri 18").place(x=40,y=65)
                                    Label(ohk_table_frame,text="3-4 People",bg="#FFDDEB",font="Calibri 18").place(x=40,y=215)
                                    Label(ohk_table_frame,text="5-6 People",bg="#FFDDEB",font="Calibri 18").place(x=40,y=365)
                                    # conn
                                    conn = sqlite3.connect("projectdb.db")
                                    cursor = conn.cursor()
                                    sql = """
                                            SELECT * FROM shop_ohk_table """
                                    cursor.execute(sql)
                                    result = cursor.fetchall()
                                    conn.close()
                                    # 1
                                    if result[0][1] == "default" :
                                        table_1 = Button(ohk_table_frame,image=teble_green_act,bg="#FFDDEB",font="Calibri 22 bold",border=0,activebackground="#FFDDEB",text="1",compound="center",fg="white",command=lambda:tableinfomation(1))
                                        table_1.place(x=50,y=120)
                                        def staff_1() :
                                            conn = sqlite3.connect("projectdb.db")
                                            cursor = conn.cursor()
                                            sql = """
                                                    UPDATE shop_ohk_table
                                                    SET staffcall=?
                                                    WHERE table_no=? """
                                            cursor.execute(sql,["no","1"])
                                            conn.commit()
                                        if result[0][4] == "yes" :
                                            Button(ohk_table_frame,image=staff_cal,border=0,bg="#62943B",command=staff_1).place(x=100,y=125)
                                        else :
                                            pass
                                    else :
                                        table_1 = Button(ohk_table_frame,image=teble_green_act,bg="#FFDDEB",font="Calibri 22 bold",border=0,activebackground="#FFDDEB",text="1",compound="center",fg="white",command=lambda:tableinfomation(1),state="disabled")
                                        table_1.place(x=50,y=120)
                                    # 2
                                    if result[1][1] == "default" :
                                        table_2 = Button(ohk_table_frame,image=teble_green_act,bg="#FFDDEB",font="Calibri 22 bold",border=0,activebackground="#FFDDEB",text="2",compound="center",fg="white",command=lambda:tableinfomation(2))
                                        table_2.place(x=140,y=120)
                                        def staff_2() :
                                            conn = sqlite3.connect("projectdb.db")
                                            cursor = conn.cursor()
                                            sql = """
                                                    UPDATE shop_ohk_table
                                                    SET staffcall=?
                                                    WHERE table_no=? """
                                            cursor.execute(sql,["no","2"])
                                            conn.commit()
                                        if result[1][4] == "yes" :
                                            Button(ohk_table_frame,image=staff_cal,border=0,bg="#62943B",command=staff_2).place(x=190,y=125)
                                        else :
                                            pass
                                    else :
                                        table_2 = Button(ohk_table_frame,image=teble_green_act,bg="#FFDDEB",font="Calibri 22 bold",border=0,activebackground="#FFDDEB",text="2",compound="center",fg="white",command=lambda:tableinfomation(2),state="disabled")
                                        table_2.place(x=140,y=120)
                                    # 3
                                    if result[2][1] == "default" :
                                        table_3 = Button(ohk_table_frame,image=teble_green_act,bg="#FFDDEB",font="Calibri 22 bold",border=0,activebackground="#FFDDEB",text="3",compound="center",fg="white",command=lambda:tableinfomation(3))
                                        table_3.place(x=230,y=120)
                                        def staff_3() :
                                            conn = sqlite3.connect("projectdb.db")
                                            cursor = conn.cursor()
                                            sql = """
                                                    UPDATE shop_ohk_table
                                                    SET staffcall=?
                                                    WHERE table_no=? """
                                            cursor.execute(sql,["no","3"])
                                            conn.commit()
                                        if result[2][4] == "yes" :
                                            Button(ohk_table_frame,image=staff_cal,border=0,bg="#62943B",command=staff_3).place(x=280,y=125)
                                        else :
                                            pass
                                    else :
                                        table_3 = Button(ohk_table_frame,image=teble_green_act,bg="#FFDDEB",font="Calibri 22 bold",border=0,activebackground="#FFDDEB",text="3",compound="center",fg="white",command=lambda:tableinfomation(3),state="disabled")
                                        table_3.place(x=230,y=120)
                                    # 4
                                    if result[3][1] == "default" :
                                        table_4 = Button(ohk_table_frame,image=teble_yellow_act,bg="#FFDDEB",font="Calibri 22 bold",border=0,activebackground="#FFDDEB",text="4",compound="center",fg="white",command=lambda:tableinfomation(4))
                                        table_4.place(x=50,y=270)
                                        def staff_4() :
                                            conn = sqlite3.connect("projectdb.db")
                                            cursor = conn.cursor()
                                            sql = """
                                                    UPDATE shop_ohk_table
                                                    SET staffcall=?
                                                    WHERE table_no=? """
                                            cursor.execute(sql,["no","4"])
                                            conn.commit()
                                        if result[3][4] == "yes" :
                                            Button(ohk_table_frame,image=staff_cal,border=0,bg="#62943B",command=staff_4).place(x=100,y=275)
                                        else :
                                            pass
                                    else :
                                        table_4 = Button(ohk_table_frame,image=teble_yellow_act,bg="#FFDDEB",font="Calibri 22 bold",border=0,activebackground="#FFDDEB",text="4",compound="center",fg="white",command=lambda:tableinfomation(4),state="disabled")
                                        table_4.place(x=50,y=270)
                                    # 5
                                    if result[4][1] == "default" :
                                        table_5 = Button(ohk_table_frame,image=teble_yellow_act,bg="#FFDDEB",font="Calibri 22 bold",border=0,activebackground="#FFDDEB",text="5",compound="center",fg="white",command=lambda:tableinfomation(5))
                                        table_5.place(x=140,y=270)
                                        def staff_5() :
                                            conn = sqlite3.connect("projectdb.db")
                                            cursor = conn.cursor()
                                            sql = """
                                                    UPDATE shop_ohk_table
                                                    SET staffcall=?
                                                    WHERE table_no=? """
                                            cursor.execute(sql,["no","5"])
                                            conn.commit()
                                        if result[4][4] == "yes" :
                                            Button(ohk_table_frame,image=staff_cal,border=0,bg="#62943B",command=staff_5).place(x=190,y=275)
                                        else :
                                            pass
                                    else :
                                        table_5 = Button(ohk_table_frame,image=teble_yellow_act,bg="#FFDDEB",font="Calibri 22 bold",border=0,activebackground="#FFDDEB",text="5",compound="center",fg="white",command=lambda:tableinfomation(5),state="disabled")
                                        table_5.place(x=140,y=270)
                                    # 6
                                    if result[5][1] == "default" :
                                        table_6 = Button(ohk_table_frame,image=teble_yellow_act,bg="#FFDDEB",font="Calibri 22 bold",border=0,activebackground="#FFDDEB",text="6",compound="center",fg="white",command=lambda:tableinfomation(6))
                                        table_6.place(x=230,y=270)
                                        def staff_6() :
                                            conn = sqlite3.connect("projectdb.db")
                                            cursor = conn.cursor()
                                            sql = """
                                                    UPDATE shop_ohk_table
                                                    SET staffcall=?
                                                    WHERE table_no=? """
                                            cursor.execute(sql,["no","5"])
                                            conn.commit()
                                        if result[5][4] == "yes" :
                                            Button(ohk_table_frame,image=staff_cal,border=0,bg="#62943B",command=staff_6).place(x=280,y=275)
                                        else :
                                            pass
                                    else :
                                        table_6 = Button(ohk_table_frame,image=teble_yellow_act,bg="#FFDDEB",font="Calibri 22 bold",border=0,activebackground="#FFDDEB",text="6",compound="center",fg="white",command=lambda:tableinfomation(6),state="disabled")
                                        table_6.place(x=230,y=270)
                                    # 7
                                    if result[6][1] == "default" :
                                        def staff_7() :
                                            conn = sqlite3.connect("projectdb.db")
                                            cursor = conn.cursor()
                                            sql = """
                                                    UPDATE shop_ohk_table
                                                    SET staffcall=?
                                                    WHERE table_no=? """
                                            cursor.execute(sql,["no","5"])
                                            conn.commit()
                                        table_7 = Button(ohk_table_frame,image=teble_red_act,bg="#FFDDEB",font="Calibri 22 bold",border=0,activebackground="#FFDDEB",text="7",compound="center",fg="white",command=lambda:tableinfomation(7))
                                        table_7.place(x=50,y=420)
                                        if result[6][4] == "yes" :
                                            Button(ohk_table_frame,image=staff_cal,border=0,bg="#62943B",command=staff_7).place(x=100,y=425)
                                        else :
                                            pass
                                    else :
                                        table_7 = Button(ohk_table_frame,image=teble_red_act,bg="#FFDDEB",font="Calibri 22 bold",border=0,activebackground="#FFDDEB",text="7",compound="center",fg="white",command=lambda:tableinfomation(7),state="disabled")
                                        table_7.place(x=50,y=420)
                                    # 8
                                    if result[7][1] == "default" :
                                        table_8 = Button(ohk_table_frame,image=teble_red_act,bg="#FFDDEB",font="Calibri 22 bold",border=0,activebackground="#FFDDEB",text="8",compound="center",fg="white",command=lambda:tableinfomation(8))
                                        table_8.place(x=140,y=420)
                                        def staff_8() :
                                            conn = sqlite3.connect("projectdb.db")
                                            cursor = conn.cursor()
                                            sql = """
                                                    UPDATE shop_ohk_table
                                                    SET staffcall=?
                                                    WHERE table_no=? """
                                            cursor.execute(sql,["no","5"])
                                            conn.commit()
                                        if result[7][4] == "yes" :
                                            Button(ohk_table_frame,image=staff_cal,border=0,bg="#62943B",command=staff_8).place(x=190,y=425)
                                        else :
                                            pass
                                    else :
                                        table_8 = Button(ohk_table_frame,image=teble_red_act,bg="#FFDDEB",font="Calibri 22 bold",border=0,activebackground="#FFDDEB",text="8",compound="center",fg="white",command=lambda:tableinfomation(8),state="disabled")
                                        table_8.place(x=140,y=420)
                                    conn.close()
                                # Start             
                                Label(ohk_admin_frame,image=ohk_header,bg="#FFFBEA").place(x=-2,y=-15)
                                Label(ohk_admin_frame,image=ohk_logo,bg="#FFFBEA").place(x=40,y=0)
                                tablebut = Button(ohk_admin_frame,image=button_yellow,border=0,activebackground="white",activeforeground="white",bg="white",text="Table",compound="center",font="Calibri 16",command=ohk_table)
                                tablebut.place(x=880,y=112)
                                queuebut = Button(ohk_admin_frame,image=button_yellow,border=0,activebackground="white",activeforeground="white",bg="white",text="Queue",compound="center",font="Calibri 16",command=ohk_queue)
                                queuebut.place(x=780,y=112)
                                showtext = Label(ohk_admin_frame,text="",font="Calibri 24 bold",bg="#E8C9AB")
                                showtext.place(x=250,y=30)
                                ohk_table()
                        else :
                            messagebox.showwarning("Admin","Wrong username or password") 
                    else :
                        messagebox.showwarning("Admin","Please enter Password") 
                        if  entry_password_admin_spy.get() == "" :
                            entry_password_admin_spy.set("Password   ")
                            entry_password_admin["fg"] = "#AAAAAA"
                else :
                    messagebox.showwarning("Admin","Please enter Username") 
                    if  entry_username_admin_spy.get() == "" :
                        entry_username_admin_spy.set("Username   ")
                        entry_username_admin["fg"] = "#AAAAAA"
                    if  entry_password_admin_spy.get() == "" :
                        entry_password_admin_spy.set("Password   ")
                        entry_password_admin["fg"] = "#AAAAAA"
            #
            admin = Toplevel()
            admin.title("Admin Window")
            x = admin.winfo_screenwidth()/2 - w/2
            y = admin.winfo_screenheight()/2 - h/2
            admin.geometry("%dx%d+%d+%d"%(w,h,x,y))
            admin.resizable(FALSE,False)
            admin.option_add('*font',"Calibri 20")
            # Spy set
            entry_username_admin_spy.set("Username   ")
            entry_password_admin_spy.set("Password   ")
            # frame setting
            frame_adminlogin = Frame(admin,bg="#7587AE")
            frame_adminlogin.place(x=0,y=0,w=w,h=h)
            # Canvas
            canv = Canvas(frame_adminlogin, width=w, height=h,bg="#242F47")
            canv.pack()
            canv.create_rectangle(635, 255, 885, 258, fill="#A6BFD6", outline = '#A6BFD6')
            canv.create_rectangle(635, 355, 885, 358, fill="#A6BFD6", outline = '#A6BFD6')
            # widget
            # frame setting
            # widget
            # photo
            photo_1 = Label(frame_adminlogin,image=admin_login,bg="#242F47")
            photo_1.place(x=-2,y=-1)
            # text = signin
            text_signin_admin = Label(frame_adminlogin,text="Admin",fg="#D4DDF1",bg="#242F47",font="Calibri 42 bold")
            text_signin_admin.place(x=685,y=100)
            # entry = username
            entry_username_admin = Entry(frame_adminlogin,text="",bg="#242F47",fg="#FFFFFF",font="Calibri 18 bold",textvariable=entry_username_admin_spy,border=0,width=20)
            entry_username_admin.place(x=640,y=220)
            # entry = password
            entry_password_admin = Entry(frame_adminlogin,text="",bg="#242F47",fg="#FFFFFF",font="Calibri 18 bold",textvariable=entry_password_admin_spy,border=0,width=20)
            entry_password_admin.place(x=640,y=320)
            # button = signin
            button_signin_admin = Button(frame_adminlogin,text="Sign in",width=18,height=1,bg="#7587AE",fg="white",font="Calibri 18 bold",border=2,activebackground="#7587AE")
            button_signin_admin.place(x=640,y=420)
            button_back_admin = Button(frame_adminlogin,text="< Back",font="Calibri 12 underline",bg="#242F47",activebackground="#242F47",border=0,fg="white",command=exitx,activeforeground="white")
            button_back_admin.place(x=w-65,y=10)
            # bind
            if entry_username_admin_spy.get() == "Username   " :
                entry_username_admin.bind("<Button-1>",entry_username_admin_click)
            if entry_password_admin_spy.get() == "Password   " :
                entry_password_admin.bind("<Button-1>",entry_password_admin_click)
            button_signin_admin.bind("<Button-1>",button_signin_admin_click)
    # def 2 customer mainpage
    def allfunctionin_mainpage() : # all function about mainpage
        global customermainpage , adminmainpage 
        # userinfomation Spy
        userid_spy = StringVar() # id customer
        userfname_spy = StringVar() # firstname customer
        userlname_spy = StringVar() # lastname customer
        usertel_spy = StringVar() # telephone customer
        usergender_spy = StringVar() # gedner customer
        member_spy = StringVar() # member customer
        point_spy = StringVar() # point customer
        money_spy = StringVar() # money customer
        fav_spy = StringVar()
        #
        def customermainpage(id) :
            global account_frame
            # Main frame
            frame_customermainpage = Frame(root,bg="#E4D3D3")
            frame_customermainpage.place(x=0,y=0,width=w,height=h)
            # database
            conn = sqlite3.connect("projectdb.db")
            cursor = conn.cursor()
            sql = """
                    SELECT * FROM customer_information 
                    WHERE id_customer=? """
            cursor.execute(sql,[id])
            result = cursor.fetchone()
            userid_spy.set(result[0]) # user spy
            userfname_spy.set(result[1]) # fname spy
            userlname_spy.set(result[2]) # lname spy
            usertel_spy.set(result[3]) # tele spy
            usergender_spy.set(result[4]) # gender spy
            member_spy.set(result[5]) # member spy
            point_spy.set(result[6]) # point customer
            money_spy.set(result[7]) # money customer
            fav_spy.set(result[8]) # favshop customer
            def framemenu() :
                global home_button , account_button , q_button , favshop_button , button_quit , whatqueue
                def quitporcess() :
                    ansquit = messagebox.askquestion("Admin","Are you sure that you want to logout?")
                    if ansquit == "yes" :
                        customerlogin()
                # menu
                frame_menu = Frame(frame_customermainpage,bg="#F9E9C1")
                frame_menu.place(x=0,y=0,width=100,height=h) 
                # image
                logophoto = Label(frame_menu,image=logoapp,bg="#F9E9C1")
                logophoto.place(x=20,y=20)
                # widget
                whatqueue = StringVar()
                whatqueue.set("empty")
                #
                home_button = Button(frame_menu,text="Home",font="Calibri 12 bold",command=home_frame,image=button_home_activate,bg="#F9E9C1",borderwidth=0,activebackground="#F9E9C1")
                home_button.place(x=18,y=100)
                #
                account_button = Button(frame_menu,text="Wallet",font="Calibri 12 bold",command=account_frame,image=button_wallet_not,bg="#F9E9C1",activebackground="#F9E9C1",border=0)
                account_button.place(x=18,y=200)
                #
                q_button = Button(frame_menu,text="Queue",font="Calibri 12 bold",command=queue_frame,image=button_q_not,bg="#F9E9C1",activebackground="#F9E9C1",border=0)
                q_button.place(x=18,y=300)
                #
                favshop_button = Button(frame_menu,text="Favorite Shop",font="Calibri 12 bold",command=favshop_frame,image=button_fav_not,bg="#F9E9C1",activebackground="#F9E9C1",border=0)
                favshop_button.place(x=18,y=400)
                # customerlogin
                but_quit = Button(frame_menu,image=quit_button,command=quitporcess,bg="#F9E9C1",activebackground="#F9E9C1",border=0)
                but_quit.place(x=26,y=h-50)               
            def home_frame() :
                global label_showtime
                global shop1,shop2,shop3,shop4,shop5,shop6
                # button_home_not
                home_button["image"] = button_home_activate
                account_button["image"] = button_wallet_not
                q_button["image"] = button_q_not
                favshop_button["image"] = button_fav_not
                # function
                # Group
                def category_restaurant() : # Restaurant
                    all_restaurant = Frame(frame_home,bg="#F8EFE0")
                    all_restaurant.place(x=0,y=100,width=w-100,height=h-100)
                    #
                    def favoriteres(shopname) :
                        sql = """
                                    UPDATE customer_information
                                    SET fav_shop=? 
                                    WHERE id_customer=? """
                        cursor.execute(sql,[shopname,userid_spy.get()])
                        conn.commit()
                        customermainpage(id)
                    # shop 1
                    Button(all_restaurant,image=frameshop_yyo,border=0,bg="#F8EFE0",activebackground="#F8EFE0",command=shop2).place(x=30,y=20)
                    if fav_spy.get() == "yyo" :
                        favsr1 = Button(all_restaurant,image=addtofav_act,border=0,bg="white",command= lambda:favoriteres("yyo") )
                        favsr1.place(x=240,y=175)
                    else :
                        favsr1 = Button(all_restaurant,image=addtofav_not,border=0,bg="white",command= lambda:favoriteres("yyo") )
                        favsr1.place(x=240,y=175)
                    # shop 2
                    Button(all_restaurant,image=frameshop_shin,border=0,bg="#F8EFE0",activebackground="#F8EFE0",command=shop5).place(x=320,y=20)
                    if fav_spy.get() == "shin" :
                        favsr2 = Button(all_restaurant,image=addtofav_act,border=0,bg="white",command= lambda:favoriteres("shin") )
                        favsr2.place(x=530,y=175)
                    else :
                        favsr2 = Button(all_restaurant,image=addtofav_not,border=0,bg="white",command= lambda:favoriteres("shin") )
                        favsr2.place(x=530,y=175)
                    # shop 3
                    Button(all_restaurant,image=frameshop_okj,border=0,bg="#F8EFE0",activebackground="#F8EFE0",command=shop6).place(x=610,y=20)
                    if fav_spy.get() == "okj" :
                        favsr3 = Button(all_restaurant,image=addtofav_act,border=0,bg="white",command= lambda:favoriteres("okj") )
                        favsr3.place(x=820,y=175)
                    else :
                        favsr3 = Button(all_restaurant,image=addtofav_not,border=0,bg="white",command= lambda:favoriteres("okj") )
                        favsr3.place(x=820,y=175)
                    # shop 4
                    Button(all_restaurant,image=frameshop_yyo,border=0,bg="#F8EFE0",activebackground="#F8EFE0")#.place(x=30,y=310)
                    # shop 5
                    Button(all_restaurant,image=frameshop_yyo,border=0,bg="#F8EFE0",activebackground="#F8EFE0")#.place(x=320,y=310)
                    # shop 6
                    Button(all_restaurant,image=frameshop_yyo,border=0,bg="#F8EFE0",activebackground="#F8EFE0")#.place(x=610,y=310)
                def category_hotel() : # Hotel
                    # Frame
                    all_hotel = Frame(frame_home,bg="#21253E")
                    all_hotel.place(x=0,y=0,width=w-100,height=h)
                    # function
                    def finishbookhotel1() :
                        hotel1porcess_frame.destroy()
                        hotel1page()
                    def finishbookhotel2() :
                        hotel2porcess_frame.destroy()
                        hotel2page()
                    def finishbookhotel3() :
                        hotel3porcess_frame.destroy()
                        hotel3page()
                    def backfromhotel1() : # quitframe
                        hotel1_frame.destroy()
                    def backfromhotel2() : # quitframe
                        hotel2_frame.destroy()
                    def backfromhotel3() : # quitframe
                        hotel3_frame.destroy()
                    def hotel1processback() : # quitframe
                        hotel1porcess_frame.destroy()
                    def hotel2processback() : # quitframe
                        hotel2porcess_frame.destroy()
                    def hotel3processback() : # quitframe
                        hotel3porcess_frame.destroy()
                    # main function
                    def hotel1porcess() :
                        def back() :
                            book1processframe.destroy()
                        def bookprocess() :
                            if in_day_spy.get() != "" :
                                if in_month_spy.get() != "" :
                                    if out_day_spy.get() != "" :
                                        if out_month_spy.get() != "" :
                                            if adult_spy.get() != "" :
                                                if roomt_spy.get() != "" :
                                                    global book1processframe
                                                    def finishprocess(money,price) :
                                                        yesno = messagebox.askquestion("Admin","Confirm Payment")  
                                                        if yesno == "yes" :
                                                            newbalance = str(money-price)
                                                            sql = """
                                                                    UPDATE customer_information
                                                                    SET money_customer=? 
                                                                    WHERE id_customer=?"""
                                                            cursor.execute(sql,[newbalance,userid_spy.get()])
                                                            conn.commit()
                                                            sql = """
                                                                    INSERT INTO hotel_1(Date,Month,Name,Room)
                                                                    VALUES (?,?,?,?)"""
                                                            cursor.execute(sql,[in_day_spy.get()+" "+in_month_spy.get(),out_day_spy.get()+" "+out_month_spy.get(),userfname_spy.get(),roomt_spy.get()])
                                                            conn.commit()
                                                            messagebox.showinfo("Admin","Booking Succesfully")
                                                            finishbookhotel1()
                                                        else :
                                                            pass
                                                    book1processframe = Frame(hotel1_frame,bg="#21253E")
                                                    book1processframe.place(x=0,y=0,width=w-100,height=h)
                                                    bg = Label(book1processframe,image=hotel_1_bg)
                                                    bg.place(x=0,y=0)
                                                    bg_1 = Label(book1processframe,bg="#21253E")
                                                    bg_1.place(x=100,y=100,height=h-200,width=w-330)
                                                    back_but = Button(book1processframe,text="< Back",border=0,bg="#15345F",fg="white",command=back,activebackground="#15345F",activeforeground="white")
                                                    back_but.place(x=10,y=10)
                                                    # ["Normal Bedroom,1 bed","Normal Bedroom,2 bed","Premium Bedroom","Executive Room"]
                                                    text_info = Label(book1processframe,text="Booking Information",font="Calibri 24 bold",bg="#21253E",fg="white").place(x=300,y=120)  #fix
                                                    text_chkinday = Label(book1processframe,text="Check in date : %s %s"%(in_day_spy.get(),in_month_spy.get()),bg="#21253E",fg="white").place(x=160,y=180)
                                                    text_chkoutday = Label(book1processframe,text="Check out date : %s %s"%(out_day_spy.get(),out_month_spy.get()),bg="#21253E",fg="white").place(x=160,y=240)
                                                    text_roomtype = Label(book1processframe,text="Room Type : %s"%(roomt_spy.get()),bg="#21253E",fg="white").place(x=160,y=300)
                                                    totalprice = 0
                                                    if roomt_spy.get() == "Normal Bedroom,1 bed" :
                                                        totalprice = 2000
                                                    elif roomt_spy.get() == "Normal Bedroom,2 bed" :
                                                        totalprice = 3000
                                                    elif roomt_spy.get() == "Premium Bedroom" :
                                                        totalprice = 4000
                                                    elif roomt_spy.get() == "Executive Room" :
                                                        totalprice = 5000
                                                    # "January","February","March","April","May","June","July","August","September","October","November","December"
                                                    in_monthindex = 0
                                                    if in_month_spy.get() == "January" :
                                                        in_monthindex = 1
                                                    elif in_month_spy.get() == "February" :
                                                        in_monthindex = 2
                                                    elif in_month_spy.get() == "March" :
                                                        in_monthindex = 3
                                                    elif in_month_spy.get() == "April" :
                                                        in_monthindex = 4
                                                    elif in_month_spy.get() == "May" :
                                                        in_monthindex = 5
                                                    elif in_month_spy.get() == "June" :
                                                        in_monthindex = 6
                                                    elif in_month_spy.get() == "July" :
                                                        in_monthindex = 7
                                                    elif in_month_spy.get() == "August" :
                                                        in_monthindex = 8
                                                    elif in_month_spy.get() == "September" :
                                                        in_monthindex = 9
                                                    elif in_month_spy.get() == "October" :
                                                        in_monthindex = 10
                                                    elif in_month_spy.get() == "November" :
                                                        in_monthindex = 11
                                                    elif in_month_spy.get() == "December" :
                                                        in_monthindex = 12
                                                    #
                                                    out_monthindex = 0
                                                    if out_month_spy.get() == "January" :
                                                        out_monthindex = 1
                                                    elif out_month_spy.get() == "February" :
                                                        out_monthindex = 2
                                                    elif out_month_spy.get() == "March" :
                                                        out_monthindex = 3
                                                    elif out_month_spy.get() == "April" :
                                                        out_monthindex = 4
                                                    elif out_month_spy.get() == "May" :
                                                        out_monthindex = 5
                                                    elif out_month_spy.get() == "June" :
                                                        out_monthindex = 6
                                                    elif out_month_spy.get() == "July" :
                                                        out_monthindex = 7
                                                    elif out_month_spy.get() == "August" :
                                                        out_monthindex = 8
                                                    elif out_month_spy.get() == "September" :
                                                        out_monthindex = 9
                                                    elif out_month_spy.get() == "October" :
                                                        out_monthindex = 10
                                                    elif out_month_spy.get() == "November" :
                                                        out_monthindex = 11
                                                    elif out_month_spy.get() == "December" :
                                                        out_monthindex = 12
                                                    timetype_datein = time.datetime(2020, int(in_monthindex), int(in_day_spy.get()))
                                                    timetype_dateout = time.datetime(2020, int(out_monthindex), int(out_day_spy.get()))
                                                    timetype_diff = (str(timetype_dateout-timetype_datein)[0:2])
                                                    conn = sqlite3.connect("projectdb.db")
                                                    cursor = conn.cursor()
                                                    sql = """
                                                            SELECT * FROM customer_information
                                                            WHERE id_customer=? """
                                                    cursor.execute(sql,[userid_spy.get()])
                                                    result = cursor.fetchone()
                                                    alltotalprice = (totalprice*int(timetype_diff))//1
                                                    text_roomprice = Label(book1processframe,text="Room price : %s"%(totalprice),bg="#21253E",fg="white").place(x=160,y=360)
                                                    text_total = Label(book1processframe,text="Total : %s Baht"%(alltotalprice),bg="#21253E",fg="white").place(x=330,y=440)
                                                    if float(result[7]) >= alltotalprice :
                                                        but_payment = Button(book1processframe,image=hotel_paymnet,bg="#21253E",border=0,activebackground="#21253E",command=lambda:finishprocess(float(result[7]),alltotalprice))
                                                        but_payment.place(x=280,y=540)
                                                    else :
                                                        text = Label(book1processframe,text="Not enough money in your Wallet\nPlease top up before booking",bg="#21253E",fg="white")
                                                        text.place(x=280,y=490)
                                                else :
                                                    messagebox.showwarning("Admin","Please enter room type")
                                            else :
                                                messagebox.showwarning("Admin","Please enter number of guest")
                                        else :
                                            messagebox.showwarning("Admin","Please enter Check-out month") 
                                    else :
                                        messagebox.showwarning("Admin","Please enter Check-out day")   
                                else :
                                    messagebox.showwarning("Admin","Please enter month")
                            else :
                                messagebox.showwarning("Admin","Please enter Check-in day")
                        global hotel1porcess_frame
                        hotel1porcess_frame = Frame(hotel1_frame,bg="#21253E")
                        hotel1porcess_frame.place(x=0,y=0,width=w-100,height=h)
                        bg = Label(hotel1porcess_frame,image=hotel_1_bg)
                        bg.place(x=0,y=0)
                        bg_1 = Label(hotel1porcess_frame,bg="#21253E")
                        bg_1.place(x=100,y=100,height=h-200,width=w-330)
                        in_day_spy = StringVar()
                        in_month_spy = StringVar()
                        out_day_spy = StringVar()
                        out_month_spy = StringVar()
                        adult_spy = StringVar()
                        roomt_spy = StringVar()
                        #
                        back_but = Button(hotel1porcess_frame,text="< Back",border=0,bg="#15345F",fg="white",command=hotel1processback,activebackground="#15345F",activeforeground="white")
                        back_but.place(x=10,y=10)
                        text_date = Label(hotel1porcess_frame,text="Date",font='Calibri 20 bold',bg="#21253E",fg="white")
                        text_date.place(x=120,y=110)
                        text_day = Label(hotel1porcess_frame,text="Check-in Day",bg="#21253E",fg="white")
                        text_day.place(x=120,y=160)
                        text_month = Label(hotel1porcess_frame,text="Month",bg="#21253E",fg="white")
                        text_month.place(x=450,y=160)
                        text_month = Label(hotel1porcess_frame,text="Month",bg="#21253E",fg="white")
                        text_month.place(x=450,y=260)
                        text_how = Label(hotel1porcess_frame,text="Check-out day",bg="#21253E",fg="white")
                        text_how.place(x=120,y=260)
                        day = [i for i in range(1,32)]
                        month = ["January","February","March","April","May","June","July","August","September","October","November","December"]
                        spinbox_day = ttk.Combobox(hotel1porcess_frame,values=day,textvariable=in_day_spy)
                        spinbox_day.place(x=120,y=210)
                        spinbox_month = ttk.Combobox(hotel1porcess_frame,values=month,textvariable=in_month_spy)
                        spinbox_month.place(x=450,y=210)
                        spinbox_how = ttk.Combobox(hotel1porcess_frame,values=day,textvariable=out_day_spy)
                        spinbox_how.place(x=120,y=310)
                        spinbox_month = ttk.Combobox(hotel1porcess_frame,values=month,textvariable=out_month_spy)
                        spinbox_month.place(x=450,y=310)
                        #
                        adult = [i for i in range(1,6)]
                        room_type = ["Normal Bedroom,1 bed","Normal Bedroom,2 bed","Premium Bedroom","Executive Room"]
                        text_room = Label(hotel1porcess_frame,text="Room",font='Calibri 20 bold',bg="#21253E",fg="white")
                        text_room.place(x=120,y=360)
                        text_people = Label(hotel1porcess_frame,text="Number of guest",bg="#21253E",fg="white")
                        text_people.place(x=120,y=410)
                        text_room = Label(hotel1porcess_frame,text="Room type",bg="#21253E",fg="white")
                        text_room.place(x=450,y=410)
                        spinbox_adult = ttk.Combobox(hotel1porcess_frame,values=adult,textvariable=adult_spy)
                        spinbox_adult.place(x=120,y=460)
                        spinbox_room = ttk.Combobox(hotel1porcess_frame,values=room_type,textvariable=roomt_spy)
                        spinbox_room.place(x=450,y=460)
                        #
                        but_con = Button(hotel1porcess_frame,image=hotel_confirm,bg="#21253E",border=0,activebackground="#21253E",command=bookprocess)
                        but_con.place(x=280,y=530)
                    def hotel2porcess() :
                        def back() :
                            book2processframe.destroy()
                        def bookprocess() :
                            if in_day_spy.get() != "" :
                                if in_month_spy.get() != "" :
                                    if out_day_spy.get() != "" :
                                        if out_month_spy.get() != "" :
                                            if adult_spy.get() != "" :
                                                if roomt_spy.get() != "" :
                                                    global book2processframe
                                                    def finishprocess(money,price) :
                                                        yesno = messagebox.askquestion("Admin","Confirm Payment of booking hotel") 
                                                        if yesno == "yes" :
                                                            newbalance = str(money-price)
                                                            sql = """
                                                                    UPDATE customer_information
                                                                    SET money_customer=? 
                                                                    WHERE id_customer=?"""
                                                            cursor.execute(sql,[newbalance,userid_spy.get()])
                                                            conn.commit()
                                                            sql = """
                                                                    INSERT INTO hotel_2(Date,Month,Name,Room)
                                                                    VALUES (?,?,?,?)"""
                                                            cursor.execute(sql,[in_day_spy.get()+" "+in_month_spy.get(),out_day_spy.get()+" "+out_month_spy.get(),userfname_spy.get(),roomt_spy.get()])
                                                            conn.commit()
                                                            messagebox.showinfo("Admin","Booking Succesfully")
                                                            finishbookhotel2 ()
                                                        else :
                                                            pass
                                                    book2processframe = Frame(hotel2_frame,bg="#21253E")
                                                    book2processframe.place(x=0,y=0,width=w-100,height=h)
                                                    bg = Label(book2processframe,image=hotel_2_bg)
                                                    bg.place(x=0,y=0)
                                                    bg_1 = Label(book2processframe,bg="#21253E")
                                                    bg_1.place(x=100,y=100,height=h-200,width=w-330)
                                                    back_but = Button(book2processframe,text="< Back",border=0,bg="#15345F",fg="white",command=back,activebackground="#15345F",activeforeground="white")
                                                    back_but.place(x=10,y=10)
                                                    # ["Normal Bedroom,1 bed","Normal Bedroom,2 bed","Premium Bedroom","Executive Room"]
                                                    text_info = Label(book2processframe,text="Booking Information",font="Calibri 24 bold",bg="#21253E",fg="white").place(x=330,y=120)
                                                    text_chkinday = Label(book2processframe,text="Check in date : %s %s"%(in_day_spy.get(),in_month_spy.get()),bg="#21253E",fg="white").place(x=160,y=180)
                                                    text_chkoutday = Label(book2processframe,text="Check out date : %s %s"%(out_day_spy.get(),out_month_spy.get()),bg="#21253E",fg="white").place(x=160,y=240)
                                                    text_roomtype = Label(book2processframe,text="Room Type : %s"%(roomt_spy.get()),bg="#21253E",fg="white").place(x=160,y=300)
                                                    totalprice = 0
                                                    if roomt_spy.get() == "Normal Bedroom,1 bed" :
                                                        totalprice = 2000
                                                    elif roomt_spy.get() == "Normal Bedroom,2 bed" :
                                                        totalprice = 3000
                                                    elif roomt_spy.get() == "Premium Bedroom" :
                                                        totalprice = 4000
                                                    elif roomt_spy.get() == "Executive Room" :
                                                        totalprice = 5000
                                                    # "January","February","March","April","May","June","July","August","September","October","November","December"
                                                    in_monthindex = 0
                                                    if in_month_spy.get() == "January" :
                                                        in_monthindex = 1
                                                    elif in_month_spy.get() == "February" :
                                                        in_monthindex = 2
                                                    elif in_month_spy.get() == "March" :
                                                        in_monthindex = 3
                                                    elif in_month_spy.get() == "April" :
                                                        in_monthindex = 4
                                                    elif in_month_spy.get() == "May" :
                                                        in_monthindex = 5
                                                    elif in_month_spy.get() == "June" :
                                                        in_monthindex = 6
                                                    elif in_month_spy.get() == "July" :
                                                        in_monthindex = 7
                                                    elif in_month_spy.get() == "August" :
                                                        in_monthindex = 8
                                                    elif in_month_spy.get() == "September" :
                                                        in_monthindex = 9
                                                    elif in_month_spy.get() == "October" :
                                                        in_monthindex = 10
                                                    elif in_month_spy.get() == "November" :
                                                        in_monthindex = 11
                                                    elif in_month_spy.get() == "December" :
                                                        in_monthindex = 12
                                                    #
                                                    out_monthindex = 0
                                                    if out_month_spy.get() == "January" :
                                                        out_monthindex = 1
                                                    elif out_month_spy.get() == "February" :
                                                        out_monthindex = 2
                                                    elif out_month_spy.get() == "March" :
                                                        out_monthindex = 3
                                                    elif out_month_spy.get() == "April" :
                                                        out_monthindex = 4
                                                    elif out_month_spy.get() == "May" :
                                                        out_monthindex = 5
                                                    elif out_month_spy.get() == "June" :
                                                        out_monthindex = 6
                                                    elif out_month_spy.get() == "July" :
                                                        out_monthindex = 7
                                                    elif out_month_spy.get() == "August" :
                                                        out_monthindex = 8
                                                    elif out_month_spy.get() == "September" :
                                                        out_monthindex = 9
                                                    elif out_month_spy.get() == "October" :
                                                        out_monthindex = 10
                                                    elif out_month_spy.get() == "November" :
                                                        out_monthindex = 11
                                                    elif out_month_spy.get() == "December" :
                                                        out_monthindex = 12
                                                    timetype_datein = time.datetime(2020, int(in_monthindex), int(in_day_spy.get()))
                                                    timetype_dateout = time.datetime(2020, int(out_monthindex), int(out_day_spy.get()))
                                                    timetype_diff = (str(timetype_dateout-timetype_datein)[0:2])
                                                    conn = sqlite3.connect("projectdb.db")
                                                    cursor = conn.cursor()
                                                    sql = """
                                                            SELECT * FROM customer_information
                                                            WHERE id_customer=? """
                                                    cursor.execute(sql,[userid_spy.get()])
                                                    result = cursor.fetchone()
                                                    alltotalprice = (totalprice*int(timetype_diff))//1
                                                    text_roomprice = Label(book2processframe,text="Room price : %s"%(totalprice),bg="#21253E",fg="white").place(x=160,y=360)
                                                    text_total = Label(book2processframe,text="Total : %s Baht"%(alltotalprice),bg="#21253E",fg="white").place(x=330,y=440)
                                                    if float(result[7]) >= alltotalprice :
                                                        but_payment = Button(book2processframe,image=hotel_paymnet,bg="#21253E",border=0,activebackground="#21253E",command=lambda:finishprocess(float(result[7]),alltotalprice))
                                                        but_payment.place(x=280,y=540)
                                                    else :
                                                        text = Label(book2processframe,text="Not enough money in your Wallet\nPlease top up before booking",bg="#21253E",fg="white")
                                                        text.place(x=280,y=490)
                                                else :
                                                    messagebox.showwarning("Admin","Please enter room type")
                                            else :
                                                messagebox.showwarning("Admin","Please enter number of guest")
                                        else :
                                            messagebox.showwarning("Admin","Please enter Check-out month") 
                                    else :
                                        messagebox.showwarning("Admin","Please enter Check-out day")   
                                else :
                                    messagebox.showwarning("Admin","Please enter month")
                            else :
                                messagebox.showwarning("Admin","Please enter Check-in day")
                        global hotel2porcess_frame
                        hotel2porcess_frame = Frame(hotel2_frame,bg="#21253E")
                        hotel2porcess_frame.place(x=0,y=0,width=w-100,height=h)
                        bg = Label(hotel2porcess_frame,image=hotel_2_bg)
                        bg.place(x=0,y=0)
                        bg_1 = Label(hotel2porcess_frame,bg="#21253E")
                        bg_1.place(x=100,y=100,height=h-200,width=w-330)
                        in_day_spy = StringVar()
                        in_month_spy = StringVar()
                        out_day_spy = StringVar()
                        out_month_spy = StringVar()
                        adult_spy = StringVar()
                        roomt_spy = StringVar()
                        #
                        back_but = Button(hotel2porcess_frame,text="< Back",border=0,bg="#15345F",fg="white",command=hotel2processback,activebackground="#15345F",activeforeground="white")
                        back_but.place(x=10,y=10)
                        text_date = Label(hotel2porcess_frame,text="Date",font='Calibri 20 bold',bg="#21253E",fg="white")
                        text_date.place(x=120,y=110)
                        text_day = Label(hotel2porcess_frame,text="Check-in Day",bg="#21253E",fg="white")
                        text_day.place(x=120,y=160)
                        text_month = Label(hotel2porcess_frame,text="Month",bg="#21253E",fg="white")
                        text_month.place(x=450,y=160)
                        text_month = Label(hotel2porcess_frame,text="Month",bg="#21253E",fg="white")
                        text_month.place(x=450,y=260)
                        text_how = Label(hotel2porcess_frame,text="Check-out day",bg="#21253E",fg="white")
                        text_how.place(x=120,y=260)
                        day = [i for i in range(1,32)]
                        month = ["January","February","March","April","May","June","July","August","September","October","November","December"]
                        spinbox_day = ttk.Combobox(hotel2porcess_frame,values=day,textvariable=in_day_spy)
                        spinbox_day.place(x=120,y=210)
                        spinbox_month = ttk.Combobox(hotel2porcess_frame,values=month,textvariable=in_month_spy)
                        spinbox_month.place(x=450,y=210)
                        spinbox_how = ttk.Combobox(hotel2porcess_frame,values=day,textvariable=out_day_spy)
                        spinbox_how.place(x=120,y=310)
                        spinbox_month = ttk.Combobox(hotel2porcess_frame,values=month,textvariable=out_month_spy)
                        spinbox_month.place(x=450,y=310)
                        #
                        adult = [i for i in range(1,6)]
                        room_type = ["Normal Bedroom,1 bed","Normal Bedroom,2 bed","Premium Bedroom","Executive Room"]
                        text_room = Label(hotel2porcess_frame,text="Room",font='Calibri 20 bold',bg="#21253E",fg="white")
                        text_room.place(x=120,y=360)
                        text_people = Label(hotel2porcess_frame,text="Number of guest",bg="#21253E",fg="white")
                        text_people.place(x=120,y=410)
                        text_room = Label(hotel2porcess_frame,text="Room type",bg="#21253E",fg="white")
                        text_room.place(x=450,y=410)
                        spinbox_adult = ttk.Combobox(hotel2porcess_frame,values=adult,textvariable=adult_spy)
                        spinbox_adult.place(x=120,y=460)
                        spinbox_room = ttk.Combobox(hotel2porcess_frame,values=room_type,textvariable=roomt_spy)
                        spinbox_room.place(x=450,y=460)
                        #
                        but_con = Button(hotel2porcess_frame,image=hotel_confirm,bg="#21253E",border=0,activebackground="#21253E",command=bookprocess)
                        but_con.place(x=280,y=530)
                    def hotel3porcess() :
                        def back() :
                            book3processframe.destroy()
                        def bookprocess() :
                            if in_day_spy.get() != "" :
                                if in_month_spy.get() != "" :
                                    if out_day_spy.get() != "" :
                                        if out_month_spy.get() != "" :
                                            if adult_spy.get() != "" :
                                                if roomt_spy.get() != "" :
                                                    global book3processframe
                                                    def finishprocess(money,price) :
                                                        yesno = messagebox.askquestion("Admin","Confirm Payment of booking hotel")  
                                                        if yesno == "yes" :
                                                            newbalance = str(money-price)
                                                            sql = """
                                                                    UPDATE customer_information
                                                                    SET money_customer=? 
                                                                    WHERE id_customer=?"""
                                                            cursor.execute(sql,[newbalance,userid_spy.get()])
                                                            conn.commit()
                                                            sql = """
                                                                    INSERT INTO hotel_3(Date,Month,Name,Room)
                                                                    VALUES (?,?,?,?)"""
                                                            cursor.execute(sql,[in_day_spy.get()+" "+in_month_spy.get(),out_day_spy.get()+" "+out_month_spy.get(),userfname_spy.get(),roomt_spy.get()])
                                                            conn.commit()
                                                            messagebox.showinfo("Admin","Booking Succesfully")
                                                            finishbookhotel3()
                                                        else :
                                                            pass
                                                    book3processframe = Frame(hotel3_frame,bg="#21253E")
                                                    book3processframe.place(x=0,y=0,width=w-100,height=h)
                                                    bg = Label(book3processframe,image=hotel_3_bg)
                                                    bg.place(x=0,y=0)
                                                    bg_1 = Label(book3processframe,bg="#21253E")
                                                    bg_1.place(x=100,y=100,height=h-200,width=w-330)
                                                    back_but = Button(book3processframe,text="< Back",border=0,bg="#15345F",fg="white",command=back,activebackground="#15345F",activeforeground="white")
                                                    back_but.place(x=10,y=10)
                                                    # ["Normal Bedroom,1 bed","Normal Bedroom,2 bed","Premium Bedroom","Executive Room"]
                                                    text_info = Label(book3processframe,text="Booking Information",font="Calibri 24 bold",bg="#21253E",fg="white").place(x=330,y=120)
                                                    text_chkinday = Label(book3processframe,text="Check in date : %s %s"%(in_day_spy.get(),in_month_spy.get()),bg="#21253E",fg="white").place(x=160,y=180)
                                                    text_chkoutday = Label(book3processframe,text="Check out date : %s %s"%(out_day_spy.get(),out_month_spy.get()),bg="#21253E",fg="white").place(x=160,y=240)
                                                    text_roomtype = Label(book3processframe,text="Room Type : %s"%(roomt_spy.get()),bg="#21253E",fg="white").place(x=160,y=300)
                                                    totalprice = 0
                                                    if roomt_spy.get() == "Normal Bedroom,1 bed" :
                                                        totalprice = 2000
                                                    elif roomt_spy.get() == "Normal Bedroom,2 bed" :
                                                        totalprice = 3000
                                                    elif roomt_spy.get() == "Premium Bedroom" :
                                                        totalprice = 4000
                                                    elif roomt_spy.get() == "Executive Room" :
                                                        totalprice = 5000
                                                    # "January","February","March","April","May","June","July","August","September","October","November","December"
                                                    in_monthindex = 0
                                                    if in_month_spy.get() == "January" :
                                                        in_monthindex = 1
                                                    elif in_month_spy.get() == "February" :
                                                        in_monthindex = 2
                                                    elif in_month_spy.get() == "March" :
                                                        in_monthindex = 3
                                                    elif in_month_spy.get() == "April" :
                                                        in_monthindex = 4
                                                    elif in_month_spy.get() == "May" :
                                                        in_monthindex = 5
                                                    elif in_month_spy.get() == "June" :
                                                        in_monthindex = 6
                                                    elif in_month_spy.get() == "July" :
                                                        in_monthindex = 7
                                                    elif in_month_spy.get() == "August" :
                                                        in_monthindex = 8
                                                    elif in_month_spy.get() == "September" :
                                                        in_monthindex = 9
                                                    elif in_month_spy.get() == "October" :
                                                        in_monthindex = 10
                                                    elif in_month_spy.get() == "November" :
                                                        in_monthindex = 11
                                                    elif in_month_spy.get() == "December" :
                                                        in_monthindex = 12
                                                    #
                                                    out_monthindex = 0
                                                    if out_month_spy.get() == "January" :
                                                        out_monthindex = 1
                                                    elif out_month_spy.get() == "February" :
                                                        out_monthindex = 2
                                                    elif out_month_spy.get() == "March" :
                                                        out_monthindex = 3
                                                    elif out_month_spy.get() == "April" :
                                                        out_monthindex = 4
                                                    elif out_month_spy.get() == "May" :
                                                        out_monthindex = 5
                                                    elif out_month_spy.get() == "June" :
                                                        out_monthindex = 6
                                                    elif out_month_spy.get() == "July" :
                                                        out_monthindex = 7
                                                    elif out_month_spy.get() == "August" :
                                                        out_monthindex = 8
                                                    elif out_month_spy.get() == "September" :
                                                        out_monthindex = 9
                                                    elif out_month_spy.get() == "October" :
                                                        out_monthindex = 10
                                                    elif out_month_spy.get() == "November" :
                                                        out_monthindex = 11
                                                    elif out_month_spy.get() == "December" :
                                                        out_monthindex = 12
                                                    timetype_datein = time.datetime(2020, int(in_monthindex), int(in_day_spy.get()))
                                                    timetype_dateout = time.datetime(2020, int(out_monthindex), int(out_day_spy.get()))
                                                    timetype_diff = (str(timetype_dateout-timetype_datein)[0:2])
                                                    conn = sqlite3.connect("projectdb.db")
                                                    cursor = conn.cursor()
                                                    sql = """
                                                            SELECT * FROM customer_information
                                                            WHERE id_customer=? """
                                                    cursor.execute(sql,[userid_spy.get()])
                                                    result = cursor.fetchone()
                                                    alltotalprice = (totalprice*int(timetype_diff))//1
                                                    text_roomprice = Label(book3processframe,text="Room price : %s"%(totalprice),bg="#21253E",fg="white").place(x=160,y=360)
                                                    text_total = Label(book3processframe,text="Total : %s Baht"%(alltotalprice),bg="#21253E",fg="white").place(x=330,y=440)
                                                    if float(result[7]) >= alltotalprice :
                                                        but_payment = Button(book3processframe,image=hotel_paymnet,bg="#21253E",border=0,activebackground="#21253E",command=lambda:finishprocess(float(result[7]),alltotalprice))
                                                        but_payment.place(x=280,y=540)
                                                    else :
                                                        text = Label(book3processframe,text="Not enough money in your Wallet\nPlease top up before booking",bg="#21253E",fg="white")
                                                        text.place(x=280,y=490)
                                                else :
                                                    messagebox.showwarning("Admin","Please enter room type")
                                            else :
                                                messagebox.showwarning("Admin","Please enter number of guest")
                                        else :
                                            messagebox.showwarning("Admin","Please enter Check-out month") 
                                    else :
                                        messagebox.showwarning("Admin","Please enter Check-out day")   
                                else :
                                    messagebox.showwarning("Admin","Please enter month")
                            else :
                                messagebox.showwarning("Admin","Please enter Check-in day")
                        global hotel3porcess_frame
                        hotel3porcess_frame = Frame(hotel3_frame,bg="#21253E")
                        hotel3porcess_frame.place(x=0,y=0,width=w-100,height=h)
                        bg = Label(hotel3porcess_frame,image=hotel_3_bg)
                        bg.place(x=0,y=0)
                        bg_1 = Label(hotel3porcess_frame,bg="#21253E")
                        bg_1.place(x=100,y=100,height=h-200,width=w-330)
                        in_day_spy = StringVar()
                        in_month_spy = StringVar()
                        out_day_spy = StringVar()
                        out_month_spy = StringVar()
                        adult_spy = StringVar()
                        roomt_spy = StringVar()
                        #
                        back_but = Button(hotel3porcess_frame,text="< Back",border=0,bg="#15345F",fg="white",command=hotel3processback,activebackground="#15345F",activeforeground="white")
                        back_but.place(x=10,y=10)
                        text_date = Label(hotel3porcess_frame,text="Date",font='Calibri 20 bold',bg="#21253E",fg="white")
                        text_date.place(x=120,y=110)
                        text_day = Label(hotel3porcess_frame,text="Check-in Day",bg="#21253E",fg="white")
                        text_day.place(x=120,y=160)
                        text_month = Label(hotel3porcess_frame,text="Month",bg="#21253E",fg="white")
                        text_month.place(x=450,y=160)
                        text_month = Label(hotel3porcess_frame,text="Month",bg="#21253E",fg="white")
                        text_month.place(x=450,y=260)
                        text_how = Label(hotel3porcess_frame,text="Check-out day",bg="#21253E",fg="white")
                        text_how.place(x=120,y=260)
                        day = [i for i in range(1,32)]
                        month = ["January","February","March","April","May","June","July","August","September","October","November","December"]
                        spinbox_day = ttk.Combobox(hotel3porcess_frame,values=day,textvariable=in_day_spy)
                        spinbox_day.place(x=120,y=210)
                        spinbox_month = ttk.Combobox(hotel3porcess_frame,values=month,textvariable=in_month_spy)
                        spinbox_month.place(x=450,y=210)
                        spinbox_how = ttk.Combobox(hotel3porcess_frame,values=day,textvariable=out_day_spy)
                        spinbox_how.place(x=120,y=310)
                        spinbox_month = ttk.Combobox(hotel3porcess_frame,values=month,textvariable=out_month_spy)
                        spinbox_month.place(x=450,y=310)
                        #
                        adult = [i for i in range(1,6)]
                        room_type = ["Normal Bedroom,1 bed","Normal Bedroom,2 bed","Premium Bedroom","Executive Room"]
                        text_room = Label(hotel3porcess_frame,text="Room",font='Calibri 20 bold',bg="#21253E",fg="white")
                        text_room.place(x=120,y=360)
                        text_people = Label(hotel3porcess_frame,text="Number of guest",bg="#21253E",fg="white")
                        text_people.place(x=120,y=410)
                        text_room = Label(hotel3porcess_frame,text="Room type",bg="#21253E",fg="white")
                        text_room.place(x=450,y=410)
                        spinbox_adult = ttk.Combobox(hotel3porcess_frame,values=adult,textvariable=adult_spy)
                        spinbox_adult.place(x=120,y=460)
                        spinbox_room = ttk.Combobox(hotel3porcess_frame,values=room_type,textvariable=roomt_spy)
                        spinbox_room.place(x=450,y=460)
                        #
                        but_con = Button(hotel3porcess_frame,image=hotel_confirm,bg="#21253E",border=0,activebackground="#21253E",command=bookprocess)
                        but_con.place(x=280,y=530)
                    def hotel1page() :
                        global hotel1_frame
                        hotel1_frame = Frame(frame_home,bg="#21253E")
                        hotel1_frame.place(x=0,y=0,width=w-100,height=h)
                        #
                        back_but = Button(hotel1_frame,text="< Back",border=0,bg="#21253E",fg="white",command=backfromhotel1,activebackground="#21253E",activeforeground="white")
                        back_but.place(x=10,y=10)
                        shopinfo = Label(hotel1_frame,image=hotel_1_info,bg="#21253E")
                        shopinfo.place(x=-7,y=70)
                        text_shopname = Label(hotel1_frame,text="Bangkok Marriott Hotel The Surawongse - SHA Extra Plus",bg="#21253E",fg="white")
                        text_shopname.place(x=20,y=490)
                        but_book = Button(hotel1_frame,image=bookhotel,border=0,bg="#21253E",activebackground="#21253E",command=hotel1porcess)
                        but_book.place(x=560,y=600)
                        #
                        def chkbooking1() :     
                            chkbook_frame = Frame(hotel1_frame,bg="#21253E")
                            chkbook_frame.place(x=0,y=470,width=w,height=h-470)
                            text_chkbook = Label(hotel1_frame,text="Your reserved",bg="#21253E",fg="white")
                            text_chkbook.place(x=20,y=490)
                            #Create Treeview
                            mytree = ttk.Treeview(hotel1_frame, columns=("day", "mth", "nm", "rm"), height=2)
                            #create headings
                            mytree.heading('#0', text='') #default
                            mytree.heading('day', text="Check-in", anchor=CENTER)
                            mytree.heading('mth', text="Check-out", anchor=CENTER)
                            mytree.heading('nm', text="Name", anchor=CENTER)
                            mytree.heading('rm', text="Room", anchor=CENTER)
                            #format columns
                            mytree.column("#0", width=0, minwidth=0)
                            mytree.column('day', anchor=CENTER, width=220)
                            mytree.column('mth', anchor=CENTER, width=220)
                            mytree.column('nm', anchor=CENTER, width=220)
                            mytree.column('rm', anchor=CENTER, width=220)
                            mytree.place(x=0,y=540,width=w-100,height=160)
                            sql = """
                                    SELECT * FROM hotel_1
                                    WHERE Name=? """
                            cursor.execute(sql,[userfname_spy.get()])
                            result_hotel = cursor.fetchall()
                            if result_hotel:
                                for i,data in enumerate(result_hotel) :
                                    mytree.insert('','end',values=(data[0],data[1],data[2],data[3]))
                        hotel_chkbook = Button(hotel1_frame,image=hotel_checkbook,border=0,bg="#21253E",activebackground="#21253E",command=chkbooking1)
                        hotel_chkbook.place(x=320,y=600)
                    def hotel2page() :
                        global hotel2_frame
                        hotel2_frame = Frame(frame_home,bg="#21253E")
                        hotel2_frame.place(x=0,y=0,width=w-100,height=h)
                        #
                        back_but = Button(hotel2_frame,text="< Back",border=0,bg="#21253E",fg="white",command=backfromhotel2,activebackground="#21253E",activeforeground="white")
                        back_but.place(x=10,y=10)
                        shopinfo = Label(hotel2_frame,image=hotel_2_info,bg="#21253E")
                        shopinfo.place(x=-7,y=70)
                        text_shopname = Label(hotel2_frame,text="Eastin Grand Hotel Sathorn - SHA Extra Plus",bg="#21253E",fg="white")
                        text_shopname.place(x=20,y=490)
                        but_book = Button(hotel2_frame,image=bookhotel,border=0,bg="#21253E",activebackground="#21253E",command=hotel2porcess)
                        but_book.place(x=560,y=600)
                        #
                        def chkbooking2() :
                            chkbook_frame = Frame(hotel2_frame,bg="#21253E")
                            chkbook_frame.place(x=0,y=470,width=w,height=h-470)
                            text_chkbook = Label(hotel2_frame,text="Your reserved",bg="#21253E",fg="white")
                            text_chkbook.place(x=20,y=490)
                            #Create Treeview
                            mytree = ttk.Treeview(hotel2_frame, columns=("day", "mth", "nm", "rm"), height=2)
                            #create headings
                            mytree.heading('#0', text='') #default
                            mytree.heading('day', text="Check-in", anchor=CENTER)
                            mytree.heading('mth', text="Check-out", anchor=CENTER)
                            mytree.heading('nm', text="Name", anchor=CENTER)
                            mytree.heading('rm', text="Room", anchor=CENTER)
                            #format columns
                            mytree.column("#0", width=0, minwidth=0)
                            mytree.column('day', anchor=CENTER, width=220)
                            mytree.column('mth', anchor=CENTER, width=220)
                            mytree.column('nm', anchor=CENTER, width=220)
                            mytree.column('rm', anchor=CENTER, width=220)
                            mytree.place(x=0,y=540,width=w-100,height=160)
                            sql = """
                                    SELECT * FROM hotel_2
                                    WHERE Name=? """
                            cursor.execute(sql,[userfname_spy.get()])
                            result_hotel = cursor.fetchall()
                            if result_hotel:
                                for i,data in enumerate(result_hotel) :
                                    mytree.insert('','end',values=(data[0],data[1],data[2],data[3]))
                        hotel_chkbook = Button(hotel2_frame,image=hotel_checkbook,border=0,bg="#21253E",activebackground="#21253E",command=chkbooking2)
                        hotel_chkbook.place(x=320,y=600)
                    def hotel3page() :
                        global hotel3_frame
                        hotel3_frame = Frame(frame_home,bg="#21253E")
                        hotel3_frame.place(x=0,y=0,width=w-100,height=h)
                        #
                        back_but = Button(hotel3_frame,text="< Back",border=0,bg="#21253E",fg="white",command=backfromhotel3,activebackground="#21253E",activeforeground="white")
                        back_but.place(x=10,y=10)
                        shopinfo = Label(hotel3_frame,image=hotel_3_info,bg="#21253E")
                        shopinfo.place(x=-7,y=70)
                        text_shopname = Label(hotel3_frame,text="Sindhorn Midtown, an IHG Hotel - SHA Extra Plus",bg="#21253E",fg="white")
                        text_shopname.place(x=20,y=490)
                        but_book = Button(hotel3_frame,image=bookhotel,border=0,bg="#21253E",activebackground="#21253E",command=hotel3porcess)
                        but_book.place(x=560,y=600)
                        #
                        def chkbooking3() :
                            chkbook_frame = Frame(hotel3_frame,bg="#21253E")
                            chkbook_frame.place(x=0,y=470,width=w,height=h-470)
                            text_chkbook = Label(hotel3_frame,text="Your reserved",bg="#21253E",fg="white")
                            text_chkbook.place(x=20,y=490)
                            #Create Treeview
                            mytree = ttk.Treeview(hotel3_frame, columns=("day", "mth", "nm", "rm"), height=2)
                            #create headings
                            mytree.heading('#0', text='') #default
                            mytree.heading('day', text="Check-in", anchor=CENTER)
                            mytree.heading('mth', text="Check-out", anchor=CENTER)
                            mytree.heading('nm', text="Name", anchor=CENTER)
                            mytree.heading('rm', text="Room", anchor=CENTER)
                            #format columns
                            mytree.column("#0", width=0, minwidth=0)
                            mytree.column('day', anchor=CENTER, width=220)
                            mytree.column('mth', anchor=CENTER, width=220)
                            mytree.column('nm', anchor=CENTER, width=220)
                            mytree.column('rm', anchor=CENTER, width=220)
                            mytree.place(x=0,y=540,width=w-100,height=160)
                            sql = """
                                    SELECT * FROM hotel_3
                                    WHERE Name=? """
                            cursor.execute(sql,[userfname_spy.get()])
                            result_hotel = cursor.fetchall()
                            if result_hotel:
                                for i,data in enumerate(result_hotel) :
                                    mytree.insert('','end',values=(data[0],data[1],data[2],data[3]))
                        hotel_chkbook = Button(hotel3_frame,image=hotel_checkbook,border=0,bg="#21253E",activebackground="#21253E",command=chkbooking3)
                        hotel_chkbook.place(x=320,y=600)
                    # Spy
                    where_spy = StringVar()
                    num_spy = StringVar()
                    where_spy.set("Where  ")
                    num_spy.set("-")
                    #
                    Label(all_hotel,image=hotel_frame,bg="#21253E").place(x=-5,y=0)
                    def hotel_w(e) :
                        # where
                        if where_spy.get() == "Where  " :
                            hotel_where["fg"] == "black"
                            where_spy.set("")
                        if num_spy.get() == "" :
                            num_spy.set("-")
                    def hotel_n(e) :
                        # number
                        if num_spy.get() == "-" :
                            num_spy.set("")
                            hotel_num["fg"] == "black"
                        if where_spy.get() == "" :
                            where_spy.set("Where  ")
                    def quitfromsearch() :
                        where_spy.set("Where  ")
                        num_spy.set("-")
                        searchhotel_home.destroy()
                    def searchhotel() :
                        if where_spy.get() != "Where  " and where_spy.get() != "" :
                            if num_spy.get() != "-" and num_spy.get() != "":
                                chknumisrealnum = num_spy.get().isnumeric()
                                if chknumisrealnum == True :
                                    global searchhotel_home
                                    if where_spy.get().upper() == "BANGKOK" :
                                        searchhotel_home = Frame(all_hotel,bg="#21253E")
                                        searchhotel_home.place(x=0,y=0,width=w,height=h)
                                        #
                                        hotel_shop_1 = Button(searchhotel_home,image=hotel_shop1,bg="#21253E",border=0,activebackground="#21253E",command=hotel1page).place(x=8,y=100)
                                        hotel_shop_2 = Button(searchhotel_home,image=hotel_shop2,bg="#21253E",border=0,activebackground="#21253E",command=hotel2page).place(x=306,y=100)
                                        hotel_shop_3 = Button(searchhotel_home,image=hotel_shop3,bg="#21253E",border=0,activebackground="#21253E",command=hotel3page).place(x=604,y=100)
                                        #
                                        back_but = Button(searchhotel_home,text="< Back",bg="#21253E",fg="white",activebackground="#21253E",command=quitfromsearch,border=0)
                                        back_but.place(x=20,y=20)
                                    elif where_spy.get().upper() == "SILOM" :
                                        searchhotel_home = Frame(all_hotel,bg="#21253E")
                                        searchhotel_home.place(x=0,y=0,width=w,height=h)
                                        #
                                        hotel_shop_1 = Button(searchhotel_home,image=hotel_shop1,bg="#21253E",border=0,activebackground="#21253E",command=hotel1page).place(x=8,y=100)
                                        #
                                        back_but = Button(searchhotel_home,text="< Back",bg="#21253E",fg="white",activebackground="#21253E",command=quitfromsearch,border=0)
                                        back_but.place(x=20,y=20)
                                    elif where_spy.get().upper() == "SATHORN" :
                                        searchhotel_home = Frame(all_hotel,bg="#21253E")
                                        searchhotel_home.place(x=0,y=0,width=w,height=h)
                                        #
                                        hotel_shop_2 = Button(searchhotel_home,image=hotel_shop2,bg="#21253E",border=0,activebackground="#21253E",command=hotel2page).place(x=8,y=100)
                                        #
                                        back_but = Button(searchhotel_home,text="< Back",bg="#21253E",fg="white",activebackground="#21253E",command=quitfromsearch,border=0)
                                        back_but.place(x=20,y=20)

                                    elif where_spy.get().upper() == "SIAM" :
                                        searchhotel_home = Frame(all_hotel,bg="#21253E")
                                        searchhotel_home.place(x=0,y=0,width=w,height=h)
                                        hotel_shop_3 = Button(searchhotel_home,image=hotel_shop3,bg="#21253E",border=0,activebackground="#21253E",command=hotel3page).place(x=8,y=100)
                                        #
                                        back_but = Button(searchhotel_home,text="< Back",bg="#21253E",fg="white",activebackground="#21253E",command=quitfromsearch,border=0)
                                        back_but.place(x=20,y=20)
                                else :
                                    messagebox.showwarning("Admin","Please enter number only")
                            else :
                                messagebox.showwarning("Admin","Please enter number of guests")
                        else :
                            messagebox.showwarning("Admin","Please enter Place")
                    def chkbooking() :
                        chkbooking_frame = Frame(all_hotel,bg="#21253E")
                        chkbooking_frame.place(x=0,y=310,width=w-100,height=h-310)
                        #
                        text_chk = Label(chkbooking_frame,text="Your reserved",bg="#21253E").place(x=20,y=20)
                        
                    # widget
                    hotel_where = Entry(all_hotel,width=10,bg="#FBE5E5",border=0,textvariable=where_spy,fg="#AEA8A8")
                    hotel_where.place(x=420,y=239)
                    hotel_num = Entry(all_hotel,width=6,bg="#FBE5E5",border=0,textvariable=num_spy,fg="#AEA8A8")
                    hotel_num.place(x=660,y=239)
                    hotel_search_but = Button(all_hotel,image=hotel_search,border=0,bg="#C1A0A0",activebackground="#C1A0A0",command=searchhotel)
                    hotel_search_but.place(x=791,y=238)
                    # bind
                    hotel_where.bind("<Button-1>",hotel_w)
                    hotel_num.bind("<Button-1>",hotel_n)
                    #
                    text_image = Label(all_hotel,image=hotel_text_1,bg="#21253E")
                    text_image.place(x=40,y=330)
                    hotel_shop_1 = Button(all_hotel,image=hotel_shop1,bg="#21253E",border=0,activebackground="#21253E",command=hotel1page).place(x=8,y=380)
                    hotel_shop_2 = Button(all_hotel,image=hotel_shop2,bg="#21253E",border=0,activebackground="#21253E",command=hotel2page).place(x=306,y=380)
                    hotel_shop_3 = Button(all_hotel,image=hotel_shop3,bg="#21253E",border=0,activebackground="#21253E",command=hotel3page).place(x=604,y=380)
                def category_dessert() : # Dessert
                    all_dessert = Frame(frame_home,bg="#F8EFE0")
                    all_dessert.place(x=0,y=100,width=w-100,height=h-100)
                    #
                    def favoritedes(shopname) :
                        sql = """
                                    UPDATE customer_information
                                    SET fav_shop=? 
                                    WHERE id_customer=? """
                        cursor.execute(sql,[shopname,userid_spy.get()])
                        conn.commit()
                        customermainpage(id)
                    # shop 1
                    Button(all_dessert,image=frameshop_aty,border=0,bg="#F8EFE0",activebackground="#F8EFE0",command=shop1).place(x=30,y=20)
                    if fav_spy.get() == "aty" :
                        favsr1 = Button(all_dessert,image=addtofav_act,border=0,bg="white",command=lambda:favoritedes("aty") )
                        favsr1.place(x=240,y=175)
                    else :
                        favsr1 = Button(all_dessert,image=addtofav_not,border=0,bg="white",command=lambda:favoritedes("aty") )
                        favsr1.place(x=240,y=175)
                    # shop 2
                    Button(all_dessert,image=frameshop_kyo,border=0,bg="#F8EFE0",activebackground="#F8EFE0",command=shop3).place(x=320,y=20)
                    if fav_spy.get() == "kyo" :
                        favsr2 = Button(all_dessert,image=addtofav_act,border=0,bg="white",command=lambda:favoritedes("kyo") )
                        favsr2.place(x=530,y=175)
                    else :
                        favsr2 = Button(all_dessert,image=addtofav_not,border=0,bg="white",command=lambda:favoritedes("kyo") )
                        favsr2.place(x=530,y=175)
                    # shop 3
                    Button(all_dessert,image=frameshop_code,border=0,bg="#F8EFE0",activebackground="#F8EFE0",command=shop4).place(x=610,y=20)
                    if fav_spy.get() == "code" :
                        favsr3 = Button(all_dessert,image=addtofav_act,border=0,bg="white",command=lambda:favoritedes("code") )
                        favsr3.place(x=820,y=175)
                    else :
                        favsr3 = Button(all_dessert,image=addtofav_not,border=0,bg="white",command=lambda:favoritedes("code") )
                        favsr3.place(x=820,y=175)
                    # shop 4
                    Button(all_dessert,image=frameshop_aty,border=0,bg="#F8EFE0",activebackground="#F8EFE0")#.place(x=30,y=310)
                    # shop 5
                    Button(all_dessert,image=frameshop_aty,border=0,bg="#F8EFE0",activebackground="#F8EFE0")#.place(x=320,y=310)
                    # shop 6
                    Button(all_dessert,image=frameshop_aty,border=0,bg="#F8EFE0",activebackground="#F8EFE0")#.place(x=610,y=310)
                # Shop
                def shop1() : # AFTERYOU
                    whatqueue.set("AFTERYOU")
                    queue_frame()
                def shop2() : # YAYOI
                    whatqueue.set("YAYOI")
                    queue_frame()
                def shop3() : # KYO
                    whatqueue.set("KYO")
                    queue_frame()
                def shop4() : # CODE
                    whatqueue.set("CODE")
                    queue_frame()
                def shop5() : # SHIN
                    whatqueue.set("SHIN")
                    queue_frame()
                def shop6() : # OHK
                    whatqueue.set("OHK")
                    queue_frame()
                # Search
                def searchprocess() :
                    if entry_search.get().upper() == "AFTERYOU" or entry_search.get().upper() == "CODE" or entry_search.get().upper() == "KYO" or entry_search.get().upper() == "OHKAJU" or entry_search.get().upper() == "SHINKANZEN" or entry_search.get().upper() == "YAYOI" or entry_search.get().upper() == "YYI" or entry_search.get().upper() == "SHIN" or entry_search.get().upper() == "OH KA JU" or entry_search.get().upper() == "OKJ" or entry_search.get().upper() == "AFTER YOU" or entry_search.get().upper() == "ATY" or entry_search.get().upper() == "KYO ROLL EN" or entry_search.get().upper() == "KYO ROLL" or entry_search.get().upper() == "KYOROLLEN":
                        search_home = Frame(root,bg="#F8EFE0")
                        search_home.place(x=100,y=0,width=w-100,height=h)
                        # Button(favshop_home,image=frameshop_yyo,border=0,bg="#F8EFE0",activebackground="#F8EFE0",command=shop2).place(x=30,y=20)
                        if entry_search.get().upper() == "YAYOI" or entry_search.get().upper() == "YYI":
                            Button(search_home,image=frameshop_yyo,border=0,bg="#F8EFE0",activebackground="#F8EFE0",command=shop2).place(x=30,y=20)
                        elif entry_search.get().upper() == "SHINKANZEN" or entry_search.get().upper() == "SHIN" :
                            Button(search_home,image=frameshop_shin,border=0,bg="#F8EFE0",activebackground="#F8EFE0",command=shop5).place(x=30,y=20)
                        elif entry_search.get().upper() == "OHKAJU" or entry_search.get().upper() == "OH KA JU" or entry_search.get().upper() == "OKJ":
                            Button(search_home,image=frameshop_okj,border=0,bg="#F8EFE0",activebackground="#F8EFE0",command=shop6).place(x=30,y=20)
                        elif entry_search.get().upper() == "AFTERYOU" or entry_search.get().upper() == "AFTER YOU" or entry_search.get().upper() == "ATY":
                            Button(search_home,image=frameshop_aty,border=0,bg="#F8EFE0",activebackground="#F8EFE0",command=shop1).place(x=30,y=20)
                        elif entry_search.get().upper() == "CODE" :
                            Button(search_home,image=frameshop_code,border=0,bg="#F8EFE0",activebackground="#F8EFE0",command=shop4).place(x=30,y=20)
                        elif entry_search.get().upper() == "KYO" or entry_search.get().upper() == "KYO ROLL EN" or entry_search.get().upper() == "KYO ROLL" or entry_search.get().upper() == "KYOROLLEN":
                            Button(search_home,image=frameshop_kyo,border=0,bg="#F8EFE0",activebackground="#F8EFE0",command=shop3).place(x=30,y=20)
                    else :
                        customermainpage(id)
                search_spy = StringVar()
                search_spy.set("Search Restaurant  ")
                #
                frame_home = Frame(root,bg="#F8EFE0")
                frame_home.place(x=100,y=0,width=w-100,height=h)
                #
                Label(frame_home,bg="#F8EFE0").place(x=0,y=0,width=w,height=90)
                #
                entry_searchphoto1 = Label(frame_home,image=searchbar1,bg="#F8EFE0")
                entry_searchphoto1.place(x=20,y=30)
                entry_searchphoto2 = Label(frame_home,image=searchbar2,bg="#F9E9C1")
                entry_searchphoto2.place(x=30,y=44)
                def searchclick(e) :
                    if search_spy.get() == "Search Restaurant  " :
                        search_spy.set("")
                        entry_search["fg"] = "black"
                entry_search = Entry(frame_home,width=30,border=0,bg="#F9E9C1",textvariable=search_spy,fg="gray")
                entry_search.place(x=70,y=38)
                entry_search.bind("<Button-1>",searchclick)
                button_search = Button(frame_home,image=picbutton_search,border=0,bg="#F8EFE0",activebackground="#F8EFE0",command=searchprocess)
                button_search.place(x=530,y=30)
                #
                if usergender_spy.get() == "Male" or usergender_spy.get() == "Other" :
                    text_gender = Label(frame_home,image=boy_image,bg="#F8EFE0")
                elif usergender_spy.get() == "Female" :
                    text_gender = Label(frame_home,image=girl_image,bg="#F8EFE0")
                text_gender.place(x=640,y=30)
                label_hello = Label(frame_home,text="Hello %s"%(userfname_spy.get()[0:8]),bg="#F8EFE0",font="Calibri 18 bold")
                label_hello.place(x=700,y=40)
                #
                label_category = Label(frame_home,image=text_cate,bg="#F8EFE0")
                label_category.place(x=35,y=105)
                #
                button_hotel = Button(frame_home,text="Hotel",justify="center",border=2,command=category_hotel,image=photobutton_hotel,bg="#F8EFE0",borderwidth=0,activebackground="#F8EFE0")
                button_hotel.place(x=30,y=140,width=400,height=210)
                #
                button_restaurant = Button(frame_home,text="Restaurant",justify="center",border=2,command=category_restaurant,image=photobutton_resta,bg="#F8EFE0",borderwidth=0,activebackground="#F8EFE0")
                button_restaurant.place(x=450,y=150,width=400,height=100)
                #
                button_dessert = Button(frame_home,text="Dessert",justify="center",border=2,command=category_dessert,image=photobutton_dessert,bg="#F8EFE0",borderwidth=0,activebackground="#F8EFE0")
                button_dessert.place(x=450,y=240,width=400,height=100)
                #
                label_suggest = Label(frame_home,text="Suggest for you",image=text_sugg,bg="#F8EFE0")
                label_suggest.place(x=35,y=350)
                #
                show_shop1 = Button(frame_home,image=frameshop_shin,border=0,activebackground="#F8EFE0",command=shop5,bg="#F8EFE0")
                show_shop1.place(x=30,y=400)
                def favorite(shopname) :
                    sql = """
                                UPDATE customer_information
                                SET fav_shop=? 
                                WHERE id_customer=? """
                    cursor.execute(sql,[shopname,userid_spy.get()])
                    conn.commit()
                    customermainpage(id)
                if fav_spy.get() == "shin" :
                    favs1 = Button(frame_home,image=addtofav_act,border=0,bg="white",command= lambda:favorite("shin") )
                    favs1.place(x=240,y=555)
                else :
                    favs1 = Button(frame_home,image=addtofav_not,border=0,bg="white",command= lambda:favorite("shin") )
                    favs1.place(x=240,y=555)
                show_shop2 = Button(frame_home,image=frameshop_yyo,border=0,activebackground="#F8EFE0",command=shop2,bg="#F8EFE0")
                show_shop2.place(x=315,y=400)
                if fav_spy.get() == "yyo" :
                    favs2 = Button(frame_home,image=addtofav_act,border=0,bg="white",command= lambda:favorite("yyo") )
                    favs2.place(x=525,y=555)
                else :
                    favs2 = Button(frame_home,image=addtofav_not,border=0,bg="white",command= lambda:favorite("yyo") )
                    favs2.place(x=525,y=555)
                show_shop3 = Button(frame_home,image=frameshop_kyo,border=0,activebackground="#F8EFE0",command=shop3,bg="#F8EFE0")
                show_shop3.place(x=600,y=400)
                if fav_spy.get() == "kyo" :
                    favs3 = Button(frame_home,image=addtofav_act,border=0,bg="white",command= lambda:favorite("kyo") )
                    favs3.place(x=815,y=555)
                else :
                    favs3 = Button(frame_home,image=addtofav_not,border=0,bg="white",command= lambda:favorite("kyo") )
                    favs3.place(x=815,y=555)
            def account_frame() :
                # button_wallet_activate
                home_button["image"] = button_home_not
                account_button["image"] = button_wallet_activate
                q_button["image"] = button_q_not
                favshop_button["image"] = button_fav_not
                #
                global account_home , label_fnamelanme_account
                account_home = Frame(root,bg="#F8EFE0")
                account_home.place(x=100,y=0,width=w-100,height=h)
                # database
                conn = sqlite3.connect("projectdb.db")
                cursor = conn.cursor()
                sql = """
                        SELECT * FROM customer_information 
                        WHERE id_customer=? """
                cursor.execute(sql,[id])
                result = cursor.fetchone()
                # widget
                bg_1 = Label(account_home,bg="#FFF4D7").place(x=20,y=20,width=500,height=500)
                bg_2 = Label(account_home,bg="#F3F3F3").place(x=540,y=20,width=340,height=500)
                # bg_1
                label_info_account = Label(account_home,text="Information",font='Candara 20 bold',bg="#FFF4D7")
                label_info_account.place(x=30,y=30)
                #
                label_name_account = Label(account_home,text="Name :",bg="#FFF4D7")
                label_name_account.place(x=30,y=120)
                user_name = userfname_spy.get()+" "+userlname_spy.get() # name
                label_fnamelanme_account = Label(account_home,text=user_name,bg="#FFF4D7")
                label_fnamelanme_account.place(x=140,y=120)
                # bg_1
                label_tel_account = Label(account_home,text="Telephone :",bg="#FFF4D7")
                label_tel_account.place(x=30,y=170)
                label_infotel_account = Label(account_home,text=usertel_spy.get(),bg="#FFF4D7")
                label_infotel_account.place(x=190,y=170)
                # bg_1
                label_gender_account = Label(account_home,text="Gender :",bg="#FFF4D7")
                label_gender_account.place(x=30,y=220)
                label_infogender_account = Label(account_home,text=usergender_spy.get(),bg="#FFF4D7")
                label_infogender_account.place(x=150,y=220)
                # bg_2
                label_member_account = Label(account_home,text="Member level :",bg="#F3F3F3")
                label_member_account.place(x=550,y=220)
                label_infomember_account = Label(account_home,text=member_spy.get(),bg="#F3F3F3")
                label_infomember_account.place(x=740,y=220)
                # bg_1
                button_manage_account = Button(account_home, text="Manage Account" ,image=button_manage, border=0, bg="#F8EFE0",command= lambda: manageaccountprocess(userid_spy.get()),activebackground="#F8EFE0",activeforeground="#F8EFE0") # manage account
                button_manage_account.place(x=30,y=455)
                # bg_1
                button_cpass_account = Button(account_home, text="Change password" ,image=button_change, border=0, bg="#F8EFE0",command= lambda: managecpassprocess(userid_spy.get()),activebackground="#F8EFE0",activeforeground="#F8EFE0") # manage password
                button_cpass_account.place(x=250,y=455)
                # bg_2
                label_wallet_account = Label(account_home,text="Wallet",font='Candara 20 bold',bg="#F3F3F3")
                label_wallet_account.place(x=550,y=30)
                # bg_2
                label_money_account = Label(account_home,text="Balance :",bg="#F3F3F3")
                label_money_account.place(x=550,y=120)
                label_infomoney_account = Label(account_home,text=money_spy.get(),bg="#F3F3F3")
                label_infomoney_account.place(x=660,y=120)
                # bg_2
                label_point_account = Label(account_home,text="Point :",bg="#F3F3F3")
                label_point_account.place(x=550,y=170)
                label_infopoint_account = Label(account_home,text="%0.f"%float(point_spy.get()),bg="#F3F3F3")
                label_infopoint_account.place(x=660,y=170)
                # bg_2
                button_topup_account = Button(account_home, text=" Top up & Point " ,image=button_topup, border=0,bg="#F3F3F3", fg="black",command= lambda: topupprocess(userid_spy.get()),activebackground="#F3F3F3",activeforeground="black") # manage account
                button_topup_account.place(x=550,y=455)
            def queue_frame() :
                #
                if whatqueue.get() == "empty" :
                    home_button["image"] = button_home_not
                    account_button["image"] = button_wallet_not
                    q_button["image"] = button_q_activate
                    favshop_button["image"] = button_fav_not
                    wallet_home = Frame(root,bg="#F8EFE0")
                    wallet_home.place(x=100,y=0,width=w-100,height=h)
                elif whatqueue.get() == "YAYOI" :
                    def checkamt() :
                        if combo_amount.get() == "-" or  combo_amount.get() == "" :
                            messagebox.showwarning("Admin","Please enter number of guest")
                        elif combo_amount.get() == "1-2" or combo_amount.get() == "3-4" or combo_amount.get() == "5-6" :
                            def waitingyayoi() :
                                def Refreshpage() :
                                    conn = sqlite3.connect("projectdb.db")
                                    cursor = conn.cursor()
                                    sql = """
                                            SELECT * FROM shop_yayoi_queue WHERE q_name=? """
                                    cursor.execute(sql,[userfname_spy.get()])
                                    result = cursor.fetchone()
                                    sql = """
                                            SELECT * FROM shop_yayoi_table
                                            WHERE name=? """
                                    cursor.execute(sql,[userfname_spy.get()])
                                    result_2 = cursor.fetchone()
                                    conn.close()
                                    if result[3] == "wait" :
                                        pass
                                    elif result[3] == "ready" :
                                        yayoi_mainprogram(result_2[0],userfname_spy.get())
                                def cancelq() :
                                    dis = messagebox.askokcancel("Admin","Do you want to Cancel?")
                                    if dis == True :
                                        conn = sqlite3.connect("projectdb.db")
                                        cursor = conn.cursor()
                                        sql = """
                                                DELETE FROM shop_yayoi_queue
                                                WHERE q_name=? """
                                        cursor.execute(sql,[userfname_spy.get()])
                                        conn.commit()
                                        conn.close()
                                        whatqueue.set("empty")
                                        home_frame()
                                    else :
                                        pass
                                conn = sqlite3.connect("projectdb.db")
                                cursor = conn.cursor()
                                if combo_amount.get() == "1-2" :
                                    sql = """
                                                INSERT INTO shop_yayoi_queue (q_name,q_amount,q_status)
                                                values(?,?,?) """
                                    cursor.execute(sql,[userfname_spy.get(),"1-2","wait"])
                                    conn.commit()
                                elif combo_amount.get() == "3-4" :
                                    sql = """
                                                INSERT INTO shop_yayoi_queue (q_name,q_amount,q_status)
                                                values(?,?,?) """
                                    cursor.execute(sql,[userfname_spy.get(),"3-4","wait"])
                                    conn.commit()
                                elif combo_amount.get() == "5-6" :
                                    sql = """
                                                INSERT INTO shop_yayoi_queue (q_name,q_amount,q_status)
                                                values(?,?,?) """
                                    cursor.execute(sql,[userfname_spy.get(),"5-6","wait"])
                                    conn.commit()
                                conn.close()
                                #
                                conn = sqlite3.connect("projectdb.db")
                                cursor = conn.cursor()
                                sql = """
                                        SELECT * FROM shop_yayoi_queue """
                                cursor.execute(sql)
                                result = cursor.fetchall()
                                queuex = 0
                                for i,data in enumerate(result):
                                    queuex = queuex + 1
                                Label(wallet_home,text="Your queue number : %s"%(queuex),font="Calibri 20 bold",bg="#FFA1C9").place(x=60,y=480)
                                Label(wallet_home,text="%s more queue will reach your queue"%(queuex-1),font="Calibri 20",bg="#FFA1C9").place(x=60,y=530)
                                Label(wallet_home,text="Around %s minutes"%(queuex*5),font="Calibri 20",bg="#FFA1C9").place(x=60,y=580)
                                Button(wallet_home,text="Cancel queue",font="Calibri 20 underline",bg="#FFA1C9",border=0,command=cancelq,activebackground="#FFA1C9").place(x=670,y=590)
                                Button(wallet_home,text="Refresh",command=Refreshpage,border=0).place(x=700,y=500)
                                sql = """
                                        SELECT * FROM shop_yayoi_queue WHERE q_name=? """
                                cursor.execute(sql,[userfname_spy.get()])
                                result = cursor.fetchone()
                                conn.close()
                                chkque["state"] = DISABLED
                            waitingyayoi()
                    home_button["image"] = button_home_not
                    account_button["image"] = button_wallet_not
                    q_button["image"] = button_q_activate
                    favshop_button["image"] = button_fav_not
                    wallet_home = Frame(root,bg="#FFDDEB")
                    wallet_home.place(x=100,y=0,width=w-100,height=h)
                    Label(wallet_home,image=queue_yayoi,bg="#FFDDEB").place(x=0,y=-30,w=900,h=395)
                    Label(wallet_home,bg="#FFA1C9").place(x=50,y=380,w=800,h=270)
                    Label(wallet_home,text="Number of customer :",font="Calibri 22",bg="#FFA1C9").place(x=60,y=400)
                    Label(wallet_home,image=amountpeople,bg="#FFA1C9").place(x=330,y=400)
                    amountspy = StringVar()
                    amountlist = ["-","1-2","3-4","5-6"]
                    combo_amount = ttk.Combobox(wallet_home,value=amountlist,textvariable=amountspy)
                    combo_amount.place(x=340,y=405)
                    chkque = Button(wallet_home,image=amountpeople_1,bg="#FFA1C9",border=0,activebackground="#FFA1C9",command=checkamt)
                    chkque.place(x=660,y=400)
                elif whatqueue.get() == "AFTERYOU" :
                    def checkamt() :
                        if combo_amount.get() == "-" or  combo_amount.get() == "" :
                            messagebox.showwarning("Admin","Please enter number of guest")
                        elif combo_amount.get() == "1-2" or combo_amount.get() == "3-4" or combo_amount.get() == "5-6" :
                            def waitingyayoi() :
                                def Refreshpage() :
                                    conn = sqlite3.connect("projectdb.db")
                                    cursor = conn.cursor()
                                    sql = """
                                            SELECT * FROM shop_afteryou_queue WHERE q_name=? """
                                    cursor.execute(sql,[userfname_spy.get()])
                                    result = cursor.fetchone()
                                    sql = """
                                            SELECT * FROM shop_afteryou_table
                                            WHERE name=? """
                                    cursor.execute(sql,[userfname_spy.get()])
                                    result_2 = cursor.fetchone()
                                    conn.close()
                                    if result[3] == "wait" :
                                        pass
                                    elif result[3] == "ready" :
                                        afteryou_mainprogram(result_2[0],userfname_spy.get())
                                def cancelq() :
                                    dis = messagebox.askokcancel("Admin","Do you want to cancel")
                                    if dis == True :
                                        conn = sqlite3.connect("projectdb.db")
                                        cursor = conn.cursor()
                                        sql = """
                                                DELETE FROM shop_afteryou_queue
                                                WHERE q_name=? """
                                        cursor.execute(sql,[userfname_spy.get()])
                                        conn.commit()
                                        conn.close()
                                        whatqueue.set("empty")
                                        home_frame()
                                conn = sqlite3.connect("projectdb.db")
                                cursor = conn.cursor()
                                if combo_amount.get() == "1-2" :
                                    sql = """
                                                INSERT INTO shop_afteryou_queue (q_name,q_amount,q_status)
                                                values(?,?,?) """
                                    cursor.execute(sql,[userfname_spy.get(),"1-2","wait"])
                                    conn.commit()
                                elif combo_amount.get() == "3-4" :
                                    sql = """
                                                INSERT INTO shop_afteryou_queue (q_name,q_amount,q_status)
                                                values(?,?,?) """
                                    cursor.execute(sql,[userfname_spy.get(),"3-4","wait"])
                                    conn.commit()
                                elif combo_amount.get() == "5-6" :
                                    sql = """
                                                INSERT INTO shop_afteryou_queue (q_name,q_amount,q_status)
                                                values(?,?,?) """
                                    cursor.execute(sql,[userfname_spy.get(),"5-6","wait"])
                                    conn.commit()
                                conn.close()
                                #
                                conn = sqlite3.connect("projectdb.db")
                                cursor = conn.cursor()
                                sql = """
                                        SELECT * FROM shop_afteryou_queue """
                                cursor.execute(sql)
                                result = cursor.fetchall()
                                queuex = 0
                                for i,data in enumerate(result):
                                    queuex = queuex + 1
                                Label(wallet_home,text="Your queue number : %s"%(queuex),font="Calibri 20 bold",bg="#F0E0C9").place(x=60,y=480)
                                Label(wallet_home,text="%s more queue will reach your queue"%(queuex-1),font="Calibri 20",bg="#F0E0C9").place(x=60,y=530)
                                Label(wallet_home,text="Around %s minutes"%(queuex*5),font="Calibri 20",bg="#F0E0C9").place(x=60,y=580)
                                Button(wallet_home,text="Cancel queue",font="Calibri 20 underline",bg="#F0E0C9",border=0,command=cancelq,activebackground="#F0E0C9").place(x=670,y=590)
                                Button(wallet_home,text="Refresh",command=Refreshpage,border=0).place(x=700,y=500)
                                sql = """
                                        SELECT * FROM shop_afteryou_queue WHERE q_name=? """
                                cursor.execute(sql,[userfname_spy.get()])
                                result = cursor.fetchone()
                                conn.close()
                                chkque["state"] = DISABLED
                            waitingyayoi()
                    home_button["image"] = button_home_not
                    account_button["image"] = button_wallet_not
                    q_button["image"] = button_q_activate
                    favshop_button["image"] = button_fav_not
                    wallet_home = Frame(root,bg="#FFFBEA")
                    wallet_home.place(x=100,y=0,width=w-100,height=h)
                    Label(wallet_home,image=afteryou_queuepic,bg="#FFFBEA").place(x=-18,y=-14,w=938,h=370) 
                    Label(wallet_home,bg="#F0E0C9").place(x=50,y=380,w=800,h=270) 
                    Label(wallet_home,text="Number of customer :",font="Calibri 22",bg="#F0E0C9").place(x=60,y=400)
                    Label(wallet_home,image=amountpeople,bg="#F0E0C9").place(x=330,y=400)
                    amountspy = StringVar()
                    amountlist = ["-","1-2","3-4","5-6"]
                    combo_amount = ttk.Combobox(wallet_home,value=amountlist,textvariable=amountspy)
                    combo_amount.place(x=340,y=405)
                    chkque = Button(wallet_home,image=amountpeople_1,bg="#F0E0C9",border=0,activebackground="#F0E0C9",command=checkamt)
                    chkque.place(x=660,y=400)
                elif whatqueue.get() == "KYO" :
                    def checkamt() :
                        if combo_amount.get() == "-" or  combo_amount.get() == "" :
                            messagebox.showwarning("Admin","Please enter number of guest")
                        elif combo_amount.get() == "1-2" or combo_amount.get() == "3-4" or combo_amount.get() == "5-6" :
                            def waitingyayoi() :
                                def Refreshpage() :
                                    conn = sqlite3.connect("projectdb.db")
                                    cursor = conn.cursor()
                                    sql = """
                                            SELECT * FROM shop_kyo_queue WHERE q_name=? """
                                    cursor.execute(sql,[userfname_spy.get()])
                                    result = cursor.fetchone()
                                    sql = """
                                            SELECT * FROM shop_kyo_table
                                            WHERE name=? """
                                    cursor.execute(sql,[userfname_spy.get()])
                                    result_2 = cursor.fetchone()
                                    conn.close()
                                    if result[3] == "wait" :
                                        pass
                                    elif result[3] == "ready" :
                                        kyo_mainprogram(result_2[0],userfname_spy.get())
                                def cancelq() :
                                    dis = messagebox.askokcancel("Admin","Do you want to cancel")
                                    if dis == True :
                                        conn = sqlite3.connect("projectdb.db")
                                        cursor = conn.cursor()
                                        sql = """
                                                DELETE FROM shop_kyo_queue
                                                WHERE q_name=? """
                                        cursor.execute(sql,[userfname_spy.get()])
                                        conn.commit()
                                        conn.close()
                                        whatqueue.set("empty")
                                        home_frame()
                                conn = sqlite3.connect("projectdb.db")
                                cursor = conn.cursor()
                                if combo_amount.get() == "1-2" :
                                    sql = """
                                                INSERT INTO shop_kyo_queue (q_name,q_amount,q_status)
                                                values(?,?,?) """
                                    cursor.execute(sql,[userfname_spy.get(),"1-2","wait"])
                                    conn.commit()
                                elif combo_amount.get() == "3-4" :
                                    sql = """
                                                INSERT INTO shop_kyo_queue (q_name,q_amount,q_status)
                                                values(?,?,?) """
                                    cursor.execute(sql,[userfname_spy.get(),"3-4","wait"])
                                    conn.commit()
                                elif combo_amount.get() == "5-6" :
                                    sql = """
                                                INSERT INTO shop_kyo_queue (q_name,q_amount,q_status)
                                                values(?,?,?) """
                                    cursor.execute(sql,[userfname_spy.get(),"5-6","wait"])
                                    conn.commit()
                                conn.close()
                                #
                                conn = sqlite3.connect("projectdb.db")
                                cursor = conn.cursor()
                                sql = """
                                        SELECT * FROM shop_kyo_queue """
                                cursor.execute(sql)
                                result = cursor.fetchall()
                                queuex = 0
                                for i,data in enumerate(result):
                                    queuex = queuex + 1
                                Label(wallet_home,text="Your queue number : %s"%(queuex),font="Calibri 20 bold",bg="#FFF1F2").place(x=60,y=480)
                                Label(wallet_home,text="%s more queue will reach your queue"%(queuex-1),font="Calibri 20",bg="#FFF1F2").place(x=60,y=530)
                                Label(wallet_home,text="Around %s minutes"%(queuex*5),font="Calibri 20",bg="#FFF1F2").place(x=60,y=580)
                                Button(wallet_home,text="Cancel queue",font="Calibri 20 underline",bg="#FFF1F2",border=0,command=cancelq,activebackground="#FFF1F2").place(x=670,y=590)
                                Button(wallet_home,text="Refresh",command=Refreshpage,border=0).place(x=700,y=500)
                                sql = """
                                        SELECT * FROM shop_kyo_queue WHERE q_name=? """
                                cursor.execute(sql,[userfname_spy.get()])
                                result = cursor.fetchone()
                                conn.close()
                                chkque["state"] = DISABLED
                            waitingyayoi()
                    home_button["image"] = button_home_not
                    account_button["image"] = button_wallet_not
                    q_button["image"] = button_q_activate
                    favshop_button["image"] = button_fav_not
                    wallet_home = Frame(root,bg="#FAC8CB")
                    wallet_home.place(x=100,y=0,width=w-100,height=h)
                    Label(wallet_home,image=kyo_queuepic,bg="#FAC8CB").place(x=-18,y=0,w=938,h=370)
                    Label(wallet_home,bg="#FFF1F2").place(x=50,y=380,w=800,h=270) 
                    Label(wallet_home,text="Number of customer :",font="Calibri 22",bg="#FFF1F2").place(x=60,y=400)
                    Label(wallet_home,image=amountpeople,bg="#FFF1F2").place(x=330,y=400)
                    amountspy = StringVar()
                    amountlist = ["-","1-2","3-4","5-6"]
                    combo_amount = ttk.Combobox(wallet_home,value=amountlist,textvariable=amountspy)
                    combo_amount.place(x=340,y=405)
                    chkque = Button(wallet_home,image=amountpeople_1,bg="#FFF1F2",border=0,activebackground="#FFF1F2",command=checkamt,activeforeground="#FFF1F2")
                    chkque.place(x=660,y=400)
                elif whatqueue.get() == "CODE" :
                    def checkamt() :
                        if combo_amount.get() == "-" or  combo_amount.get() == "" :
                            messagebox.showwarning("Admin","Please enter number of guest")
                        elif combo_amount.get() == "1-2" or combo_amount.get() == "3-4" or combo_amount.get() == "5-6" :
                            def waitingyayoi() :
                                def Refreshpage() :
                                    conn = sqlite3.connect("projectdb.db")
                                    cursor = conn.cursor()
                                    sql = """
                                            SELECT * FROM shop_code_queue WHERE q_name=? """
                                    cursor.execute(sql,[userfname_spy.get()])
                                    result = cursor.fetchone()
                                    sql = """
                                            SELECT * FROM shop_code_table
                                            WHERE name=? """
                                    cursor.execute(sql,[userfname_spy.get()])
                                    result_2 = cursor.fetchone()
                                    conn.close()
                                    if result[3] == "wait" :
                                        pass
                                    elif result[3] == "ready" :
                                        code_mainprogram(result_2[0],userfname_spy.get())
                                def cancelq() :
                                    dis = messagebox.askokcancel("Admin","Do you want to cancel")
                                    if dis == True :
                                        conn = sqlite3.connect("projectdb.db")
                                        cursor = conn.cursor()
                                        sql = """
                                                DELETE FROM shop_code_queue
                                                WHERE q_name=? """
                                        cursor.execute(sql,[userfname_spy.get()])
                                        conn.commit()
                                        conn.close()
                                        whatqueue.set("empty")
                                        home_frame()
                                conn = sqlite3.connect("projectdb.db")
                                cursor = conn.cursor()
                                if combo_amount.get() == "1-2" :
                                    sql = """
                                                INSERT INTO shop_code_queue (q_name,q_amount,q_status)
                                                values(?,?,?) """
                                    cursor.execute(sql,[userfname_spy.get(),"1-2","wait"])
                                    conn.commit()
                                elif combo_amount.get() == "3-4" :
                                    sql = """
                                                INSERT INTO shop_code_queue (q_name,q_amount,q_status)
                                                values(?,?,?) """
                                    cursor.execute(sql,[userfname_spy.get(),"3-4","wait"])
                                    conn.commit()
                                elif combo_amount.get() == "5-6" :
                                    sql = """
                                                INSERT INTO shop_code_queue (q_name,q_amount,q_status)
                                                values(?,?,?) """
                                    cursor.execute(sql,[userfname_spy.get(),"5-6","wait"])
                                    conn.commit()
                                conn.close()
                                #
                                conn = sqlite3.connect("projectdb.db")
                                cursor = conn.cursor()
                                sql = """
                                        SELECT * FROM shop_code_queue """
                                cursor.execute(sql)
                                result = cursor.fetchall()
                                queuex = 0
                                for i,data in enumerate(result):
                                    queuex = queuex + 1
                                Label(wallet_home,text="Your queue number : %s"%(queuex),font="Calibri 20 bold",bg="#FFF1F2").place(x=60,y=480)
                                Label(wallet_home,text="%s more queue will reach your queue"%(queuex-1),font="Calibri 20",bg="#FFF1F2").place(x=60,y=530)
                                Label(wallet_home,text="Around %s minutes"%(queuex*5),font="Calibri 20",bg="#FFF1F2").place(x=60,y=580)
                                Button(wallet_home,text="Cancel queue",font="Calibri 20 underline",bg="#FFF1F2",border=0,command=cancelq).place(x=670,y=590)
                                Button(wallet_home,text="Refresh",command=Refreshpage,border=0).place(x=700,y=500)
                                sql = """
                                        SELECT * FROM shop_code_queue WHERE q_name=? """
                                cursor.execute(sql,[userfname_spy.get()])
                                result = cursor.fetchone()
                                conn.close()
                                chkque["state"] = DISABLED
                            waitingyayoi()
                    home_button["image"] = button_home_not
                    account_button["image"] = button_wallet_not
                    q_button["image"] = button_q_activate
                    favshop_button["image"] = button_fav_not
                    wallet_home = Frame(root,bg="#FAC8CB")
                    wallet_home.place(x=100,y=0,width=w-100,height=h)
                    Label(wallet_home,image=code_queuepic,bg="#FAC8CB").place(x=-18,y=-10,w=938,h=370) 
                    Label(wallet_home,bg="#FFF1F2").place(x=50,y=380,w=800,h=270) 
                    Label(wallet_home,text="Number of customer :",font="Calibri 22",bg="#FFF1F2").place(x=60,y=400)
                    Label(wallet_home,image=amountpeople,bg="#FFF1F2").place(x=330,y=400)
                    amountspy = StringVar()
                    amountlist = ["-","1-2","3-4","5-6"]
                    combo_amount = ttk.Combobox(wallet_home,value=amountlist,textvariable=amountspy)
                    combo_amount.place(x=340,y=405)
                    chkque = Button(wallet_home,image=amountpeople_1,bg="#FFF1F2",border=0,activebackground="#F0E0C9",command=checkamt,activeforeground="#FFF1F2")
                    chkque.place(x=660,y=400)
                elif whatqueue.get() == "SHIN" :
                    def checkamt() :
                        if combo_amount.get() == "-" or  combo_amount.get() == "" :
                            messagebox.showwarning("Admin","Please enter number of guest")
                        elif combo_amount.get() == "1-2" or combo_amount.get() == "3-4" or combo_amount.get() == "5-6" :
                            def waitingyayoi() :
                                def Refreshpage() :
                                    conn = sqlite3.connect("projectdb.db")
                                    cursor = conn.cursor()
                                    sql = """
                                            SELECT * FROM shop_shin_queue WHERE q_name=? """
                                    cursor.execute(sql,[userfname_spy.get()])
                                    result = cursor.fetchone()
                                    sql = """
                                            SELECT * FROM shop_shin_table
                                            WHERE name=? """
                                    cursor.execute(sql,[userfname_spy.get()])
                                    result_2 = cursor.fetchone()
                                    conn.close()
                                    if result[3] == "wait" :
                                        pass
                                    elif result[3] == "ready" :
                                        shin_mainprogram(result_2[0],userfname_spy.get())
                                def cancelq() :
                                    dis = messagebox.askokcancel("Admin","Do you want to cancel")
                                    if dis == True :
                                        conn = sqlite3.connect("projectdb.db")
                                        cursor = conn.cursor()
                                        sql = """
                                                DELETE FROM shop_shin_queue
                                                WHERE q_name=? """
                                        cursor.execute(sql,[userfname_spy.get()])
                                        conn.commit()
                                        conn.close()
                                        whatqueue.set("empty")
                                        home_frame()
                                conn = sqlite3.connect("projectdb.db")
                                cursor = conn.cursor()
                                if combo_amount.get() == "1-2" :
                                    sql = """
                                                INSERT INTO shop_shin_queue (q_name,q_amount,q_status)
                                                values(?,?,?) """
                                    cursor.execute(sql,[userfname_spy.get(),"1-2","wait"])
                                    conn.commit()
                                elif combo_amount.get() == "3-4" :
                                    sql = """
                                                INSERT INTO shop_shin_queue (q_name,q_amount,q_status)
                                                values(?,?,?) """
                                    cursor.execute(sql,[userfname_spy.get(),"3-4","wait"])
                                    conn.commit()
                                elif combo_amount.get() == "5-6" :
                                    sql = """
                                                INSERT INTO shop_shin_queue (q_name,q_amount,q_status)
                                                values(?,?,?) """
                                    cursor.execute(sql,[userfname_spy.get(),"5-6","wait"])
                                    conn.commit()
                                conn.close()
                                #
                                conn = sqlite3.connect("projectdb.db")
                                cursor = conn.cursor()
                                sql = """
                                        SELECT * FROM shop_shin_queue """
                                cursor.execute(sql)
                                result = cursor.fetchall()
                                queuex = 0
                                for i,data in enumerate(result):
                                    queuex = queuex + 1
                                Label(wallet_home,text="Your queue number : %s"%(queuex),font="Calibri 20 bold",bg="#FB9B9B").place(x=60,y=480)
                                Label(wallet_home,text="%s more queue will reach your queue"%(queuex-1),font="Calibri 20",bg="#FB9B9B").place(x=60,y=530)
                                Label(wallet_home,text="Around %s minutes"%(queuex*5),font="Calibri 20",bg="#FB9B9B").place(x=60,y=580)
                                Button(wallet_home,text="Cancel queue",font="Calibri 20 underline",bg="#FB9B9B",border=0,command=cancelq).place(x=670,y=590)
                                Button(wallet_home,text="Refresh",command=Refreshpage,border=0).place(x=700,y=500)
                                sql = """
                                        SELECT * FROM shop_shin_queue WHERE q_name=? """
                                cursor.execute(sql,[userfname_spy.get()])
                                result = cursor.fetchone()
                                conn.close()
                                chkque["state"] = DISABLED
                            waitingyayoi()
                    home_button["image"] = button_home_not
                    account_button["image"] = button_wallet_not
                    q_button["image"] = button_q_activate
                    favshop_button["image"] = button_fav_not
                    wallet_home = Frame(root,bg="#8E2F2F")
                    wallet_home.place(x=100,y=0,width=w-100,height=h)
                    Label(wallet_home,image=shin_queuepic,bg="#8E2F2F").place(x=-18,y=-10,w=938,h=370) 
                    Label(wallet_home,bg="#FB9B9B").place(x=50,y=380,w=800,h=270)
                    Label(wallet_home,text="Number of customer :",font="Calibri 22",bg="#FB9B9B").place(x=60,y=400)
                    Label(wallet_home,image=amountpeople,bg="#FB9B9B").place(x=330,y=400)
                    amountspy = StringVar()
                    amountlist = ["-","1-2","3-4","5-6"]
                    combo_amount = ttk.Combobox(wallet_home,value=amountlist,textvariable=amountspy)
                    combo_amount.place(x=340,y=405)
                    chkque = Button(wallet_home,image=amountpeople_1,bg="#FB9B9B",border=0,activebackground="#F0E0C9",command=checkamt)
                    chkque.place(x=660,y=400)
                elif whatqueue.get() == "OHK" :
                    def checkamt() :
                        if combo_amount.get() == "-" or  combo_amount.get() == "" :
                            messagebox.showwarning("Admin","Please enter number of guest")
                        elif combo_amount.get() == "1-2" or combo_amount.get() == "3-4" or combo_amount.get() == "5-6" :
                            def waitingyayoi() :
                                def Refreshpage() :
                                    conn = sqlite3.connect("projectdb.db")
                                    cursor = conn.cursor()
                                    sql = """
                                            SELECT * FROM shop_ohk_queue WHERE q_name=? """
                                    cursor.execute(sql,[userfname_spy.get()])
                                    result = cursor.fetchone()
                                    sql = """
                                            SELECT * FROM shop_ohk_table
                                            WHERE name=? """
                                    cursor.execute(sql,[userfname_spy.get()])
                                    result_2 = cursor.fetchone()
                                    conn.close()
                                    if result[3] == "wait" :
                                        pass
                                    elif result[3] == "ready" :
                                        ohk_mainprogram(result_2[0],userfname_spy.get())
                                def cancelq() :
                                    dis = messagebox.askokcancel("Admin","Do you want to cancel")
                                    if dis == True :
                                        conn = sqlite3.connect("projectdb.db")
                                        cursor = conn.cursor()
                                        sql = """
                                                DELETE FROM shop_ohk_queue
                                                WHERE q_name=? """
                                        cursor.execute(sql,[userfname_spy.get()])
                                        conn.commit()
                                        conn.close()
                                        whatqueue.set("empty")
                                        home_frame()
                                conn = sqlite3.connect("projectdb.db")
                                cursor = conn.cursor()
                                if combo_amount.get() == "1-2" :
                                    sql = """
                                                INSERT INTO shop_ohk_queue (q_name,q_amount,q_status)
                                                values(?,?,?) """
                                    cursor.execute(sql,[userfname_spy.get(),"1-2","wait"])
                                    conn.commit()
                                elif combo_amount.get() == "3-4" :
                                    sql = """
                                                INSERT INTO shop_ohk_queue (q_name,q_amount,q_status)
                                                values(?,?,?) """
                                    cursor.execute(sql,[userfname_spy.get(),"3-4","wait"])
                                    conn.commit()
                                elif combo_amount.get() == "5-6" :
                                    sql = """
                                                INSERT INTO shop_ohk_queue (q_name,q_amount,q_status)
                                                values(?,?,?) """
                                    cursor.execute(sql,[userfname_spy.get(),"5-6","wait"])
                                    conn.commit()
                                conn.close()
                                #
                                conn = sqlite3.connect("projectdb.db")
                                cursor = conn.cursor()
                                sql = """
                                        SELECT * FROM shop_ohk_queue """
                                cursor.execute(sql)
                                result = cursor.fetchall()
                                queuex = 0
                                for i,data in enumerate(result):
                                    queuex = queuex + 1
                                Label(wallet_home,text="Your queue number : %s"%(queuex),font="Calibri 20 bold",bg="#ECC998").place(x=60,y=480)
                                Label(wallet_home,text="%s more queue will reach your queue"%(queuex-1),font="Calibri 20",bg="#ECC998").place(x=60,y=530)
                                Label(wallet_home,text="Around %s minutes"%(queuex*5),font="Calibri 20",bg="#ECC998").place(x=60,y=580)
                                Button(wallet_home,text="Cancel queue",font="Calibri 20 underline",bg="#ECC998",border=0,command=cancelq).place(x=670,y=590)
                                Button(wallet_home,text="Refresh",command=Refreshpage,border=0).place(x=700,y=500)
                                sql = """
                                        SELECT * FROM shop_ohk_queue WHERE q_name=? """
                                cursor.execute(sql,[userfname_spy.get()])
                                result = cursor.fetchone()
                                conn.close()
                                chkque["state"] = DISABLED
                            waitingyayoi()
                    home_button["image"] = button_home_not
                    account_button["image"] = button_wallet_not
                    q_button["image"] = button_q_activate
                    favshop_button["image"] = button_fav_not
                    wallet_home = Frame(root,bg="#AAC09B")
                    wallet_home.place(x=100,y=0,width=w-100,height=h)
                    Label(wallet_home,image=ohk_queuepic,bg="#AAC09B").place(x=-18,y=-15,w=938,h=370) # เเก้รูป
                    Label(wallet_home,bg="#ECC998").place(x=50,y=380,w=800,h=270) # เเก้สี
                    Label(wallet_home,text="Number of customer :",font="Calibri 22",bg="#ECC998").place(x=60,y=400)
                    Label(wallet_home,image=amountpeople,bg="#ECC998").place(x=330,y=400)
                    amountspy = StringVar()
                    amountlist = ["-","1-2","3-4","5-6"]
                    combo_amount = ttk.Combobox(wallet_home,value=amountlist,textvariable=amountspy)
                    combo_amount.place(x=340,y=405)
                    chkque = Button(wallet_home,image=amountpeople_1,bg="#ECC998",border=0,activebackground="#ECC998",command=checkamt)
                    chkque.place(x=660,y=400)
            def favshop_frame() :
                #
                home_button["image"] = button_home_not
                account_button["image"] = button_wallet_not
                q_button["image"] = button_q_not
                favshop_button["image"] = button_fav_activate
                #
                favshop_home = Frame(root,bg="#F8EFE0")
                favshop_home.place(x=100,y=0,width=w-100,height=h)
                Label(favshop_home,text="Favorite",bg="#F8EFE0",font="Calibri 26 bold").place(x=40,y=20)
                #
                if fav_spy.get() != "-" :
                    if fav_spy.get() == "yyo" :
                        Button(favshop_home,image=frameshop_yyo,border=0,bg="#F8EFE0",activebackground="#F8EFE0",command=shop2).place(x=30,y=90)
                    elif fav_spy.get() == "shin" :
                        Button(favshop_home,image=frameshop_shin,border=0,bg="#F8EFE0",activebackground="#F8EFE0",command=shop5).place(x=30,y=90)
                    elif fav_spy.get() == "okj" :
                        Button(favshop_home,image=frameshop_okj,border=0,bg="#F8EFE0",activebackground="#F8EFE0",command=shop6).place(x=30,y=90)
                    elif fav_spy.get() == "aty" :
                        Button(favshop_home,image=frameshop_aty,border=0,bg="#F8EFE0",activebackground="#F8EFE0",command=shop1).place(x=30,y=90)
                    elif fav_spy.get() == "kyo" :
                        Button(favshop_home,image=frameshop_kyo,border=0,bg="#F8EFE0",activebackground="#F8EFE0",command=shop3).place(x=30,y=90)
                    elif fav_spy.get() == "code" :
                        Button(favshop_home,image=frameshop_code,border=0,bg="#F8EFE0",activebackground="#F8EFE0",command=shop4).place(x=30,y=90)
                    Label(favshop_home,image=addtofav_act,bg="white").place(x=240,y=245)
            # call function 
            framemenu()
            home_frame()
    # def 3 exit function
    def allexitfuntion() :
        global regisgotologin , manageaccountprocess , managecpassprocess , topupprocess, yayoi_mainprogram , afteryou_mainprogram , kyo_mainprogram , code_mainprogram , shin_mainprogram , ohk_mainprogram , backtomainpage
        def regisgotologin() :
            customerlogin()
            frame_customerregister.destroy()
        def manageaccountprocess(id) :
            # function
            def changeinfo() :
                if change_fname.get() != "" :
                    if change_lname.get() != "" :
                        if change_tele.get() != "" :
                            conn = sqlite3.connect("projectdb.db")
                            cursor = conn.cursor()
                            sql = """
                                    UPDATE customer_information SET firstname_customer=? , lastname_customer = ?,
                                    tel_customer=? WHERE id_customer=? """
                            cursor.execute(sql,[change_fname.get(), change_lname.get(), change_tele.get(), id])
                            conn.commit()
                            messagebox.showinfo("Admin","Update successfully")
                            #
                            customermainpage(id)
                            change_fname.set("")
                            change_lname.set("")
                            change_tele.set("")
                            
                        else :
                            messagebox.showwarning("Admin","Please enter Telephone number")
                    else :
                        messagebox.showwarning("Admin","Please enter last name")
                else :
                    messagebox.showwarning("Admin","Please enter first name")   
            def backtoaccount() :
                customermainpage(id)
                account_frame()
                manageaccount_frame.destroy()
            # spy
            change_fname = StringVar()
            change_lname = StringVar()
            change_tele = StringVar()
            manageaccount_frame = Frame(root,bg="#F8EFE0")
            manageaccount_frame.place(x=100,y=0,width=w-100,height=h)
            account_home.destroy()
            #
            conn = sqlite3.connect("projectdb.db")
            cursor = conn.cursor()
            sql = """
                    SELECT * FROM customer_information 
                    WHERE id_customer=? """
            cursor.execute(sql,[id])
            result = cursor.fetchone()
            # set spy
            change_fname.set(result[1])
            change_lname.set(result[2])
            change_tele.set(result[3])
            # first name
            text_fname_manage = Label(manageaccount_frame,text="First Name :",bg="#F8EFE0")
            text_fname_manage.place(x=150,y=230)
            entry_fname_manage = Entry(manageaccount_frame,text="",textvariable=change_fname,bg="#FFFFFF")
            entry_fname_manage.place(x=400,y=230)
            # lastname
            text_lname_manage = Label(manageaccount_frame,text="Last Name :",bg="#F8EFE0")
            text_lname_manage.place(x=150,y=280)
            entry_lname_manage = Entry(manageaccount_frame,text="",textvariable=change_lname,bg="#FFFFFF")
            entry_lname_manage.place(x=400,y=280)
            # telephone num
            text_tel_manage = Label(manageaccount_frame,text="Telephone number :",bg="#F8EFE0")
            text_tel_manage.place(x=150,y=330)
            entry_tel_manage = Entry(manageaccount_frame,text="",textvariable=change_tele,bg="#FFFFFF")
            entry_tel_manage.place(x=400,y=330)
            # button = confirm
            button_confirm_manage = Button(manageaccount_frame,text="Confirm",image=button_cf,bg="#F8EFE0",fg="white",command=changeinfo,activebackground="#F8EFE0",border=0) 
            button_confirm_manage.place(x=320,y=450)
            # button = back
            button_back_manage = Button(manageaccount_frame,text="< Back",bg="#F8EFE0",fg="black",width=20,command=backtoaccount,border=0,activebackground="#F8EFE0") 
            button_back_manage.place(x=-90,y=10)
        def managecpassprocess(id) :
            # function
            def changeprocess() :
                if new_password.get() != "" :
                    if new_cfpassword.get() != "" :
                        if new_password.get() == new_cfpassword.get() :
                            if new_password.get() != old_password.get() :
                                conn = sqlite3.connect("projectdb.db")
                                cursor = conn.cursor()
                                sql ="""
                                        UPDATE customer_login SET password_customer=?
                                        WHERE id_customer=? """
                                cursor.execute(sql,[new_password.get(), id])
                                conn.commit()
                                new_password.set("")
                                new_cfpassword.set("")
                                messagebox.showinfo("Admin","Change password successfully")    
                                customermainpage(id)
                                managecpass_frame.destroy()
                            else :
                                messagebox.showwarning("Admin","Please use new password") 
                        else :
                            messagebox.showwarning("Admin","Password isn't match") 
                    else :
                       messagebox.showwarning("Admin","Please Enter Comfirm Password") 
                else :
                    messagebox.showwarning("Admin","Please Enter Password")   
            def backtomenu() :
                new_password.set("")
                new_cfpassword.set("")
                customermainpage(id)
                account_frame()
                managecpass_frame.destroy()
            managecpass_frame = Frame(root,bg="#F8EFE0")
            managecpass_frame.place(x=100,y=0,width=w-100,height=h)
            account_home.destroy()
            #
            conn = sqlite3.connect("projectdb.db")
            cursor = conn.cursor()
            sql = """
                    SELECT * FROM customer_login 
                    WHERE id_customer=? """
            cursor.execute(sql,[id])
            result = cursor.fetchone()
            # spy
            old_password = StringVar()
            old_password.set(result[2])
            new_password = StringVar()
            new_cfpassword = StringVar()
            # widget
            label_password_managecpass = Label(managecpass_frame,text="New password :",bg="#F8EFE0")
            label_password_managecpass.place(x=200,y=230)
            label_cfpassword_managecpass = Label(managecpass_frame,text="Confrim new password :",bg="#F8EFE0")
            label_cfpassword_managecpass.place(x=110,y=300)
            #
            entry_password_managecpass = Entry(managecpass_frame,width=20,textvariable=new_password)
            entry_password_managecpass.place(x=400,y=230)
            entry_cfpassword_managecpass = Entry(managecpass_frame,width=20,textvariable=new_cfpassword)
            entry_cfpassword_managecpass.place(x=400,y=300)
            #
            button_confirm_managecpass = Button(managecpass_frame,text="Confirm",image=button_cf,command=changeprocess,bg="#F8EFE0",fg="white",activebackground="#F8EFE0",border=0)
            button_confirm_managecpass.place(x=300,y=470)
            #
            button_back_managecpass = Button(managecpass_frame,text="< Back",command=backtomenu,border=0,bg="#F8EFE0",activebackground="#F8EFE0")
            button_back_managecpass.place(x=10,y=10)
        # shop
        def topupprocess(id) :
            # function
            def buttontopup() :
                def paymenthappen() :
                    def topupprocess() :
                        if payment_spy.get() != "-" :
                            if tel_spy.get() != "" and len(tel_spy.get()) == 10 :
                                if amount.get() != "" :
                                    num_chk = amount.get().isnumeric()
                                    if num_chk == True :
                                        if int(amount.get()) <= 10000 :
                                            time_now = time.datetime.now()
                                            conn = sqlite3.connect("projectdb.db") 
                                            cursor = conn.cursor()
                                            sql = """
                                                        INSERT INTO customer_topup (id_customer, payment_with, payment_tel, amount, date)
                                                        values (?,?,?,?,?)"""
                                            cursor.execute(sql,[userid.get(), payment_spy.get(), tel_spy.get(), amount.get(), time_now])
                                            conn.commit()
                                            #
                                            sql = """
                                                        SELECT money_customer 
                                                        FROM customer_information
                                                        WHERE id_customer=? """
                                            cursor.execute(sql,[userid.get()])
                                            result = cursor.fetchone()
                                            newresult = (float(result[0])//1) + float(amount.get())
                                            sql = """
                                                        UPDATE customer_information
                                                        SET money_customer=?
                                                        WHERE id_customer=? """
                                            cursor.execute(sql,[newresult,userid.get()])
                                            conn.commit()
                                            conn.close()
                                            messagebox.showinfo("Admin","Top-up succesfully")    
                                            moneyleft.set(newresult)
                                            payment_spy.set("-")
                                            amount.set("")
                                            tel_spy.set("")
                                            customermainpage(id)
                                            account_frame()

                                        else :
                                            messagebox.showwarning("Admin","Can top-up not more than 10000 Baht per time") 
                                    else :
                                        messagebox.showwarning("Admin","Enter number only") 
                                else :
                                   messagebox.showwarning("Admin","Please enter amount") 
                            else :
                                messagebox.showwarning("Admin","Enter wrong number")
                        else :
                            messagebox.showwarning("Admin","Error")  
                    # spy
                    tel_spy = StringVar()
                    amount = StringVar()
                    #
                    if payment_spy.get() != "-" :
                        bg_4 = Label(topup_frame,bg="#FFFFFF")
                        bg_4.place(x=500,y=280,width=370,height=320)
                        youselect_payment = Label(topup_frame,text="You select %s"%(payment_spy.get()),bg="#FFFFFF")
                        youselect_payment.place(x=520,y=300)
                        telephone_payment = Label(topup_frame,text="Tel no",bg="#FFFFFF")
                        telephone_payment.place(x=520,y=360)
                        insert_telenum = Entry(topup_frame,width=15,textvariable=tel_spy,bg="white")
                        insert_telenum.place(x=620,y=360)
                        money_payment = Label(topup_frame,text="money",bg="#FFFFFF")
                        money_payment.place(x=520,y=420)
                        insert_money = Entry(topup_frame,width=15,textvariable=amount,bg="white")
                        insert_money.place(x=620,y=420)
                        confirm_payment = Button(topup_frame,text="Confirm",command=topupprocess,width=10,bg="#FFD058",fg="white",activebackground="white")
                        confirm_payment.place(x=690,y=480)
                bg_3 = Label(topup_frame,bg="#FFFFFF")
                bg_3.place(x=500,y=80,width=370,height=520)
                point_process_text = Label(topup_frame,text="Top up",font="Calibri 24 bold",bg="#FFFFFF")
                point_process_text.place(x=640,y=100)
                # Combobox
                payment_spy  = StringVar()
                paymentlist = ["-","K PLUS","SCB EASY","Krungthai NEXT","TrueMoney Wallet","Bualuang mBanking","KMA","ธ.ก.ส A-Moblie"]
                combo_bank = ttk.Combobox(topup_frame,value=paymentlist,textvariable=payment_spy)
                combo_bank.set("-")
                combo_bank.place(x=540,y=170)
                #
                check_payment = Button(topup_frame,text="Confirm",command=paymenthappen,border=0)
                check_payment.place(x=540,y=230)
            def buttonpoint() :
                bg_4 = Label(topup_frame,bg="#FFFFFF")
                bg_4.place(x=500,y=80,width=370,height=520)
                point_process_text = Label(topup_frame,text="Point exchange",font="Calibri 24 bold",bg="white")
                point_process_text.place(x=590,y=100)
                # define function
                def item_1_enter(e) :
                    item_1["border"] = 1
                def item_1_outer(e) : 
                    item_1["border"] = 0
                def item_2_enter(e) :
                    item_2["border"] = 1
                def item_2_outer(e) : 
                    item_2["border"] = 0
                def item_3_enter(e) :
                    item_3["border"] = 1
                def item_3_outer(e) : 
                    item_3["border"] = 0
                def item1process() :
                    sql = """
                            SELECT point_customer 
                            FROM customer_information
                            WHERE id_customer=? """
                    cursor.execute(sql,[id])
                    result = cursor.fetchone()
                    if float(result[0]) > 99 :
                        ans = messagebox.askquestion("Admin","Do you want to use your point?") 
                        if ans == "yes" :
                            balance_point = (float(result[0]) - 100)//1
                            sql = """
                                    UPDATE customer_information
                                    SET point_customer=? 
                                    WHERE id_customer=? """
                            cursor.execute(sql,[balance_point, id])
                            conn.commit()
                            messagebox.showinfo("Admin","Exchange Success \n Souvenir can be picked up from any store that joins us") 
                        else :
                            pass
                    else :
                        messagebox.showwarning("Admin","Not enough point") 
                def item2process() :
                    sql = """
                            SELECT point_customer 
                            FROM customer_information
                            WHERE id_customer=? """
                    cursor.execute(sql,[id])
                    result = cursor.fetchone()
                    if float(result[0]) > 99 :
                        ans = messagebox.askquestion("Admin","Do you want to use your point?") 
                        if ans == "yes" :
                            balance_point = (float(result[0]) - 100)//1
                            sql = """
                                    UPDATE customer_information
                                    SET point_customer=? 
                                    WHERE id_customer=? """
                            cursor.execute(sql,[balance_point, id])
                            conn.commit()
                            messagebox.showinfo("Admin","Exchange Success \n Souvenir can be picked up from any store that joins us") 
                        else :
                            pass
                    else :
                        messagebox.showwarning("Admin","Not enough point") 
                def item3process() :
                    sql = """
                            SELECT point_customer 
                            FROM customer_information
                            WHERE id_customer=? """
                    cursor.execute(sql,[id])
                    result = cursor.fetchone()
                    if float(result[0]) > 99 :
                        ans = messagebox.askquestion("Admin","Do you want to use your point?") 
                        if ans == "yes" :
                            balance_point = (float(result[0]) - 100)//1
                            sql = """
                                    UPDATE customer_information
                                    SET point_customer=? 
                                    WHERE id_customer=? """
                            cursor.execute(sql,[balance_point, id])
                            conn.commit()
                            messagebox.showinfo("Admin","Exchange Success \n Souvenir can be picked up from any store that joins us") 
                    else :
                        messagebox.showwarning("Admin","Not enough point") 
                # item        
                item_1 = Button(topup_frame,image=pic_item_1,text=" 100 point ",compound=LEFT,bg="white",border=0,activebackground="white",command=item1process)
                item_1.place(x=560,y=170)
                item_2 =Button(topup_frame,image=pic_item_2,text=" 100 point ",compound=LEFT,bg="white",border=0,activebackground="white",command=item2process)
                item_2.place(x=560,y=320)
                item_3 =Button(topup_frame,image=pic_item_3,text=" 100 point ",compound=LEFT,bg="white",border=0,activebackground="white",command=item3process)
                item_3.place(x=560,y=470)
                # bind
                item_1.bind("<Enter>",item_1_enter)
                item_1.bind("<Leave>",item_1_outer)
                item_2.bind("<Enter>",item_2_enter)
                item_2.bind("<Leave>",item_2_outer)
                item_3.bind("<Enter>",item_3_enter)
                item_3.bind("<Leave>",item_3_outer)
            def backtoaccount() :
                customermainpage(id)
                account_frame()
                topup_frame.destroy()
            # spy id
            userid = StringVar()
            userid.set(id)
            pointleft = StringVar()
            moneyleft = StringVar()
            #
            topup_frame = Frame(root,bg="#F8EFE0")
            topup_frame.place(x=100,y=0,width=w-100,height=h)
            account_home.destroy()
            #
            conn = sqlite3.connect("projectdb.db")
            cursor = conn.cursor()
            sql ="""
                    SELECT point_customer,money_customer FROM customer_information
                    WHERE id_customer=? """
            cursor.execute(sql,[id])
            result = cursor.fetchone()
            # widget
            bg_1 = Label(topup_frame,image=frame_point,bg="#F8EFE0",border=0)
            bg_1.place(x=20,y=130)
            bg_2 = Label(topup_frame,image=frame_money,bg="#F8EFE0",border=0)
            bg_2.place(x=20,y=360)
            #
            text_point_topup = Label(topup_frame,text="Point",font="Calibri 24 bold",bg="#F8EFE0")
            text_point_topup.place(x=20,y=70)
            text_money_topup = Label(topup_frame,text="Money",font="Calibri 24 bold",bg="#F8EFE0")
            text_money_topup.place(x=20,y=300)
            #
            button_topup_topup = Button(topup_frame,text="Top up",image=button_money,command=buttontopup,bg="#DDEAD6",fg="white",activebackground="#DDEAD6",border=0)
            button_topup_topup.place(x=300,y=400)
            button_point_topup = Button(topup_frame,text="Point",image=button_exc,command=buttonpoint,bg="#FFEAEA",fg="white",activebackground="#FFEAEA",border=0)
            button_point_topup.place(x=300,y=170)
            button_back_topup = Button(topup_frame,text="< Back",width=10,command=backtoaccount,bg="#F8EFE0",fg="black",border=0)
            button_back_topup.place(x=-10,y=10)
            # show point
            conn = sqlite3.connect("projectdb.db")
            cursor = conn.cursor()
            sql ="""
                        SELECT point_customer,money_customer
                        FROM customer_information
                        WHERE id_customer=? """
            cursor.execute(sql,[userid.get()])
            result = cursor.fetchone()
            pointleft.set(result[0])
            moneyleft.set(result[1])
            show_point_topup = Label(topup_frame,text="%0.f"%float(pointleft.get()),bg="#FFEAEA")
            show_point_topup.place(x=100,y=180)
            show_money_topup = Label(topup_frame,text="%0.f"%float(moneyleft.get()),bg="#DDEAD6")
            show_money_topup.place(x=100,y=410)
        def yayoi_mainprogram(table,customername) :
            global yayoishop_indexpage,yayoishop_indexmenubar,yayoishop_tablex
            yayoiroot = Frame(root,bg="white")
            yayoiroot.place(x=0,y=0,width=1000,height=700)
            #
            conn = sqlite3.connect("projectdb.db")
            cursor = conn.cursor()
            sql = """
                        DELETE FROM shop_yayoi_queue
                        WHERE q_name=? """
            cursor.execute(sql,[customername])
            conn.commit()
            username = customername
            yayoishop_indexpage = StringVar()
            yayoishop_indexpage.set("0")
            yayoishop_indexmenubar = StringVar()
            yayoishop_indexmenubar.set("0")
            yayoishop_tablex = StringVar()
            yayoishop_tablex.set(table)
            def yayoishop_addtocartprocess(ordername,price) :
                statusx = "NF"
                amount = 1
                conn = sqlite3.connect("projectdb.db")
                cursor = conn.cursor()
                sql = """
                        SELECT * FROM shop_yayoi_orderprocess
                        WHERE table_index = ? and amount > 0 and menu_name = ?"""
                cursor.execute(sql,[yayoishop_tablex.get(),ordername])
                result = cursor.fetchone()
                conn.close()
                if result:
                    if ordername == result[1] :
                        newamount = int(result[3]) + 1
                        conn = sqlite3.connect("projectdb.db")
                        cursor = conn.cursor()
                        sql = """
                                UPDATE shop_yayoi_orderprocess
                                SET amount = ?
                                WHERE menu_name = ? """
                        cursor.execute(sql,[newamount,ordername])
                        conn.commit()
                        conn.close()
                        messagebox.showinfo("Admin","Added to cart")   
                else : 
                    conn = sqlite3.connect("projectdb.db")
                    cursor = conn.cursor()
                    sql = """
                            INSERT INTO shop_yayoi_orderprocess 
                            values(?,?,?,?,?)"""
                    cursor.execute(sql,[yayoishop_tablex.get(),ordername,price,amount,statusx])
                    conn.commit()
                    conn.close()
                    messagebox.showinfo("Admin","Added to cart")   
                    conn = sqlite3.connect("projectdb.db")
                    cursor = conn.cursor()
                    sql = """
                                SELECT * FROM shop_yayoi_orderprocess
                                WHERE table_index=? """
                    cursor.execute(sql,[yayoishop_tablex.get()])
                    result = cursor.fetchall()
                    nuborder = 0
                    for i,date in enumerate(result) :
                        nuborder = nuborder + 1
                    lenorder = StringVar()
                    lenorder.set(nuborder)
                    yayoishop_amount_order["text"] = lenorder.get()
            def yayoishop_click1(e) :
                if yayoishop_indexpage.get() == "1" :
                    yayoishop_frameone.destroy()
                elif yayoishop_indexpage.get() == "2" :
                    yayoishop_frametwo.destroy()
                elif yayoishop_indexpage.get() == "3" :
                    yayoishop_framethree.destroy()
                elif yayoishop_indexpage.get() == "4" :
                    yayoishop_framefour.destroy()
                elif yayoishop_indexpage.get() == "5" :
                    yayoishop_framefive.destroy()
                yayoishop_cate_1["image"] = yayoishop_cate_frame_1
                yayoishop_cate_2["image"] = yayoishop_cate_frame_2
                yayoishop_cate_3["image"] = yayoishop_cate_frame_2
                yayoishop_cate_4["image"] = yayoishop_cate_frame_2
                yayoishop_cate_5["image"] = yayoishop_cate_frame_2
            def yayoishop_click2(e) :
                if yayoishop_indexpage.get() == "1" :
                    yayoishop_frameone.destroy()
                elif yayoishop_indexpage.get() == "2" :
                    yayoishop_frametwo.destroy()
                elif yayoishop_indexpage.get() == "3" :
                    yayoishop_framethree.destroy()
                elif yayoishop_indexpage.get() == "4" :
                    yayoishop_framefour.destroy()
                elif yayoishop_indexpage.get() == "5" :
                    yayoishop_framefive.destroy()
                yayoishop_cate_1["image"] = yayoishop_cate_frame_2
                yayoishop_cate_2["image"] = yayoishop_cate_frame_1
                yayoishop_cate_3["image"] = yayoishop_cate_frame_2
                yayoishop_cate_4["image"] = yayoishop_cate_frame_2
                yayoishop_cate_5["image"] = yayoishop_cate_frame_2
            def yayoishop_click3(e) :
                if yayoishop_indexpage.get() == "1" :
                    yayoishop_frameone.destroy()
                elif yayoishop_indexpage.get() == "2" :
                    yayoishop_frametwo.destroy()
                elif yayoishop_indexpage.get() == "3" :
                    yayoishop_framethree.destroy()
                elif yayoishop_indexpage.get() == "4" :
                    yayoishop_framefour.destroy()
                elif yayoishop_indexpage.get() == "5" :
                    yayoishop_framefive.destroy()
                yayoishop_cate_1["image"] = yayoishop_cate_frame_2
                yayoishop_cate_2["image"] = yayoishop_cate_frame_2
                yayoishop_cate_3["image"] = yayoishop_cate_frame_1
                yayoishop_cate_4["image"] = yayoishop_cate_frame_2
                yayoishop_cate_5["image"] = yayoishop_cate_frame_2
            def yayoishop_click4(e) :
                if yayoishop_indexpage.get() == "1" :
                    yayoishop_frameone.destroy()
                elif yayoishop_indexpage.get() == "2" :
                    yayoishop_frametwo.destroy()
                elif yayoishop_indexpage.get() == "3" :
                    yayoishop_framethree.destroy()
                elif yayoishop_indexpage.get() == "4" :
                    yayoishop_framefour.destroy()
                elif yayoishop_indexpage.get() == "5" :
                    yayoishop_framefive.destroy()
                yayoishop_cate_1["image"] = yayoishop_cate_frame_2
                yayoishop_cate_2["image"] = yayoishop_cate_frame_2
                yayoishop_cate_3["image"] = yayoishop_cate_frame_2
                yayoishop_cate_4["image"] = yayoishop_cate_frame_1
                yayoishop_cate_5["image"] = yayoishop_cate_frame_2
            def yayoishop_click5(e) :
                if yayoishop_indexpage.get() == "1" :
                    yayoishop_frameone.destroy()
                elif yayoishop_indexpage.get() == "2" :
                    yayoishop_frametwo.destroy()
                elif yayoishop_indexpage.get() == "3" :
                    yayoishop_framethree.destroy()
                elif yayoishop_indexpage.get() == "4" :
                    yayoishop_framefour.destroy()
                elif yayoishop_indexpage.get() == "5" :
                    yayoishop_framefive.destroy()
                yayoishop_cate_1["image"] = yayoishop_cate_frame_2
                yayoishop_cate_2["image"] = yayoishop_cate_frame_2
                yayoishop_cate_3["image"] = yayoishop_cate_frame_2
                yayoishop_cate_4["image"] = yayoishop_cate_frame_2
                yayoishop_cate_5["image"] = yayoishop_cate_frame_1
            def yayoishop_frame_one() :
                global yayoishop_frameone
                yayoishop_indexpage.set("1")
                yayoishop_frameone = Frame(yayoishop_frame,bg="#FFFFFF")
                yayoishop_frameone.place(x=0,y=155,width=1000,height=545)
                # menu 1
                menu_1 = Label(yayoishop_frameone,image=yayoishop_menuset_1,bg="#FFFFFF")
                menu_1.place(x=0,y=20)
                # menu 2
                menu_2 = Label(yayoishop_frameone,image=yayoishop_menuset_2,bg="#FFFFFF")
                menu_2.place(x=200,y=20)
                # menu 3
                menu_3 = Label(yayoishop_frameone,image=yayoishop_menuset_3,bg="#FFFFFF")
                menu_3.place(x=400,y=20)
                # menu 4
                menu_4 = Label(yayoishop_frameone,image=yayoishop_menuset_4,bg="#FFFFFF")
                menu_4.place(x=600,y=20)
                # menu 5
                menu_5 = Label(yayoishop_frameone,image=yayoishop_menuset_5,bg="#FFFFFF")
                menu_5.place(x=800,y=20)
                # menu 6
                menu_6 = Label(yayoishop_frameone,image=yayoishop_menuset_6,bg="#FFFFFF")
                menu_6.place(x=0,y=285)
                # menu 7 
                menu_7 = Label(yayoishop_frameone,image=yayoishop_menuset_7,bg="#FFFFFF")
                menu_7.place(x=200,y=285)
                # menu 8
                menu_8 = Label(yayoishop_frameone,image=yayoishop_menuset_8,bg="#FFFFFF")
                menu_8.place(x=400,y=285)
                # menu 9
                menu_9 = Label(yayoishop_frameone,image=yayoishop_menuset_9,bg="#FFFFFF")
                menu_9.place(x=600,y=285)
                # menu 10
                menu_10 = Label(yayoishop_frameone,image=yayoishop_menuset_10,bg="#FFFFFF")
                menu_10.place(x=800,y=285)
                #
                mart_number_1 = Button(yayoishop_frameone,image=yayoishop_mart_photo,border=0,command=lambda:yayoishop_addtocartprocess("สุดคุ้ม_1","459"))  
                mart_number_1.place(x=139,y=238)
                mart_number_2 = Button(yayoishop_frameone,image=yayoishop_mart_photo,border=0,command=lambda:yayoishop_addtocartprocess("สุดคุ้ม_2","259"))
                mart_number_2.place(x=339,y=238)
                mart_number_3 = Button(yayoishop_frameone,image=yayoishop_mart_photo,border=0,command=lambda:yayoishop_addtocartprocess("สุดคุ้ม_3","459"))
                mart_number_3.place(x=539,y=238)
                mart_number_4 = Button(yayoishop_frameone,image=yayoishop_mart_photo,border=0,command=lambda:yayoishop_addtocartprocess("Mk Vitamin Strawberry","280"))
                mart_number_4.place(x=739,y=238)
                mart_number_5 = Button(yayoishop_frameone,image=yayoishop_mart_photo,border=0,command=lambda:yayoishop_addtocartprocess("Mk Vitamin orange","280"))
                mart_number_5.place(x=939,y=238)
                mart_number_6 = Button(yayoishop_frameone,image=yayoishop_mart_photo,border=0,command=lambda:yayoishop_addtocartprocess("นมอัดเม็ด 10+2","200"))
                mart_number_6.place(x=139,y=503)
                mart_number_7 = Button(yayoishop_frameone,image=yayoishop_mart_photo,border=0,command=lambda:yayoishop_addtocartprocess("เมมเบอรี่ ลาเต้","200"))
                mart_number_7.place(x=339,y=503)
                mart_number_8 = Button(yayoishop_frameone,image=yayoishop_mart_photo,border=0,command=lambda:yayoishop_addtocartprocess("วอเทอเมลอน ครัช","95"))
                mart_number_8.place(x=539,y=503)
                mart_number_9 = Button(yayoishop_frameone,image=yayoishop_mart_photo,border=0,command=lambda:yayoishop_addtocartprocess("สควีช ออเรนจ์","95"))
                mart_number_9.place(x=739,y=503)
                mart_number_10 = Button(yayoishop_frameone,image=yayoishop_mart_photo,border=0,command=lambda:yayoishop_addtocartprocess("เอเมอรัล โฟลว์","95"))
                mart_number_10.place(x=939,y=503)
            def yayoishop_frame_two() :
                global yayoishop_frametwo
                yayoishop_indexpage.set("2")
                yayoishop_frametwo = Frame(yayoishop_frame,bg="white")
                yayoishop_frametwo.place(x=0,y=155,width=1000,height=545)
                # menu 1
                menu_1 = Label(yayoishop_frametwo,image=yayoishop_menuset_11,bg="#FFFFFF")
                menu_1.place(x=0,y=20)
                # menu 2
                menu_2 = Label(yayoishop_frametwo,image=yayoishop_menuset_12,bg="#FFFFFF")
                menu_2.place(x=200,y=20)
                # menu 3
                menu_3 = Label(yayoishop_frametwo,image=yayoishop_menuset_13,bg="#FFFFFF")
                menu_3.place(x=400,y=20)
                # menu 4
                menu_4 = Label(yayoishop_frametwo,image=yayoishop_menuset_14,bg="#FFFFFF")
                menu_4.place(x=600,y=20)
                # menu 5
                menu_5 = Label(yayoishop_frametwo,image=yayoishop_menuset_15,bg="#FFFFFF")
                menu_5.place(x=800,y=20)
                # menu 6
                menu_6 = Label(yayoishop_frametwo,image=yayoishop_menuset_16,bg="#FFFFFF")
                menu_6.place(x=0,y=285)
                # menu 7 
                menu_7 = Label(yayoishop_frametwo,image=yayoishop_menuset_17,bg="#FFFFFF")
                menu_7.place(x=200,y=285)
                # menu 8
                menu_8 = Label(yayoishop_frametwo,image=yayoishop_menuset_18,bg="#FFFFFF")
                menu_8.place(x=400,y=285)
                # menu 9
                menu_9 = Label(yayoishop_frametwo,image=yayoishop_menuset_19,bg="#FFFFFF")
                menu_9.place(x=600,y=285)
                # menu 10
                menu_10 = Label(yayoishop_frametwo,image=yayoishop_menuset_20,bg="#FFFFFF")
                menu_10.place(x=800,y=285)
                #
                mart_number_1 = Button(yayoishop_frametwo,image=yayoishop_mart_photo,border=0,command=lambda:yayoishop_addtocartprocess("แซลมอน เมนไท ลาวา","339"))
                mart_number_1.place(x=139,y=238)
                mart_number_2 = Button(yayoishop_frametwo,image=yayoishop_mart_photo,border=0,command=lambda:yayoishop_addtocartprocess("บูตะ เทปปันยากิ","269"))
                mart_number_2.place(x=339,y=238)
                mart_number_3 = Button(yayoishop_frametwo,image=yayoishop_mart_photo,border=0,command=lambda:yayoishop_addtocartprocess("ซารุ โซบะ เอบิ เทมปุระ","199"))
                mart_number_3.place(x=539,y=238)
                mart_number_4 = Button(yayoishop_frametwo,image=yayoishop_mart_photo,border=0,command=lambda:yayoishop_addtocartprocess("เซ็นได ยูซุ เรเมน","179"))
                mart_number_4.place(x=739,y=238)
                mart_number_5 = Button(yayoishop_frametwo,image=yayoishop_mart_photo,border=0,command=lambda:yayoishop_addtocartprocess("เซตปลาแซลมอน","319"))
                mart_number_5.place(x=939,y=238)
                mart_number_6 = Button(yayoishop_frametwo,image=yayoishop_mart_photo,border=0,command=lambda:yayoishop_addtocartprocess("เซตปลาซาบะย่างเกลือ","205"))
                mart_number_6.place(x=139,y=503)
                mart_number_7 = Button(yayoishop_frametwo,image=yayoishop_mart_photo,border=0,command=lambda:yayoishop_addtocartprocess("เเซตชีสเบอร์เกอร์เนื้อ","215"))
                mart_number_7.place(x=339,y=503)
                mart_number_8 = Button(yayoishop_frametwo,image=yayoishop_mart_photo,border=0,command=lambda:yayoishop_addtocartprocess("เซตชีสเบอร์เกอร์หมู","205"))
                mart_number_8.place(x=539,y=503)
                mart_number_9 = Button(yayoishop_frametwo,image=yayoishop_mart_photo,border=0,command=lambda:yayoishop_addtocartprocess("ไก่ทอดราดซอสนัมบัง","195"))
                mart_number_9.place(x=739,y=503)
                mart_number_10 = Button(yayoishop_frametwo,image=yayoishop_mart_photo,border=0,command=lambda:yayoishop_addtocartprocess("เซตปลากะพงชุบแป้งทอด","189"))
                mart_number_10.place(x=939,y=503)
            def yayoishop_frame_three() :
                global yayoishop_framethree
                yayoishop_indexpage.set("3")
                yayoishop_framethree = Frame(yayoishop_frame,bg="white")
                yayoishop_framethree.place(x=0,y=155,width=1000,height=545)
                # menu 1
                menu_1 = Label(yayoishop_framethree,image=yayoishop_menuset_21,bg="#FFFFFF")
                menu_1.place(x=0,y=20)
                # menu 2
                menu_2 = Label(yayoishop_framethree,image=yayoishop_menuset_22,bg="#FFFFFF")
                menu_2.place(x=200,y=20)
                # menu 3
                menu_3 = Label(yayoishop_framethree,image=yayoishop_menuset_23,bg="#FFFFFF")
                menu_3.place(x=400,y=20)
                # menu 4
                menu_4 = Label(yayoishop_framethree,image=yayoishop_menuset_24,bg="#FFFFFF")
                menu_4.place(x=600,y=20)
                # menu 5
                menu_5 = Label(yayoishop_framethree,image=yayoishop_menuset_25,bg="#FFFFFF")
                menu_5.place(x=800,y=20)
                # menu 6
                menu_6 = Label(yayoishop_framethree,image=yayoishop_menuset_26,bg="#FFFFFF")
                menu_6.place(x=0,y=285)
                # menu 7 
                menu_7 = Label(yayoishop_framethree,image=yayoishop_menuset_27,bg="#FFFFFF")
                menu_7.place(x=200,y=285)
                # menu 8
                menu_8 = Label(yayoishop_framethree,image=yayoishop_menuset_28,bg="#FFFFFF")
                menu_8.place(x=400,y=285)
                # menu 9
                menu_9 = Label(yayoishop_framethree,image=yayoishop_menuset_29,bg="#FFFFFF")
                menu_9.place(x=600,y=285)
                # menu 10
                menu_10 = Label(yayoishop_framethree,image=yayoishop_menuset_30,bg="#FFFFFF")
                menu_10.place(x=800,y=285)
                #
                mart_number_1 = Button(yayoishop_framethree,image=yayoishop_mart_photo,border=0,command=lambda:yayoishop_addtocartprocess("ยูซุ รูบี้ โซดา","59"))
                mart_number_1.place(x=139,y=238)
                mart_number_2 = Button(yayoishop_framethree,image=yayoishop_mart_photo,border=0,command=lambda:yayoishop_addtocartprocess("ยูซุ คอฟฟี่","59"))
                mart_number_2.place(x=339,y=238)
                mart_number_3 = Button(yayoishop_framethree,image=yayoishop_mart_photo,border=0,command=lambda:yayoishop_addtocartprocess("ยูซุ ที เฟรปเป้","69"))
                mart_number_3.place(x=539,y=238)
                mart_number_4 = Button(yayoishop_framethree,image=yayoishop_mart_photo,border=0,command=lambda:yayoishop_addtocartprocess("มัทฉะ เฟรปเป้","75"))
                mart_number_4.place(x=739,y=238)
                mart_number_5 = Button(yayoishop_framethree,image=yayoishop_mart_photo,border=0,command=lambda:yayoishop_addtocartprocess("มัทฉะ ลาเต้","59"))
                mart_number_5.place(x=939,y=238)
                mart_number_6 = Button(yayoishop_framethree,image=yayoishop_mart_photo,border=0,command=lambda:yayoishop_addtocartprocess("น้ำส้มคั้น","65"))
                mart_number_6.place(x=139,y=503)
                mart_number_7 = Button(yayoishop_framethree,image=yayoishop_mart_photo,border=0,command=lambda:yayoishop_addtocartprocess("น้ำมะนาว","55"))
                mart_number_7.place(x=339,y=503)
                mart_number_8 = Button(yayoishop_framethree,image=yayoishop_mart_photo,border=0,command=lambda:yayoishop_addtocartprocess("น้ำอัดลมโคล่า","30"))
                mart_number_8.place(x=539,y=503)
                mart_number_9 = Button(yayoishop_framethree,image=yayoishop_mart_photo,border=0,command=lambda:yayoishop_addtocartprocess("น้ำชาเขียวเย็น","29"))
                mart_number_9.place(x=739,y=503)
                mart_number_10 = Button(yayoishop_framethree,image=yayoishop_mart_photo,border=0,command=lambda:yayoishop_addtocartprocess("น้ำแร่","25"))
                mart_number_10.place(x=939,y=503)
            def yayoishop_frame_four() :
                global yayoishop_framefour
                yayoishop_indexpage.set("4")
                yayoishop_framefour = Frame(yayoishop_frame,bg="white")
                yayoishop_framefour.place(x=0,y=155,width=1000,height=545)
                # menu 1
                menu_1 = Label(yayoishop_framefour,image=yayoishop_menuset_31,bg="#FFFFFF")
                menu_1.place(x=0,y=20)
                # menu 2
                menu_2 = Label(yayoishop_framefour,image=yayoishop_menuset_32,bg="#FFFFFF")
                menu_2.place(x=200,y=20)
                # menu 3
                menu_3 = Label(yayoishop_framefour,image=yayoishop_menuset_33,bg="#FFFFFF")
                menu_3.place(x=400,y=20)
                # menu 4
                menu_4 = Label(yayoishop_framefour,image=yayoishop_menuset_34,bg="#FFFFFF")
                menu_4.place(x=600,y=20)
                # menu 5
                menu_5 = Label(yayoishop_framefour,image=yayoishop_menuset_35,bg="#FFFFFF")
                menu_5.place(x=800,y=20)
                # menu 6
                menu_6 = Label(yayoishop_framefour,image=yayoishop_menuset_36,bg="#FFFFFF")
                menu_6.place(x=0,y=285)
                # menu 7 
                menu_7 = Label(yayoishop_framefour,image=yayoishop_menuset_37,bg="#FFFFFF")
                menu_7.place(x=200,y=285)
                # menu 8
                menu_8 = Label(yayoishop_framefour,image=yayoishop_menuset_38,bg="#FFFFFF")
                menu_8.place(x=400,y=285)
                # menu 9
                menu_9 = Label(yayoishop_framefour,image=yayoishop_menuset_39,bg="#FFFFFF")
                menu_9.place(x=600,y=285)
                #
                mart_number_1 = Button(yayoishop_framefour,image=yayoishop_mart_photo,border=0,command=lambda:yayoishop_addtocartprocess("ราเม็งแชมป์เปี้ยน","169"))
                mart_number_1.place(x=139,y=238)
                mart_number_2 = Button(yayoishop_framefour,image=yayoishop_mart_photo,border=0,command=lambda:yayoishop_addtocartprocess("คะระราเม็งแชมป์เปี้ยน","169"))
                mart_number_2.place(x=339,y=238)
                mart_number_3 = Button(yayoishop_framefour,image=yayoishop_mart_photo,border=0,command=lambda:yayoishop_addtocartprocess("อุด้งหมูสุกี้ยากี้","155"))
                mart_number_3.place(x=539,y=238)
                mart_number_4 = Button(yayoishop_framefour,image=yayoishop_mart_photo,border=0,command=lambda:yayoishop_addtocartprocess("โซเม็ง(นิวเม็ง)","155"))
                mart_number_4.place(x=739,y=238)
                mart_number_5 = Button(yayoishop_framefour,image=yayoishop_mart_photo,border=0,command=lambda:yayoishop_addtocartprocess("เทมปุระโซเม็ง","155"))
                mart_number_5.place(x=939,y=238)
                mart_number_6 = Button(yayoishop_framefour,image=yayoishop_mart_photo,border=0,command=lambda:yayoishop_addtocartprocess("อุด้งเทมปุระ","65"))
                mart_number_6.place(x=139,y=503)
                mart_number_7 = Button(yayoishop_framefour,image=yayoishop_mart_photo,border=0,command=lambda:yayoishop_addtocartprocess("ยากิโซบะกระทะร้อนห่อไข่","125"))
                mart_number_7.place(x=339,y=503)
                mart_number_8 = Button(yayoishop_framefour,image=yayoishop_mart_photo,border=0,command=lambda:yayoishop_addtocartprocess("ยากิโซบะกระทะร้อน","125"))
                mart_number_8.place(x=539,y=503)
                mart_number_9 = Button(yayoishop_framefour,image=yayoishop_mart_photo,border=0,command=lambda:yayoishop_addtocartprocess("โซบะเย็น","29"))
                mart_number_9.place(x=739,y=503)
            def yayoishop_frame_five() :
                global yayoishop_framefive
                yayoishop_indexpage.set("5")
                yayoishop_framefive = Frame(yayoishop_frame,bg="white")
                yayoishop_framefive.place(x=0,y=155,width=1000,height=545)
                # menu 1
                menu_1 = Label(yayoishop_framefive,image=yayoishop_menuset_41,bg="#FFFFFF")
                menu_1.place(x=0,y=20)
                # menu 2
                menu_2 = Label(yayoishop_framefive,image=yayoishop_menuset_42,bg="#FFFFFF")
                menu_2.place(x=200,y=20)
                # menu 3
                menu_3 = Label(yayoishop_framefive,image=yayoishop_menuset_43,bg="#FFFFFF")
                menu_3.place(x=400,y=20)
                # menu 4
                menu_4 = Label(yayoishop_framefive,image=yayoishop_menuset_44,bg="#FFFFFF")
                menu_4.place(x=600,y=20)
                # menu 5
                menu_5 = Label(yayoishop_framefive,image=yayoishop_menuset_45,bg="#FFFFFF")
                menu_5.place(x=800,y=20)
                # menu 6
                menu_6 = Label(yayoishop_framefive,image=yayoishop_menuset_46,bg="#FFFFFF")
                menu_6.place(x=0,y=285)
                # menu 7 
                menu_7 = Label(yayoishop_framefive,image=yayoishop_menuset_47,bg="#FFFFFF")
                menu_7.place(x=200,y=285)
                # menu 8
                menu_8 = Label(yayoishop_framefive,image=yayoishop_menuset_48,bg="#FFFFFF")
                menu_8.place(x=400,y=285)
                # menu 9
                menu_9 = Label(yayoishop_framefive,image=yayoishop_menuset_49,bg="#FFFFFF")
                menu_9.place(x=600,y=285)
                # menu 10
                menu_10 = Label(yayoishop_framefive,image=yayoishop_menuset_50,bg="#FFFFFF")
                menu_10.place(x=800,y=285)
                #
                mart_number_1 = Button(yayoishop_framefive,image=yayoishop_mart_photo,border=0,command=lambda:yayoishop_addtocartprocess("อุนางิ ดงบุริ","369"))
                mart_number_1.place(x=139,y=238)
                mart_number_2 = Button(yayoishop_framefive,image=yayoishop_mart_photo,border=0,command=lambda:yayoishop_addtocartprocess("แซลมอนทรงเครื่อง ดงบุริ","195"))
                mart_number_2.place(x=339,y=238)
                mart_number_3 = Button(yayoishop_framefive,image=yayoishop_mart_photo,border=0,command=lambda:yayoishop_addtocartprocess("หมูชาชู ดงบุริ","165"))
                mart_number_3.place(x=539,y=238)
                mart_number_4 = Button(yayoishop_framefive,image=yayoishop_mart_photo,border=0,command=lambda:yayoishop_addtocartprocess("สไปซี่บูตะ ดงบุริ","149"))
                mart_number_4.place(x=739,y=238)
                mart_number_5 = Button(yayoishop_framefive,image=yayoishop_mart_photo,border=0,command=lambda:yayoishop_addtocartprocess("ข้าวหน้าเนื้อ","189"))
                mart_number_5.place(x=939,y=238)
                mart_number_6 = Button(yayoishop_framefive,image=yayoishop_mart_photo,border=0,command=lambda:yayoishop_addtocartprocess("ข้าวหน้าเนื้อผัดเผ็ดซอส","189"))
                mart_number_6.place(x=139,y=503)
                mart_number_7 = Button(yayoishop_framefive,image=yayoishop_mart_photo,border=0,command=lambda:yayoishop_addtocartprocess("ข้าวราดหน้าหมูชุบแป้งทอด","185"))
                mart_number_7.place(x=339,y=503)
                mart_number_8 = Button(yayoishop_framefive,image=yayoishop_mart_photo,border=0,command=lambda:yayoishop_addtocartprocess("ข้าวหน้าหมู","149"))
                mart_number_8.place(x=539,y=503)
                mart_number_9 = Button(yayoishop_framefive,image=yayoishop_mart_photo,border=0,command=lambda:yayoishop_addtocartprocess("ข้าวราดหน้าไก่ใส่ไข่","195"))
                mart_number_9.place(x=739,y=503)
                mart_number_10 = Button(yayoishop_framefive,image=yayoishop_mart_photo,border=0,command=lambda:yayoishop_addtocartprocess("ข้าวหน้าแซลมอน ไข่กุ้ง","229"))
                mart_number_10.place(x=939,y=503)
            def yayoishop_menuframe() :
                global yayoishop_cate_1 , yayoishop_cate_2 , yayoishop_cate_3 , yayoishop_cate_4 , yayoishop_cate_5 , yayoishop_indexmenubar
                yayoishop_menu_butt["state"] = "disabled"
                yayoishop_button_orders["state"] = "active"
                if yayoishop_indexmenubar.get() == "1" :
                    yayoishop_allorder.destroy()
                elif yayoishop_indexmenubar.get() == "0" :
                    pass
                yayoishop_indexmenubar.set("0")
                if yayoishop_indexpage.get() == "1" :
                    yayoishop_frameone.destroy()
                elif yayoishop_indexpage.get() == "2" :
                    yayoishop_frametwo.destroy()
                elif yayoishop_indexpage.get() == "3" :
                    yayoishop_framethree.destroy()
                elif yayoishop_indexpage.get() == "4" :
                    yayoishop_framefour.destroy()
                elif yayoishop_indexpage.get() == "5" :
                    yayoishop_framefive.destroy()
                yayoishop_frame_one()
                # category
                yayoishop_cate_1 = Button(yayoishop_frame,text="Recommand",image=yayoishop_cate_frame_1,compound="center",fg="black",border=0,bg="#FFFFFF",activebackground="#FFFFFF",font="Calibri 13",command=yayoishop_frame_one)
                yayoishop_cate_1.place(relx=0.375,y=110)
                #
                yayoishop_cate_2 = Button(yayoishop_frame,text="Set menu",image=yayoishop_cate_frame_2,compound="center",fg="black",border=0,bg="#FFFFFF",activebackground="#FFFFFF",font="Calibri 13",command=yayoishop_frame_two)
                yayoishop_cate_2.place(relx=0.5,y=110)
                #
                yayoishop_cate_3 = Button(yayoishop_frame,text="Drink",image=yayoishop_cate_frame_2,compound="center",fg="black",border=0,bg="#FFFFFF",activebackground="#FFFFFF",font="Calibri 13",command=yayoishop_frame_three)
                yayoishop_cate_3.place(relx=0.875,y=110)
                #
                yayoishop_cate_4 = Button(yayoishop_frame,text="Ramen",image=yayoishop_cate_frame_2,compound="center",fg="black",border=0,bg="#FFFFFF",activebackground="#FFFFFF",font="Calibri 13",command=yayoishop_frame_four)
                yayoishop_cate_4.place(relx=0.75,y=110)
                #
                yayoishop_cate_5 = Button(yayoishop_frame,text="Donburi",image=yayoishop_cate_frame_2,compound="center",fg="black",border=0,bg="#FFFFFF",activebackground="#FFFFFF",font="Calibri 13",command=yayoishop_frame_five)
                yayoishop_cate_5.place(relx=0.625,y=110)
                # bind
                yayoishop_cate_1.bind("<Button-1>",yayoishop_click1)
                yayoishop_cate_2.bind("<Button-1>",yayoishop_click2)
                yayoishop_cate_3.bind("<Button-1>",yayoishop_click3)
                yayoishop_cate_4.bind("<Button-1>",yayoishop_click4)
                yayoishop_cate_5.bind("<Button-1>",yayoishop_click5)
            def yayoishop_orderframe() :
                global yayoishop_indexmenubar,yayoishop_allorder
                yayoishop_menu_butt["state"] = "active"
                yayoishop_button_orders["state"] = "disabled"
                if yayoishop_indexmenubar.get() == "0" :
                    pass
                elif yayoishop_indexmenubar.get() == "1" :
                    yayoishop_allorder.destroy()
                yayoishop_indexmenubar.set("1")
                #
                yayoishop_cate_1.place(relx=10)
                yayoishop_cate_2.place(relx=10)
                yayoishop_cate_3.place(relx=10)
                yayoishop_cate_4.place(relx=10)
                yayoishop_cate_5.place(relx=10)
                #
                yayoishop_allorder = Frame(yayoishop_frame,bg="#FFFFFF")
                yayoishop_allorder.place(x=0,y=150,width=1000,height=550)
                yayoishop_allorder.rowconfigure((0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20),weight=1)
                yayoishop_allorder.columnconfigure((0,1,2,3),weight=1)
                #
                def yayoishop_payment(Total,cusinfo) :
                    def paymentprocess(total) :
                        ans = messagebox.askquestion("Admin","Are you sure you want to make a payment?") 
                        if ans == "yes" :
                            if float(cusinfo[7]) >= total :
                                shoppoint = 0
                                shoppoint = (total/20)//1
                                Label(paymentframe,image=yayoishop_payment_3,bg="white").place(x=40,y=0)
                                Label(paymentframe,text="Bill",bg="#EAE8E9",font="Calibri 25").place(x=60,y=10)
                                data = time.datetime.now()
                                time_now = (data.strftime("%x"))
                                Label(paymentframe,text=time_now,bg="#EAE8E9",font="Calibri 16").place(x=380,y=20)
                                Label(paymentframe,text="Menu",bg="#EAE8E9",font="Calibri 16 bold").place(x=60,y=70)
                                Label(paymentframe,text="Amount",bg="#EAE8E9",font="Calibri 16 bold").place(x=280,y=70)
                                Label(paymentframe,text="Price",bg="#EAE8E9",font="Calibri 16 bold").place(x=400,y=70)
                                yaix = 120
                                for i,data in enumerate(orderresult):
                                    if i < 6 :
                                        if data[4] == "F" :
                                            Label(paymentframe,text=data[1][0:25],bg="#EAE8E9",font="Calibri 16").place(x=60,y=yaix)
                                            Label(paymentframe,text=data[3],bg="#EAE8E9",font="Calibri 16").place(x=300,y=yaix)
                                            Label(paymentframe,text=data[2],bg="#EAE8E9",font="Calibri 16").place(x=400,y=yaix)
                                            yaix = yaix + 50
                                        else :
                                            pass
                                newbalance = (float(cusinfo[7])-total)//1
                                newpoint = (float(cusinfo[6])+shoppoint)//1
                                conn=sqlite3.connect("projectdb.db")
                                cursor = conn.cursor()
                                sql = """
                                            UPDATE customer_information
                                            SET money_customer=?,point_customer=?
                                            WHERE id_customer=?"""
                                cursor.execute(sql,[newbalance,newpoint,cusinfo[0]])
                                conn.commit()
                                messagebox.showinfo("Admin","Payment Successfully")
                                Label(paymentframe,text="VAT",bg="#EAE8E9",font="Calibri 16").place(x=60,y=410)
                                Label(paymentframe,text="7 %",bg="#EAE8E9",font="Calibri 16").place(x=400,y=410)
                                Label(paymentframe,text="Point",bg="#EAE8E9",font="Calibri 16").place(x=60,y=450)
                                Label(paymentframe,text="%0.f"%(shoppoint),bg="#EAE8E9",font="Calibri 16").place(x=400,y=450)
                                Label(paymentframe,text="Total Cost",bg="#EAE8E9",font="Calibri 16 bold").place(x=60,y=490)
                                Label(paymentframe,text="%0.f"%(total),bg="#EAE8E9",font="Calibri 16 bold").place(x=400,y=490)
                                Button(paymentframe,text="Exit",bg="#EAE8E9",font="Calibri 16 bold",command=quit).place(x=890,y=480)
                                yayoishop_menu_butt["state"] = "disabled"
                                yayoishop_button_staff["state"] = "disabled"
                                sql = """
                                        DELETE FROM shop_yayoi_orderprocess
                                        WHERE table_index=?"""
                                cursor.execute(sql,[table])   
                                conn.commit()
                                sql = """
                                        UPDATE shop_yayoi_table
                                        SET status=?,name=?,amount=?
                                        WHERE table_no=? """
                                cursor.execute(sql,['free','','',table])
                                conn.commit()
                                conn.close()
                            else :
                                messagebox.showwarning("Admin","Not enough money in your wallet \n Please pay at the counter")
                                yayoishop_menu_butt["state"] = "disabled"
                                yayoishop_button_staff["state"] = "disabled"
                                Button(paymentframe,text="Exit",bg="#EAE8E9",font="Calibri 16 bold",command=quit).place(x=890,y=480)
                                conn=sqlite3.connect("projectdb.db")
                                cursor = conn.cursor()
                                sql = """
                                        DELETE FROM shop_yayoi_orderprocess
                                        WHERE table_index=?"""
                                cursor.execute(sql,[table])   
                                conn.commit()
                                sql = """
                                        UPDATE shop_yayoi_table
                                        SET status=?,name=?,amount=?
                                        WHERE table_no=? """
                                cursor.execute(sql,['free','','',table])
                                conn.commit()
                                conn.close()
                        else :
                            pass 
                    # name
                    paymentframe = Frame(yayoishop_allorder,bg="#FFFFFF")
                    paymentframe.place(x=0,y=0,width=1000,height=550)
                    Label(paymentframe,image=yayoishop_payment_1,bg="white").place(x=40,y=0)
                    Label(paymentframe,image=yayoishop_payment_2,bg="white").place(x=510,y=0)
                    # widget
                    text_yourwallet = Label(paymentframe,text="Yourwallet",bg="#FFE6A7").place(x=60,y=10)
                    text_balance = Label(paymentframe,text="balance : %s"%(cusinfo[7]),bg="#FFE6A7").place(x=120,y=50)
                    text_point = Label(paymentframe,text="Point   : %s"%(cusinfo[6]),bg="#FFE6A7").place(x=120,y=90)
                    text_member = Label(paymentframe,text="membership : %s"%(cusinfo[5]),bg="#FFE6A7").place(x=120,y=130)
                    # 
                    text_Payout = Label(paymentframe,text="Payout",bg="#FFF2D0").place(x=60,y=210)
                    text_name = Label(paymentframe,text="Name : %s %s"%(cusinfo[1],cusinfo[2]),bg="#FFF2D0").place(x=120,y=260)
                    discount = 1
                    discountpercent = 0
                    if cusinfo[5] == "None" :
                        discount = 0.95
                        discountpercent = 5
                    elif cusinfo[5] == "Level1" :
                        discount = 0.9
                        discountpercent = 10
                    elif cusinfo[5] == "Level2" :
                        discount = 0.85
                        discountpercent = 15
                    text_tax = Label(paymentframe,text="Discount : %s Percent"%(discountpercent),bg="#FFF2D0").place(x=120,y=310)
                    total = (Total*discount*1.07)//1
                    text_total = Label(paymentframe,text="Total : %0.f Baht"%(total),bg="#FFF2D0").place(x=120,y=360)
                    text_point = Label(paymentframe,text="Point : %s"%((Totalx/20)//1),bg="#FFF2D0").place(x=120,y=410)
                    but_payment = Button(paymentframe,image=yayoishop_confirm,bg="#FFF2D0",fg="black",font="Calibri 16",border=0,command=lambda : paymentprocess(total))
                    but_payment.place(x=140,y=460)
                #
                Label(yayoishop_allorder,text="Status",bg="#FFFFFF").grid(row=0,column=0)
                Label(yayoishop_allorder,text="Menu",bg="#FFFFFF").grid(row=0,column=1)
                Label(yayoishop_allorder,text="Amount",bg="#FFFFFF").grid(row=0,column=2)
                Label(yayoishop_allorder,text="Price per unit",bg="#FFFFFF").grid(row=0,column=3)
                #
                conn = sqlite3.connect("projectdb.db")
                cursor = conn.cursor()
                sql = """
                        SELECT * FROM shop_yayoi_orderprocess 
                        WHERE table_index =?
                        """
                cursor.execute(sql,[yayoishop_tablex.get()])
                orderresult= cursor.fetchall()
                conn.close()
                #
                Totalx = 0
                for i,data in enumerate(orderresult) :
                    if i < 10 :
                        if data[4] == "NF" : 
                            Label(yayoishop_allorder,image=yayoishop_red_status,bg="#FFFFFF").grid(row=i+1,column=0)
                            Label(yayoishop_allorder,text=data[1],bg="white").grid(row=i+1,column=1)
                            Label(yayoishop_allorder,text=data[3],bg="white").grid(row=i+1,column=2)
                            Label(yayoishop_allorder,text=data[2],bg="white").grid(row=i+1,column=3)
                        elif data[4] == "CF" : 
                            Label(yayoishop_allorder,image=yayoishop_red_status,bg="#FFFFFF").grid(row=i+1,column=0)
                            Label(yayoishop_allorder,text=data[1],bg="white").grid(row=i+1,column=1)
                            Label(yayoishop_allorder,text=data[3],bg="white").grid(row=i+1,column=2)
                            Label(yayoishop_allorder,text=data[2],bg="white").grid(row=i+1,column=3)
                        elif data[4] == "F" :
                            Label(yayoishop_allorder,image=yayoishop_green_status,bg="#FFFFFF").grid(row=i+1,column=0)
                            Label(yayoishop_allorder,text=data[1],bg="white").grid(row=i+1,column=1)
                            Label(yayoishop_allorder,text=data[3],bg="white").grid(row=i+1,column=2)
                            Label(yayoishop_allorder,text=data[2],bg="white").grid(row=i+1,column=3)
                            Totalx = Totalx + (int(data[3])*int(data[2]))
                conn = sqlite3.connect("projectdb.db")
                cursor = conn.cursor()
                sql = """
                            SELECT * FROM customer_information
                            WHERE firstname_customer=? """
                cursor.execute(sql,[customername])
                cusinfo = cursor.fetchone()
                Button(yayoishop_allorder,text="Pay out",image=yayoishop_yayoishop_payout,command=lambda:yayoishop_payment(Totalx,cusinfo),border=0,bg="white",activebackground="white").grid(row=20,column=1,columnspan=2)
            def staffcalling() :
                sql = """
                        UPDATE shop_yayoi_table
                        SET staffcall=?
                        WHERE table_no=?"""
                cursor.execute(sql,["yes",yayoishop_tablex.get()])
                conn.commit()
            #
            amt_table = "0"
            if yayoishop_tablex.get() == "1" or yayoishop_tablex.get() == "2" or yayoishop_tablex.get() == "3" :
                amt_table = "1-2"
            elif yayoishop_tablex.get() == "4" or yayoishop_tablex.get() == "5" or yayoishop_tablex.get() == "6":
                amt_table = "3-4"
            elif yayoishop_tablex.get() == "7" or yayoishop_tablex.get() == "8":
                amt_table = "5-6"
            yayoishop_frame = Frame(yayoiroot,bg="#FFFFFF")
            yayoishop_frame.place(x=0,y=0,height=700,width=1000)
            Label(yayoishop_frame,image=yayoishop_header,bg="#FFFFFF").place(x=-2,y=-35)
            Label(yayoishop_frame,image=yayoishop_logo,bg="#FFFFFF").place(x=40,y=0)
            # table no
            yayoishop_table_no_wframe = Label(yayoishop_frame,image=yayoishop_whiteframe_1,bg="#FFA1C9")
            yayoishop_table_no_wframe.place(relx=0.519,y=15)
            yayoishop_text_no_people = Label(yayoishop_frame,text="Table No : %s \n %s people"%(yayoishop_tablex.get(),amt_table),bg="white",font="Calibri 16")
            yayoishop_text_no_people.place(relx=0.54,y=23)
            #
            yayoishop_order_wfame = Label(yayoishop_frame,image=yayoishop_whiteframe_2,bg="#FFA1C9")
            yayoishop_order_wfame.place(relx=0.7,y=15)
            yayoishop_chk_wfame = Label(yayoishop_frame,image=yayoishop_whiteframe_2,bg="#FFA1C9")
            yayoishop_chk_wfame.place(relx=0.8,y=15)
            yayoishop_staff_wfame = Label(yayoishop_frame,image=yayoishop_whiteframe_2,bg="#FFA1C9")
            yayoishop_staff_wfame.place(relx=0.9,y=15)
            #
            yayoishop_button_orders = Button(yayoishop_frame,image=yayoishop_but_orders,border=0,bg="#FBE5E5",activebackground="#FBE5E5",command=yayoishop_orderframe)
            yayoishop_button_orders.place(relx=0.814,y=27)
            #
            conn = sqlite3.connect("projectdb.db")
            cursor = conn.cursor()
            sql = """
                        SELECT * FROM shop_yayoi_orderprocess
                        WHERE table_index=? """
            cursor.execute(sql,[yayoishop_tablex.get()])
            result = cursor.fetchall()
            nuborder = 0
            for i,date in enumerate(result) :
                nuborder = nuborder + 1
            lenorder = StringVar()
            lenorder.set(nuborder)
            #
            yayoishop_amount_order = Label(yayoishop_frame,border=0,bg="#FBE5E5",text=lenorder.get(),compound="center",font="bold")
            yayoishop_amount_order.place(relx=0.855,y=19)
            # relx=0.752,y=17
            yayoishop_button_staff = Button(yayoishop_frame,image=yayoishop_but_staff,border=0,bg="#FBE5E5",activebackground="#FBE5E5",command=staffcalling)
            yayoishop_button_staff.place(relx=0.92,y=26)
            # 1
            yayoishop_menu_butt = Button(yayoishop_frame,image=yayoishop_but_menu,border=0,bg="#FBE5E5",activebackground="#FBE5E5",command=yayoishop_menuframe)
            yayoishop_menu_butt.place(relx=0.72,y=28)
            yayoishop_menuframe()
        def afteryou_mainprogram(table,customername) :
            global afteryoushop_indexpage,afteryoushop_indexmenubar,afteryoushop_tablex
            afteryouroot = Frame(root,bg="white")
            afteryouroot.place(x=0,y=0,width=1000,height=700)
            #
            conn = sqlite3.connect("projectdb.db")
            cursor = conn.cursor()
            sql = """
                        DELETE FROM shop_afteryou_queue
                        WHERE q_name=? """
            cursor.execute(sql,[customername])
            conn.commit()
            username = customername
            afteryoushop_indexpage = StringVar()
            afteryoushop_indexpage.set("0")
            afteryoushop_indexmenubar = StringVar()
            afteryoushop_indexmenubar.set("0")
            afteryoushop_tablex = StringVar()
            afteryoushop_tablex.set(table)
            def afteryoupicture() :
                #
                global afteryou_menuset_1, afteryou_menuset_2 ,afteryou_menuset_3 ,afteryou_menuset_4,afteryou_menuset_5,afteryou_menuset_6,afteryou_menuset_7,afteryou_menuset_8,afteryou_menuset_9,afteryou_menuset_10,afteryou_menuset_11,afteryou_menuset_12,afteryou_menuset_13,afteryou_menuset_14,afteryou_menuset_15,afteryou_menuset_16,afteryou_menuset_17,afteryou_menuset_18,afteryou_menuset_19,afteryou_menuset_20,afteryou_menuset_21,afteryou_menuset_22,afteryou_menuset_23,afteryou_menuset_24,afteryou_menuset_25,afteryou_menuset_26,afteryou_menuset_27,afteryou_menuset_28,afteryou_menuset_29,afteryou_menuset_30,afteryou_menuset_31,afteryou_menuset_32,afteryou_menuset_33,afteryou_menuset_34,afteryou_menuset_35,afteryou_menuset_36,afteryou_menuset_37,afteryou_menuset_38,afteryou_menuset_39,afteryou_menuset_40,afteryou_menuset_41,afteryou_menuset_42,afteryou_menuset_43,afteryou_menuset_44,afteryou_menuset_45,afteryou_menuset_46,afteryou_menuset_47,afteryou_menuset_48
                #
                global afteryoushop_mart_photo,afteryoushop_logo,afteryoushop_header,afteryoushop_showtable,afteryoushop_cat_1,afteryoushop_cat_2
                #
                afteryoushop_mart_photo = PhotoImage(file="image/Afteryou-shop/martphoto.png")
                afteryoushop_logo = PhotoImage(file="image/Afteryou-shop/logo-afteryou.png")
                afteryoushop_header = PhotoImage(file="image/Afteryou-shop/edge.png")
                afteryoushop_showtable = PhotoImage(file="image/Afteryou-shop/showtable.png")
                afteryoushop_cat_1 = PhotoImage(file="image/Afteryou-shop/cat1.png")
                afteryoushop_cat_2 = PhotoImage(file="image/Afteryou-shop/cat2.png")
                #
                afteryou_menuset_1 = PhotoImage(file="image/Afteryou-shop/menuset_1.png")
                afteryou_menuset_2 = PhotoImage(file="image/Afteryou-shop/menuset_2.png")
                afteryou_menuset_3 = PhotoImage(file="image/Afteryou-shop/menuset_3.png")
                afteryou_menuset_4 = PhotoImage(file="image/Afteryou-shop/menuset_4.png")
                afteryou_menuset_5 = PhotoImage(file="image/Afteryou-shop/menuset_5.png")
                afteryou_menuset_6 = PhotoImage(file="image/Afteryou-shop/menuset_6.png")
                afteryou_menuset_7 = PhotoImage(file="image/Afteryou-shop/menuset_7.png")
                afteryou_menuset_8 = PhotoImage(file="image/Afteryou-shop/menuset_8.png")
                afteryou_menuset_9 = PhotoImage(file="image/Afteryou-shop/menuset_9.png")
                afteryou_menuset_10 = PhotoImage(file="image/Afteryou-shop/menuset_10.png")
                afteryou_menuset_11 = PhotoImage(file="image/Afteryou-shop/menuset_11.png")
                afteryou_menuset_12 = PhotoImage(file="image/Afteryou-shop/menuset_12.png")
                afteryou_menuset_13 = PhotoImage(file="image/Afteryou-shop/menuset_13.png")
                afteryou_menuset_14 = PhotoImage(file="image/Afteryou-shop/menuset_14.png")
                afteryou_menuset_15 = PhotoImage(file="image/Afteryou-shop/menuset_15.png")
                afteryou_menuset_16 = PhotoImage(file="image/Afteryou-shop/menuset_16.png")
                afteryou_menuset_17 = PhotoImage(file="image/Afteryou-shop/menuset_17.png")
                afteryou_menuset_18 = PhotoImage(file="image/Afteryou-shop/menuset_18.png")
                afteryou_menuset_19 = PhotoImage(file="image/Afteryou-shop/menuset_19.png")
                afteryou_menuset_20 = PhotoImage(file="image/Afteryou-shop/menuset_20.png")
                afteryou_menuset_21 = PhotoImage(file="image/Afteryou-shop/menuset_21.png")
                afteryou_menuset_22 = PhotoImage(file="image/Afteryou-shop/menuset_22.png")
                afteryou_menuset_23 = PhotoImage(file="image/Afteryou-shop/menuset_23.png")
                afteryou_menuset_24 = PhotoImage(file="image/Afteryou-shop/menuset_24.png")
                afteryou_menuset_25 = PhotoImage(file="image/Afteryou-shop/menuset_25.png")
                afteryou_menuset_26 = PhotoImage(file="image/Afteryou-shop/menuset_26.png")
                afteryou_menuset_27 = PhotoImage(file="image/Afteryou-shop/menuset_27.png")
                afteryou_menuset_28 = PhotoImage(file="image/Afteryou-shop/menuset_28.png")
                afteryou_menuset_29 = PhotoImage(file="image/Afteryou-shop/menuset_29.png")
                afteryou_menuset_30 = PhotoImage(file="image/Afteryou-shop/menuset_30.png")
                afteryou_menuset_31 = PhotoImage(file="image/Afteryou-shop/menuset_31.png")
                afteryou_menuset_32 = PhotoImage(file="image/Afteryou-shop/menuset_32.png")
                afteryou_menuset_33 = PhotoImage(file="image/Afteryou-shop/menuset_33.png")
                afteryou_menuset_34 = PhotoImage(file="image/Afteryou-shop/menuset_34.png")
                afteryou_menuset_35 = PhotoImage(file="image/Afteryou-shop/menuset_35.png")
                afteryou_menuset_36 = PhotoImage(file="image/Afteryou-shop/menuset_36.png")
                afteryou_menuset_37 = PhotoImage(file="image/Afteryou-shop/menuset_37.png")
                afteryou_menuset_38 = PhotoImage(file="image/Afteryou-shop/menuset_38.png")
                afteryou_menuset_39 = PhotoImage(file="image/Afteryou-shop/menuset_39.png")
                afteryou_menuset_40 = PhotoImage(file="image/Afteryou-shop/menuset_40.png")
                afteryou_menuset_41 = PhotoImage(file="image/Afteryou-shop/menuset_41.png")
                afteryou_menuset_42 = PhotoImage(file="image/Afteryou-shop/menuset_42.png")
                afteryou_menuset_43 = PhotoImage(file="image/Afteryou-shop/menuset_43.png")
                afteryou_menuset_44 = PhotoImage(file="image/Afteryou-shop/menuset_44.png")
                afteryou_menuset_45 = PhotoImage(file="image/Afteryou-shop/menuset_45.png")
                afteryou_menuset_46 = PhotoImage(file="image/Afteryou-shop/menuset_46.png")
                afteryou_menuset_47 = PhotoImage(file="image/Afteryou-shop/menuset_47.png")
                afteryou_menuset_48 = PhotoImage(file="image/Afteryou-shop/menuset_48.png")
            def afteryoushop_addtocartprocess(ordername,price) :
                statusx = "NF"
                amount = 1
                conn = sqlite3.connect("projectdb.db")
                cursor = conn.cursor()
                sql = """
                        SELECT * FROM shop_afteryou_orderprocess
                        WHERE table_index = ? and amount > 0 and menu_name = ?"""
                cursor.execute(sql,[afteryoushop_tablex.get(),ordername])
                result = cursor.fetchone()
                conn.close()
                if result:
                    if ordername == result[1] :
                        newamount = int(result[3]) + 1
                        conn = sqlite3.connect("projectdb.db")
                        cursor = conn.cursor()
                        sql = """
                                UPDATE shop_afteryou_orderprocess
                                SET amount = ?
                                WHERE menu_name = ? """
                        cursor.execute(sql,[newamount,ordername])
                        conn.commit()
                        conn.close()
                        messagebox.showinfo("Admin","Added to cart")    
                else :
                    conn = sqlite3.connect("projectdb.db")
                    cursor = conn.cursor()
                    sql = """
                            INSERT INTO shop_afteryou_orderprocess 
                            values(?,?,?,?,?)"""
                    cursor.execute(sql,[afteryoushop_tablex.get(),ordername,price,amount,statusx])
                    conn.commit()
                    conn.close()
                    messagebox.showinfo("Admin","Added to cart")
                    conn = sqlite3.connect("projectdb.db")
                    cursor = conn.cursor()
                    sql = """
                                SELECT * FROM shop_afteryou_orderprocess
                                WHERE table_index=? """
                    cursor.execute(sql,[afteryoushop_tablex.get()])
                    result = cursor.fetchall()
                    nuborder = 0
                    for i,date in enumerate(result) :
                        nuborder = nuborder + 1
                    lenorder = StringVar()
                    lenorder.set(nuborder)
                    afteryoushop_amount_order["text"] = lenorder.get()
            def afteryoushop_click1(e) :
                if afteryoushop_indexpage.get() == "1" :
                    afteryoushop_frameone.destroy()
                elif afteryoushop_indexpage.get() == "2" :
                    afteryoushop_frametwo.destroy()
                elif afteryoushop_indexpage.get() == "3" :
                    afteryoushop_framethree.destroy()
                elif afteryoushop_indexpage.get() == "4" :
                    afteryoushop_framefour.destroy()
                elif afteryoushop_indexpage.get() == "5" :
                    afteryoushop_framefive.destroy()
                afteryoushop_cate_1["image"] = afteryoushop_cat_1
                afteryoushop_cate_2["image"] = afteryoushop_cat_2
                afteryoushop_cate_3["image"] = afteryoushop_cat_2
                afteryoushop_cate_4["image"] = afteryoushop_cat_2
                afteryoushop_cate_5["image"] = afteryoushop_cat_2
            def afteryoushop_click2(e) :
                if afteryoushop_indexpage.get() == "1" :
                    afteryoushop_frameone.destroy()
                elif afteryoushop_indexpage.get() == "2" :
                    afteryoushop_frametwo.destroy()
                elif afteryoushop_indexpage.get() == "3" :
                    afteryoushop_framethree.destroy()
                elif afteryoushop_indexpage.get() == "4" :
                    afteryoushop_framefour.destroy()
                elif afteryoushop_indexpage.get() == "5" :
                    afteryoushop_framefive.destroy()
                afteryoushop_cate_1["image"] = afteryoushop_cat_2
                afteryoushop_cate_2["image"] = afteryoushop_cat_1
                afteryoushop_cate_3["image"] = afteryoushop_cat_2
                afteryoushop_cate_4["image"] = afteryoushop_cat_2
                afteryoushop_cate_5["image"] = afteryoushop_cat_2
            def afteryoushop_click3(e) :
                if afteryoushop_indexpage.get() == "1" :
                    afteryoushop_frameone.destroy()
                elif afteryoushop_indexpage.get() == "2" :
                    afteryoushop_frametwo.destroy()
                elif afteryoushop_indexpage.get() == "3" :
                    afteryoushop_framethree.destroy()
                elif afteryoushop_indexpage.get() == "4" :
                    afteryoushop_framefour.destroy()
                elif afteryoushop_indexpage.get() == "5" :
                    afteryoushop_framefive.destroy()
                afteryoushop_cate_1["image"] = afteryoushop_cat_2
                afteryoushop_cate_2["image"] = afteryoushop_cat_2
                afteryoushop_cate_3["image"] = afteryoushop_cat_1
                afteryoushop_cate_4["image"] = afteryoushop_cat_2
                afteryoushop_cate_5["image"] = afteryoushop_cat_2
            def afteryoushop_click4(e) :
                if afteryoushop_indexpage.get() == "1" :
                    afteryoushop_frameone.destroy()
                elif afteryoushop_indexpage.get() == "2" :
                    afteryoushop_frametwo.destroy()
                elif afteryoushop_indexpage.get() == "3" :
                    afteryoushop_framethree.destroy()
                elif afteryoushop_indexpage.get() == "4" :
                    afteryoushop_framefour.destroy()
                elif afteryoushop_indexpage.get() == "5" :
                    afteryoushop_framefive.destroy()
                afteryoushop_cate_1["image"] = afteryoushop_cat_2
                afteryoushop_cate_2["image"] = afteryoushop_cat_2
                afteryoushop_cate_3["image"] = afteryoushop_cat_2
                afteryoushop_cate_4["image"] = afteryoushop_cat_1
                afteryoushop_cate_5["image"] = afteryoushop_cat_2
            def afteryoushop_click5(e) :
                if afteryoushop_indexpage.get() == "1" :
                    afteryoushop_frameone.destroy()
                elif afteryoushop_indexpage.get() == "2" :
                    afteryoushop_frametwo.destroy()
                elif afteryoushop_indexpage.get() == "3" :
                    afteryoushop_framethree.destroy()
                elif afteryoushop_indexpage.get() == "4" :
                    afteryoushop_framefour.destroy()
                elif afteryoushop_indexpage.get() == "5" :
                    afteryoushop_framefive.destroy()
                afteryoushop_cate_1["image"] = afteryoushop_cat_2
                afteryoushop_cate_2["image"] = afteryoushop_cat_2
                afteryoushop_cate_3["image"] = afteryoushop_cat_2
                afteryoushop_cate_4["image"] = afteryoushop_cat_2
                afteryoushop_cate_5["image"] = afteryoushop_cat_1
            def afteryoushop_frame_one() : # 1
                global afteryoushop_frameone
                afteryoushop_indexpage.set("1")
                afteryoushop_frameone = Frame(afteryoushop_frame,bg="#FFFFFF")
                afteryoushop_frameone.place(x=0,y=155,width=1000,height=545)
                # menu 1
                menu_1 = Label(afteryoushop_frameone,image=afteryou_menuset_1,bg="#FFFFFF")
                menu_1.place(x=0,y=20)
                # menu 2
                menu_2 = Label(afteryoushop_frameone,image=afteryou_menuset_2,bg="#FFFFFF")
                menu_2.place(x=200,y=20)
                # menu 3
                menu_3 = Label(afteryoushop_frameone,image=afteryou_menuset_3,bg="#FFFFFF")
                menu_3.place(x=400,y=20)
                # menu 4
                menu_4 = Label(afteryoushop_frameone,image=afteryou_menuset_4,bg="#FFFFFF")
                menu_4.place(x=600,y=20)
                # menu 5
                menu_5 = Label(afteryoushop_frameone,image=afteryou_menuset_5,bg="#FFFFFF")
                menu_5.place(x=800,y=20)
                # menu 6
                menu_6 = Label(afteryoushop_frameone,image=afteryou_menuset_6,bg="#FFFFFF")
                menu_6.place(x=0,y=285)
                # menu 7 
                menu_7 = Label(afteryoushop_frameone,image=afteryou_menuset_7,bg="#FFFFFF")
                menu_7.place(x=200,y=285)
                # menu 8
                menu_8 = Label(afteryoushop_frameone,image=afteryou_menuset_8,bg="#FFFFFF")
                menu_8.place(x=400,y=285)
                # menu 9
                menu_9 = Label(afteryoushop_frameone,image=afteryou_menuset_9,bg="#FFFFFF")
                menu_9.place(x=600,y=285)
                # menu 10
                menu_10 = Label(afteryoushop_frameone,image=afteryou_menuset_10,bg="#FFFFFF")
                menu_10.place(x=800,y=285)
                #
                mart_number_1 = Button(afteryoushop_frameone,image=afteryoushop_mart_photo,border=0,command=lambda:afteryoushop_addtocartprocess("Boba brown sugar","75"))
                mart_number_1.place(x=139,y=238)
                mart_number_2 = Button(afteryoushop_frameone,image=afteryoushop_mart_photo,border=0,command=lambda:afteryoushop_addtocartprocess("Boba yin yang","70"))
                mart_number_2.place(x=339,y=238)
                mart_number_3 = Button(afteryoushop_frameone,image=afteryoushop_mart_photo,border=0,command=lambda:afteryoushop_addtocartprocess("Strawberry Kakigori","180"))
                mart_number_3.place(x=539,y=238)
                mart_number_4 = Button(afteryoushop_frameone,image=afteryoushop_mart_photo,border=0,command=lambda:afteryoushop_addtocartprocess("Two tone Kakigori","199"))
                mart_number_4.place(x=739,y=238)
                mart_number_5 = Button(afteryoushop_frameone,image=afteryoushop_mart_photo,border=0,command=lambda:afteryoushop_addtocartprocess("Ferrero Toast","280"))
                mart_number_5.place(x=939,y=238)
                mart_number_6 = Button(afteryoushop_frameone,image=afteryoushop_mart_photo,border=0,command=lambda:afteryoushop_addtocartprocess("Chocolate Toast","180"))
                mart_number_6.place(x=139,y=503)
                mart_number_7 = Button(afteryoushop_frameone,image=afteryoushop_mart_photo,border=0,command=lambda:afteryoushop_addtocartprocess("Choc&Berry pancake","200"))
                mart_number_7.place(x=339,y=503)
                mart_number_8 = Button(afteryoushop_frameone,image=afteryoushop_mart_photo,border=0,command=lambda:afteryoushop_addtocartprocess("Nutella Pancake","175"))
                mart_number_8.place(x=539,y=503)
                mart_number_9 = Button(afteryoushop_frameone,image=afteryoushop_mart_photo,border=0,command=lambda:afteryoushop_addtocartprocess("Fudge cake","119"))
                mart_number_9.place(x=739,y=503)
                mart_number_10 = Button(afteryoushop_frameone,image=afteryoushop_mart_photo,border=0,command=lambda:afteryoushop_addtocartprocess("Souffle cheesecake","110"))
                mart_number_10.place(x=939,y=503)
            def afteryoushop_frame_two() : # 2
                global afteryoushop_frametwo
                afteryoushop_indexpage.set("2")
                afteryoushop_frametwo = Frame(afteryoushop_frame,bg="white")
                afteryoushop_frametwo.place(x=0,y=155,width=1000,height=545)
                # menu 1
                menu_1 = Label(afteryoushop_frametwo,image=afteryou_menuset_11,bg="#FFFFFF")
                menu_1.place(x=0,y=20)
                # menu 2
                menu_2 = Label(afteryoushop_frametwo,image=afteryou_menuset_12,bg="#FFFFFF")
                menu_2.place(x=200,y=20)
                # menu 3
                menu_3 = Label(afteryoushop_frametwo,image=afteryou_menuset_13,bg="#FFFFFF")
                menu_3.place(x=400,y=20)
                # menu 4
                menu_4 = Label(afteryoushop_frametwo,image=afteryou_menuset_14,bg="#FFFFFF")
                menu_4.place(x=600,y=20)
                # menu 5
                menu_5 = Label(afteryoushop_frametwo,image=afteryou_menuset_15,bg="#FFFFFF")
                menu_5.place(x=800,y=20)
                # menu 6
                menu_6 = Label(afteryoushop_frametwo,image=afteryou_menuset_16,bg="#FFFFFF")
                menu_6.place(x=0,y=285)
                # menu 7 
                menu_7 = Label(afteryoushop_frametwo,image=afteryou_menuset_17,bg="#FFFFFF")
                menu_7.place(x=200,y=285)
                # menu 8
                menu_8 = Label(afteryoushop_frametwo,image=afteryou_menuset_18,bg="#FFFFFF")
                menu_8.place(x=400,y=285)
                # menu 9
                menu_9 = Label(afteryoushop_frametwo,image=afteryou_menuset_19,bg="#FFFFFF")
                menu_9.place(x=600,y=285)
                # menu 10
                menu_10 = Label(afteryoushop_frametwo,image=afteryou_menuset_20,bg="#FFFFFF")
                menu_10.place(x=800,y=285)
                #
                mart_number_1 = Button(afteryoushop_frametwo,image=afteryoushop_mart_photo,border=0,command=lambda:afteryoushop_addtocartprocess("Hojicha kakigori","250"))
                mart_number_1.place(x=139,y=238)
                mart_number_2 = Button(afteryoushop_frametwo,image=afteryoushop_mart_photo,border=0,command=lambda:afteryoushop_addtocartprocess("Horlicks kakikori","250"))
                mart_number_2.place(x=339,y=238)
                mart_number_3 = Button(afteryoushop_frametwo,image=afteryoushop_mart_photo,border=0,command=lambda:afteryoushop_addtocartprocess("Strawberry Kakigori","180"))
                mart_number_3.place(x=539,y=238)
                mart_number_4 = Button(afteryoushop_frametwo,image=afteryoushop_mart_photo,border=0,command=lambda:afteryoushop_addtocartprocess("Two tone Kakigori","200"))
                mart_number_4.place(x=739,y=238)
                mart_number_5 = Button(afteryoushop_frametwo,image=afteryoushop_mart_photo,border=0,command=lambda:afteryoushop_addtocartprocess("Mango Kakigori","319"))
                mart_number_5.place(x=939,y=238)
                mart_number_6 = Button(afteryoushop_frametwo,image=afteryoushop_mart_photo,border=0,command=lambda:afteryoushop_addtocartprocess("Thai tea kakigori","195"))
                mart_number_6.place(x=139,y=503)
                mart_number_7 = Button(afteryoushop_frametwo,image=afteryoushop_mart_photo,border=0,command=lambda:afteryoushop_addtocartprocess("Milo volcano kakigori","200"))
                mart_number_7.place(x=339,y=503)
                mart_number_8 = Button(afteryoushop_frametwo,image=afteryoushop_mart_photo,border=0,command=lambda:afteryoushop_addtocartprocess("Conflake Cookie","120"))
                mart_number_8.place(x=539,y=503)
                mart_number_9 = Button(afteryoushop_frametwo,image=afteryoushop_mart_photo,border=0,command=lambda:afteryoushop_addtocartprocess("Raspberry Cookie","120"))
                mart_number_9.place(x=739,y=503)
                mart_number_10 = Button(afteryoushop_frametwo,image=afteryoushop_mart_photo,border=0,command=lambda:afteryoushop_addtocartprocess("Caramel Waffle bite","120"))
                mart_number_10.place(x=939,y=503)
            def afteryoushop_frame_three() : # 5
                global afteryoushop_framethree
                afteryoushop_indexpage.set("3")
                afteryoushop_framethree = Frame(afteryoushop_frame,bg="white")
                afteryoushop_framethree.place(x=0,y=155,width=1000,height=545)
                # menu 1
                menu_1 = Label(afteryoushop_framethree,image=afteryou_menuset_21,bg="#FFFFFF")
                menu_1.place(x=0,y=20)
                # menu 2
                menu_2 = Label(afteryoushop_framethree,image=afteryou_menuset_22,bg="#FFFFFF")
                menu_2.place(x=200,y=20)
                # menu 3
                menu_3 = Label(afteryoushop_framethree,image=afteryou_menuset_23,bg="#FFFFFF")
                menu_3.place(x=400,y=20)
                # menu 4
                menu_4 = Label(afteryoushop_framethree,image=afteryou_menuset_24,bg="#FFFFFF")
                menu_4.place(x=600,y=20)
                # menu 5
                menu_5 = Label(afteryoushop_framethree,image=afteryou_menuset_25,bg="#FFFFFF")
                menu_5.place(x=800,y=20)
                # menu 6
                menu_6 = Label(afteryoushop_framethree,image=afteryou_menuset_26,bg="#FFFFFF")
                menu_6.place(x=0,y=285)
                # menu 7 
                menu_7 = Label(afteryoushop_framethree,image=afteryou_menuset_27,bg="#FFFFFF")
                menu_7.place(x=200,y=285)
                # menu 8
                menu_8 = Label(afteryoushop_framethree,image=afteryou_menuset_28,bg="#FFFFFF")
                menu_8.place(x=400,y=285)
                # menu 9
                menu_9 = Label(afteryoushop_framethree,image=afteryou_menuset_29,bg="#FFFFFF")
                menu_9.place(x=600,y=285)
                # menu 10
                menu_10 = Label(afteryoushop_framethree,image=afteryou_menuset_30,bg="#FFFFFF")
                menu_10.place(x=800,y=285)
                #
                mart_number_1 = Button(afteryoushop_framethree,image=afteryoushop_mart_photo,border=0,command=lambda:afteryoushop_addtocartprocess("Boba brown sugar","75"))
                mart_number_1.place(x=139,y=238)
                mart_number_2 = Button(afteryoushop_framethree,image=afteryoushop_mart_photo,border=0,command=lambda:afteryoushop_addtocartprocess("Iced americano","69"))
                mart_number_2.place(x=339,y=238)
                mart_number_3 = Button(afteryoushop_framethree,image=afteryoushop_mart_photo,border=0,command=lambda:afteryoushop_addtocartprocess("Strawberry limeade","60"))
                mart_number_3.place(x=539,y=238)
                mart_number_4 = Button(afteryoushop_framethree,image=afteryoushop_mart_photo,border=0,command=lambda:afteryoushop_addtocartprocess("Matcha frappe","75"))
                mart_number_4.place(x=739,y=238)
                mart_number_5 = Button(afteryoushop_framethree,image=afteryoushop_mart_photo,border=0,command=lambda:afteryoushop_addtocartprocess("Nutella crunch coffee","80"))
                mart_number_5.place(x=939,y=238)
                mart_number_6 = Button(afteryoushop_framethree,image=afteryoushop_mart_photo,border=0,command=lambda:afteryoushop_addtocartprocess("Earl grey milk tea","70"))
                mart_number_6.place(x=139,y=503)
                mart_number_7 = Button(afteryoushop_framethree,image=afteryoushop_mart_photo,border=0,command=lambda:afteryoushop_addtocartprocess("World best iced","70"))
                mart_number_7.place(x=339,y=503)
                mart_number_8 = Button(afteryoushop_framethree,image=afteryoushop_mart_photo,border=0,command=lambda:afteryoushop_addtocartprocess("Lavender lychee soda","70"))
                mart_number_8.place(x=539,y=503)
                mart_number_9 = Button(afteryoushop_framethree,image=afteryoushop_mart_photo,border=0,command=lambda:afteryoushop_addtocartprocess("Pink lemonade","70"))
                mart_number_9.place(x=739,y=503)
                mart_number_10 = Button(afteryoushop_framethree,image=afteryoushop_mart_photo,border=0,command=lambda:afteryoushop_addtocartprocess("Strawberry frappe","80"))
                mart_number_10.place(x=939,y=503)
            def afteryoushop_frame_four() : # 4
                global afteryoushop_framefour
                afteryoushop_indexpage.set("4")
                afteryoushop_framefour = Frame(afteryoushop_frame,bg="white")
                afteryoushop_framefour.place(x=0,y=155,width=1000,height=545)
                # menu 1
                menu_1 = Label(afteryoushop_framefour,image=afteryou_menuset_10,bg="#FFFFFF")
                menu_1.place(x=0,y=20)
                # menu 2
                menu_2 = Label(afteryoushop_framefour,image=afteryou_menuset_32,bg="#FFFFFF")
                menu_2.place(x=200,y=20)
                # menu 3
                menu_3 = Label(afteryoushop_framefour,image=afteryou_menuset_33,bg="#FFFFFF")
                menu_3.place(x=400,y=20)
                # menu 4
                menu_4 = Label(afteryoushop_framefour,image=afteryou_menuset_34,bg="#FFFFFF")
                menu_4.place(x=600,y=20)
                # menu 5
                menu_5 = Label(afteryoushop_framefour,image=afteryou_menuset_35,bg="#FFFFFF")
                menu_5.place(x=800,y=20)
                # menu 6
                menu_6 = Label(afteryoushop_framefour,image=afteryou_menuset_36,bg="#FFFFFF")
                menu_6.place(x=0,y=285)
                # menu 7 
                menu_7 = Label(afteryoushop_framefour,image=afteryou_menuset_37,bg="#FFFFFF")
                menu_7.place(x=200,y=285)
                # menu 8
                menu_8 = Label(afteryoushop_framefour,image=afteryou_menuset_38,bg="#FFFFFF")
                menu_8.place(x=400,y=285)
                # menu 9
                menu_9 = Label(afteryoushop_framefour,image=afteryou_menuset_39,bg="#FFFFFF")
                menu_9.place(x=600,y=285)
                # menu 10
                menu_10 = Label(afteryoushop_framefour,image=afteryou_menuset_40,bg="#FFFFFF")
                menu_10.place(x=800,y=285)
                #
                mart_number_1 = Button(afteryoushop_framefour,image=afteryoushop_mart_photo,border=0,command=lambda:afteryoushop_addtocartprocess("Couffle cheesecake","110"))
                mart_number_1.place(x=139,y=238)
                mart_number_2 = Button(afteryoushop_framefour,image=afteryoushop_mart_photo,border=0,command=lambda:afteryoushop_addtocartprocess("Puddings","150"))
                mart_number_2.place(x=339,y=238)
                mart_number_3 = Button(afteryoushop_framefour,image=afteryoushop_mart_photo,border=0,command=lambda:afteryoushop_addtocartprocess("Strawberry crumble","129"))
                mart_number_3.place(x=539,y=238)
                mart_number_4 = Button(afteryoushop_framefour,image=afteryoushop_mart_photo,border=0,command=lambda:afteryoushop_addtocartprocess("Chocolate lava","115"))
                mart_number_4.place(x=739,y=238)
                mart_number_5 = Button(afteryoushop_framefour,image=afteryoushop_mart_photo,border=0,command=lambda:afteryoushop_addtocartprocess("Figgy pudding","110"))
                mart_number_5.place(x=939,y=238)
                mart_number_6 = Button(afteryoushop_framefour,image=afteryoushop_mart_photo,border=0,command=lambda:afteryoushop_addtocartprocess("Chocolate brownie","155"))
                mart_number_6.place(x=139,y=503)
                mart_number_7 = Button(afteryoushop_framefour,image=afteryoushop_mart_photo,border=0,command=lambda:afteryoushop_addtocartprocess("Queen B fudge cake","130"))
                mart_number_7.place(x=339,y=503)
                mart_number_8 = Button(afteryoushop_framefour,image=afteryoushop_mart_photo,border=0,command=lambda:afteryoushop_addtocartprocess("Strawberry platter","200"))
                mart_number_8.place(x=539,y=503)
                mart_number_9 = Button(afteryoushop_framefour,image=afteryoushop_mart_photo,border=0,command=lambda:afteryoushop_addtocartprocess("Choc&Berry pancake","180"))
                mart_number_9.place(x=739,y=503)
                mart_number_10 = Button(afteryoushop_framefour,image=afteryoushop_mart_photo,border=0,command=lambda:afteryoushop_addtocartprocess("Nutella Pancake","175"))
                mart_number_10.place(x=939,y=503)
            def afteryoushop_frame_five() : # 3
                global afteryoushop_framefive
                afteryoushop_indexpage.set("5")
                afteryoushop_framefive = Frame(afteryoushop_frame,bg="white")
                afteryoushop_framefive.place(x=0,y=155,width=1000,height=545)
                # menu 1
                menu_1 = Label(afteryoushop_framefive,image=afteryou_menuset_41,bg="#FFFFFF")
                menu_1.place(x=0,y=20)
                # menu 2
                menu_2 = Label(afteryoushop_framefive,image=afteryou_menuset_42,bg="#FFFFFF")
                menu_2.place(x=200,y=20)
                # menu 3
                menu_3 = Label(afteryoushop_framefive,image=afteryou_menuset_43,bg="#FFFFFF")
                menu_3.place(x=400,y=20)
                # menu 4
                menu_4 = Label(afteryoushop_framefive,image=afteryou_menuset_44,bg="#FFFFFF")
                menu_4.place(x=600,y=20)
                # menu 5
                menu_5 = Label(afteryoushop_framefive,image=afteryou_menuset_45,bg="#FFFFFF")
                menu_5.place(x=800,y=20)
                # menu 6
                menu_6 = Label(afteryoushop_framefive,image=afteryou_menuset_46,bg="#FFFFFF")
                menu_6.place(x=0,y=285)
                # menu 7 
                menu_7 = Label(afteryoushop_framefive,image=afteryou_menuset_47,bg="#FFFFFF")
                menu_7.place(x=200,y=285)
                # menu 8
                menu_8 = Label(afteryoushop_framefive,image=afteryou_menuset_48,bg="#FFFFFF")
                menu_8.place(x=400,y=285)
                #
                mart_number_1 = Button(afteryoushop_framefive,image=afteryoushop_mart_photo,border=0,command=lambda:afteryoushop_addtocartprocess("Thai Tea Toast","220"))
                mart_number_1.place(x=139,y=238)
                mart_number_2 = Button(afteryoushop_framefive,image=afteryoushop_mart_photo,border=0,command=lambda:afteryoushop_addtocartprocess("Shibuya honey toast","215"))
                mart_number_2.place(x=339,y=238)
                mart_number_3 = Button(afteryoushop_framefive,image=afteryoushop_mart_photo,border=0,command=lambda:afteryoushop_addtocartprocess("Ferrero Toast","280"))
                mart_number_3.place(x=539,y=238)
                mart_number_4 = Button(afteryoushop_framefive,image=afteryoushop_mart_photo,border=0,command=lambda:afteryoushop_addtocartprocess("Nutella Toast","240"))
                mart_number_4.place(x=739,y=238)
                mart_number_5 = Button(afteryoushop_framefive,image=afteryoushop_mart_photo,border=0,command=lambda:afteryoushop_addtocartprocess("Matcha Toast","230"))
                mart_number_5.place(x=939,y=238)
                mart_number_6 = Button(afteryoushop_framefive,image=afteryoushop_mart_photo,border=0,command=lambda:afteryoushop_addtocartprocess("Chocolate Toast","280"))
                mart_number_6.place(x=139,y=503)
                mart_number_7 = Button(afteryoushop_framefive,image=afteryoushop_mart_photo,border=0,command=lambda:afteryoushop_addtocartprocess("Sticky Toffee Toast","190"))
                mart_number_7.place(x=339,y=503)
                mart_number_8 = Button(afteryoushop_framefive,image=afteryoushop_mart_photo,border=0,command=lambda:afteryoushop_addtocartprocess("Cheddar Cheese Toast","250"))
                mart_number_8.place(x=539,y=503)
            def afteryoushop_menuframe() :
                global afteryoushop_cate_1 , afteryoushop_cate_2 , afteryoushop_cate_3 , afteryoushop_cate_4 , afteryoushop_cate_5 , afteryoushop_indexmenubar
                afteryoushop_menu_butt["state"] = "disabled"
                afteryoushop_button_orders["state"] = "active"
                if afteryoushop_indexmenubar.get() == "1" :
                    afteryoushop_allorder.destroy()
                elif afteryoushop_indexmenubar.get() == "0" :
                    pass
                afteryoushop_indexmenubar.set("0")
                if afteryoushop_indexpage.get() == "1" :
                    afteryoushop_frameone.destroy()
                elif afteryoushop_indexpage.get() == "2" :
                    afteryoushop_frametwo.destroy()
                elif afteryoushop_indexpage.get() == "3" :
                    afteryoushop_framethree.destroy()
                elif afteryoushop_indexpage.get() == "4" :
                    afteryoushop_framefour.destroy()
                elif afteryoushop_indexpage.get() == "5" :
                    afteryoushop_framefive.destroy()
                afteryoushop_frame_one()
                # category
                afteryoushop_cate_1 = Button(afteryoushop_frame,text="Recommand",image=afteryoushop_cat_1,compound="center",fg="#FFFFFF",border=0,bg="#FFFFFF",activebackground="#FFFFFF",font="Calibri 13",command=afteryoushop_frame_one)
                afteryoushop_cate_1.place(relx=0.375,y=110)
                #
                afteryoushop_cate_2 = Button(afteryoushop_frame,text="Kakigori",image=afteryoushop_cat_2,compound="center",fg="#FFFFFF",border=0,bg="#FFFFFF",activebackground="#FFFFFF",font="Calibri 13",command=afteryoushop_frame_two)
                afteryoushop_cate_2.place(relx=0.5,y=110)
                #
                afteryoushop_cate_3 = Button(afteryoushop_frame,text="Beverages",image=afteryoushop_cat_2,compound="center",fg="#FFFFFF",border=0,bg="#FFFFFF",activebackground="#FFFFFF",font="Calibri 13",command=afteryoushop_frame_three)
                afteryoushop_cate_3.place(relx=0.875,y=110)
                #
                afteryoushop_cate_4 = Button(afteryoushop_frame,text="Dessert",image=afteryoushop_cat_2,compound="center",fg="#FFFFFF",border=0,bg="#FFFFFF",activebackground="#FFFFFF",font="Calibri 13",command=afteryoushop_frame_four)
                afteryoushop_cate_4.place(relx=0.75,y=110)
                #
                afteryoushop_cate_5 = Button(afteryoushop_frame,text="Toast",image=afteryoushop_cat_2,compound="center",fg="#FFFFFF",border=0,bg="#FFFFFF",activebackground="#FFFFFF",font="Calibri 13",command=afteryoushop_frame_five)
                afteryoushop_cate_5.place(relx=0.625,y=110)
                # bind
                afteryoushop_cate_1.bind("<Button-1>",afteryoushop_click1)
                afteryoushop_cate_2.bind("<Button-1>",afteryoushop_click2)
                afteryoushop_cate_3.bind("<Button-1>",afteryoushop_click3)
                afteryoushop_cate_4.bind("<Button-1>",afteryoushop_click4)
                afteryoushop_cate_5.bind("<Button-1>",afteryoushop_click5)
            def afteryoushop_orderframe() :
                global afteryoushop_indexmenubar,afteryoushop_allorder
                afteryoushop_menu_butt["state"] = "active"
                afteryoushop_button_orders["state"] = "disabled"
                if afteryoushop_indexmenubar.get() == "0" :
                    pass
                elif afteryoushop_indexmenubar.get() == "1" :
                    afteryoushop_allorder.destroy()
                afteryoushop_indexmenubar.set("1")
                #
                afteryoushop_cate_1.place(relx=10)
                afteryoushop_cate_2.place(relx=10)
                afteryoushop_cate_3.place(relx=10)
                afteryoushop_cate_4.place(relx=10)
                afteryoushop_cate_5.place(relx=10)
                #
                afteryoushop_allorder = Frame(afteryoushop_frame,bg="#FFFFFF")
                afteryoushop_allorder.place(x=0,y=150,width=1000,height=550)
                afteryoushop_allorder.rowconfigure((0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20),weight=1)
                afteryoushop_allorder.columnconfigure((0,1,2,3),weight=1)
                def afteryoushop_payment(Total,cusinfo) :
                    def paymentprocess(total) :
                        ans = messagebox.askquestion("Admin","Are you sure you want to make a payment?") 
                        if ans == "yes" :
                            if float(cusinfo[7]) >= total :
                                shoppoint = 0
                                shoppoint = (total/20)//1
                                Label(paymentframe,image=yayoishop_payment_3,bg="white").place(x=40,y=0)
                                Label(paymentframe,text="Bill",bg="#EAE8E9",font="Calibri 25").place(x=60,y=10)
                                data = time.datetime.now()
                                time_now = (data.strftime("%x"))
                                Label(paymentframe,text=time_now,bg="#EAE8E9",font="Calibri 16").place(x=380,y=20)
                                Label(paymentframe,text="Menu",bg="#EAE8E9",font="Calibri 16 bold").place(x=60,y=70)
                                Label(paymentframe,text="Amount",bg="#EAE8E9",font="Calibri 16 bold").place(x=280,y=70)
                                Label(paymentframe,text="Price",bg="#EAE8E9",font="Calibri 16 bold").place(x=400,y=70)
                                yaix = 120
                                for i,data in enumerate(orderresult):
                                    if i < 6 :
                                        if data[4] == "F" :
                                            Label(paymentframe,text=data[1][0:25],bg="#EAE8E9",font="Calibri 16").place(x=60,y=yaix)
                                            Label(paymentframe,text=data[3],bg="#EAE8E9",font="Calibri 16").place(x=300,y=yaix)
                                            Label(paymentframe,text=data[2],bg="#EAE8E9",font="Calibri 16").place(x=400,y=yaix)
                                            yaix = yaix + 50
                                        else :
                                            pass
                                newbalance = (float(cusinfo[7])-total)//1
                                newpoint = (float(cusinfo[6])+shoppoint)//1
                                conn=sqlite3.connect("projectdb.db")
                                cursor = conn.cursor()
                                sql = """
                                            UPDATE customer_information
                                            SET money_customer=?,point_customer=?
                                            WHERE id_customer=?"""
                                cursor.execute(sql,[newbalance,newpoint,cusinfo[0]])
                                conn.commit()
                                messagebox.showinfo("Admin","Payment Successfully")
                                Label(paymentframe,text="VAT",bg="#EAE8E9",font="Calibri 16").place(x=60,y=410)
                                Label(paymentframe,text="7 %",bg="#EAE8E9",font="Calibri 16").place(x=400,y=410)
                                Label(paymentframe,text="Point",bg="#EAE8E9",font="Calibri 16").place(x=60,y=450)
                                Label(paymentframe,text="%0.f"%(shoppoint),bg="#EAE8E9",font="Calibri 16").place(x=400,y=450)
                                Label(paymentframe,text="Total Cost",bg="#EAE8E9",font="Calibri 16 bold").place(x=60,y=490)
                                Label(paymentframe,text="%0.f"%(total),bg="#EAE8E9",font="Calibri 16 bold").place(x=400,y=490)
                                Button(paymentframe,text="Exit",bg="#EAE8E9",font="Calibri 16 bold",command=quit).place(x=890,y=480)
                                afteryoushop_menu_butt["state"] = "disabled"
                                afteryoushop_button_staff["state"] = "disabled"
                                sql = """
                                        DELETE FROM shop_afteryou_orderprocess
                                        WHERE table_index=?"""
                                cursor.execute(sql,[table])   
                                conn.commit()
                                sql = """
                                        UPDATE shop_afteryou_table
                                        SET status=?,name=?,amount=?
                                        WHERE table_no=? """
                                cursor.execute(sql,['free','','',table])
                                conn.commit()
                                conn.close()
                            else :
                                messagebox.showwarning("Admin","Not enough money in your wallet \n Please make a payment at the counter")     
                                afteryoushop_menu_butt["state"] = "disabled"
                                afteryoushop_button_staff["state"] = "disabled"
                                Button(paymentframe,text="Exit",bg="#EAE8E9",font="Calibri 16 bold",command=quit).place(x=890,y=480)
                                conn=sqlite3.connect("projectdb.db")
                                cursor = conn.cursor()
                                sql = """
                                        DELETE FROM shop_afteryou_orderprocess
                                        WHERE table_index=?"""
                                cursor.execute(sql,[table])   
                                conn.commit()
                                sql = """
                                        UPDATE shop_afteryou_table
                                        SET status=?,name=?,amount=?
                                        WHERE table_no=? """
                                cursor.execute(sql,['free','','',table])
                                conn.commit()
                                conn.close()
                        else :
                            pass 
                    # name
                    paymentframe = Frame(afteryoushop_allorder,bg="#FFFFFF")
                    paymentframe.place(x=0,y=0,width=1000,height=550)
                    Label(paymentframe,image=yayoishop_payment_1,bg="white").place(x=40,y=0)
                    Label(paymentframe,image=yayoishop_payment_2,bg="white").place(x=510,y=0)
                    # widget
                    text_yourwallet = Label(paymentframe,text="Yourwallet",bg="#FFE6A7").place(x=60,y=10)
                    text_balance = Label(paymentframe,text="balance : %s"%(cusinfo[7]),bg="#FFE6A7").place(x=120,y=50)
                    text_point = Label(paymentframe,text="Point   : %s"%(cusinfo[6]),bg="#FFE6A7").place(x=120,y=90)
                    text_member = Label(paymentframe,text="membership : %s"%(cusinfo[5]),bg="#FFE6A7").place(x=120,y=130)
                    # 
                    text_Payout = Label(paymentframe,text="Payout",bg="#FFF2D0").place(x=60,y=210)
                    text_name = Label(paymentframe,text="Name : %s %s"%(cusinfo[1],cusinfo[2]),bg="#FFF2D0").place(x=120,y=260)
                    discount = 1
                    discountpercent = 0
                    if cusinfo[5] == "None" :
                        discount = 0.95
                        discountpercent = 5
                    elif cusinfo[5] == "Level1" :
                        discount = 0.9
                        discountpercent = 10
                    elif cusinfo[5] == "Level2" :
                        discount = 0.85
                        discountpercent = 15
                    text_tax = Label(paymentframe,text="Discount : %s Percent"%(discountpercent),bg="#FFF2D0").place(x=120,y=310)
                    total = (Total*discount*1.07)//1
                    text_total = Label(paymentframe,text="Total : %0.f Baht"%(total),bg="#FFF2D0").place(x=120,y=360)
                    text_point = Label(paymentframe,text="Point : %s"%((Totalx/20)//1),bg="#FFF2D0").place(x=120,y=410)
                    but_payment = Button(paymentframe,image=yayoishop_confirm,bg="#FFF2D0",fg="black",font="Calibri 16",border=0,command=lambda : paymentprocess(total))
                    but_payment.place(x=140,y=460)
                #
                Label(afteryoushop_allorder,text="Status",bg="#FFFFFF").grid(row=0,column=0)
                Label(afteryoushop_allorder,text="Menu",bg="#FFFFFF").grid(row=0,column=1)
                Label(afteryoushop_allorder,text="Amount",bg="#FFFFFF").grid(row=0,column=2)
                Label(afteryoushop_allorder,text="Price per unit",bg="#FFFFFF").grid(row=0,column=3)
                #
                conn = sqlite3.connect("projectdb.db")
                cursor = conn.cursor()
                sql = """
                        SELECT * FROM shop_afteryou_orderprocess 
                        WHERE table_index =?
                        """
                cursor.execute(sql,[afteryoushop_tablex.get()])
                orderresult= cursor.fetchall()
                conn.close()
                #
                Totalx = 0
                for i,data in enumerate(orderresult) :
                    if i < 10 :
                        if data[4] == "NF" : 
                            Label(afteryoushop_allorder,image=yayoishop_red_status,bg="#FFFFFF").grid(row=i+1,column=0)
                            Label(afteryoushop_allorder,text=data[1],bg="white").grid(row=i+1,column=1)
                            Label(afteryoushop_allorder,text=data[3],bg="white").grid(row=i+1,column=2)
                            Label(afteryoushop_allorder,text=data[2],bg="white").grid(row=i+1,column=3)
                        elif data[4] == "CF" : 
                            Label(afteryoushop_allorder,image=yayoishop_red_status,bg="#FFFFFF").grid(row=i+1,column=0)
                            Label(afteryoushop_allorder,text=data[1],bg="white").grid(row=i+1,column=1)
                            Label(afteryoushop_allorder,text=data[3],bg="white").grid(row=i+1,column=2)
                            Label(afteryoushop_allorder,text=data[2],bg="white").grid(row=i+1,column=3)
                        elif data[4] == "F" :
                            Label(afteryoushop_allorder,image=yayoishop_green_status,bg="#FFFFFF").grid(row=i+1,column=0)
                            Label(afteryoushop_allorder,text=data[1],bg="white").grid(row=i+1,column=1)
                            Label(afteryoushop_allorder,text=data[3],bg="white").grid(row=i+1,column=2)
                            Label(afteryoushop_allorder,text=data[2],bg="white").grid(row=i+1,column=3)
                            Totalx = Totalx + (int(data[3])*int(data[2]))
                conn = sqlite3.connect("projectdb.db")
                cursor = conn.cursor()
                sql = """
                            SELECT * FROM customer_information
                            WHERE firstname_customer=? """
                cursor.execute(sql,[customername])
                cusinfo = cursor.fetchone()
                Button(afteryoushop_allorder,text="Pay out",image=yayoishop_yayoishop_payout,command=lambda:afteryoushop_payment(Totalx,cusinfo),border=0,bg="white",activebackground="white").grid(row=20,column=1,columnspan=2)
            def staffcalling() :
                sql = """
                        UPDATE shop_afteryou_table
                        SET staffcall=?
                        WHERE table_no=?"""
                cursor.execute(sql,["yes",afteryoushop_tablex.get()])
                conn.commit()
            # start
            afteryoupicture()
            amt_table = "0"
            if afteryoushop_tablex.get() == "1" or afteryoushop_tablex.get() == "2" or afteryoushop_tablex.get() == "3" :
                amt_table = "1-2"
            elif afteryoushop_tablex.get() == "4" or afteryoushop_tablex.get() == "5" or afteryoushop_tablex.get() == "6":
                amt_table = "3-4"
            elif afteryoushop_tablex.get() == "7" or afteryoushop_tablex.get() == "8":
                amt_table = "5-6"
            afteryoushop_frame = Frame(afteryouroot,bg="#FFFFFF")
            afteryoushop_frame.place(x=0,y=0,height=700,width=1000)
            Label(afteryoushop_frame,image=afteryoushop_header,bg="#FFFFFF").place(x=-2,y=-5)
            Label(afteryoushop_frame,image=afteryoushop_logo,bg="#FFFFFF").place(x=40,y=0)
            # table no
            afteryoushop_table_no_wframe = Label(afteryoushop_frame,image=afteryoushop_showtable,bg="#DCC6AE")
            afteryoushop_table_no_wframe.place(relx=0.519,y=15)
            afteryoushop_text_no_people = Label(afteryoushop_frame,text="Table No : %s \n %s people"%(afteryoushop_tablex.get(),amt_table),bg="#FFEDD6",font="Calibri 16")
            afteryoushop_text_no_people.place(relx=0.54,y=23)
            #
            afteryoushop_order_wfame = Label(afteryoushop_frame,image=yayoishop_whiteframe_2,bg="#DCC6AE")
            afteryoushop_order_wfame.place(relx=0.7,y=15)
            afteryoushop_chk_wfame = Label(afteryoushop_frame,image=yayoishop_whiteframe_2,bg="#DCC6AE")
            afteryoushop_chk_wfame.place(relx=0.8,y=15)
            afteryoushop_staff_wfame = Label(afteryoushop_frame,image=yayoishop_whiteframe_2,bg="#DCC6AE")
            afteryoushop_staff_wfame.place(relx=0.9,y=15)
            #
            afteryoushop_button_orders = Button(afteryoushop_frame,image=yayoishop_but_orders,border=0,bg="#FBE5E5",activebackground="#FBE5E5",command=afteryoushop_orderframe)
            afteryoushop_button_orders.place(relx=0.814,y=27)
            #
            conn = sqlite3.connect("projectdb.db")
            cursor = conn.cursor()
            sql = """
                        SELECT * FROM shop_afteryou_orderprocess
                        WHERE table_index=? """
            cursor.execute(sql,[afteryoushop_tablex.get()])
            result = cursor.fetchall()
            nuborder = 0
            for i,date in enumerate(result) :
                nuborder = nuborder + 1
            lenorder = StringVar()
            lenorder.set(nuborder)
            #
            afteryoushop_amount_order = Label(afteryoushop_frame,border=0,bg="#FBE5E5",text=lenorder.get(),compound="center",font="bold")
            afteryoushop_amount_order.place(relx=0.855,y=19)
            # relx=0.752,y=17
            afteryoushop_button_staff = Button(afteryoushop_frame,image=yayoishop_but_staff,border=0,bg="#FBE5E5",activebackground="#FBE5E5",command=staffcalling)
            afteryoushop_button_staff.place(relx=0.92,y=26)
            # 1
            afteryoushop_menu_butt = Button(afteryoushop_frame,image=yayoishop_but_menu,border=0,bg="#FBE5E5",activebackground="#FBE5E5",command=afteryoushop_menuframe)
            afteryoushop_menu_butt.place(relx=0.72,y=28)
            afteryoushop_menuframe()
        def kyo_mainprogram(table,customername) :
            global kyoshop_indexpage,kyoshop_indexmenubar,kyoshop_tablex
            kyoroot = Frame(root,bg="white")
            kyoroot.place(x=0,y=0,width=1000,height=700)
            #
            conn = sqlite3.connect("projectdb.db")
            cursor = conn.cursor()
            sql = """
                        DELETE FROM shop_kyo_queue
                        WHERE q_name=? """
            cursor.execute(sql,[customername])
            conn.commit()
            username = customername
            kyoshop_indexpage = StringVar()
            kyoshop_indexpage.set("0")
            kyoshop_indexmenubar = StringVar()
            kyoshop_indexmenubar.set("0")
            kyoshop_tablex = StringVar()
            kyoshop_tablex.set(table)
            def kyopicture() :
                #
                global kyo_menuset_1, kyo_menuset_2 ,kyo_menuset_3 ,kyo_menuset_4,kyo_menuset_5,kyo_menuset_6,kyo_menuset_7,kyo_menuset_8,kyo_menuset_9,kyo_menuset_10,kyo_menuset_11,kyo_menuset_12,kyo_menuset_13,kyo_menuset_14,kyo_menuset_15,kyo_menuset_16,kyo_menuset_17,kyo_menuset_18,kyo_menuset_19,kyo_menuset_20,kyo_menuset_21,kyo_menuset_22,kyo_menuset_23,kyo_menuset_24,kyo_menuset_25,kyo_menuset_26,kyo_menuset_27,kyo_menuset_28,kyo_menuset_29,kyo_menuset_30,kyo_menuset_31,kyo_menuset_32,kyo_menuset_33,kyo_menuset_34,kyo_menuset_35,kyo_menuset_36,kyo_menuset_37,kyo_menuset_38,kyo_menuset_39,kyo_menuset_40,kyo_menuset_41,kyo_menuset_42,kyo_menuset_43,kyo_menuset_44,kyo_menuset_45,kyo_menuset_46,kyo_menuset_47,kyo_menuset_48,kyo_menuset_49,kyo_menuset_50
                #
                global kyoshop_mart_photo,kyoshop_logo,kyoshop_showtable,kyoshop_cat_1,kyoshop_cat_2
                #
                kyoshop_mart_photo = PhotoImage(file="image/Kyo-shop/martphoto.png")
                kyoshop_logo = PhotoImage(file="image/Kyo-shop/logo-kyo.png")
                kyoshop_showtable = PhotoImage(file="image/Kyo-shop/showtable.png")
                kyoshop_cat_1 = PhotoImage(file="image/Kyo-shop/cat1.png")
                kyoshop_cat_2 = PhotoImage(file="image/Kyo-shop/cat2.png")
                #
                kyo_menuset_1 = PhotoImage(file="image/Kyo-shop/menuset_1.png")
                kyo_menuset_2 = PhotoImage(file="image/Kyo-shop/menuset_2.png")
                kyo_menuset_3 = PhotoImage(file="image/Kyo-shop/menuset_3.png")
                kyo_menuset_4 = PhotoImage(file="image/Kyo-shop/menuset_4.png")
                kyo_menuset_5 = PhotoImage(file="image/Kyo-shop/menuset_5.png")
                kyo_menuset_6 = PhotoImage(file="image/Kyo-shop/menuset_6.png")
                kyo_menuset_7 = PhotoImage(file="image/Kyo-shop/menuset_7.png")
                kyo_menuset_8 = PhotoImage(file="image/Kyo-shop/menuset_8.png")
                kyo_menuset_9 = PhotoImage(file="image/Kyo-shop/menuset_9.png")
                kyo_menuset_10 = PhotoImage(file="image/Kyo-shop/menuset_10.png")
                kyo_menuset_11 = PhotoImage(file="image/Kyo-shop/menuset_11.png")
                kyo_menuset_12 = PhotoImage(file="image/Kyo-shop/menuset_12.png")
                kyo_menuset_13 = PhotoImage(file="image/Kyo-shop/menuset_13.png")
                kyo_menuset_14 = PhotoImage(file="image/Kyo-shop/menuset_14.png")
                kyo_menuset_15 = PhotoImage(file="image/Kyo-shop/menuset_15.png")
                kyo_menuset_16 = PhotoImage(file="image/Kyo-shop/menuset_16.png")
                kyo_menuset_17 = PhotoImage(file="image/Kyo-shop/menuset_17.png")
                kyo_menuset_18 = PhotoImage(file="image/Kyo-shop/menuset_18.png")
                kyo_menuset_19 = PhotoImage(file="image/Kyo-shop/menuset_19.png")
                kyo_menuset_20 = PhotoImage(file="image/Kyo-shop/menuset_20.png")
                kyo_menuset_21 = PhotoImage(file="image/Kyo-shop/menuset_21.png")
                kyo_menuset_22 = PhotoImage(file="image/Kyo-shop/menuset_22.png")
                kyo_menuset_23 = PhotoImage(file="image/Kyo-shop/menuset_23.png")
                kyo_menuset_24 = PhotoImage(file="image/Kyo-shop/menuset_24.png")
                kyo_menuset_25 = PhotoImage(file="image/Kyo-shop/menuset_25.png")
                kyo_menuset_26 = PhotoImage(file="image/Kyo-shop/menuset_26.png")
                kyo_menuset_27 = PhotoImage(file="image/Kyo-shop/menuset_27.png")
                kyo_menuset_28 = PhotoImage(file="image/Kyo-shop/menuset_28.png")
                kyo_menuset_29 = PhotoImage(file="image/Kyo-shop/menuset_29.png")
                kyo_menuset_30 = PhotoImage(file="image/Kyo-shop/menuset_30.png")
                kyo_menuset_31 = PhotoImage(file="image/Kyo-shop/menuset_31.png")
                kyo_menuset_32 = PhotoImage(file="image/Kyo-shop/menuset_32.png")
                kyo_menuset_33 = PhotoImage(file="image/Kyo-shop/menuset_33.png")
                kyo_menuset_34 = PhotoImage(file="image/Kyo-shop/menuset_34.png")
                kyo_menuset_35 = PhotoImage(file="image/Kyo-shop/menuset_35.png")
                kyo_menuset_36 = PhotoImage(file="image/Kyo-shop/menuset_36.png")
                kyo_menuset_37 = PhotoImage(file="image/Kyo-shop/menuset_37.png")
                kyo_menuset_38 = PhotoImage(file="image/Kyo-shop/menuset_38.png")
                kyo_menuset_39 = PhotoImage(file="image/Kyo-shop/menuset_39.png")
                kyo_menuset_40 = PhotoImage(file="image/Kyo-shop/menuset_40.png")
                kyo_menuset_41 = PhotoImage(file="image/Kyo-shop/menuset_41.png")
                kyo_menuset_42 = PhotoImage(file="image/Kyo-shop/menuset_42.png")
                kyo_menuset_43 = PhotoImage(file="image/Kyo-shop/menuset_43.png")
                kyo_menuset_44 = PhotoImage(file="image/Kyo-shop/menuset_44.png")
                kyo_menuset_45 = PhotoImage(file="image/Kyo-shop/menuset_45.png")
                kyo_menuset_46 = PhotoImage(file="image/Kyo-shop/menuset_46.png")
                kyo_menuset_47 = PhotoImage(file="image/Kyo-shop/menuset_47.png")
                kyo_menuset_48 = PhotoImage(file="image/Kyo-shop/menuset_48.png")
                kyo_menuset_49 = PhotoImage(file="image/Kyo-shop/menuset_49.png")
                kyo_menuset_50 = PhotoImage(file="image/Kyo-shop/menuset_50.png")
            def kyoshop_addtocartprocess(ordername,price) :
                statusx = "NF"
                amount = 1
                conn = sqlite3.connect("projectdb.db")
                cursor = conn.cursor()
                sql = """
                        SELECT * FROM shop_kyo_orderprocess
                        WHERE table_index = ? and amount > 0 and menu_name = ?"""
                cursor.execute(sql,[kyoshop_tablex.get(),ordername])
                result = cursor.fetchone()
                conn.close()
                if result:
                    if ordername == result[1] :
                        newamount = int(result[3]) + 1
                        conn = sqlite3.connect("projectdb.db")
                        cursor = conn.cursor()
                        sql = """
                                UPDATE shop_kyo_orderprocess
                                SET amount = ?
                                WHERE menu_name = ? """
                        cursor.execute(sql,[newamount,ordername])
                        conn.commit()
                        conn.close()
                        messagebox.showinfo("Admin","Added to cart")    
                else :
                    conn = sqlite3.connect("projectdb.db")
                    cursor = conn.cursor()
                    sql = """
                            INSERT INTO shop_kyo_orderprocess 
                            values(?,?,?,?,?)"""
                    cursor.execute(sql,[kyoshop_tablex.get(),ordername,price,amount,statusx])
                    conn.commit()
                    conn.close()
                    messagebox.showinfo("Admin","Added to cart")
                    conn = sqlite3.connect("projectdb.db")
                    cursor = conn.cursor()
                    sql = """
                                SELECT * FROM shop_kyo_orderprocess
                                WHERE table_index=? """
                    cursor.execute(sql,[kyoshop_tablex.get()])
                    result = cursor.fetchall()
                    nuborder = 0
                    for i,date in enumerate(result) :
                        nuborder = nuborder + 1
                    lenorder = StringVar()
                    lenorder.set(nuborder)
                    kyoshop_amount_order["text"] = lenorder.get()
            def kyoshop_click1(e) :
                if kyoshop_indexpage.get() == "1" :
                    kyoshop_frameone.destroy()
                elif kyoshop_indexpage.get() == "2" :
                    kyoshop_frametwo.destroy()
                elif kyoshop_indexpage.get() == "3" :
                    kyoshop_framethree.destroy()
                elif kyoshop_indexpage.get() == "4" :
                    kyoshop_framefour.destroy()
                elif kyoshop_indexpage.get() == "5" :
                    kyoshop_framefive.destroy()
                kyoshop_cate_1["image"] = kyoshop_cat_1
                kyoshop_cate_2["image"] = kyoshop_cat_2
                kyoshop_cate_3["image"] = kyoshop_cat_2
                kyoshop_cate_4["image"] = kyoshop_cat_2
                kyoshop_cate_5["image"] = kyoshop_cat_2
            def kyoshop_click2(e) :
                if kyoshop_indexpage.get() == "1" :
                    kyoshop_frameone.destroy()
                elif kyoshop_indexpage.get() == "2" :
                    kyoshop_frametwo.destroy()
                elif kyoshop_indexpage.get() == "3" :
                    kyoshop_framethree.destroy()
                elif kyoshop_indexpage.get() == "4" :
                    kyoshop_framefour.destroy()
                elif kyoshop_indexpage.get() == "5" :
                    kyoshop_framefive.destroy()
                kyoshop_cate_1["image"] = kyoshop_cat_2
                kyoshop_cate_2["image"] = kyoshop_cat_1
                kyoshop_cate_3["image"] = kyoshop_cat_2
                kyoshop_cate_4["image"] = kyoshop_cat_2
                kyoshop_cate_5["image"] = kyoshop_cat_2
            def kyoshop_click3(e) :
                if kyoshop_indexpage.get() == "1" :
                    kyoshop_frameone.destroy()
                elif kyoshop_indexpage.get() == "2" :
                    kyoshop_frametwo.destroy()
                elif kyoshop_indexpage.get() == "3" :
                    kyoshop_framethree.destroy()
                elif kyoshop_indexpage.get() == "4" :
                    kyoshop_framefour.destroy()
                elif kyoshop_indexpage.get() == "5" :
                    kyoshop_framefive.destroy()
                kyoshop_cate_1["image"] = kyoshop_cat_2
                kyoshop_cate_2["image"] = kyoshop_cat_2
                kyoshop_cate_3["image"] = kyoshop_cat_1
                kyoshop_cate_4["image"] = kyoshop_cat_2
                kyoshop_cate_5["image"] = kyoshop_cat_2
            def kyoshop_click4(e) :
                if kyoshop_indexpage.get() == "1" :
                    kyoshop_frameone.destroy()
                elif kyoshop_indexpage.get() == "2" :
                    kyoshop_frametwo.destroy()
                elif kyoshop_indexpage.get() == "3" :
                    kyoshop_framethree.destroy()
                elif kyoshop_indexpage.get() == "4" :
                    kyoshop_framefour.destroy()
                elif kyoshop_indexpage.get() == "5" :
                    kyoshop_framefive.destroy()
                kyoshop_cate_1["image"] = kyoshop_cat_2
                kyoshop_cate_2["image"] = kyoshop_cat_2
                kyoshop_cate_3["image"] = kyoshop_cat_2
                kyoshop_cate_4["image"] = kyoshop_cat_1
                kyoshop_cate_5["image"] = kyoshop_cat_2
            def kyoshop_click5(e) :
                if kyoshop_indexpage.get() == "1" :
                    kyoshop_frameone.destroy()
                elif kyoshop_indexpage.get() == "2" :
                    kyoshop_frametwo.destroy()
                elif kyoshop_indexpage.get() == "3" :
                    kyoshop_framethree.destroy()
                elif kyoshop_indexpage.get() == "4" :
                    kyoshop_framefour.destroy()
                elif kyoshop_indexpage.get() == "5" :
                    kyoshop_framefive.destroy()
                kyoshop_cate_1["image"] = kyoshop_cat_2
                kyoshop_cate_2["image"] = kyoshop_cat_2
                kyoshop_cate_3["image"] = kyoshop_cat_2
                kyoshop_cate_4["image"] = kyoshop_cat_2
                kyoshop_cate_5["image"] = kyoshop_cat_1
            def kyoshop_frame_one() : # 1
                global kyoshop_frameone
                kyoshop_indexpage.set("1")
                kyoshop_frameone = Frame(kyoshop_frame,bg="#FFFFFF")
                kyoshop_frameone.place(x=0,y=155,width=1000,height=545)
                # menu 1
                menu_1 = Label(kyoshop_frameone,image=kyo_menuset_1,bg="#FFFFFF")
                menu_1.place(x=0,y=20)
                # menu 2
                menu_2 = Label(kyoshop_frameone,image=kyo_menuset_2,bg="#FFFFFF")
                menu_2.place(x=200,y=20)
                # menu 3
                menu_3 = Label(kyoshop_frameone,image=kyo_menuset_3,bg="#FFFFFF")
                menu_3.place(x=400,y=20)
                # menu 4
                menu_4 = Label(kyoshop_frameone,image=kyo_menuset_4,bg="#FFFFFF")
                menu_4.place(x=600,y=20)
                # menu 5
                menu_5 = Label(kyoshop_frameone,image=kyo_menuset_5,bg="#FFFFFF")
                menu_5.place(x=800,y=20)
                # menu 6
                menu_6 = Label(kyoshop_frameone,image=kyo_menuset_6,bg="#FFFFFF")
                menu_6.place(x=0,y=285)
                # menu 7 
                menu_7 = Label(kyoshop_frameone,image=kyo_menuset_7,bg="#FFFFFF")
                menu_7.place(x=200,y=285)
                # menu 8
                menu_8 = Label(kyoshop_frameone,image=kyo_menuset_8,bg="#FFFFFF")
                menu_8.place(x=400,y=285)
                # menu 9
                menu_9 = Label(kyoshop_frameone,image=kyo_menuset_9,bg="#FFFFFF")
                menu_9.place(x=600,y=285)
                # menu 10
                menu_10 = Label(kyoshop_frameone,image=kyo_menuset_10,bg="#FFFFFF")
                menu_10.place(x=800,y=285)
                #
                mart_number_1 = Button(kyoshop_frameone,image=kyoshop_mart_photo,border=0,command=lambda:kyoshop_addtocartprocess("Mango Granita","165"))
                mart_number_1.place(x=139,y=238) #yk
                mart_number_2 = Button(kyoshop_frameone,image=kyoshop_mart_photo,border=0,command=lambda:kyoshop_addtocartprocess("Strawberry Yogurt","155"))
                mart_number_2.place(x=339,y=238)
                mart_number_3 = Button(kyoshop_frameone,image=kyoshop_mart_photo,border=0,command=lambda:kyoshop_addtocartprocess("Matcha Soft","165"))
                mart_number_3.place(x=539,y=238)
                mart_number_4 = Button(kyoshop_frameone,image=kyoshop_mart_photo,border=0,command=lambda:kyoshop_addtocartprocess("Chocolate Melt","145"))
                mart_number_4.place(x=739,y=238)
                mart_number_5 = Button(kyoshop_frameone,image=kyoshop_mart_photo,border=0,command=lambda:kyoshop_addtocartprocess("Mango Blossom","165"))
                mart_number_5.place(x=939,y=238)
                mart_number_6 = Button(kyoshop_frameone,image=kyoshop_mart_photo,border=0,command=lambda:kyoshop_addtocartprocess("Strawberry","145"))
                mart_number_6.place(x=139,y=503)
                mart_number_7 = Button(kyoshop_frameone,image=kyoshop_mart_photo,border=0,command=lambda:kyoshop_addtocartprocess("Ravioli","199"))
                mart_number_7.place(x=339,y=503)
                mart_number_8 = Button(kyoshop_frameone,image=kyoshop_mart_photo,border=0,command=lambda:kyoshop_addtocartprocess("Cocao Story","285"))
                mart_number_8.place(x=539,y=503)
                mart_number_9 = Button(kyoshop_frameone,image=kyoshop_mart_photo,border=0,command=lambda:kyoshop_addtocartprocess("Soba","230"))
                mart_number_9.place(x=739,y=503)
                mart_number_10 = Button(kyoshop_frameone,image=kyoshop_mart_photo,border=0,command=lambda:kyoshop_addtocartprocess("BBQ","279"))
                mart_number_10.place(x=939,y=503)
            def kyoshop_frame_two() : # 2
                global kyoshop_frametwo
                kyoshop_indexpage.set("2")
                kyoshop_frametwo = Frame(kyoshop_frame,bg="white")
                kyoshop_frametwo.place(x=0,y=155,width=1000,height=545)
                # menu 1
                menu_1 = Label(kyoshop_frametwo,image=kyo_menuset_11,bg="#FFFFFF")
                menu_1.place(x=0,y=20)
                # menu 2
                menu_2 = Label(kyoshop_frametwo,image=kyo_menuset_12,bg="#FFFFFF")
                menu_2.place(x=200,y=20)
                # menu 3
                menu_3 = Label(kyoshop_frametwo,image=kyo_menuset_13,bg="#FFFFFF")
                menu_3.place(x=400,y=20)
                # menu 4
                menu_4 = Label(kyoshop_frametwo,image=kyo_menuset_14,bg="#FFFFFF")
                menu_4.place(x=600,y=20)
                # menu 5
                menu_5 = Label(kyoshop_frametwo,image=kyo_menuset_15,bg="#FFFFFF")
                menu_5.place(x=800,y=20)
                # menu 6
                menu_6 = Label(kyoshop_frametwo,image=kyo_menuset_16,bg="#FFFFFF")
                menu_6.place(x=0,y=285)
                # menu 7 
                menu_7 = Label(kyoshop_frametwo,image=kyo_menuset_17,bg="#FFFFFF")
                menu_7.place(x=200,y=285)
                # menu 8
                menu_8 = Label(kyoshop_frametwo,image=kyo_menuset_18,bg="#FFFFFF")
                menu_8.place(x=400,y=285)
                # menu 9
                menu_9 = Label(kyoshop_frametwo,image=kyo_menuset_19,bg="#FFFFFF")
                menu_9.place(x=600,y=285)
                # menu 10
                menu_10 = Label(kyoshop_frametwo,image=kyo_menuset_20,bg="#FFFFFF")
                menu_10.place(x=800,y=285)
                #
                mart_number_1 = Button(kyoshop_frametwo,image=kyoshop_mart_photo,border=0,command=lambda:kyoshop_addtocartprocess("Mango Granita","165"))
                mart_number_1.place(x=139,y=245)
                mart_number_2 = Button(kyoshop_frametwo,image=kyoshop_mart_photo,border=0,command=lambda:kyoshop_addtocartprocess("Strawberry Yogurt","155"))
                mart_number_2.place(x=337,y=245) 
                mart_number_3 = Button(kyoshop_frametwo,image=kyoshop_mart_photo,border=0,command=lambda:kyoshop_addtocartprocess("Matcha Soft","165"))
                mart_number_3.place(x=539,y=238)
                mart_number_4 = Button(kyoshop_frametwo,image=kyoshop_mart_photo,border=0,command=lambda:kyoshop_addtocartprocess("Matcha Coco","175"))
                mart_number_4.place(x=739,y=246)
                mart_number_5 = Button(kyoshop_frametwo,image=kyoshop_mart_photo,border=0,command=lambda:kyoshop_addtocartprocess("Berry Cheesecake","180"))
                mart_number_5.place(x=937,y=238)
                mart_number_6 = Button(kyoshop_frametwo,image=kyoshop_mart_photo,border=0,command=lambda:kyoshop_addtocartprocess("Goma Sesame","160"))
                mart_number_6.place(x=137,y=503)
                mart_number_7 = Button(kyoshop_frametwo,image=kyoshop_mart_photo,border=0,command=lambda:kyoshop_addtocartprocess("Duo Anmitsu","245"))
                mart_number_7.place(x=339,y=503)
                mart_number_8 = Button(kyoshop_frametwo,image=kyoshop_mart_photo,border=0,command=lambda:kyoshop_addtocartprocess("Berry Yogurt","190"))
                mart_number_8.place(x=539,y=503)
                mart_number_9 = Button(kyoshop_frametwo,image=kyoshop_mart_photo,border=0,command=lambda:kyoshop_addtocartprocess("Warabi Mochi","195"))
                mart_number_9.place(x=739,y=503)
                mart_number_10 = Button(kyoshop_frametwo,image=kyoshop_mart_photo,border=0,command=lambda:kyoshop_addtocartprocess("Sumi Matcha","195"))
                mart_number_10.place(x=939,y=503)
            def kyoshop_frame_three() : # 5
                global kyoshop_framethree
                kyoshop_indexpage.set("3")
                kyoshop_framethree = Frame(kyoshop_frame,bg="white")
                kyoshop_framethree.place(x=0,y=155,width=1000,height=545)
                # menu 1
                menu_1 = Label(kyoshop_framethree,image=kyo_menuset_21,bg="#FFFFFF")
                menu_1.place(x=0,y=20)
                # menu 2
                menu_2 = Label(kyoshop_framethree,image=kyo_menuset_22,bg="#FFFFFF")
                menu_2.place(x=200,y=20)
                # menu 3
                menu_3 = Label(kyoshop_framethree,image=kyo_menuset_23,bg="#FFFFFF")
                menu_3.place(x=400,y=20)
                # menu 4
                menu_4 = Label(kyoshop_framethree,image=kyo_menuset_24,bg="#FFFFFF")
                menu_4.place(x=600,y=20)
                # menu 5
                menu_5 = Label(kyoshop_framethree,image=kyo_menuset_25,bg="#FFFFFF")
                menu_5.place(x=800,y=20)
                # menu 6
                menu_6 = Label(kyoshop_framethree,image=kyo_menuset_26,bg="#FFFFFF")
                menu_6.place(x=0,y=285)
                # menu 7 
                menu_7 = Label(kyoshop_framethree,image=kyo_menuset_27,bg="#FFFFFF")
                menu_7.place(x=200,y=285)
                # menu 8
                menu_8 = Label(kyoshop_framethree,image=kyo_menuset_28,bg="#FFFFFF")
                menu_8.place(x=400,y=285)
                # menu 9
                menu_9 = Label(kyoshop_framethree,image=kyo_menuset_29,bg="#FFFFFF")
                menu_9.place(x=600,y=285)
                # menu 10
                menu_10 = Label(kyoshop_framethree,image=kyo_menuset_30,bg="#FFFFFF")
                menu_10.place(x=800,y=285)
                #
                mart_number_1 = Button(kyoshop_framethree,image=kyoshop_mart_photo,border=0,command=lambda:kyoshop_addtocartprocess("Zen","217"))
                mart_number_1.place(x=136,y=238)
                mart_number_2 = Button(kyoshop_framethree,image=kyoshop_mart_photo,border=0,command=lambda:kyoshop_addtocartprocess("Gion","215"))
                mart_number_2.place(x=337,y=232)
                mart_number_3 = Button(kyoshop_framethree,image=kyoshop_mart_photo,border=0,command=lambda:kyoshop_addtocartprocess("Milky","189"))
                mart_number_3.place(x=537,y=239)
                mart_number_4 = Button(kyoshop_framethree,image=kyoshop_mart_photo,border=0,command=lambda:kyoshop_addtocartprocess("Kyo roll","189"))
                mart_number_4.place(x=736,y=241)
                mart_number_5 = Button(kyoshop_framethree,image=kyoshop_mart_photo,border=0,command=lambda:kyoshop_addtocartprocess("Valrhona","185"))
                mart_number_5.place(x=940,y=238)
                mart_number_6 = Button(kyoshop_framethree,image=kyoshop_mart_photo,border=0,command=lambda:kyoshop_addtocartprocess("Thai Roll","180"))
                mart_number_6.place(x=139,y=503)
                mart_number_7 = Button(kyoshop_framethree,image=kyoshop_mart_photo,border=0,command=lambda:kyoshop_addtocartprocess("Mango Mania","200"))
                mart_number_7.place(x=339,y=503)
                mart_number_8 = Button(kyoshop_framethree,image=kyoshop_mart_photo,border=0,command=lambda:kyoshop_addtocartprocess("Custard Pudding","95"))
                mart_number_8.place(x=539,y=503)
                mart_number_9 = Button(kyoshop_framethree,image=kyoshop_mart_photo,border=0,command=lambda:kyoshop_addtocartprocess("Warabi Mochi","185"))
                mart_number_9.place(x=739,y=503)
                mart_number_10 = Button(kyoshop_framethree,image=kyoshop_mart_photo,border=0,command=lambda:kyoshop_addtocartprocess("Signature Soft Cream","140"))
                mart_number_10.place(x=936,y=503)
            def kyoshop_frame_four() : # 4
                global kyoshop_framefour
                kyoshop_indexpage.set("4")
                kyoshop_framefour = Frame(kyoshop_frame,bg="white")
                kyoshop_framefour.place(x=0,y=155,width=1000,height=545)
                # menu 1
                menu_1 = Label(kyoshop_framefour,image=kyo_menuset_31,bg="#FFFFFF")
                menu_1.place(x=0,y=20)
                # menu 2
                menu_2 = Label(kyoshop_framefour,image=kyo_menuset_32,bg="#FFFFFF")
                menu_2.place(x=200,y=20)
                # menu 3
                menu_3 = Label(kyoshop_framefour,image=kyo_menuset_33,bg="#FFFFFF")
                menu_3.place(x=400,y=20)
                # menu 4
                menu_4 = Label(kyoshop_framefour,image=kyo_menuset_34,bg="#FFFFFF")
                menu_4.place(x=600,y=20)
                # menu 5
                menu_5 = Label(kyoshop_framefour,image=kyo_menuset_35,bg="#FFFFFF")
                menu_5.place(x=800,y=20)
                # menu 6
                menu_6 = Label(kyoshop_framefour,image=kyo_menuset_36,bg="#FFFFFF")
                menu_6.place(x=0,y=285)
                # menu 7 
                menu_7 = Label(kyoshop_framefour,image=kyo_menuset_37,bg="#FFFFFF")
                menu_7.place(x=200,y=285)
                # menu 8
                menu_8 = Label(kyoshop_framefour,image=kyo_menuset_38,bg="#FFFFFF")
                menu_8.place(x=400,y=285)
                # menu 9
                menu_9 = Label(kyoshop_framefour,image=kyo_menuset_39,bg="#FFFFFF")
                menu_9.place(x=600,y=285)
                # menu 10
                menu_10 = Label(kyoshop_framefour,image=kyo_menuset_40,bg="#FFFFFF")
                menu_10.place(x=800,y=285)
                #
                mart_number_1 = Button(kyoshop_framefour,image=kyoshop_mart_photo,border=0,command=lambda:kyoshop_addtocartprocess("Oops Strawberry","210"))
                mart_number_1.place(x=139,y=238)
                mart_number_2 = Button(kyoshop_framefour,image=kyoshop_mart_photo,border=0,command=lambda:kyoshop_addtocartprocess("Ravioli","199"))
                mart_number_2.place(x=339,y=238)
                mart_number_3 = Button(kyoshop_framefour,image=kyoshop_mart_photo,border=0,command=lambda:kyoshop_addtocartprocess("Cocao Story","285"))
                mart_number_3.place(x=539,y=238)
                mart_number_4 = Button(kyoshop_framefour,image=kyoshop_mart_photo,border=0,command=lambda:kyoshop_addtocartprocess("Soba","230"))
                mart_number_4.place(x=739,y=238)
                mart_number_5 = Button(kyoshop_framefour,image=kyoshop_mart_photo,border=0,command=lambda:kyoshop_addtocartprocess("BBQ","279"))
                mart_number_5.place(x=939,y=238)
                mart_number_6 = Button(kyoshop_framefour,image=kyoshop_mart_photo,border=0,command=lambda:kyoshop_addtocartprocess("Mont Blanc","195"))
                mart_number_6.place(x=139,y=503)
                mart_number_7 = Button(kyoshop_framefour,image=kyoshop_mart_photo,border=0,command=lambda:kyoshop_addtocartprocess("Zen Garden","299"))
                mart_number_7.place(x=339,y=503)
                mart_number_8 = Button(kyoshop_framefour,image=kyoshop_mart_photo,border=0,command=lambda:kyoshop_addtocartprocess("Momo Pop","65"))
                mart_number_8.place(x=539,y=503)
                mart_number_9 = Button(kyoshop_framefour,image=kyoshop_mart_photo,border=0,command=lambda:kyoshop_addtocartprocess("Yuzu Float","75"))
                mart_number_9.place(x=739,y=503)
                mart_number_10 = Button(kyoshop_framefour,image=kyoshop_mart_photo,border=0,command=lambda:kyoshop_addtocartprocess("Strawberry Higiscus","89"))
                mart_number_10.place(x=937,y=503)
            def kyoshop_frame_five() : # 3
                global kyoshop_framefive
                kyoshop_indexpage.set("5")
                kyoshop_framefive = Frame(kyoshop_frame,bg="white")
                kyoshop_framefive.place(x=0,y=155,width=1000,height=545)
                # menu 1
                menu_1 = Label(kyoshop_framefive,image=kyo_menuset_41,bg="#FFFFFF")
                menu_1.place(x=0,y=20)
                # menu 2
                menu_2 = Label(kyoshop_framefive,image=kyo_menuset_42,bg="#FFFFFF")
                menu_2.place(x=200,y=20)
                # menu 3
                menu_3 = Label(kyoshop_framefive,image=kyo_menuset_43,bg="#FFFFFF")
                menu_3.place(x=400,y=20)
                # menu 4
                menu_4 = Label(kyoshop_framefive,image=kyo_menuset_44,bg="#FFFFFF")
                menu_4.place(x=600,y=20)
                # menu 5
                menu_5 = Label(kyoshop_framefive,image=kyo_menuset_45,bg="#FFFFFF")
                menu_5.place(x=800,y=20)
                # menu 6
                menu_6 = Label(kyoshop_framefive,image=kyo_menuset_46,bg="#FFFFFF")
                menu_6.place(x=0,y=285)
                # menu 7 
                menu_7 = Label(kyoshop_framefive,image=kyo_menuset_47,bg="#FFFFFF")
                menu_7.place(x=200,y=285)
                # menu 8
                menu_8 = Label(kyoshop_framefive,image=kyo_menuset_48,bg="#FFFFFF")
                menu_8.place(x=400,y=285)
                # menu 9
                menu_9 = Label(kyoshop_framefive,image=kyo_menuset_49,bg="#FFFFFF")
                menu_9.place(x=600,y=285)
                # menu 10
                menu_10 = Label(kyoshop_framefive,image=kyo_menuset_50,bg="#FFFFFF")
                menu_10.place(x=800,y=285)
                #
                mart_number_1 = Button(kyoshop_framefive,image=kyoshop_mart_photo,border=0,command=lambda:kyoshop_addtocartprocess("Matcha Deluxe","199"))
                mart_number_1.place(x=137,y=238)
                mart_number_2 = Button(kyoshop_framefive,image=kyoshop_mart_photo,border=0,command=lambda:kyoshop_addtocartprocess("Chocolate Melt","145"))
                mart_number_2.place(x=339,y=238)
                mart_number_3 = Button(kyoshop_framefive,image=kyoshop_mart_photo,border=0,command=lambda:kyoshop_addtocartprocess("Mango Blossom","165"))
                mart_number_3.place(x=539,y=238)
                mart_number_4 = Button(kyoshop_framefive,image=kyoshop_mart_photo,border=0,command=lambda:kyoshop_addtocartprocess("Yubari Melon","170"))
                mart_number_4.place(x=739,y=238)
                mart_number_5 = Button(kyoshop_framefive,image=kyoshop_mart_photo,border=0,command=lambda:kyoshop_addtocartprocess("Mutsuri","160"))
                mart_number_5.place(x=939,y=238)
                mart_number_6 = Button(kyoshop_framefive,image=kyoshop_mart_photo,border=0,command=lambda:kyoshop_addtocartprocess("Goma","149"))
                mart_number_6.place(x=139,y=503)
                mart_number_7 = Button(kyoshop_framefive,image=kyoshop_mart_photo,border=0,command=lambda:kyoshop_addtocartprocess("Strawberry","145"))
                mart_number_7.place(x=339,y=503)
                mart_number_8 = Button(kyoshop_framefive,image=kyoshop_mart_photo,border=0,command=lambda:kyoshop_addtocartprocess("Hojicha Latte","75"))
                mart_number_8.place(x=539,y=503)
                mart_number_9 = Button(kyoshop_framefive,image=kyoshop_mart_photo,border=0,command=lambda:kyoshop_addtocartprocess("Matcha Latte","80"))
                mart_number_9.place(x=739,y=503)
                mart_number_10 = Button(kyoshop_framefive,image=kyoshop_mart_photo,border=0,command=lambda:kyoshop_addtocartprocess("Chocolate","65"))
                mart_number_10.place(x=939,y=503)
            def kyoshop_menuframe() :
                global kyoshop_cate_1 , kyoshop_cate_2 , kyoshop_cate_3 , kyoshop_cate_4 , kyoshop_cate_5 , kyoshop_indexmenubar
                kyoshop_menu_butt["state"] = "disabled"
                kyoshop_button_orders["state"] = "active"
                if kyoshop_indexmenubar.get() == "1" :
                    kyoshop_allorder.destroy()
                elif kyoshop_indexmenubar.get() == "0" :
                    pass
                kyoshop_indexmenubar.set("0")
                if kyoshop_indexpage.get() == "1" :
                    kyoshop_frameone.destroy()
                elif kyoshop_indexpage.get() == "2" :
                    kyoshop_frametwo.destroy()
                elif kyoshop_indexpage.get() == "3" :
                    kyoshop_framethree.destroy()
                elif kyoshop_indexpage.get() == "4" :
                    kyoshop_framefour.destroy()
                elif kyoshop_indexpage.get() == "5" :
                    kyoshop_framefive.destroy()
                kyoshop_frame_one()
                # category
                kyoshop_cate_1 = Button(kyoshop_frame,text="Recommand",image=kyoshop_cat_1,compound="center",fg="#FFFFFF",border=0,bg="#FFFFFF",activebackground="#FFFFFF",font="Calibri 13",command=kyoshop_frame_one)
                kyoshop_cate_1.place(relx=0.375,y=110)
                #
                kyoshop_cate_2 = Button(kyoshop_frame,text="FRESH",image=kyoshop_cat_2,compound="center",fg="#FFFFFF",border=0,bg="#FFFFFF",activebackground="#FFFFFF",font="Calibri 13",command=kyoshop_frame_two)
                kyoshop_cate_2.place(relx=0.5,y=110)
                #
                kyoshop_cate_3 = Button(kyoshop_frame,text="ROLL SET",image=kyoshop_cat_2,compound="center",fg="#FFFFFF",border=0,bg="#FFFFFF",activebackground="#FFFFFF",font="Calibri 13",command=kyoshop_frame_three)
                kyoshop_cate_3.place(relx=0.625,y=110)
                #
                kyoshop_cate_4 = Button(kyoshop_frame,text="KYO BAR",image=kyoshop_cat_2,compound="center",fg="#FFFFFF",border=0,bg="#FFFFFF",activebackground="#FFFFFF",font="Calibri 13",command=kyoshop_frame_four)
                kyoshop_cate_4.place(relx=0.75,y=110)
                #
                kyoshop_cate_5 = Button(kyoshop_frame,text="SOFT",image=kyoshop_cat_2,compound="center",fg="#FFFFFF",border=0,bg="#FFFFFF",activebackground="#FFFFFF",font="Calibri 13",command=kyoshop_frame_five)
                kyoshop_cate_5.place(relx=0.875,y=110)
                # bind
                kyoshop_cate_1.bind("<Button-1>",kyoshop_click1)
                kyoshop_cate_2.bind("<Button-1>",kyoshop_click2)
                kyoshop_cate_3.bind("<Button-1>",kyoshop_click3)
                kyoshop_cate_4.bind("<Button-1>",kyoshop_click4)
                kyoshop_cate_5.bind("<Button-1>",kyoshop_click5)
            def kyoshop_orderframe() :
                global kyoshop_indexmenubar,kyoshop_allorder
                kyoshop_menu_butt["state"] = "active"
                kyoshop_button_orders["state"] = "disabled"
                if kyoshop_indexmenubar.get() == "0" :
                    pass
                elif kyoshop_indexmenubar.get() == "1" :
                    kyoshop_allorder.destroy()
                kyoshop_indexmenubar.set("1")
                #
                kyoshop_cate_1.place(relx=10)
                kyoshop_cate_2.place(relx=10)
                kyoshop_cate_3.place(relx=10)
                kyoshop_cate_4.place(relx=10)
                kyoshop_cate_5.place(relx=10)
                #
                kyoshop_allorder = Frame(kyoshop_frame,bg="#FFFFFF")
                kyoshop_allorder.place(x=0,y=150,width=1000,height=550)
                kyoshop_allorder.rowconfigure((0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20),weight=1)
                kyoshop_allorder.columnconfigure((0,1,2,3),weight=1)
                #
                def kyoshop_payment(Total,cusinfo) :
                    def paymentprocess(total) :
                        ans = messagebox.askquestion("Admin","Are you sure you want to make a payment?")     
                        if ans == "yes" :
                            if float(cusinfo[7]) >= total :
                                shoppoint = 0
                                shoppoint = (total/20)//1
                                Label(paymentframe,image=yayoishop_payment_3,bg="white").place(x=40,y=0)
                                Label(paymentframe,text="Bill",bg="#EAE8E9",font="Calibri 25").place(x=60,y=10)
                                data = time.datetime.now()
                                time_now = (data.strftime("%x"))
                                Label(paymentframe,text=time_now,bg="#EAE8E9",font="Calibri 16").place(x=380,y=20)
                                Label(paymentframe,text="Menu",bg="#EAE8E9",font="Calibri 16 bold").place(x=60,y=70)
                                Label(paymentframe,text="Amount",bg="#EAE8E9",font="Calibri 16 bold").place(x=280,y=70)
                                Label(paymentframe,text="Price",bg="#EAE8E9",font="Calibri 16 bold").place(x=400,y=70)
                                yaix = 120
                                for i,data in enumerate(orderresult):
                                    if i < 6 :
                                        if data[4] == "F" :
                                            Label(paymentframe,text=data[1][0:25],bg="#EAE8E9",font="Calibri 16").place(x=60,y=yaix)
                                            Label(paymentframe,text=data[3],bg="#EAE8E9",font="Calibri 16").place(x=300,y=yaix)
                                            Label(paymentframe,text=data[2],bg="#EAE8E9",font="Calibri 16").place(x=400,y=yaix)
                                            yaix = yaix + 50
                                        else :
                                            pass
                                newbalance = (float(cusinfo[7])-total)//1
                                newpoint = (float(cusinfo[6])+shoppoint)//1
                                conn=sqlite3.connect("projectdb.db")
                                cursor = conn.cursor()
                                sql = """
                                            UPDATE customer_information
                                            SET money_customer=?,point_customer=?
                                            WHERE id_customer=?"""
                                cursor.execute(sql,[newbalance,newpoint,cusinfo[0]])
                                conn.commit()
                                messagebox.showinfo("Admin","Payment Successfully")
                                Label(paymentframe,text="VAT",bg="#EAE8E9",font="Calibri 16").place(x=60,y=410)
                                Label(paymentframe,text="7 %",bg="#EAE8E9",font="Calibri 16").place(x=400,y=410)
                                Label(paymentframe,text="Point",bg="#EAE8E9",font="Calibri 16").place(x=60,y=450)
                                Label(paymentframe,text="%0.f"%(shoppoint),bg="#EAE8E9",font="Calibri 16").place(x=400,y=450)
                                Label(paymentframe,text="Total Cost",bg="#EAE8E9",font="Calibri 16 bold").place(x=60,y=490)
                                Label(paymentframe,text="%0.f"%(total),bg="#EAE8E9",font="Calibri 16 bold").place(x=400,y=490)
                                Button(paymentframe,text="Exit",bg="#EAE8E9",font="Calibri 16 bold",command=quit).place(x=890,y=480)
                                kyoshop_menu_butt["state"] = "disabled"
                                kyoshop_button_staff["state"] = "disabled"
                                sql = """
                                        DELETE FROM shop_kyo_orderprocess
                                        WHERE table_index=?"""
                                cursor.execute(sql,[table])   
                                conn.commit()
                                sql = """
                                        UPDATE shop_kyo_table
                                        SET status=?,name=?,amount=?
                                        WHERE table_no=? """
                                cursor.execute(sql,['free','','',table])
                                conn.commit()
                                conn.close()
                            else :
                                messagebox.showwarning("Admin","Not enough money in your wallet \n Please pay at the counter")    
                                kyoshop_menu_butt["state"] = "disabled"
                                kyoshop_button_staff["state"] = "disabled"
                                Button(paymentframe,text="Exit",bg="#EAE8E9",font="Calibri 16 bold",command=quit).place(x=890,y=480)
                                conn=sqlite3.connect("projectdb.db")
                                cursor = conn.cursor()
                                sql = """
                                        DELETE FROM shop_kyo_orderprocess
                                        WHERE table_index=?"""
                                cursor.execute(sql,[table])   
                                conn.commit()
                                sql = """
                                        UPDATE shop_kyo_table
                                        SET status=?,name=?,amount=?
                                        WHERE table_no=? """
                                cursor.execute(sql,['free','','',table])
                                conn.commit()
                                conn.close()
                        else :
                            pass 
                    # name
                    paymentframe = Frame(kyoshop_allorder,bg="#FFFFFF")
                    paymentframe.place(x=0,y=0,width=1000,height=550)
                    Label(paymentframe,image=yayoishop_payment_1,bg="white").place(x=40,y=0)
                    Label(paymentframe,image=yayoishop_payment_2,bg="white").place(x=510,y=0)
                    # widget
                    text_yourwallet = Label(paymentframe,text="Yourwallet",bg="#FFE6A7").place(x=60,y=10)
                    text_balance = Label(paymentframe,text="balance : %s"%(cusinfo[7]),bg="#FFE6A7").place(x=120,y=50)
                    text_point = Label(paymentframe,text="Point   : %s"%(cusinfo[6]),bg="#FFE6A7").place(x=120,y=90)
                    text_member = Label(paymentframe,text="membership : %s"%(cusinfo[5]),bg="#FFE6A7").place(x=120,y=130)
                    # 
                    text_Payout = Label(paymentframe,text="Payout",bg="#FFF2D0").place(x=60,y=210)
                    text_name = Label(paymentframe,text="Name : %s %s"%(cusinfo[1],cusinfo[2]),bg="#FFF2D0").place(x=120,y=260)
                    discount = 1
                    discountpercent = 0
                    if cusinfo[5] == "None" :
                        discount = 0.95
                        discountpercent = 5
                    elif cusinfo[5] == "Level1" :
                        discount = 0.9
                        discountpercent = 10
                    elif cusinfo[5] == "Level2" :
                        discount = 0.85
                        discountpercent = 15
                    text_tax = Label(paymentframe,text="Discount : %s Percent"%(discountpercent),bg="#FFF2D0").place(x=120,y=310)
                    total = (Total*discount*1.07)//1
                    text_total = Label(paymentframe,text="Total : %0.f Baht"%(total),bg="#FFF2D0").place(x=120,y=360)
                    text_point = Label(paymentframe,text="Point : %s"%((Totalx/20)//1),bg="#FFF2D0").place(x=120,y=410)
                    but_payment = Button(paymentframe,image=yayoishop_confirm,bg="#FFF2D0",fg="black",font="Calibri 16",border=0,command=lambda : paymentprocess(total))
                    but_payment.place(x=140,y=460)
                #
                Label(kyoshop_allorder,text="Status",bg="#FFFFFF").grid(row=0,column=0)
                Label(kyoshop_allorder,text="Menu",bg="#FFFFFF").grid(row=0,column=1)
                Label(kyoshop_allorder,text="Amount",bg="#FFFFFF").grid(row=0,column=2)
                Label(kyoshop_allorder,text="Price per unit",bg="#FFFFFF").grid(row=0,column=3)
                #
                conn = sqlite3.connect("projectdb.db")
                cursor = conn.cursor()
                sql = """
                        SELECT * FROM shop_kyo_orderprocess 
                        WHERE table_index =?
                        """
                cursor.execute(sql,[kyoshop_tablex.get()])
                orderresult= cursor.fetchall()
                conn.close()
                #
                Totalx = 0
                for i,data in enumerate(orderresult) :
                    if i < 10 :
                        if data[4] == "NF" : 
                            Label(kyoshop_allorder,image=yayoishop_red_status,bg="#FFFFFF").grid(row=i+1,column=0)
                            Label(kyoshop_allorder,text=data[1],bg="white").grid(row=i+1,column=1)
                            Label(kyoshop_allorder,text=data[3],bg="white").grid(row=i+1,column=2)
                            Label(kyoshop_allorder,text=data[2],bg="white").grid(row=i+1,column=3)
                        elif data[4] == "CF" : 
                            Label(kyoshop_allorder,image=yayoishop_red_status,bg="#FFFFFF").grid(row=i+1,column=0)
                            Label(kyoshop_allorder,text=data[1],bg="white").grid(row=i+1,column=1)
                            Label(kyoshop_allorder,text=data[3],bg="white").grid(row=i+1,column=2)
                            Label(kyoshop_allorder,text=data[2],bg="white").grid(row=i+1,column=3)
                        elif data[4] == "F" :
                            Label(kyoshop_allorder,image=yayoishop_green_status,bg="#FFFFFF").grid(row=i+1,column=0)
                            Label(kyoshop_allorder,text=data[1],bg="white").grid(row=i+1,column=1)
                            Label(kyoshop_allorder,text=data[3],bg="white").grid(row=i+1,column=2)
                            Label(kyoshop_allorder,text=data[2],bg="white").grid(row=i+1,column=3)
                            Totalx = Totalx + (int(data[3])*int(data[2]))
                conn = sqlite3.connect("projectdb.db")
                cursor = conn.cursor()
                sql = """
                            SELECT * FROM customer_information
                            WHERE firstname_customer=? """
                cursor.execute(sql,[customername])
                cusinfo = cursor.fetchone()
                Button(kyoshop_allorder,text="Pay out",image=yayoishop_yayoishop_payout,command=lambda:kyoshop_payment(Totalx,cusinfo),border=0,bg="white",activebackground="white").grid(row=20,column=1,columnspan=2)
            def staffcalling() :
                sql = """
                        UPDATE shop_kyo_table
                        SET staffcall=?
                        WHERE table_no=?"""
                cursor.execute(sql,["yes",kyoshop_tablex.get()])
                conn.commit()
            #
            kyopicture()
            amt_table = "0"
            if kyoshop_tablex.get() == "1" or kyoshop_tablex.get() == "2" or kyoshop_tablex.get() == "3" :
                amt_table = "1-2"
            elif kyoshop_tablex.get() == "4" or kyoshop_tablex.get() == "5" or kyoshop_tablex.get() == "6":
                amt_table = "3-4"
            elif kyoshop_tablex.get() == "7" or kyoshop_tablex.get() == "8":
                amt_table = "5-6"
            kyoshop_frame = Frame(kyoroot,bg="#FFFFFF")
            kyoshop_frame.place(x=0,y=0,height=700,width=1000)
            Label(kyoshop_frame,image=kyo_header,bg="#FFFFFF").place(x=-2,y=-5)
            Label(kyoshop_frame,image=kyoshop_logo,bg="#FFFFFF").place(x=40,y=0)
            # table no
            kyoshop_table_no_wframe = Label(kyoshop_frame,image=kyoshop_showtable,bg="#B1A698")
            kyoshop_table_no_wframe.place(relx=0.519,y=15)
            kyoshop_text_no_people = Label(kyoshop_frame,text="Table No : %s \n %s people"%(kyoshop_tablex.get(),amt_table),bg="#FFEDD6",font="Calibri 16")
            kyoshop_text_no_people.place(relx=0.54,y=23)
            #
            kyoshop_order_wfame = Label(kyoshop_frame,image=yayoishop_whiteframe_2,bg="#B1A698")
            kyoshop_order_wfame.place(relx=0.7,y=15)
            kyoshop_chk_wfame = Label(kyoshop_frame,image=yayoishop_whiteframe_2,bg="#B1A698")
            kyoshop_chk_wfame.place(relx=0.8,y=15)
            kyoshop_staff_wfame = Label(kyoshop_frame,image=yayoishop_whiteframe_2,bg="#B1A698")
            kyoshop_staff_wfame.place(relx=0.9,y=15)
            #
            kyoshop_button_orders = Button(kyoshop_frame,image=yayoishop_but_orders,border=0,bg="#FBE5E5",activebackground="#FBE5E5",command=kyoshop_orderframe)
            kyoshop_button_orders.place(relx=0.814,y=27)
            #
            conn = sqlite3.connect("projectdb.db")
            cursor = conn.cursor()
            sql = """
                        SELECT * FROM shop_kyo_orderprocess
                        WHERE table_index=? """
            cursor.execute(sql,[kyoshop_tablex.get()])
            result = cursor.fetchall()
            nuborder = 0
            for i,date in enumerate(result) :
                nuborder = nuborder + 1
            lenorder = StringVar()
            lenorder.set(nuborder)
            #
            kyoshop_amount_order = Label(kyoshop_frame,border=0,bg="#FBE5E5",text=lenorder.get(),compound="center",font="bold")
            kyoshop_amount_order.place(relx=0.855,y=19)
            # relx=0.752,y=17
            kyoshop_button_staff = Button(kyoshop_frame,image=yayoishop_but_staff,border=0,bg="#FBE5E5",activebackground="#FBE5E5",command=staffcalling)
            kyoshop_button_staff.place(relx=0.92,y=26)
            # 1
            kyoshop_menu_butt = Button(kyoshop_frame,image=yayoishop_but_menu,border=0,bg="#FBE5E5",activebackground="#FBE5E5",command=kyoshop_menuframe)
            kyoshop_menu_butt.place(relx=0.72,y=28)
            kyoshop_menuframe()
        def code_mainprogram(table,customername) :
            global codeshop_indexpage,codeshop_indexmenubar,codeshop_tablex
            coderoot = Frame(root,bg="white")
            coderoot.place(x=0,y=0,width=1000,height=700)
            #
            conn = sqlite3.connect("projectdb.db")
            cursor = conn.cursor()
            sql = """
                        DELETE FROM shop_code_queue
                        WHERE q_name=? """
            cursor.execute(sql,[customername])
            conn.commit()
            username = customername
            codeshop_indexpage = StringVar()
            codeshop_indexpage.set("0")
            codeshop_indexmenubar = StringVar()
            codeshop_indexmenubar.set("0")
            codeshop_tablex = StringVar()
            codeshop_tablex.set(table)
            def codepicture() :
                #
                global code_menuset_1, code_menuset_2 ,code_menuset_3 ,code_menuset_4,code_menuset_5,code_menuset_6,code_menuset_7,code_menuset_8,code_menuset_9,code_menuset_10,code_menuset_11,code_menuset_12,code_menuset_13,code_menuset_14,code_menuset_15,code_menuset_16,code_menuset_17,code_menuset_18,code_menuset_19,code_menuset_20,code_menuset_21,code_menuset_22,code_menuset_23,code_menuset_24,code_menuset_25,code_menuset_26,code_menuset_27,code_menuset_28,code_menuset_29,code_menuset_30,code_menuset_31,code_menuset_32,code_menuset_33,code_menuset_34,code_menuset_35,code_menuset_36,code_menuset_37,code_menuset_38,code_menuset_39,code_menuset_40,code_menuset_41,code_menuset_42,code_menuset_43,code_menuset_44,code_menuset_45,code_menuset_46,code_menuset_47,code_menuset_48,code_menuset_49,code_menuset_50
                #
                global codeshop_mart_photo,codeshop_logo,codeshop_header,codeshop_showtable,codeshop_cat_1,codeshop_cat_2
                #
                codeshop_mart_photo = PhotoImage(file="image/Code-shop/martphoto.png")
                codeshop_logo = PhotoImage(file="image/Code-shop/logo-code.png")
                codeshop_header = PhotoImage(file="image/Code-shop/edge.png")
                codeshop_showtable = PhotoImage(file="image/Code-shop/showtable.png")
                codeshop_cat_1 = PhotoImage(file="image/Code-shop/cat1.png")
                codeshop_cat_2 = PhotoImage(file="image/Code-shop/cat2.png")
                #
                code_menuset_1 = PhotoImage(file="image/Code-shop/menuset_1.png")
                code_menuset_2 = PhotoImage(file="image/Code-shop/menuset_2.png")
                code_menuset_3 = PhotoImage(file="image/Code-shop/menuset_3.png")
                code_menuset_4 = PhotoImage(file="image/Code-shop/menuset_4.png")
                code_menuset_5 = PhotoImage(file="image/Code-shop/menuset_5.png")
                code_menuset_6 = PhotoImage(file="image/Code-shop/menuset_6.png")
                code_menuset_7 = PhotoImage(file="image/Code-shop/menuset_7.png")
                code_menuset_8 = PhotoImage(file="image/Code-shop/menuset_8.png")
                code_menuset_9 = PhotoImage(file="image/Code-shop/menuset_9.png")
                code_menuset_10 = PhotoImage(file="image/Code-shop/menuset_10.png")
                code_menuset_11 = PhotoImage(file="image/Code-shop/menuset_11.png")
                code_menuset_12 = PhotoImage(file="image/Code-shop/menuset_12.png")
                code_menuset_13 = PhotoImage(file="image/Code-shop/menuset_13.png")
                code_menuset_14 = PhotoImage(file="image/Code-shop/menuset_14.png")
                code_menuset_15 = PhotoImage(file="image/Code-shop/menuset_15.png")
                code_menuset_16 = PhotoImage(file="image/Code-shop/menuset_16.png")
                code_menuset_17 = PhotoImage(file="image/Code-shop/menuset_17.png")
                code_menuset_18 = PhotoImage(file="image/Code-shop/menuset_18.png")
                code_menuset_19 = PhotoImage(file="image/Code-shop/menuset_19.png")
                code_menuset_20 = PhotoImage(file="image/Code-shop/menuset_20.png")
                code_menuset_21 = PhotoImage(file="image/Code-shop/menuset_21.png")
                code_menuset_22 = PhotoImage(file="image/Code-shop/menuset_22.png")
                code_menuset_23 = PhotoImage(file="image/Code-shop/menuset_23.png")
                code_menuset_24 = PhotoImage(file="image/Code-shop/menuset_24.png")
                code_menuset_25 = PhotoImage(file="image/Code-shop/menuset_25.png")
                code_menuset_26 = PhotoImage(file="image/Code-shop/menuset_26.png")
                code_menuset_27 = PhotoImage(file="image/Code-shop/menuset_27.png")
                code_menuset_28 = PhotoImage(file="image/Code-shop/menuset_28.png")
                code_menuset_29 = PhotoImage(file="image/Code-shop/menuset_29.png")
                code_menuset_30 = PhotoImage(file="image/Code-shop/menuset_30.png")
                code_menuset_31 = PhotoImage(file="image/Code-shop/menuset_31.png")
                code_menuset_32 = PhotoImage(file="image/Code-shop/menuset_32.png")
                code_menuset_33 = PhotoImage(file="image/Code-shop/menuset_33.png")
                code_menuset_34 = PhotoImage(file="image/Code-shop/menuset_34.png")
                code_menuset_35 = PhotoImage(file="image/Code-shop/menuset_35.png")
                code_menuset_36 = PhotoImage(file="image/Code-shop/menuset_36.png")
                code_menuset_37 = PhotoImage(file="image/Code-shop/menuset_37.png")
                code_menuset_38 = PhotoImage(file="image/Code-shop/menuset_38.png")
                code_menuset_39 = PhotoImage(file="image/Code-shop/menuset_39.png")
                code_menuset_40 = PhotoImage(file="image/Code-shop/menuset_40.png")
                code_menuset_41 = PhotoImage(file="image/Code-shop/menuset_41.png")
                code_menuset_42 = PhotoImage(file="image/Code-shop/menuset_42.png")
                code_menuset_43 = PhotoImage(file="image/Code-shop/menuset_43.png")
                code_menuset_44 = PhotoImage(file="image/Code-shop/menuset_44.png")
                code_menuset_45 = PhotoImage(file="image/Code-shop/menuset_45.png")
                code_menuset_46 = PhotoImage(file="image/Code-shop/menuset_46.png")
                code_menuset_47 = PhotoImage(file="image/Code-shop/menuset_47.png")
                code_menuset_48 = PhotoImage(file="image/Code-shop/menuset_48.png")
                code_menuset_49 = PhotoImage(file="image/Code-shop/menuset_49.png")
                code_menuset_50 = PhotoImage(file="image/Code-shop/menuset_50.png")
            def codeshop_addtocartprocess(ordername,price) :
                statusx = "NF"
                amount = 1
                conn = sqlite3.connect("projectdb.db")
                cursor = conn.cursor()
                sql = """
                        SELECT * FROM shop_code_orderprocess
                        WHERE table_index = ? and amount > 0 and menu_name = ?"""
                cursor.execute(sql,[codeshop_tablex.get(),ordername])
                result = cursor.fetchone()
                conn.close()
                if result:
                    if ordername == result[1] :
                        newamount = int(result[3]) + 1
                        conn = sqlite3.connect("projectdb.db")
                        cursor = conn.cursor()
                        sql = """
                                UPDATE shop_code_orderprocess
                                SET amount = ?
                                WHERE menu_name = ? """
                        cursor.execute(sql,[newamount,ordername])
                        conn.commit()
                        conn.close()
                        messagebox.showinfo("Admin","Added to cart")    
                else :
                    conn = sqlite3.connect("projectdb.db")
                    cursor = conn.cursor()
                    sql = """
                            INSERT INTO shop_code_orderprocess 
                            values(?,?,?,?,?)"""
                    cursor.execute(sql,[codeshop_tablex.get(),ordername,price,amount,statusx])
                    conn.commit()
                    conn.close()
                    messagebox.showinfo("Admin","Added to cart")   
                    conn = sqlite3.connect("projectdb.db")
                    cursor = conn.cursor()
                    sql = """
                                SELECT * FROM shop_code_orderprocess
                                WHERE table_index=? """
                    cursor.execute(sql,[codeshop_tablex.get()])
                    result = cursor.fetchall()
                    nuborder = 0
                    for i,date in enumerate(result) :
                        nuborder = nuborder + 1
                    lenorder = StringVar()
                    lenorder.set(nuborder)
                    codeshop_amount_order["text"] = lenorder.get()
            def codeshop_click1(e) :
                if codeshop_indexpage.get() == "1" :
                    codeshop_frameone.destroy()
                elif codeshop_indexpage.get() == "2" :
                    codeshop_frametwo.destroy()
                elif codeshop_indexpage.get() == "3" :
                    codeshop_framethree.destroy()
                elif codeshop_indexpage.get() == "4" :
                    codeshop_framefour.destroy()
                elif codeshop_indexpage.get() == "5" :
                    codeshop_framefive.destroy()
                codeshop_cate_1["image"] = codeshop_cat_1
                codeshop_cate_2["image"] = codeshop_cat_2
                codeshop_cate_3["image"] = codeshop_cat_2
                codeshop_cate_4["image"] = codeshop_cat_2
                codeshop_cate_5["image"] = codeshop_cat_2
            def codeshop_click2(e) :
                if codeshop_indexpage.get() == "1" :
                    codeshop_frameone.destroy()
                elif codeshop_indexpage.get() == "2" :
                    codeshop_frametwo.destroy()
                elif codeshop_indexpage.get() == "3" :
                    codeshop_framethree.destroy()
                elif codeshop_indexpage.get() == "4" :
                    codeshop_framefour.destroy()
                elif codeshop_indexpage.get() == "5" :
                    codeshop_framefive.destroy()
                codeshop_cate_1["image"] = codeshop_cat_2
                codeshop_cate_2["image"] = codeshop_cat_1
                codeshop_cate_3["image"] = codeshop_cat_2
                codeshop_cate_4["image"] = codeshop_cat_2
                codeshop_cate_5["image"] = codeshop_cat_2
            def codeshop_click3(e) :
                if codeshop_indexpage.get() == "1" :
                    codeshop_frameone.destroy()
                elif codeshop_indexpage.get() == "2" :
                    codeshop_frametwo.destroy()
                elif codeshop_indexpage.get() == "3" :
                    codeshop_framethree.destroy()
                elif codeshop_indexpage.get() == "4" :
                    codeshop_framefour.destroy()
                elif codeshop_indexpage.get() == "5" :
                    codeshop_framefive.destroy()
                codeshop_cate_1["image"] = codeshop_cat_2
                codeshop_cate_2["image"] = codeshop_cat_2
                codeshop_cate_3["image"] = codeshop_cat_1
                codeshop_cate_4["image"] = codeshop_cat_2
                codeshop_cate_5["image"] = codeshop_cat_2
            def codeshop_click4(e) :
                if codeshop_indexpage.get() == "1" :
                    codeshop_frameone.destroy()
                elif codeshop_indexpage.get() == "2" :
                    codeshop_frametwo.destroy()
                elif codeshop_indexpage.get() == "3" :
                    codeshop_framethree.destroy()
                elif codeshop_indexpage.get() == "4" :
                    codeshop_framefour.destroy()
                elif codeshop_indexpage.get() == "5" :
                    codeshop_framefive.destroy()
                codeshop_cate_1["image"] = codeshop_cat_2
                codeshop_cate_2["image"] = codeshop_cat_2
                codeshop_cate_3["image"] = codeshop_cat_2
                codeshop_cate_4["image"] = codeshop_cat_1
                codeshop_cate_5["image"] = codeshop_cat_2
            def codeshop_click5(e) :
                if codeshop_indexpage.get() == "1" :
                    codeshop_frameone.destroy()
                elif codeshop_indexpage.get() == "2" :
                    codeshop_frametwo.destroy()
                elif codeshop_indexpage.get() == "3" :
                    codeshop_framethree.destroy()
                elif codeshop_indexpage.get() == "4" :
                    codeshop_framefour.destroy()
                elif codeshop_indexpage.get() == "5" :
                    codeshop_framefive.destroy()
                codeshop_cate_1["image"] = codeshop_cat_2
                codeshop_cate_2["image"] = codeshop_cat_2
                codeshop_cate_3["image"] = codeshop_cat_2
                codeshop_cate_4["image"] = codeshop_cat_2
                codeshop_cate_5["image"] = codeshop_cat_1
            def codeshop_frame_one() : # 1
                global codeshop_frameone
                codeshop_indexpage.set("1")
                codeshop_frameone = Frame(codeshop_frame,bg="#FFFFFF")
                codeshop_frameone.place(x=0,y=155,width=1000,height=545)
                # menu 1
                menu_1 = Label(codeshop_frameone,image=code_menuset_1,bg="#FFFFFF")
                menu_1.place(x=0,y=20)
                # menu 2
                menu_2 = Label(codeshop_frameone,image=code_menuset_2,bg="#FFFFFF")
                menu_2.place(x=200,y=20)
                # menu 3
                menu_3 = Label(codeshop_frameone,image=code_menuset_3,bg="#FFFFFF")
                menu_3.place(x=400,y=20)
                # menu 4
                menu_4 = Label(codeshop_frameone,image=code_menuset_4,bg="#FFFFFF")
                menu_4.place(x=600,y=20)
                # menu 5
                menu_5 = Label(codeshop_frameone,image=code_menuset_5,bg="#FFFFFF")
                menu_5.place(x=800,y=20)
                # menu 6
                menu_6 = Label(codeshop_frameone,image=code_menuset_6,bg="#FFFFFF")
                menu_6.place(x=0,y=285)
                # menu 7 
                menu_7 = Label(codeshop_frameone,image=code_menuset_7,bg="#FFFFFF")
                menu_7.place(x=200,y=285)
                # menu 8
                menu_8 = Label(codeshop_frameone,image=code_menuset_8,bg="#FFFFFF")
                menu_8.place(x=400,y=285)
                # menu 9
                menu_9 = Label(codeshop_frameone,image=code_menuset_9,bg="#FFFFFF")
                menu_9.place(x=600,y=285)
                # menu 10
                menu_10 = Label(codeshop_frameone,image=code_menuset_10,bg="#FFFFFF")
                menu_10.place(x=800,y=285)
                #
                mart_number_1 = Button(codeshop_frameone,image=codeshop_mart_photo,border=0,command=lambda:codeshop_addtocartprocess("Nutella Lava Toast","180"))
                mart_number_1.place(x=139,y=238)
                mart_number_2 = Button(codeshop_frameone,image=codeshop_mart_photo,border=0,command=lambda:codeshop_addtocartprocess("Croissant Thai Tea","199"))
                mart_number_2.place(x=337,y=238)
                mart_number_3 = Button(codeshop_frameone,image=codeshop_mart_photo,border=0,command=lambda:codeshop_addtocartprocess("Croissant Nutella","280"))
                mart_number_3.place(x=537,y=238)
                mart_number_4 = Button(codeshop_frameone,image=codeshop_mart_photo,border=0,command=lambda:codeshop_addtocartprocess("Mayongchid","189"))
                mart_number_4.place(x=739,y=238)
                mart_number_5 = Button(codeshop_frameone,image=codeshop_mart_photo,border=0,command=lambda:codeshop_addtocartprocess("Purple Sweet Potato","245"))
                mart_number_5.place(x=939,y=238)
                mart_number_6 = Button(codeshop_frameone,image=codeshop_mart_photo,border=0,command=lambda:codeshop_addtocartprocess("Matcha Milk Tea","95"))
                mart_number_6.place(x=139,y=503)
                mart_number_7 = Button(codeshop_frameone,image=codeshop_mart_photo,border=0,command=lambda:codeshop_addtocartprocess("Thai Milk Tea","95"))
                mart_number_7.place(x=337,y=503)
                mart_number_8 = Button(codeshop_frameone,image=codeshop_mart_photo,border=0,command=lambda:codeshop_addtocartprocess("Strawberry Croissant","60"))
                mart_number_8.place(x=537,y=503)
                mart_number_9 = Button(codeshop_frameone,image=codeshop_mart_photo,border=0,command=lambda:codeshop_addtocartprocess("Chocolate Croissant","55"))
                mart_number_9.place(x=739,y=503)
                mart_number_10 = Button(codeshop_frameone,image=codeshop_mart_photo,border=0,command=lambda:codeshop_addtocartprocess("Original Croissant","50"))
                mart_number_10.place(x=939,y=503)
            def codeshop_frame_two() : # 2
                global codeshop_frametwo
                codeshop_indexpage.set("2")
                codeshop_frametwo = Frame(codeshop_frame,bg="white")
                codeshop_frametwo.place(x=0,y=155,width=1000,height=545)
                # menu 1
                menu_1 = Label(codeshop_frametwo,image=code_menuset_11,bg="#FFFFFF")
                menu_1.place(x=0,y=20)
                # menu 2
                menu_2 = Label(codeshop_frametwo,image=code_menuset_12,bg="#FFFFFF")
                menu_2.place(x=200,y=20)
                # menu 3
                menu_3 = Label(codeshop_frametwo,image=code_menuset_13,bg="#FFFFFF")
                menu_3.place(x=400,y=20)
                # menu 4
                menu_4 = Label(codeshop_frametwo,image=code_menuset_14,bg="#FFFFFF")
                menu_4.place(x=600,y=20)
                # menu 5
                menu_5 = Label(codeshop_frametwo,image=code_menuset_15,bg="#FFFFFF")
                menu_5.place(x=800,y=20)
                # menu 6
                menu_6 = Label(codeshop_frametwo,image=code_menuset_16,bg="#FFFFFF")
                menu_6.place(x=0,y=285)
                # menu 7 
                menu_7 = Label(codeshop_frametwo,image=code_menuset_17,bg="#FFFFFF")
                menu_7.place(x=200,y=285)
                # menu 8
                menu_8 = Label(codeshop_frametwo,image=code_menuset_18,bg="#FFFFFF")
                menu_8.place(x=400,y=285)
                # menu 9
                menu_9 = Label(codeshop_frametwo,image=code_menuset_19,bg="#FFFFFF")
                menu_9.place(x=600,y=285)
                # menu 10
                menu_10 = Label(codeshop_frametwo,image=code_menuset_20,bg="#FFFFFF")
                menu_10.place(x=800,y=285)
                #
                mart_number_1 = Button(codeshop_frametwo,image=codeshop_mart_photo,border=0,command=lambda:codeshop_addtocartprocess("Salted Egg Lava","75"))
                mart_number_1.place(x=137,y=238)
                mart_number_2 = Button(codeshop_frametwo,image=codeshop_mart_photo,border=0,command=lambda:codeshop_addtocartprocess("Croissant Egg Lava","70"))
                mart_number_2.place(x=337,y=238)
                mart_number_3 = Button(codeshop_frametwo,image=codeshop_mart_photo,border=0,command=lambda:codeshop_addtocartprocess("Nutella Lava Toast","180"))
                mart_number_3.place(x=537,y=238)
                mart_number_4 = Button(codeshop_frametwo,image=codeshop_mart_photo,border=0,command=lambda:codeshop_addtocartprocess("Croissant Thai Tea","199"))
                mart_number_4.place(x=737,y=238)
                mart_number_5 = Button(codeshop_frametwo,image=codeshop_mart_photo,border=0,command=lambda:codeshop_addtocartprocess("Croissant Nutella","280"))
                mart_number_5.place(x=937,y=238)
                mart_number_6 = Button(codeshop_frametwo,image=codeshop_mart_photo,border=0,command=lambda:codeshop_addtocartprocess("Matcha Lava","280"))
                mart_number_6.place(x=139,y=503)
                mart_number_7 = Button(codeshop_frametwo,image=codeshop_mart_photo,border=0,command=lambda:codeshop_addtocartprocess("Chacoal Thai Tea","180"))
                mart_number_7.place(x=339,y=503)
                mart_number_8 = Button(codeshop_frametwo,image=codeshop_mart_photo,border=0,command=lambda:codeshop_addtocartprocess("Matcha Fudge","175"))
                mart_number_8.place(x=537,y=503)
                mart_number_9 = Button(codeshop_frametwo,image=codeshop_mart_photo,border=0,command=lambda:codeshop_addtocartprocess("Honey Fudge","119"))
                mart_number_9.place(x=737,y=503)
                mart_number_10 = Button(codeshop_frametwo,image=codeshop_mart_photo,border=0,command=lambda:codeshop_addtocartprocess("Chocolate Fudge","110"))
                mart_number_10.place(x=937,y=503)
            def codeshop_frame_three() : # 5
                global codeshop_framethree
                codeshop_indexpage.set("3")
                codeshop_framethree = Frame(codeshop_frame,bg="white")
                codeshop_framethree.place(x=0,y=155,width=1000,height=545)
                # menu 1
                menu_1 = Label(codeshop_framethree,image=code_menuset_21,bg="#FFFFFF")
                menu_1.place(x=0,y=20)
                # menu 2
                menu_2 = Label(codeshop_framethree,image=code_menuset_22,bg="#FFFFFF")
                menu_2.place(x=200,y=20)
                # menu 3
                menu_3 = Label(codeshop_framethree,image=code_menuset_23,bg="#FFFFFF")
                menu_3.place(x=400,y=20)
                # menu 4
                menu_4 = Label(codeshop_framethree,image=code_menuset_24,bg="#FFFFFF")
                menu_4.place(x=600,y=20)
                # menu 5
                menu_5 = Label(codeshop_framethree,image=code_menuset_25,bg="#FFFFFF")
                menu_5.place(x=800,y=20)
                # menu 6
                menu_6 = Label(codeshop_framethree,image=code_menuset_26,bg="#FFFFFF")
                menu_6.place(x=0,y=285)
                # menu 7 
                menu_7 = Label(codeshop_framethree,image=code_menuset_27,bg="#FFFFFF")
                menu_7.place(x=200,y=285)
                # menu 8
                menu_8 = Label(codeshop_framethree,image=code_menuset_28,bg="#FFFFFF")
                menu_8.place(x=400,y=285)
                # menu 9
                menu_9 = Label(codeshop_framethree,image=code_menuset_29,bg="#FFFFFF")
                menu_9.place(x=600,y=285)
                # menu 10
                menu_10 = Label(codeshop_framethree,image=code_menuset_30,bg="#FFFFFF")
                menu_10.place(x=800,y=285)
                #
                mart_number_1 = Button(codeshop_framethree,image=codeshop_mart_photo,border=0,command=lambda:codeshop_addtocartprocess("Banoffee","120"))
                mart_number_1.place(x=137,y=238)
                mart_number_2 = Button(codeshop_framethree,image=codeshop_mart_photo,border=0,command=lambda:codeshop_addtocartprocess("Strawberry","130"))
                mart_number_2.place(x=339,y=238)
                mart_number_3 = Button(codeshop_framethree,image=codeshop_mart_photo,border=0,command=lambda:codeshop_addtocartprocess("Chocolate","120"))
                mart_number_3.place(x=539,y=238)
                mart_number_4 = Button(codeshop_framethree,image=codeshop_mart_photo,border=0,command=lambda:codeshop_addtocartprocess("Mango","130"))
                mart_number_4.place(x=739,y=238)
                mart_number_5 = Button(codeshop_framethree,image=codeshop_mart_photo,border=0,command=lambda:codeshop_addtocartprocess("Mayongchid","189"))
                mart_number_5.place(x=939,y=238)
                mart_number_6 = Button(codeshop_framethree,image=codeshop_mart_photo,border=0,command=lambda:codeshop_addtocartprocess("Strawberry Biscuit","195"))
                mart_number_6.place(x=139,y=503)
                mart_number_7 = Button(codeshop_framethree,image=codeshop_mart_photo,border=0,command=lambda:codeshop_addtocartprocess("Lodchong Flat","179"))
                mart_number_7.place(x=337,y=503)
                mart_number_8 = Button(codeshop_framethree,image=codeshop_mart_photo,border=0,command=lambda:codeshop_addtocartprocess("Melon Japan","180"))
                mart_number_8.place(x=537,y=503)
                mart_number_9 = Button(codeshop_framethree,image=codeshop_mart_photo,border=0,command=lambda:codeshop_addtocartprocess("Strawberry Chessecake","199"))
                mart_number_9.place(x=737,y=503)
                mart_number_10 = Button(codeshop_framethree,image=codeshop_mart_photo,border=0,command=lambda:codeshop_addtocartprocess("Purple Sweet Potato","245"))
                mart_number_10.place(x=939,y=503)
            def codeshop_frame_four() : # 4
                global codeshop_framefour
                codeshop_indexpage.set("4")
                codeshop_framefour = Frame(codeshop_frame,bg="white")
                codeshop_framefour.place(x=0,y=155,width=1000,height=545)
                # menu 1
                menu_1 = Label(codeshop_framefour,image=code_menuset_31,bg="#FFFFFF")
                menu_1.place(x=0,y=20)
                # menu 2
                menu_2 = Label(codeshop_framefour,image=code_menuset_32,bg="#FFFFFF")
                menu_2.place(x=200,y=20)
                # menu 3
                menu_3 = Label(codeshop_framefour,image=code_menuset_33,bg="#FFFFFF")
                menu_3.place(x=400,y=20)
                # menu 4
                menu_4 = Label(codeshop_framefour,image=code_menuset_34,bg="#FFFFFF")
                menu_4.place(x=600,y=20)
                # menu 5
                menu_5 = Label(codeshop_framefour,image=code_menuset_35,bg="#FFFFFF")
                menu_5.place(x=800,y=20)
                # menu 6
                menu_6 = Label(codeshop_framefour,image=code_menuset_36,bg="#FFFFFF")
                menu_6.place(x=0,y=285)
                # menu 7 
                menu_7 = Label(codeshop_framefour,image=code_menuset_37,bg="#FFFFFF")
                menu_7.place(x=200,y=285)
                # menu 8
                menu_8 = Label(codeshop_framefour,image=code_menuset_38,bg="#FFFFFF")
                menu_8.place(x=400,y=285)
                # menu 9
                menu_9 = Label(codeshop_framefour,image=code_menuset_39,bg="#FFFFFF")
                menu_9.place(x=600,y=285)
                # menu 10
                menu_10 = Label(codeshop_framefour,image=code_menuset_40,bg="#FFFFFF")
                menu_10.place(x=800,y=285)
                #
                mart_number_1 = Button(codeshop_framefour,image=codeshop_mart_photo,border=0,command=lambda:codeshop_addtocartprocess("Nutella Croissant","60"))
                mart_number_1.place(x=139,y=238)
                mart_number_2 = Button(codeshop_framefour,image=codeshop_mart_photo,border=0,command=lambda:codeshop_addtocartprocess("Strawberry Croissant","60"))
                mart_number_2.place(x=339,y=238)
                mart_number_3 = Button(codeshop_framefour,image=codeshop_mart_photo,border=0,command=lambda:codeshop_addtocartprocess("Chocolate Croissant","55"))
                mart_number_3.place(x=539,y=238)
                mart_number_4 = Button(codeshop_framefour,image=codeshop_mart_photo,border=0,command=lambda:codeshop_addtocartprocess("Original Croissant","50"))
                mart_number_4.place(x=739,y=238)
                mart_number_5 = Button(codeshop_framefour,image=codeshop_mart_photo,border=0,command=lambda:codeshop_addtocartprocess("Hazelnut Croissant","55"))
                mart_number_5.place(x=939,y=238)
                mart_number_6 = Button(codeshop_framefour,image=codeshop_mart_photo,border=0,command=lambda:codeshop_addtocartprocess("Molten Chocolate","850"))
                mart_number_6.place(x=139,y=503)
                mart_number_7 = Button(codeshop_framefour,image=codeshop_mart_photo,border=0,command=lambda:codeshop_addtocartprocess("Molten Matcha","900"))
                mart_number_7.place(x=339,y=503)
                mart_number_8 = Button(codeshop_framefour,image=codeshop_mart_photo,border=0,command=lambda:codeshop_addtocartprocess("Molten Thai Tea","850"))
                mart_number_8.place(x=539,y=503)
                mart_number_9 = Button(codeshop_framefour,image=codeshop_mart_photo,border=0,command=lambda:codeshop_addtocartprocess("Brownie","89"))
                mart_number_9.place(x=739,y=503)
                mart_number_10 = Button(codeshop_framefour,image=codeshop_mart_photo,border=0,command=lambda:codeshop_addtocartprocess("Power Ball","75"))
                mart_number_10.place(x=939,y=503)
            def codeshop_frame_five() : # 3
                global codeshop_framefive
                codeshop_indexpage.set("5")
                codeshop_framefive = Frame(codeshop_frame,bg="white")
                codeshop_framefive.place(x=0,y=155,width=1000,height=545)
                # menu 1
                menu_1 = Label(codeshop_framefive,image=code_menuset_41,bg="#FFFFFF")
                menu_1.place(x=0,y=20)
                # menu 2
                menu_2 = Label(codeshop_framefive,image=code_menuset_42,bg="#FFFFFF")
                menu_2.place(x=200,y=20)
                # menu 3
                menu_3 = Label(codeshop_framefive,image=code_menuset_43,bg="#FFFFFF")
                menu_3.place(x=400,y=20)
                # menu 4
                menu_4 = Label(codeshop_framefive,image=code_menuset_44,bg="#FFFFFF")
                menu_4.place(x=600,y=20)
                # menu 5
                menu_5 = Label(codeshop_framefive,image=code_menuset_45,bg="#FFFFFF")
                menu_5.place(x=800,y=20)
                # menu 6
                menu_6 = Label(codeshop_framefive,image=code_menuset_46,bg="#FFFFFF")
                menu_6.place(x=0,y=285)
                # menu 7 
                menu_7 = Label(codeshop_framefive,image=code_menuset_47,bg="#FFFFFF")
                menu_7.place(x=200,y=285)
                # menu 8
                menu_8 = Label(codeshop_framefive,image=code_menuset_48,bg="#FFFFFF")
                menu_8.place(x=400,y=285)
                # menu 9
                menu_9 = Label(codeshop_framefive,image=code_menuset_49,bg="#FFFFFF")
                menu_9.place(x=600,y=285)
                # menu 10
                menu_10 = Label(codeshop_framefive,image=code_menuset_50,bg="#FFFFFF")
                menu_10.place(x=800,y=285)
                #
                mart_number_1 = Button(codeshop_framefive,image=codeshop_mart_photo,bg='#FFFFFF',border=0,command=lambda:codeshop_addtocartprocess("Purple Sweet Potato","95"))
                mart_number_1.place(x=139,y=238)
                mart_number_2 = Button(codeshop_framefive,image=codeshop_mart_photo,bg='#FFFFFF',border=0,command=lambda:codeshop_addtocartprocess("Berries Smoothie","79"))
                mart_number_2.place(x=339,y=238)
                mart_number_3 = Button(codeshop_framefive,image=codeshop_mart_photo,bg='#FFFFFF',border=0,command=lambda:codeshop_addtocartprocess("Blueberry Shake","85"))
                mart_number_3.place(x=539,y=238)
                mart_number_4 = Button(codeshop_framefive,image=codeshop_mart_photo,bg='#FFFFFF',border=0,command=lambda:codeshop_addtocartprocess("Blue Curacao","60"))
                mart_number_4.place(x=737,y=238)
                mart_number_5 = Button(codeshop_framefive,image=codeshop_mart_photo,bg='#FFFFFF',border=0,command=lambda:codeshop_addtocartprocess("Nutella crunch coffee","60"))
                mart_number_5.place(x=939,y=238)
                mart_number_6 = Button(codeshop_framefive,image=codeshop_mart_photo,bg='#FFFFFF',border=0,command=lambda:codeshop_addtocartprocess("Black Tea Cream","95"))
                mart_number_6.place(x=139,y=503)
                mart_number_7 = Button(codeshop_framefive,image=codeshop_mart_photo,bg='#FFFFFF',border=0,command=lambda:codeshop_addtocartprocess("Chocolate Milk","80"))
                mart_number_7.place(x=339,y=503)
                mart_number_8 = Button(codeshop_framefive,image=codeshop_mart_photo,bg='#FFFFFF',border=0,command=lambda:codeshop_addtocartprocess("Brown Sugar Milk","180"))
                mart_number_8.place(x=537,y=503)
                mart_number_9 = Button(codeshop_framefive,image=codeshop_mart_photo,bg='#FFFFFF',border=0,command=lambda:codeshop_addtocartprocess("Matcha Milk Tea","95"))
                mart_number_9.place(x=737,y=503)
                mart_number_10 = Button(codeshop_framefive,image=codeshop_mart_photo,bg='#FFFFFF',border=0,command=lambda:codeshop_addtocartprocess("Thai Milk Tea","95"))
                mart_number_10.place(x=937,y=503)
            def codeshop_menuframe() :
                global codeshop_cate_1 , codeshop_cate_2 , codeshop_cate_3 , codeshop_cate_4 , codeshop_cate_5 , codeshop_indexmenubar
                codeshop_menu_butt["state"] = "disabled"
                codeshop_button_orders["state"] = "active"
                if codeshop_indexmenubar.get() == "1" :
                    codeshop_allorder.destroy()
                elif codeshop_indexmenubar.get() == "0" :
                    pass
                codeshop_indexmenubar.set("0")
                if codeshop_indexpage.get() == "1" :
                    codeshop_frameone.destroy()
                elif codeshop_indexpage.get() == "2" :
                    codeshop_frametwo.destroy()
                elif codeshop_indexpage.get() == "3" :
                    codeshop_framethree.destroy()
                elif codeshop_indexpage.get() == "4" :
                    codeshop_framefour.destroy()
                elif codeshop_indexpage.get() == "5" :
                    codeshop_framefive.destroy()
                codeshop_frame_one()
                # category
                codeshop_cate_1 = Button(codeshop_frame,text="Recommand",image=codeshop_cat_1,compound="center",fg="#FFFFFF",border=0,bg="#FFFFFF",activebackground="#FFFFFF",font="Calibri 13",command=codeshop_frame_one)
                codeshop_cate_1.place(relx=0.375,y=110)
                #
                codeshop_cate_2 = Button(codeshop_frame,text="Lava Menu",image=codeshop_cat_2,compound="center",fg="#FFFFFF",border=0,bg="#FFFFFF",activebackground="#FFFFFF",font="Calibri 13",command=codeshop_frame_two)
                codeshop_cate_2.place(relx=0.5,y=110)
                #
                codeshop_cate_3 = Button(codeshop_frame,text="Drinks",image=codeshop_cat_2,compound="center",fg="#FFFFFF",border=0,bg="#FFFFFF",activebackground="#FFFFFF",font="Calibri 13",command=codeshop_frame_five)
                codeshop_cate_3.place(relx=0.875,y=110)
                #
                codeshop_cate_4 = Button(codeshop_frame,text="Bread",image=codeshop_cat_2,compound="center",fg="#FFFFFF",border=0,bg="#FFFFFF",activebackground="#FFFFFF",font="Calibri 13",command=codeshop_frame_four)
                codeshop_cate_4.place(relx=0.75,y=110)
                #
                codeshop_cate_5 = Button(codeshop_frame,text="Bingsu",image=codeshop_cat_2,compound="center",fg="#FFFFFF",border=0,bg="#FFFFFF",activebackground="#FFFFFF",font="Calibri 13",command=codeshop_frame_three)
                codeshop_cate_5.place(relx=0.625,y=110)
                # bind
                codeshop_cate_1.bind("<Button-1>",codeshop_click1)
                codeshop_cate_2.bind("<Button-1>",codeshop_click2)
                codeshop_cate_3.bind("<Button-1>",codeshop_click3)
                codeshop_cate_4.bind("<Button-1>",codeshop_click4)
                codeshop_cate_5.bind("<Button-1>",codeshop_click5)
            def codeshop_orderframe() :
                global codeshop_indexmenubar,codeshop_allorder
                codeshop_menu_butt["state"] = "active"
                codeshop_button_orders["state"] = "disabled"
                if codeshop_indexmenubar.get() == "0" :
                    pass
                elif codeshop_indexmenubar.get() == "1" :
                    codeshop_allorder.destroy()
                codeshop_indexmenubar.set("1")
                #
                codeshop_cate_1.place(relx=10)
                codeshop_cate_2.place(relx=10)
                codeshop_cate_3.place(relx=10)
                codeshop_cate_4.place(relx=10)
                codeshop_cate_5.place(relx=10)
                #
                codeshop_allorder = Frame(codeshop_frame,bg="#FFFFFF")
                codeshop_allorder.place(x=0,y=150,width=1000,height=550)
                codeshop_allorder.rowconfigure((0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20),weight=1)
                codeshop_allorder.columnconfigure((0,1,2,3),weight=1)
                #
                def codeshop_payment(Total,cusinfo) :
                    def paymentprocess(total) :
                        ans = messagebox.askquestion("Admin","Are you sure you want to make a payment?")   
                        if ans == "yes" :
                            if float(cusinfo[7]) >= total :
                                shoppoint = 0
                                shoppoint = (total/20)//1
                                Label(paymentframe,image=yayoishop_payment_3,bg="white").place(x=40,y=0)
                                Label(paymentframe,text="Bill",bg="#EAE8E9",font="Calibri 25").place(x=60,y=10)
                                data = time.datetime.now()
                                time_now = (data.strftime("%x"))
                                Label(paymentframe,text=time_now,bg="#EAE8E9",font="Calibri 16").place(x=380,y=20)
                                Label(paymentframe,text="Menu",bg="#EAE8E9",font="Calibri 16 bold").place(x=60,y=70)
                                Label(paymentframe,text="Amount",bg="#EAE8E9",font="Calibri 16 bold").place(x=280,y=70)
                                Label(paymentframe,text="Price",bg="#EAE8E9",font="Calibri 16 bold").place(x=400,y=70)
                                yaix = 120
                                for i,data in enumerate(orderresult):
                                    if i < 6 :
                                        if data[4] == "F" :
                                            Label(paymentframe,text=data[1][0:25],bg="#EAE8E9",font="Calibri 16").place(x=60,y=yaix)
                                            Label(paymentframe,text=data[3],bg="#EAE8E9",font="Calibri 16").place(x=300,y=yaix)
                                            Label(paymentframe,text=data[2],bg="#EAE8E9",font="Calibri 16").place(x=400,y=yaix)
                                            yaix = yaix + 50
                                        else :
                                            pass
                                newbalance = (float(cusinfo[7])-total)//1
                                newpoint = (float(cusinfo[6])+shoppoint)//1
                                conn=sqlite3.connect("projectdb.db")
                                cursor = conn.cursor()
                                sql = """
                                            UPDATE customer_information
                                            SET money_customer=?,point_customer=?
                                            WHERE id_customer=?"""
                                cursor.execute(sql,[newbalance,newpoint,cusinfo[0]])
                                conn.commit()
                                messagebox.showinfo("Admin","Payment Successfully")
                                Label(paymentframe,text="VAT",bg="#EAE8E9",font="Calibri 16").place(x=60,y=410)
                                Label(paymentframe,text="7 %",bg="#EAE8E9",font="Calibri 16").place(x=400,y=410)
                                Label(paymentframe,text="Point",bg="#EAE8E9",font="Calibri 16").place(x=60,y=450)
                                Label(paymentframe,text="%0.f"%(shoppoint),bg="#EAE8E9",font="Calibri 16").place(x=400,y=450)
                                Label(paymentframe,text="Total Cost",bg="#EAE8E9",font="Calibri 16 bold").place(x=60,y=490)
                                Label(paymentframe,text="%0.f"%(total),bg="#EAE8E9",font="Calibri 16 bold").place(x=400,y=490)
                                Button(paymentframe,text="Exit",bg="#EAE8E9",font="Calibri 16 bold",command=quit).place(x=890,y=480)
                                codeshop_menu_butt["state"] = "disabled"
                                codeshop_button_staff["state"] = "disabled"
                                sql = """
                                        DELETE FROM shop_code_orderprocess
                                        WHERE table_index=?"""
                                cursor.execute(sql,[table])   
                                conn.commit()
                                sql = """
                                        UPDATE shop_code_table
                                        SET status=?,name=?,amount=?
                                        WHERE table_no=? """
                                cursor.execute(sql,['free','','',table])
                                conn.commit()
                                conn.close()
                            else :
                                messagebox.showwarning("Admin","Not enough money in your wallet \n Please pay at the counter")   
                                codeshop_menu_butt["state"] = "disabled"
                                codeshop_button_staff["state"] = "disabled"
                                Button(paymentframe,text="Exit",bg="#EAE8E9",font="Calibri 16 bold",command=quit).place(x=890,y=480)
                                conn=sqlite3.connect("projectdb.db")
                                cursor = conn.cursor()
                                sql = """
                                        DELETE FROM shop_code_orderprocess
                                        WHERE table_index=?"""
                                cursor.execute(sql,[table])   
                                conn.commit()
                                sql = """
                                        UPDATE shop_code_table
                                        SET status=?,name=?,amount=?
                                        WHERE table_no=? """
                                cursor.execute(sql,['free','','',table])
                                conn.commit()
                                conn.close()
                        else :
                            pass 
                    # name
                    paymentframe = Frame(codeshop_allorder,bg="#FFFFFF")
                    paymentframe.place(x=0,y=0,width=1000,height=550)
                    Label(paymentframe,image=yayoishop_payment_1,bg="white").place(x=40,y=0)
                    Label(paymentframe,image=yayoishop_payment_2,bg="white").place(x=510,y=0)
                    # widget
                    text_yourwallet = Label(paymentframe,text="Yourwallet",bg="#FFE6A7").place(x=60,y=10)
                    text_balance = Label(paymentframe,text="balance : %s"%(cusinfo[7]),bg="#FFE6A7").place(x=120,y=50)
                    text_point = Label(paymentframe,text="Point   : %s"%(cusinfo[6]),bg="#FFE6A7").place(x=120,y=90)
                    text_member = Label(paymentframe,text="membership : %s"%(cusinfo[5]),bg="#FFE6A7").place(x=120,y=130)
                    # 
                    text_Payout = Label(paymentframe,text="Payout",bg="#FFF2D0").place(x=60,y=210)
                    text_name = Label(paymentframe,text="Name : %s %s"%(cusinfo[1],cusinfo[2]),bg="#FFF2D0").place(x=120,y=260)
                    discount = 1
                    discountpercent = 0
                    if cusinfo[5] == "None" :
                        discount = 0.95
                        discountpercent = 5
                    elif cusinfo[5] == "Level1" :
                        discount = 0.9
                        discountpercent = 10
                    elif cusinfo[5] == "Level2" :
                        discount = 0.85
                        discountpercent = 15
                    text_tax = Label(paymentframe,text="Discount : %s Percent"%(discountpercent),bg="#FFF2D0").place(x=120,y=310)
                    total = (Total*discount*1.07)//1
                    text_total = Label(paymentframe,text="Total : %0.f Baht"%(total),bg="#FFF2D0").place(x=120,y=360)
                    text_point = Label(paymentframe,text="Point : %s"%((Totalx/20)//1),bg="#FFF2D0").place(x=120,y=410)
                    but_payment = Button(paymentframe,image=yayoishop_confirm,bg="#FFF2D0",fg="black",font="Calibri 16",border=0,command=lambda : paymentprocess(total))
                    but_payment.place(x=140,y=460)
                #
                Label(codeshop_allorder,text="Status",bg="#FFFFFF").grid(row=0,column=0)
                Label(codeshop_allorder,text="Menu",bg="#FFFFFF").grid(row=0,column=1)
                Label(codeshop_allorder,text="Amount",bg="#FFFFFF").grid(row=0,column=2)
                Label(codeshop_allorder,text="Price per unit",bg="#FFFFFF").grid(row=0,column=3)
                #
                conn = sqlite3.connect("projectdb.db")
                cursor = conn.cursor()
                sql = """
                        SELECT * FROM shop_code_orderprocess 
                        WHERE table_index =?
                        """
                cursor.execute(sql,[codeshop_tablex.get()])
                orderresult= cursor.fetchall()
                conn.close()
                #
                Totalx = 0
                for i,data in enumerate(orderresult) :
                    if i < 10 :
                        if data[4] == "NF" : 
                            Label(codeshop_allorder,image=yayoishop_red_status,bg="#FFFFFF").grid(row=i+1,column=0)
                            Label(codeshop_allorder,text=data[1],bg="white").grid(row=i+1,column=1)
                            Label(codeshop_allorder,text=data[3],bg="white").grid(row=i+1,column=2)
                            Label(codeshop_allorder,text=data[2],bg="white").grid(row=i+1,column=3)
                        elif data[4] == "CF" : 
                            Label(codeshop_allorder,image=yayoishop_red_status,bg="#FFFFFF").grid(row=i+1,column=0)
                            Label(codeshop_allorder,text=data[1],bg="white").grid(row=i+1,column=1)
                            Label(codeshop_allorder,text=data[3],bg="white").grid(row=i+1,column=2)
                            Label(codeshop_allorder,text=data[2],bg="white").grid(row=i+1,column=3)
                        elif data[4] == "F" :
                            Label(codeshop_allorder,image=yayoishop_green_status,bg="#FFFFFF").grid(row=i+1,column=0)
                            Label(codeshop_allorder,text=data[1],bg="white").grid(row=i+1,column=1)
                            Label(codeshop_allorder,text=data[3],bg="white").grid(row=i+1,column=2)
                            Label(codeshop_allorder,text=data[2],bg="white").grid(row=i+1,column=3)
                            Totalx = Totalx + (int(data[3])*int(data[2]))
                conn = sqlite3.connect("projectdb.db")
                cursor = conn.cursor()
                sql = """
                            SELECT * FROM customer_information
                            WHERE firstname_customer=? """
                cursor.execute(sql,[customername])
                cusinfo = cursor.fetchone()
                Button(codeshop_allorder,text="Pay out",image=yayoishop_yayoishop_payout,command=lambda:codeshop_payment(Totalx,cusinfo),border=0,bg="white",activebackground="white").grid(row=20,column=1,columnspan=2)
            def staffcalling() :
                sql = """
                        UPDATE shop_code_table
                        SET staffcall=?
                        WHERE table_no=?"""
                cursor.execute(sql,["yes",codeshop_tablex.get()])
                conn.commit()
            #
            codepicture()
            amt_table = "0"
            if codeshop_tablex.get() == "1" or codeshop_tablex.get() == "2" or codeshop_tablex.get() == "3" :
                amt_table = "1-2"
            elif codeshop_tablex.get() == "4" or codeshop_tablex.get() == "5" or codeshop_tablex.get() == "6":
                amt_table = "3-4"
            elif codeshop_tablex.get() == "7" or codeshop_tablex.get() == "8":
                amt_table = "5-6"
            codeshop_frame = Frame(coderoot,bg="#FFFFFF")
            codeshop_frame.place(x=0,y=0,height=700,width=1000)
            Label(codeshop_frame,image=code_header,bg="#FFFFFF").place(x=-2,y=-5)
            Label(codeshop_frame,image=code_logo,bg="#FFFFFF").place(x=40,y=0)
            # table no
            codeshop_table_no_wframe = Label(codeshop_frame,image=codeshop_showtable,bg="#F8B4B9")
            codeshop_table_no_wframe.place(relx=0.519,y=15)
            codeshop_text_no_people = Label(codeshop_frame,text="Table No : %s \n %s people"%(codeshop_tablex.get(),amt_table),bg="#FFEDD6",font="Calibri 16")
            codeshop_text_no_people.place(relx=0.54,y=23)
            #
            codeshop_order_wfame = Label(codeshop_frame,image=yayoishop_whiteframe_2,bg="#F8B4B9")
            codeshop_order_wfame.place(relx=0.7,y=15)
            codeshop_chk_wfame = Label(codeshop_frame,image=yayoishop_whiteframe_2,bg="#F8B4B9")
            codeshop_chk_wfame.place(relx=0.8,y=15)
            codeshop_staff_wfame = Label(codeshop_frame,image=yayoishop_whiteframe_2,bg="#F8B4B9")
            codeshop_staff_wfame.place(relx=0.9,y=15)
            #
            codeshop_button_orders = Button(codeshop_frame,image=yayoishop_but_orders,border=0,bg="#FBE5E5",activebackground="#FBE5E5",command=codeshop_orderframe)
            codeshop_button_orders.place(relx=0.814,y=27)
            #
            conn = sqlite3.connect("projectdb.db")
            cursor = conn.cursor()
            sql = """
                        SELECT * FROM shop_code_orderprocess
                        WHERE table_index=? """
            cursor.execute(sql,[codeshop_tablex.get()])
            result = cursor.fetchall()
            nuborder = 0
            for i,date in enumerate(result) :
                nuborder = nuborder + 1
            lenorder = StringVar()
            lenorder.set(nuborder)
            #
            codeshop_amount_order = Label(codeshop_frame,border=0,bg="#FBE5E5",text=lenorder.get(),compound="center",font="bold")
            codeshop_amount_order.place(relx=0.855,y=19)
            # relx=0.752,y=17
            codeshop_button_staff = Button(codeshop_frame,image=yayoishop_but_staff,border=0,bg="#FBE5E5",activebackground="#FBE5E5",command=staffcalling)
            codeshop_button_staff.place(relx=0.92,y=26)
            # 1
            codeshop_menu_butt = Button(codeshop_frame,image=yayoishop_but_menu,border=0,bg="#FBE5E5",activebackground="#FBE5E5",command=codeshop_menuframe)
            codeshop_menu_butt.place(relx=0.72,y=28)
            codeshop_menuframe()
        def shin_mainprogram(table,customername) :
            global shinshop_indexpage,shinshop_indexmenubar,shinshop_tablex
            shinroot = Frame(root,bg="white")
            shinroot.place(x=0,y=0,width=1000,height=700)
            #
            conn = sqlite3.connect("projectdb.db")
            cursor = conn.cursor()
            sql = """
                        DELETE FROM shop_shin_queue
                        WHERE q_name=? """
            cursor.execute(sql,[customername])
            conn.commit()
            username = customername
            shinshop_indexpage = StringVar()
            shinshop_indexpage.set("0")
            shinshop_indexmenubar = StringVar()
            shinshop_indexmenubar.set("0")
            shinshop_tablex = StringVar()
            shinshop_tablex.set(table)
            def shinpicture() :
                #
                global shin_menuset_1, shin_menuset_2 ,shin_menuset_3 ,shin_menuset_4,shin_menuset_5,shin_menuset_6,shin_menuset_7,shin_menuset_8,shin_menuset_9,shin_menuset_10,shin_menuset_11,shin_menuset_12,shin_menuset_13,shin_menuset_14,shin_menuset_15,shin_menuset_16,shin_menuset_17,shin_menuset_18,shin_menuset_19,shin_menuset_20,shin_menuset_21,shin_menuset_22,shin_menuset_23,shin_menuset_24,shin_menuset_25,shin_menuset_26,shin_menuset_27,shin_menuset_28,shin_menuset_29,shin_menuset_30,shin_menuset_31,shin_menuset_32,shin_menuset_33,shin_menuset_34,shin_menuset_35,shin_menuset_36,shin_menuset_37,shin_menuset_38,shin_menuset_39,shin_menuset_40,shin_menuset_41,shin_menuset_42,shin_menuset_43,shin_menuset_44,shin_menuset_45,shin_menuset_46,shin_menuset_47,shin_menuset_48,shin_menuset_49,shin_menuset_50
                #
                global shinshop_mart_photo,shinshop_logo,shinshop_header,shinshop_showtable,shinshop_cat_1,shinshop_cat_2
                #
                shinshop_mart_photo = PhotoImage(file="image/Shinkanzen-shop/martphoto.png")
                shinshop_logo = PhotoImage(file="image/Shinkanzen-shop/logo-shin.png")
                shinshop_header = PhotoImage(file="image/Shinkanzen-shop/edge.png")
                shinshop_showtable = PhotoImage(file="image/Shinkanzen-shop/showtable.png")
                shinshop_cat_1 = PhotoImage(file="image/Shinkanzen-shop/cat1.png")
                shinshop_cat_2 = PhotoImage(file="image/Shinkanzen-shop/cat2.png")
                #
                shin_menuset_1 = PhotoImage(file="image/Shinkanzen-shop/menuset_1.png")
                shin_menuset_2 = PhotoImage(file="image/Shinkanzen-shop/menuset_2.png")
                shin_menuset_3 = PhotoImage(file="image/Shinkanzen-shop/menuset_3.png")
                shin_menuset_4 = PhotoImage(file="image/Shinkanzen-shop/menuset_4.png")
                shin_menuset_5 = PhotoImage(file="image/Shinkanzen-shop/menuset_5.png")
                shin_menuset_6 = PhotoImage(file="image/Shinkanzen-shop/menuset_6.png")
                shin_menuset_7 = PhotoImage(file="image/Shinkanzen-shop/menuset_7.png")
                shin_menuset_8 = PhotoImage(file="image/Shinkanzen-shop/menuset_8.png")
                shin_menuset_9 = PhotoImage(file="image/Shinkanzen-shop/menuset_9.png")
                shin_menuset_10 = PhotoImage(file="image/Shinkanzen-shop/menuset_10.png")
                shin_menuset_11 = PhotoImage(file="image/Shinkanzen-shop/menuset_11.png")
                shin_menuset_12 = PhotoImage(file="image/Shinkanzen-shop/menuset_12.png")
                shin_menuset_13 = PhotoImage(file="image/Shinkanzen-shop/menuset_13.png")
                shin_menuset_14 = PhotoImage(file="image/Shinkanzen-shop/menuset_14.png")
                shin_menuset_15 = PhotoImage(file="image/Shinkanzen-shop/menuset_15.png")
                shin_menuset_16 = PhotoImage(file="image/Shinkanzen-shop/menuset_16.png")
                shin_menuset_17 = PhotoImage(file="image/Shinkanzen-shop/menuset_17.png")
                shin_menuset_18 = PhotoImage(file="image/Shinkanzen-shop/menuset_18.png")
                shin_menuset_19 = PhotoImage(file="image/Shinkanzen-shop/menuset_19.png")
                shin_menuset_20 = PhotoImage(file="image/Shinkanzen-shop/menuset_20.png")
                shin_menuset_21 = PhotoImage(file="image/Shinkanzen-shop/menuset_21.png")
                shin_menuset_22 = PhotoImage(file="image/Shinkanzen-shop/menuset_22.png")
                shin_menuset_23 = PhotoImage(file="image/Shinkanzen-shop/menuset_23.png")
                shin_menuset_24 = PhotoImage(file="image/Shinkanzen-shop/menuset_24.png")
                shin_menuset_25 = PhotoImage(file="image/Shinkanzen-shop/menuset_25.png")
                shin_menuset_26 = PhotoImage(file="image/Shinkanzen-shop/menuset_26.png")
                shin_menuset_27 = PhotoImage(file="image/Shinkanzen-shop/menuset_27.png")
                shin_menuset_28 = PhotoImage(file="image/Shinkanzen-shop/menuset_28.png")
                shin_menuset_29 = PhotoImage(file="image/Shinkanzen-shop/menuset_29.png")
                shin_menuset_30 = PhotoImage(file="image/Shinkanzen-shop/menuset_30.png")
                shin_menuset_31 = PhotoImage(file="image/Shinkanzen-shop/menuset_31.png")
                shin_menuset_32 = PhotoImage(file="image/Shinkanzen-shop/menuset_32.png")
                shin_menuset_33 = PhotoImage(file="image/Shinkanzen-shop/menuset_33.png")
                shin_menuset_34 = PhotoImage(file="image/Shinkanzen-shop/menuset_34.png")
                shin_menuset_35 = PhotoImage(file="image/Shinkanzen-shop/menuset_35.png")
                shin_menuset_36 = PhotoImage(file="image/Shinkanzen-shop/menuset_36.png")
                shin_menuset_37 = PhotoImage(file="image/Shinkanzen-shop/menuset_37.png")
                shin_menuset_38 = PhotoImage(file="image/Shinkanzen-shop/menuset_38.png")
                shin_menuset_39 = PhotoImage(file="image/Shinkanzen-shop/menuset_39.png")
                shin_menuset_40 = PhotoImage(file="image/Shinkanzen-shop/menuset_40.png")
                shin_menuset_41 = PhotoImage(file="image/Shinkanzen-shop/menuset_41.png")
                shin_menuset_42 = PhotoImage(file="image/Shinkanzen-shop/menuset_42.png")
                shin_menuset_43 = PhotoImage(file="image/Shinkanzen-shop/menuset_43.png")
                shin_menuset_44 = PhotoImage(file="image/Shinkanzen-shop/menuset_44.png")
                shin_menuset_45 = PhotoImage(file="image/Shinkanzen-shop/menuset_45.png")
                shin_menuset_46 = PhotoImage(file="image/Shinkanzen-shop/menuset_46.png")
                shin_menuset_47 = PhotoImage(file="image/Shinkanzen-shop/menuset_47.png")
                shin_menuset_48 = PhotoImage(file="image/Shinkanzen-shop/menuset_48.png")
                shin_menuset_49 = PhotoImage(file="image/Shinkanzen-shop/menuset_49.png")
                shin_menuset_50 = PhotoImage(file="image/Shinkanzen-shop/menuset_50.png")
            def shinshop_addtocartprocess(ordername,price) :
                statusx = "NF"
                amount = 1
                conn = sqlite3.connect("projectdb.db")
                cursor = conn.cursor()
                sql = """
                        SELECT * FROM shop_shin_orderprocess
                        WHERE table_index = ? and amount > 0 and menu_name = ?"""
                cursor.execute(sql,[shinshop_tablex.get(),ordername])
                result = cursor.fetchone()
                conn.close()
                if result:
                    if ordername == result[1] :
                        newamount = int(result[3]) + 1
                        conn = sqlite3.connect("projectdb.db")
                        cursor = conn.cursor()
                        sql = """
                                UPDATE shop_shin_orderprocess
                                SET amount = ?
                                WHERE menu_name = ? """
                        cursor.execute(sql,[newamount,ordername])
                        conn.commit()
                        conn.close()
                        messagebox.showinfo("Admin","Added to cart")   
                else :
                    conn = sqlite3.connect("projectdb.db")
                    cursor = conn.cursor()
                    sql = """
                            INSERT INTO shop_shin_orderprocess 
                            values(?,?,?,?,?)"""
                    cursor.execute(sql,[shinshop_tablex.get(),ordername,price,amount,statusx])
                    conn.commit()
                    conn.close()
                    messagebox.showinfo("Admin","Added to cart")    
                    conn = sqlite3.connect("projectdb.db")
                    cursor = conn.cursor()
                    sql = """
                                SELECT * FROM shop_shin_orderprocess
                                WHERE table_index=? """
                    cursor.execute(sql,[shinshop_tablex.get()])
                    result = cursor.fetchall()
                    nuborder = 0
                    for i,date in enumerate(result) :
                        nuborder = nuborder + 1
                    lenorder = StringVar()
                    lenorder.set(nuborder)
                    shinshop_amount_order["text"] = lenorder.get()
            def shinshop_click1(e) :
                if shinshop_indexpage.get() == "1" :
                    shinshop_frameone.destroy()
                elif shinshop_indexpage.get() == "2" :
                    shinshop_frametwo.destroy()
                elif shinshop_indexpage.get() == "3" :
                    shinshop_framethree.destroy()
                elif shinshop_indexpage.get() == "4" :
                    shinshop_framefour.destroy()
                elif shinshop_indexpage.get() == "5" :
                    shinshop_framefive.destroy()
                shinshop_cate_1["image"] = shinshop_cat_1
                shinshop_cate_2["image"] = shinshop_cat_2
                shinshop_cate_3["image"] = shinshop_cat_2
                shinshop_cate_4["image"] = shinshop_cat_2
                shinshop_cate_5["image"] = shinshop_cat_2
            def shinshop_click2(e) :
                if shinshop_indexpage.get() == "1" :
                    shinshop_frameone.destroy()
                elif shinshop_indexpage.get() == "2" :
                    shinshop_frametwo.destroy()
                elif shinshop_indexpage.get() == "3" :
                    shinshop_framethree.destroy()
                elif shinshop_indexpage.get() == "4" :
                    shinshop_framefour.destroy()
                elif shinshop_indexpage.get() == "5" :
                    shinshop_framefive.destroy()
                shinshop_cate_1["image"] = shinshop_cat_2
                shinshop_cate_2["image"] = shinshop_cat_1
                shinshop_cate_3["image"] = shinshop_cat_2
                shinshop_cate_4["image"] = shinshop_cat_2
                shinshop_cate_5["image"] = shinshop_cat_2
            def shinshop_click3(e) :
                if shinshop_indexpage.get() == "1" :
                    shinshop_frameone.destroy()
                elif shinshop_indexpage.get() == "2" :
                    shinshop_frametwo.destroy()
                elif shinshop_indexpage.get() == "3" :
                    shinshop_framethree.destroy()
                elif shinshop_indexpage.get() == "4" :
                    shinshop_framefour.destroy()
                elif shinshop_indexpage.get() == "5" :
                    shinshop_framefive.destroy()
                shinshop_cate_1["image"] = shinshop_cat_2
                shinshop_cate_2["image"] = shinshop_cat_2
                shinshop_cate_3["image"] = shinshop_cat_1
                shinshop_cate_4["image"] = shinshop_cat_2
                shinshop_cate_5["image"] = shinshop_cat_2
            def shinshop_click4(e) :
                if shinshop_indexpage.get() == "1" :
                    shinshop_frameone.destroy()
                elif shinshop_indexpage.get() == "2" :
                    shinshop_frametwo.destroy()
                elif shinshop_indexpage.get() == "3" :
                    shinshop_framethree.destroy()
                elif shinshop_indexpage.get() == "4" :
                    shinshop_framefour.destroy()
                elif shinshop_indexpage.get() == "5" :
                    shinshop_framefive.destroy()
                shinshop_cate_1["image"] = shinshop_cat_2
                shinshop_cate_2["image"] = shinshop_cat_2
                shinshop_cate_3["image"] = shinshop_cat_2
                shinshop_cate_4["image"] = shinshop_cat_1
                shinshop_cate_5["image"] = shinshop_cat_2
            def shinshop_click5(e) :
                if shinshop_indexpage.get() == "1" :
                    shinshop_frameone.destroy()
                elif shinshop_indexpage.get() == "2" :
                    shinshop_frametwo.destroy()
                elif shinshop_indexpage.get() == "3" :
                    shinshop_framethree.destroy()
                elif shinshop_indexpage.get() == "4" :
                    shinshop_framefour.destroy()
                elif shinshop_indexpage.get() == "5" :
                    shinshop_framefive.destroy()
                shinshop_cate_1["image"] = shinshop_cat_2
                shinshop_cate_2["image"] = shinshop_cat_2
                shinshop_cate_3["image"] = shinshop_cat_2
                shinshop_cate_4["image"] = shinshop_cat_2
                shinshop_cate_5["image"] = shinshop_cat_1
            def shinshop_frame_one() : # 1
                global shinshop_frameone
                shinshop_indexpage.set("1")
                shinshop_frameone = Frame(shinshop_frame,bg="#FFFFFF")
                shinshop_frameone.place(x=0,y=155,width=1000,height=545)
                # menu 1
                menu_1 = Label(shinshop_frameone,image=shin_menuset_1,bg="#FFFFFF")
                menu_1.place(x=0,y=20)
                # menu 2
                menu_2 = Label(shinshop_frameone,image=shin_menuset_2,bg="#FFFFFF")
                menu_2.place(x=200,y=20)
                # menu 3
                menu_3 = Label(shinshop_frameone,image=shin_menuset_3,bg="#FFFFFF")
                menu_3.place(x=400,y=20)
                # menu 4
                menu_4 = Label(shinshop_frameone,image=shin_menuset_4,bg="#FFFFFF")
                menu_4.place(x=600,y=20)
                # menu 5
                menu_5 = Label(shinshop_frameone,image=shin_menuset_5,bg="#FFFFFF")
                menu_5.place(x=800,y=20)
                # menu 6
                menu_6 = Label(shinshop_frameone,image=shin_menuset_6,bg="#FFFFFF")
                menu_6.place(x=0,y=285)
                # menu 7 
                menu_7 = Label(shinshop_frameone,image=shin_menuset_7,bg="#FFFFFF")
                menu_7.place(x=200,y=285)
                # menu 8
                menu_8 = Label(shinshop_frameone,image=shin_menuset_8,bg="#FFFFFF")
                menu_8.place(x=400,y=285)
                # menu 9
                menu_9 = Label(shinshop_frameone,image=shin_menuset_9,bg="#FFFFFF")
                menu_9.place(x=600,y=285)
                # menu 10
                menu_10 = Label(shinshop_frameone,image=shin_menuset_10,bg="#FFFFFF")
                menu_10.place(x=800,y=285)
                #
                mart_number_1 = Button(shinshop_frameone,image=shinshop_mart_photo,border=0,command=lambda:shinshop_addtocartprocess("ข้าวหน้าแซลมอนไข่ดอง","109"),bg="#F6E9D6")
                mart_number_1.place(x=139,y=238)
                mart_number_2 = Button(shinshop_frameone,image=shinshop_mart_photo,border=0,command=lambda:shinshop_addtocartprocess("ข้าวหน้าเนื้อไข่ดอง","149"),bg="#F6E9D6")
                mart_number_2.place(x=339,y=238)
                mart_number_3 = Button(shinshop_frameone,image=shinshop_mart_photo,border=0,command=lambda:shinshop_addtocartprocess("ข้าวหน้าหมูย่างไข่ดอง","99"),bg="#F6E9D6")
                mart_number_3.place(x=539,y=238)
                mart_number_4 = Button(shinshop_frameone,image=shinshop_mart_photo,border=0,command=lambda:shinshop_addtocartprocess("ข้าวหน้าไก่คาราเกะ","89"),bg="#F6E9D6")
                mart_number_4.place(x=739,y=238)
                mart_number_5 = Button(shinshop_frameone,image=shinshop_mart_photo,border=0,command=lambda:shinshop_addtocartprocess("ข้าวหน้าเนื้อคารูบิย่าง","120"),bg="#F6E9D6")
                mart_number_5.place(x=939,y=238)
                mart_number_6 = Button(shinshop_frameone,image=shinshop_mart_photo,border=0,command=lambda:shinshop_addtocartprocess("ชุดแซลมอนกุ้งดองซีอิ้ว","380"),bg="#F6E9D6")
                mart_number_6.place(x=139,y=503)
                mart_number_7 = Button(shinshop_frameone,image=shinshop_mart_photo,border=0,command=lambda:shinshop_addtocartprocess("ทาโกะย่างมายองเนส","25"),bg="#F6E9D6")
                mart_number_7.place(x=339,y=503)
                mart_number_8 = Button(shinshop_frameone,image=shinshop_mart_photo,border=0,command=lambda:shinshop_addtocartprocess("ไข่แซลมอน","49"),bg="#F6E9D6")
                mart_number_8.place(x=539,y=503)
                mart_number_9 = Button(shinshop_frameone,image=shinshop_mart_photo,border=0,command=lambda:shinshop_addtocartprocess("โรลปลาไหลย่าง","199"),bg="#F6E9D6")
                mart_number_9.place(x=739,y=503)
                mart_number_10 = Button(shinshop_frameone,image=shinshop_mart_photo,border=0,command=lambda:shinshop_addtocartprocess("สลัดแซลมอน","75"),bg="#F6E9D6")
                mart_number_10.place(x=937,y=503)
            def shinshop_frame_two() : # 2
                global shinshop_frametwo
                shinshop_indexpage.set("2")
                shinshop_frametwo = Frame(shinshop_frame,bg="white")
                shinshop_frametwo.place(x=0,y=155,width=1000,height=545)
                # menu 1
                menu_1 = Label(shinshop_frametwo,image=shin_menuset_11,bg="#FFFFFF")
                menu_1.place(x=0,y=20)
                # menu 2
                menu_2 = Label(shinshop_frametwo,image=shin_menuset_12,bg="#FFFFFF")
                menu_2.place(x=200,y=20)
                # menu 3
                menu_3 = Label(shinshop_frametwo,image=shin_menuset_13,bg="#FFFFFF")
                menu_3.place(x=400,y=20)
                # menu 4
                menu_4 = Label(shinshop_frametwo,image=shin_menuset_14,bg="#FFFFFF")
                menu_4.place(x=600,y=20)
                # menu 5
                menu_5 = Label(shinshop_frametwo,image=shin_menuset_15,bg="#FFFFFF")
                menu_5.place(x=800,y=20)
                # menu 6
                menu_6 = Label(shinshop_frametwo,image=shin_menuset_16,bg="#FFFFFF")
                menu_6.place(x=0,y=285)
                # menu 7 
                menu_7 = Label(shinshop_frametwo,image=shin_menuset_17,bg="#FFFFFF")
                menu_7.place(x=200,y=285)
                # menu 8
                menu_8 = Label(shinshop_frametwo,image=shin_menuset_18,bg="#FFFFFF")
                menu_8.place(x=400,y=285)
                # menu 9
                menu_9 = Label(shinshop_frametwo,image=shin_menuset_19,bg="#FFFFFF")
                menu_9.place(x=600,y=285)
                # menu 10
                menu_10 = Label(shinshop_frametwo,image=shin_menuset_20,bg="#FFFFFF")
                menu_10.place(x=800,y=285)
                #
                mart_number_1 = Button(shinshop_frametwo,image=shinshop_mart_photo,border=0,command=lambda:shinshop_addtocartprocess("ซูชิแซลมอนสไปซี่","39"),bg="#F6E9D6")
                mart_number_1.place(x=139,y=238)
                mart_number_2 = Button(shinshop_frametwo,image=shinshop_mart_photo,border=0,command=lambda:shinshop_addtocartprocess("ซูชิเนื้อออสเตรเลีย","49"),bg="#F6E9D6")
                mart_number_2.place(x=339,y=238)
                mart_number_3 = Button(shinshop_frametwo,image=shinshop_mart_photo,border=0,command=lambda:shinshop_addtocartprocess("ซูชิแซล่อนสด","39"),bg="#F6E9D6")
                mart_number_3.place(x=537,y=238)
                mart_number_4 = Button(shinshop_frametwo,image=shinshop_mart_photo,border=0,command=lambda:shinshop_addtocartprocess("ซูชิยำสาหร่ายปูอัด","25"),bg="#F6E9D6")
                mart_number_4.place(x=737,y=238)
                mart_number_5 = Button(shinshop_frametwo,image=shinshop_mart_photo,border=0,command=lambda:shinshop_addtocartprocess("ซูชิแซลมอนย่างฟัวกราส์","30"),bg="#F6E9D6")
                mart_number_5.place(x=937,y=238)
                mart_number_6 = Button(shinshop_frametwo,image=shinshop_mart_photo,border=0,command=lambda:shinshop_addtocartprocess("ซูชิกุ้งทอดเบคอนสติป","25"),bg="#F6E9D6")
                mart_number_6.place(x=139,y=503)
                mart_number_7 = Button(shinshop_frametwo,image=shinshop_mart_photo,border=0,command=lambda:shinshop_addtocartprocess("ซูชิดับเบิ้ลหมูย่าง","15"),bg="#F6E9D6")
                mart_number_7.place(x=339,y=503)
                mart_number_8 = Button(shinshop_frametwo,image=shinshop_mart_photo,border=0,command=lambda:shinshop_addtocartprocess("ซูชิปลาไหลทะเลย่าง","70"),bg="#F6E9D6")
                mart_number_8.place(x=539,y=503)
                mart_number_9 = Button(shinshop_frametwo,image=shinshop_mart_photo,border=0,command=lambda:shinshop_addtocartprocess("ซูชิปลาไหลย่าง","70"),bg="#F6E9D6")
                mart_number_9.place(x=739,y=503)
                mart_number_10 = Button(shinshop_frametwo,image=shinshop_mart_photo,border=0,command=lambda:shinshop_addtocartprocess("ซูชิปลาซาบะดองย่าง","55"),bg="#F6E9D6")
                mart_number_10.place(x=939,y=503)
            def shinshop_frame_three() : # 5
                global shinshop_framethree
                shinshop_indexpage.set("3")
                shinshop_framethree = Frame(shinshop_frame,bg="white")
                shinshop_framethree.place(x=0,y=155,width=1000,height=545)
                # menu 1
                menu_1 = Label(shinshop_framethree,image=shin_menuset_21,bg="#FFFFFF")
                menu_1.place(x=0,y=20)
                # menu 2
                menu_2 = Label(shinshop_framethree,image=shin_menuset_22,bg="#FFFFFF")
                menu_2.place(x=200,y=20)
                # menu 3
                menu_3 = Label(shinshop_framethree,image=shin_menuset_23,bg="#FFFFFF")
                menu_3.place(x=400,y=20)
                # menu 4
                menu_4 = Label(shinshop_framethree,image=shin_menuset_24,bg="#FFFFFF")
                menu_4.place(x=600,y=20)
                # menu 5
                menu_5 = Label(shinshop_framethree,image=shin_menuset_25,bg="#FFFFFF")
                menu_5.place(x=800,y=20)
                # menu 6
                menu_6 = Label(shinshop_framethree,image=shin_menuset_26,bg="#FFFFFF")
                menu_6.place(x=0,y=285)
                # menu 7 
                menu_7 = Label(shinshop_framethree,image=shin_menuset_27,bg="#FFFFFF")
                menu_7.place(x=200,y=285)
                # menu 8
                menu_8 = Label(shinshop_framethree,image=shin_menuset_28,bg="#FFFFFF")
                menu_8.place(x=400,y=285)
                # menu 9
                menu_9 = Label(shinshop_framethree,image=shin_menuset_29,bg="#FFFFFF")
                menu_9.place(x=600,y=285)
                # menu 10
                menu_10 = Label(shinshop_framethree,image=shin_menuset_30,bg="#FFFFFF")
                menu_10.place(x=800,y=285)
                #
                mart_number_1 = Button(shinshop_framethree,image=shinshop_mart_photo,border=0,command=lambda:shinshop_addtocartprocess("โรลแซลมอนเอบิเทมปุระ","149"),bg="#F6E9D6")
                mart_number_1.place(x=137,y=238)
                mart_number_2 = Button(shinshop_framethree,image=shinshop_mart_photo,border=0,command=lambda:shinshop_addtocartprocess("โรลไข่กุ้งครั้นชี่","139"),bg="#F6E9D6")
                mart_number_2.place(x=337,y=238)
                mart_number_3 = Button(shinshop_framethree,image=shinshop_mart_photo,border=0,command=lambda:shinshop_addtocartprocess("โรลแซลมอน","139"),bg="#F6E9D6")
                mart_number_3.place(x=539,y=238)
                mart_number_4 = Button(shinshop_framethree,image=shinshop_mart_photo,border=0,command=lambda:shinshop_addtocartprocess("นอร์เวย์มากิ","139"),bg="#F6E9D6")
                mart_number_4.place(x=739,y=238)
                mart_number_5 = Button(shinshop_framethree,image=shinshop_mart_photo,border=0,command=lambda:shinshop_addtocartprocess("โรลแซลมอนย่างครีมชีส","165"),bg="#F6E9D6")
                mart_number_5.place(x=939,y=238)
                mart_number_6 = Button(shinshop_framethree,image=shinshop_mart_photo,border=0,command=lambda:shinshop_addtocartprocess("โรลวากิว","189"),bg="#F6E9D6")
                mart_number_6.place(x=139,y=503)
                mart_number_7 = Button(shinshop_framethree,image=shinshop_mart_photo,border=0,command=lambda:shinshop_addtocartprocess("ดราก้อนโรล","195"),bg="#F6E9D6")
                mart_number_7.place(x=341,y=503)
                mart_number_8 = Button(shinshop_framethree,image=shinshop_mart_photo,border=0,command=lambda:shinshop_addtocartprocess("โรลวากิวฟัวกราส์","199"),bg="#F6E9D6")
                mart_number_8.place(x=539,y=503)
                mart_number_9 = Button(shinshop_framethree,image=shinshop_mart_photo,border=0,command=lambda:shinshop_addtocartprocess("โรลกุ้งเทมปุระ","165"),bg="#F6E9D6")
                mart_number_9.place(x=739,y=503)
                mart_number_10 = Button(shinshop_framethree,image=shinshop_mart_photo,border=0,command=lambda:shinshop_addtocartprocess("แซลมอนสลัดมากิ","175"),bg="#F6E9D6")
                mart_number_10.place(x=937,y=503)
            def shinshop_frame_four() : # 4
                global shinshop_framefour
                shinshop_indexpage.set("4")
                shinshop_framefour = Frame(shinshop_frame,bg="white")
                shinshop_framefour.place(x=0,y=155,width=1000,height=545)
                # menu 1
                menu_1 = Label(shinshop_framefour,image=shin_menuset_31,bg="#FFFFFF")
                menu_1.place(x=0,y=20)
                # menu 2
                menu_2 = Label(shinshop_framefour,image=shin_menuset_32,bg="#FFFFFF")
                menu_2.place(x=200,y=20)
                # menu 3
                menu_3 = Label(shinshop_framefour,image=shin_menuset_33,bg="#FFFFFF")
                menu_3.place(x=400,y=20)
                # menu 4
                menu_4 = Label(shinshop_framefour,image=shin_menuset_34,bg="#FFFFFF")
                menu_4.place(x=600,y=20)
                # menu 5
                menu_5 = Label(shinshop_framefour,image=shin_menuset_35,bg="#FFFFFF")
                menu_5.place(x=800,y=20)
                # menu 6
                menu_6 = Label(shinshop_framefour,image=shin_menuset_36,bg="#FFFFFF")
                menu_6.place(x=0,y=285)
                # menu 7 
                menu_7 = Label(shinshop_framefour,image=shin_menuset_37,bg="#FFFFFF")
                menu_7.place(x=200,y=285)
                # menu 8
                menu_8 = Label(shinshop_framefour,image=shin_menuset_38,bg="#FFFFFF")
                menu_8.place(x=400,y=285)
                # menu 9
                menu_9 = Label(shinshop_framefour,image=shin_menuset_39,bg="#FFFFFF")
                menu_9.place(x=600,y=285)
                # menu 10
                menu_10 = Label(shinshop_framefour,image=shin_menuset_40,bg="#FFFFFF")
                menu_10.place(x=800,y=285)
                #
                mart_number_1 = Button(shinshop_framefour,image=shinshop_mart_photo,border=0,command=lambda:shinshop_addtocartprocess("ซาชิมิแซลมอน","99"),bg="#F6E9D6")
                mart_number_1.place(x=139,y=238)
                mart_number_2 = Button(shinshop_framefour,image=shinshop_mart_photo,border=0,command=lambda:shinshop_addtocartprocess("ซาชิมิรวม","175"),bg="#F6E9D6")
                mart_number_2.place(x=339,y=238)
                mart_number_3 = Button(shinshop_framefour,image=shinshop_mart_photo,border=0,command=lambda:shinshop_addtocartprocess("ซาชิมิปูอัด","55"),bg="#F6E9D6")
                mart_number_3.place(x=539,y=238)
                mart_number_4 = Button(shinshop_framefour,image=shinshop_mart_photo,border=0,command=lambda:shinshop_addtocartprocess("ซาชิมิหอยเชลล์","165"),bg="#F6E9D6")
                mart_number_4.place(x=739,y=238)
                mart_number_5 = Button(shinshop_framefour,image=shinshop_mart_photo,border=0,command=lambda:shinshop_addtocartprocess("ซาชิมิท้องแซลมอน","165"),bg="#F6E9D6")
                mart_number_5.place(x=939,y=238)
                mart_number_6 = Button(shinshop_framefour,image=shinshop_mart_photo,border=0,command=lambda:shinshop_addtocartprocess("ซาชิมิรวมใหญ่","299"),bg="#F6E9D6")
                mart_number_6.place(x=139,y=503)
                mart_number_7 = Button(shinshop_framefour,image=shinshop_mart_photo,border=0,command=lambda:shinshop_addtocartprocess("ซาชิมิไข่หวาน","75"),bg="#F6E9D6")
                mart_number_7.place(x=339,y=503)
                mart_number_8 = Button(shinshop_framefour,image=shinshop_mart_photo,border=0,command=lambda:shinshop_addtocartprocess("ซาชิมิทรัฟเฟิลแซลมอน","195"),bg="#F6E9D6")
                mart_number_8.place(x=539,y=503)
                mart_number_9 = Button(shinshop_framefour,image=shinshop_mart_photo,border=0,command=lambda:shinshop_addtocartprocess("แซลมอนกุ้งซาชิมิคัฟเค้ก","130"),bg="#F6E9D6")
                mart_number_9.place(x=737,y=503)
                mart_number_10 = Button(shinshop_framefour,image=shinshop_mart_photo,border=0,command=lambda:shinshop_addtocartprocess("ซาชิมิแซลมอนกุ้งอากะเอบิ","189"),bg="#F6E9D6")
                mart_number_10.place(x=937,y=503)
            def shinshop_frame_five() : # 3
                global shinshop_framefive
                shinshop_indexpage.set("5")
                shinshop_framefive = Frame(shinshop_frame,bg="white")
                shinshop_framefive.place(x=0,y=155,width=1000,height=545)
                # menu 1
                menu_1 = Label(shinshop_framefive,image=shin_menuset_41,bg="#FFFFFF")
                menu_1.place(x=0,y=20)
                # menu 2
                menu_2 = Label(shinshop_framefive,image=shin_menuset_42,bg="#FFFFFF")
                menu_2.place(x=200,y=20)
                # menu 3
                menu_3 = Label(shinshop_framefive,image=shin_menuset_43,bg="#FFFFFF")
                menu_3.place(x=400,y=20)
                # menu 4
                menu_4 = Label(shinshop_framefive,image=shin_menuset_44,bg="#FFFFFF")
                menu_4.place(x=600,y=20)
                # menu 5
                menu_5 = Label(shinshop_framefive,image=shin_menuset_45,bg="#FFFFFF")
                menu_5.place(x=800,y=20)
                # menu 6
                menu_6 = Label(shinshop_framefive,image=shin_menuset_46,bg="#FFFFFF")
                menu_6.place(x=0,y=285)
                # menu 7 
                menu_7 = Label(shinshop_framefive,image=shin_menuset_47,bg="#FFFFFF")
                menu_7.place(x=200,y=285)
                # menu 8
                menu_8 = Label(shinshop_framefive,image=shin_menuset_48,bg="#FFFFFF")
                menu_8.place(x=400,y=285)
                # menu 9
                menu_9 = Label(shinshop_framefive,image=shin_menuset_49,bg="#FFFFFF")
                menu_9.place(x=600,y=285)
                # menu 10
                menu_10 = Label(shinshop_framefive,image=shin_menuset_50,bg="#FFFFFF")
                menu_10.place(x=800,y=285)
                #
                mart_number_1 = Button(shinshop_framefive,image=shinshop_mart_photo,border=0,command=lambda:shinshop_addtocartprocess("สปาเก็ตตี้มะเขือเทศ","150"),bg="#F6E9D6")
                mart_number_1.place(x=137,y=238)
                mart_number_2 = Button(shinshop_framefive,image=shinshop_mart_photo,border=0,command=lambda:shinshop_addtocartprocess("สลัดแซลมอนสด","75"),bg="#F6E9D6")
                mart_number_2.place(x=337,y=238)
                mart_number_3 = Button(shinshop_framefive,image=shinshop_mart_photo,border=0,command=lambda:shinshop_addtocartprocess("สลัดผักปูอัด","45"),bg="#F6E9D6")
                mart_number_3.place(x=537,y=238)
                mart_number_4 = Button(shinshop_framefive,image=shinshop_mart_photo,border=0,command=lambda:shinshop_addtocartprocess("สลัดผักทูน่า","59"),bg="#F6E9D6")
                mart_number_4.place(x=739,y=238)
                mart_number_5 = Button(shinshop_framefive,image=shinshop_mart_photo,border=0,command=lambda:shinshop_addtocartprocess("สลัดผักกุ้ง","59"),bg="#F6E9D6")
                mart_number_5.place(x=939,y=238)
                mart_number_6 = Button(shinshop_framefive,image=shinshop_mart_photo,border=0,command=lambda:shinshop_addtocartprocess("ทูน่าสลัดโรล","49"),bg="#F6E9D6")
                mart_number_6.place(x=139,y=503)
                mart_number_7 = Button(shinshop_framefive,image=shinshop_mart_photo,border=0,command=lambda:shinshop_addtocartprocess("แซลม่อนสลัดโรล","69"),bg="#F6E9D6")
                mart_number_7.place(x=339,y=503)
                mart_number_8 = Button(shinshop_framefive,image=shinshop_mart_photo,border=0,command=lambda:shinshop_addtocartprocess("สลัดไข่โรล","55"),bg="#F6E9D6")
                mart_number_8.place(x=539,y=503)
                mart_number_9 = Button(shinshop_framefive,image=shinshop_mart_photo,border=0,command=lambda:shinshop_addtocartprocess("สลัดสาหร่ายพวงองุ่น","79"),bg="#F6E9D6")
                mart_number_9.place(x=739,y=503)
                mart_number_10 = Button(shinshop_framefive,image=shinshop_mart_photo,border=0,command=lambda:shinshop_addtocartprocess("สลัดแซลมอนสไปซี่","85"),bg="#F6E9D6")
                mart_number_10.place(x=939,y=503)
            def shinshop_menuframe() :
                global shinshop_cate_1 , shinshop_cate_2 , shinshop_cate_3 , shinshop_cate_4 , shinshop_cate_5 , shinshop_indexmenubar
                shinshop_menu_butt["state"] = "disabled"
                shinshop_button_orders["state"] = "active"
                if shinshop_indexmenubar.get() == "1" :
                    shinshop_allorder.destroy()
                elif shinshop_indexmenubar.get() == "0" :
                    pass
                shinshop_indexmenubar.set("0")
                if shinshop_indexpage.get() == "1" :
                    shinshop_frameone.destroy()
                elif shinshop_indexpage.get() == "2" :
                    shinshop_frametwo.destroy()
                elif shinshop_indexpage.get() == "3" :
                    shinshop_framethree.destroy()
                elif shinshop_indexpage.get() == "4" :
                    shinshop_framefour.destroy()
                elif shinshop_indexpage.get() == "5" :
                    shinshop_framefive.destroy()
                shinshop_frame_one()
                # category
                shinshop_cate_1 = Button(shinshop_frame,text="Recommand",image=shinshop_cat_1,compound="center",fg="#FFFFFF",border=0,bg="#FFFFFF",activebackground="#FFFFFF",font="Calibri 13",command=shinshop_frame_one)
                shinshop_cate_1.place(relx=0.375,y=110)
                #
                shinshop_cate_2 = Button(shinshop_frame,text="Sushi",image=shinshop_cat_2,compound="center",fg="#FFFFFF",border=0,bg="#FFFFFF",activebackground="#FFFFFF",font="Calibri 13",command=shinshop_frame_two)
                shinshop_cate_2.place(relx=0.5,y=110)
                #
                shinshop_cate_3 = Button(shinshop_frame,text="Maki",image=shinshop_cat_2,compound="center",fg="#FFFFFF",border=0,bg="#FFFFFF",activebackground="#FFFFFF",font="Calibri 13",command=shinshop_frame_three)
                shinshop_cate_3.place(relx=0.875,y=110)
                #
                shinshop_cate_4 = Button(shinshop_frame,text="Sashimi",image=shinshop_cat_2,compound="center",fg="#FFFFFF",border=0,bg="#FFFFFF",activebackground="#FFFFFF",font="Calibri 13",command=shinshop_frame_four)
                shinshop_cate_4.place(relx=0.75,y=110)
                #
                shinshop_cate_5 = Button(shinshop_frame,text="Salad",image=shinshop_cat_2,compound="center",fg="#FFFFFF",border=0,bg="#FFFFFF",activebackground="#FFFFFF",font="Calibri 13",command=shinshop_frame_five)
                shinshop_cate_5.place(relx=0.625,y=110)
                # bind
                shinshop_cate_1.bind("<Button-1>",shinshop_click1)
                shinshop_cate_2.bind("<Button-1>",shinshop_click2)
                shinshop_cate_3.bind("<Button-1>",shinshop_click3)
                shinshop_cate_4.bind("<Button-1>",shinshop_click4)
                shinshop_cate_5.bind("<Button-1>",shinshop_click5)
            def shinshop_orderframe() :
                global shinshop_indexmenubar,shinshop_allorder
                shinshop_menu_butt["state"] = "active"
                shinshop_button_orders["state"] = "disabled"
                if shinshop_indexmenubar.get() == "0" :
                    pass
                elif shinshop_indexmenubar.get() == "1" :
                    shinshop_allorder.destroy()
                shinshop_indexmenubar.set("1")
                #
                shinshop_cate_1.place(relx=10)
                shinshop_cate_2.place(relx=10)
                shinshop_cate_3.place(relx=10)
                shinshop_cate_4.place(relx=10)
                shinshop_cate_5.place(relx=10)
                #
                shinshop_allorder = Frame(shinshop_frame,bg="#FFFFFF")
                shinshop_allorder.place(x=0,y=150,width=1000,height=550)
                shinshop_allorder.rowconfigure((0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20),weight=1)
                shinshop_allorder.columnconfigure((0,1,2,3),weight=1)
                #
                def shinshop_payment(Total,cusinfo) :
                    def paymentprocess(total) :
                        ans = messagebox.askquestion("Admin","Are you sure you want to make a payment?")   
                        if ans == "yes" :
                            if float(cusinfo[7]) >= total :
                                shoppoint = 0
                                shoppoint = (total/20)//1
                                Label(paymentframe,image=yayoishop_payment_3,bg="white").place(x=40,y=0)
                                Label(paymentframe,text="Bill",bg="#EAE8E9",font="Calibri 25").place(x=60,y=10)
                                data = time.datetime.now()
                                time_now = (data.strftime("%x"))
                                Label(paymentframe,text=time_now,bg="#EAE8E9",font="Calibri 16").place(x=380,y=20)
                                Label(paymentframe,text="Menu",bg="#EAE8E9",font="Calibri 16 bold").place(x=60,y=70)
                                Label(paymentframe,text="Amount",bg="#EAE8E9",font="Calibri 16 bold").place(x=280,y=70)
                                Label(paymentframe,text="Price",bg="#EAE8E9",font="Calibri 16 bold").place(x=400,y=70)
                                yaix = 120
                                for i,data in enumerate(orderresult):
                                    if i < 6 :
                                        if data[4] == "F" :
                                            Label(paymentframe,text=data[1][0:25],bg="#EAE8E9",font="Calibri 16").place(x=60,y=yaix)
                                            Label(paymentframe,text=data[3],bg="#EAE8E9",font="Calibri 16").place(x=300,y=yaix)
                                            Label(paymentframe,text=data[2],bg="#EAE8E9",font="Calibri 16").place(x=400,y=yaix)
                                            yaix = yaix + 50
                                        else :
                                            pass
                                newbalance = (float(cusinfo[7])-total)//1
                                newpoint = (float(cusinfo[6])+shoppoint)//1
                                conn=sqlite3.connect("projectdb.db")
                                cursor = conn.cursor()
                                sql = """
                                            UPDATE customer_information
                                            SET money_customer=?,point_customer=?
                                            WHERE id_customer=?"""
                                cursor.execute(sql,[newbalance,newpoint,cusinfo[0]])
                                conn.commit()
                                messagebox.showinfo("Admin","Payment Successfully")
                                Label(paymentframe,text="VAT",bg="#EAE8E9",font="Calibri 16").place(x=60,y=410)
                                Label(paymentframe,text="7 %",bg="#EAE8E9",font="Calibri 16").place(x=400,y=410)
                                Label(paymentframe,text="Point",bg="#EAE8E9",font="Calibri 16").place(x=60,y=450)
                                Label(paymentframe,text="%0.f"%(shoppoint),bg="#EAE8E9",font="Calibri 16").place(x=400,y=450)
                                Label(paymentframe,text="Total Cost",bg="#EAE8E9",font="Calibri 16 bold").place(x=60,y=490)
                                Label(paymentframe,text="%0.f"%(total),bg="#EAE8E9",font="Calibri 16 bold").place(x=400,y=490)
                                Button(paymentframe,text="Exit",bg="#EAE8E9",font="Calibri 16 bold",command=quit).place(x=890,y=480)
                                shinshop_menu_butt["state"] = "disabled"
                                shinshop_button_staff["state"] = "disabled"
                                sql = """
                                        DELETE FROM shop_shin_orderprocess
                                        WHERE table_index=?"""
                                cursor.execute(sql,[table])   
                                conn.commit()
                                sql = """
                                        UPDATE shop_shin_table
                                        SET status=?,name=?,amount=?
                                        WHERE table_no=? """
                                cursor.execute(sql,['free','','',table])
                                conn.commit()
                                conn.close()
                            else :
                                messagebox.showwarning("Admin","Not enough money in your wallet \n Please Pay at the counter")   
                                shinshop_menu_butt["state"] = "disabled"
                                shinshop_button_staff["state"] = "disabled"
                                Button(paymentframe,text="Exit",bg="#EAE8E9",font="Calibri 16 bold",command=quit).place(x=890,y=480)
                                conn=sqlite3.connect("projectdb.db")
                                cursor = conn.cursor()
                                sql = """
                                        DELETE FROM shop_shin_orderprocess
                                        WHERE table_index=?"""
                                cursor.execute(sql,[table])   
                                conn.commit()
                                sql = """
                                        UPDATE shop_shin_table
                                        SET status=?,name=?,amount=?
                                        WHERE table_no=? """
                                cursor.execute(sql,['free','','',table])
                                conn.commit()
                                conn.close()
                        else :
                            pass 
                    # name
                    paymentframe = Frame(shinshop_allorder,bg="#FFFFFF")
                    paymentframe.place(x=0,y=0,width=1000,height=550)
                    Label(paymentframe,image=yayoishop_payment_1,bg="white").place(x=40,y=0)
                    Label(paymentframe,image=yayoishop_payment_2,bg="white").place(x=510,y=0)
                    # widget
                    text_yourwallet = Label(paymentframe,text="Yourwallet",bg="#FFE6A7").place(x=60,y=10)
                    text_balance = Label(paymentframe,text="balance : %s"%(cusinfo[7]),bg="#FFE6A7").place(x=120,y=50)
                    text_point = Label(paymentframe,text="Point   : %s"%(cusinfo[6]),bg="#FFE6A7").place(x=120,y=90)
                    text_member = Label(paymentframe,text="membership : %s"%(cusinfo[5]),bg="#FFE6A7").place(x=120,y=130)
                    # 
                    text_Payout = Label(paymentframe,text="Payout",bg="#FFF2D0").place(x=60,y=210)
                    text_name = Label(paymentframe,text="Name : %s %s"%(cusinfo[1],cusinfo[2]),bg="#FFF2D0").place(x=120,y=260)
                    discount = 1
                    discountpercent = 0
                    if cusinfo[5] == "None" :
                        discount = 0.95
                        discountpercent = 5
                    elif cusinfo[5] == "Level1" :
                        discount = 0.9
                        discountpercent = 10
                    elif cusinfo[5] == "Level2" :
                        discount = 0.85
                        discountpercent = 15
                    text_tax = Label(paymentframe,text="Discount : %s Percent"%(discountpercent),bg="#FFF2D0").place(x=120,y=310)
                    total = (Total*discount*1.07)//1
                    text_total = Label(paymentframe,text="Total : %0.f Baht"%(total),bg="#FFF2D0").place(x=120,y=360)
                    text_point = Label(paymentframe,text="Point : %s"%((Totalx/20)//1),bg="#FFF2D0").place(x=120,y=410)
                    but_payment = Button(paymentframe,image=yayoishop_confirm,bg="#FFF2D0",fg="black",font="Calibri 16",border=0,command=lambda : paymentprocess(total))
                    but_payment.place(x=140,y=460)
                #
                Label(shinshop_allorder,text="Status",bg="#FFFFFF").grid(row=0,column=0)
                Label(shinshop_allorder,text="Menu",bg="#FFFFFF").grid(row=0,column=1)
                Label(shinshop_allorder,text="Amount",bg="#FFFFFF").grid(row=0,column=2)
                Label(shinshop_allorder,text="Price per unit",bg="#FFFFFF").grid(row=0,column=3)
                #
                conn = sqlite3.connect("projectdb.db")
                cursor = conn.cursor()
                sql = """
                        SELECT * FROM shop_shin_orderprocess 
                        WHERE table_index =?
                        """
                cursor.execute(sql,[shinshop_tablex.get()])
                orderresult= cursor.fetchall()
                conn.close()
                #
                Totalx = 0
                for i,data in enumerate(orderresult) :
                    if i < 10 :
                        if data[4] == "NF" : 
                            Label(shinshop_allorder,image=yayoishop_red_status,bg="#FFFFFF").grid(row=i+1,column=0)
                            Label(shinshop_allorder,text=data[1],bg="white").grid(row=i+1,column=1)
                            Label(shinshop_allorder,text=data[3],bg="white").grid(row=i+1,column=2)
                            Label(shinshop_allorder,text=data[2],bg="white").grid(row=i+1,column=3)
                        elif data[4] == "CF" : 
                            Label(shinshop_allorder,image=yayoishop_red_status,bg="#FFFFFF").grid(row=i+1,column=0)
                            Label(shinshop_allorder,text=data[1],bg="white").grid(row=i+1,column=1)
                            Label(shinshop_allorder,text=data[3],bg="white").grid(row=i+1,column=2)
                            Label(shinshop_allorder,text=data[2],bg="white").grid(row=i+1,column=3)
                        elif data[4] == "F" :
                            Label(shinshop_allorder,image=yayoishop_green_status,bg="#FFFFFF").grid(row=i+1,column=0)
                            Label(shinshop_allorder,text=data[1],bg="white").grid(row=i+1,column=1)
                            Label(shinshop_allorder,text=data[3],bg="white").grid(row=i+1,column=2)
                            Label(shinshop_allorder,text=data[2],bg="white").grid(row=i+1,column=3)
                            Totalx = Totalx + (int(data[3])*int(data[2]))
                conn = sqlite3.connect("projectdb.db")
                cursor = conn.cursor()
                sql = """
                            SELECT * FROM customer_information
                            WHERE firstname_customer=? """
                cursor.execute(sql,[customername])
                cusinfo = cursor.fetchone()
                Button(shinshop_allorder,text="Pay out",image=yayoishop_yayoishop_payout,command=lambda:shinshop_payment(Totalx,cusinfo),border=0,bg="white",activebackground="white").grid(row=20,column=1,columnspan=2)
            def staffcalling() :
                sql = """
                        UPDATE shop_shin_table
                        SET staffcall=?
                        WHERE table_no=?"""
                cursor.execute(sql,["yes",shinshop_tablex.get()])
                conn.commit()
            #
            shinpicture()
            amt_table = "0"
            if shinshop_tablex.get() == "1" or shinshop_tablex.get() == "2" or shinshop_tablex.get() == "3" :
                amt_table = "1-2"
            elif shinshop_tablex.get() == "4" or shinshop_tablex.get() == "5" or shinshop_tablex.get() == "6":
                amt_table = "3-4"
            elif shinshop_tablex.get() == "7" or shinshop_tablex.get() == "8":
                amt_table = "5-6"
            shinshop_frame = Frame(shinroot,bg="#FFFFFF")
            shinshop_frame.place(x=0,y=0,height=700,width=1000)
            Label(shinshop_frame,image=shin_header,bg="#FFFFFF").place(x=-2,y=-5)
            Label(shinshop_frame,image=shin_logo,bg="#FFFFFF").place(x=40,y=0)
            # table no
            shinshop_table_no_wframe = Label(shinshop_frame,image=shinshop_showtable,bg="#EADDCD")
            shinshop_table_no_wframe.place(relx=0.519,y=15)
            shinshop_text_no_people = Label(shinshop_frame,text="Table No : %s \n %s people"%(shinshop_tablex.get(),amt_table),bg="#FFEDD6",font="Calibri 16")
            shinshop_text_no_people.place(relx=0.54,y=23)
            #
            shinshop_order_wfame = Label(shinshop_frame,image=yayoishop_whiteframe_2,bg="#EADDCD")
            shinshop_order_wfame.place(relx=0.7,y=15)
            shinshop_chk_wfame = Label(shinshop_frame,image=yayoishop_whiteframe_2,bg="#EADDCD")
            shinshop_chk_wfame.place(relx=0.8,y=15)
            shinshop_staff_wfame = Label(shinshop_frame,image=yayoishop_whiteframe_2,bg="#EADDCD")
            shinshop_staff_wfame.place(relx=0.9,y=15)
            #
            shinshop_button_orders = Button(shinshop_frame,image=yayoishop_but_orders,border=0,bg="#FBE5E5",activebackground="#FBE5E5",command=shinshop_orderframe)
            shinshop_button_orders.place(relx=0.814,y=27)
            #
            conn = sqlite3.connect("projectdb.db")
            cursor = conn.cursor()
            sql = """
                        SELECT * FROM shop_shin_orderprocess
                        WHERE table_index=? """
            cursor.execute(sql,[shinshop_tablex.get()])
            result = cursor.fetchall()
            nuborder = 0
            for i,date in enumerate(result) :
                nuborder = nuborder + 1
            lenorder = StringVar()
            lenorder.set(nuborder)
            #
            shinshop_amount_order = Label(shinshop_frame,border=0,bg="#FBE5E5",text=lenorder.get(),compound="center",font="bold")
            shinshop_amount_order.place(relx=0.855,y=19)
            # relx=0.752,y=17
            shinshop_button_staff = Button(shinshop_frame,image=yayoishop_but_staff,border=0,bg="#FBE5E5",activebackground="#FBE5E5",command=staffcalling)
            shinshop_button_staff.place(relx=0.92,y=26)
            # 1
            shinshop_menu_butt = Button(shinshop_frame,image=yayoishop_but_menu,border=0,bg="#FBE5E5",activebackground="#FBE5E5",command=shinshop_menuframe)
            shinshop_menu_butt.place(relx=0.72,y=28)
            shinshop_menuframe()
        def ohk_mainprogram(table,customername) :
            global ohkshop_indexpage,ohkshop_indexmenubar,ohkshop_tablex
            ohkroot = Frame(root,bg="#FFF6E8")
            ohkroot.place(x=0,y=0,width=1000,height=700)
            #
            conn = sqlite3.connect("projectdb.db")
            cursor = conn.cursor()
            sql = """
                        DELETE FROM shop_ohk_queue
                        WHERE q_name=? """
            cursor.execute(sql,[customername])
            conn.commit()
            username = customername
            ohkshop_indexpage = StringVar()
            ohkshop_indexpage.set("0")
            ohkshop_indexmenubar = StringVar()
            ohkshop_indexmenubar.set("0")
            ohkshop_tablex = StringVar()
            ohkshop_tablex.set(table)
            def ohkpicture() :
                #
                global ohk_menuset_1, ohk_menuset_2 ,ohk_menuset_3 ,ohk_menuset_4,ohk_menuset_5,ohk_menuset_6,ohk_menuset_7,ohk_menuset_8,ohk_menuset_9,ohk_menuset_10,ohk_menuset_11,ohk_menuset_12,ohk_menuset_13,ohk_menuset_14,ohk_menuset_15,ohk_menuset_16,ohk_menuset_17,ohk_menuset_18,ohk_menuset_19,ohk_menuset_20,ohk_menuset_21,ohk_menuset_22,ohk_menuset_23,ohk_menuset_24,ohk_menuset_25,ohk_menuset_26,ohk_menuset_27,ohk_menuset_28,ohk_menuset_29,ohk_menuset_30,ohk_menuset_31,ohk_menuset_32,ohk_menuset_33,ohk_menuset_34,ohk_menuset_35,ohk_menuset_36,ohk_menuset_37,ohk_menuset_38,ohk_menuset_39,ohk_menuset_40,ohk_menuset_41,ohk_menuset_42,ohk_menuset_43,ohk_menuset_44,ohk_menuset_45,ohk_menuset_46,ohk_menuset_47,ohk_menuset_48,ohk_menuset_49,ohk_menuset_50
                #
                global ohkshop_mart_photo,ohkshop_logo,ohkshop_header,ohkshop_showtable,ohkshop_cat_1,ohkshop_cat_2
                #
                ohkshop_mart_photo = PhotoImage(file="image/Ohkajhu-shop/martphoto.png")
                ohkshop_logo = PhotoImage(file="image/Ohkajhu-shop/logo-ohk.png")
                ohkshop_header = PhotoImage(file="image/Ohkajhu-shop/edge.png")
                ohkshop_showtable = PhotoImage(file="image/Ohkajhu-shop/showtable.png")
                ohkshop_cat_1 = PhotoImage(file="image/Ohkajhu-shop/cat1.png")
                ohkshop_cat_2 = PhotoImage(file="image/Ohkajhu-shop/cat2.png")
                #
                ohk_menuset_1 = PhotoImage(file="image/Ohkajhu-shop/menuset_1.png")
                ohk_menuset_2 = PhotoImage(file="image/Ohkajhu-shop/menuset_2.png")
                ohk_menuset_3 = PhotoImage(file="image/Ohkajhu-shop/menuset_3.png")
                ohk_menuset_4 = PhotoImage(file="image/Ohkajhu-shop/menuset_4.png")
                ohk_menuset_5 = PhotoImage(file="image/Ohkajhu-shop/menuset_5.png")
                ohk_menuset_6 = PhotoImage(file="image/Ohkajhu-shop/menuset_6.png")
                ohk_menuset_7 = PhotoImage(file="image/Ohkajhu-shop/menuset_7.png")
                ohk_menuset_8 = PhotoImage(file="image/Ohkajhu-shop/menuset_8.png")
                ohk_menuset_9 = PhotoImage(file="image/Ohkajhu-shop/menuset_9.png")
                ohk_menuset_10 = PhotoImage(file="image/Ohkajhu-shop/menuset_10.png")
                ohk_menuset_11 = PhotoImage(file="image/Ohkajhu-shop/menuset_11.png")
                ohk_menuset_12 = PhotoImage(file="image/Ohkajhu-shop/menuset_12.png")
                ohk_menuset_13 = PhotoImage(file="image/Ohkajhu-shop/menuset_13.png")
                ohk_menuset_14 = PhotoImage(file="image/Ohkajhu-shop/menuset_14.png")
                ohk_menuset_15 = PhotoImage(file="image/Ohkajhu-shop/menuset_15.png")
                ohk_menuset_16 = PhotoImage(file="image/Ohkajhu-shop/menuset_16.png")
                ohk_menuset_17 = PhotoImage(file="image/Ohkajhu-shop/menuset_17.png")
                ohk_menuset_18 = PhotoImage(file="image/Ohkajhu-shop/menuset_18.png")
                ohk_menuset_19 = PhotoImage(file="image/Ohkajhu-shop/menuset_19.png")
                ohk_menuset_20 = PhotoImage(file="image/Ohkajhu-shop/menuset_20.png")
                ohk_menuset_21 = PhotoImage(file="image/Ohkajhu-shop/menuset_21.png")
                ohk_menuset_22 = PhotoImage(file="image/Ohkajhu-shop/menuset_22.png")
                ohk_menuset_23 = PhotoImage(file="image/Ohkajhu-shop/menuset_23.png")
                ohk_menuset_24 = PhotoImage(file="image/Ohkajhu-shop/menuset_24.png")
                ohk_menuset_25 = PhotoImage(file="image/Ohkajhu-shop/menuset_25.png")
                ohk_menuset_26 = PhotoImage(file="image/Ohkajhu-shop/menuset_26.png")
                ohk_menuset_27 = PhotoImage(file="image/Ohkajhu-shop/menuset_27.png")
                ohk_menuset_28 = PhotoImage(file="image/Ohkajhu-shop/menuset_28.png")
                ohk_menuset_29 = PhotoImage(file="image/Ohkajhu-shop/menuset_29.png")
                ohk_menuset_30 = PhotoImage(file="image/Ohkajhu-shop/menuset_30.png")
                ohk_menuset_31 = PhotoImage(file="image/Ohkajhu-shop/menuset_31.png")
                ohk_menuset_32 = PhotoImage(file="image/Ohkajhu-shop/menuset_32.png")
                ohk_menuset_33 = PhotoImage(file="image/Ohkajhu-shop/menuset_33.png")
                ohk_menuset_34 = PhotoImage(file="image/Ohkajhu-shop/menuset_34.png")
                ohk_menuset_35 = PhotoImage(file="image/Ohkajhu-shop/menuset_35.png")
                ohk_menuset_36 = PhotoImage(file="image/Ohkajhu-shop/menuset_36.png")
                ohk_menuset_37 = PhotoImage(file="image/Ohkajhu-shop/menuset_37.png")
                ohk_menuset_38 = PhotoImage(file="image/Ohkajhu-shop/menuset_38.png")
                ohk_menuset_39 = PhotoImage(file="image/Ohkajhu-shop/menuset_39.png")
                ohk_menuset_40 = PhotoImage(file="image/Ohkajhu-shop/menuset_40.png")
                ohk_menuset_41 = PhotoImage(file="image/Ohkajhu-shop/menuset_41.png")
                ohk_menuset_42 = PhotoImage(file="image/Ohkajhu-shop/menuset_42.png")
                ohk_menuset_43 = PhotoImage(file="image/Ohkajhu-shop/menuset_43.png")
                ohk_menuset_44 = PhotoImage(file="image/Ohkajhu-shop/menuset_44.png")
                ohk_menuset_45 = PhotoImage(file="image/Ohkajhu-shop/menuset_45.png")
                ohk_menuset_46 = PhotoImage(file="image/Ohkajhu-shop/menuset_46.png")
                ohk_menuset_47 = PhotoImage(file="image/Ohkajhu-shop/menuset_47.png")
                ohk_menuset_48 = PhotoImage(file="image/Ohkajhu-shop/menuset_48.png")
                ohk_menuset_49 = PhotoImage(file="image/Ohkajhu-shop/menuset_49.png")
                ohk_menuset_50 = PhotoImage(file="image/Ohkajhu-shop/menuset_50.png")
            def ohkshop_addtocartprocess(ordername,price) :
                statusx = "NF"
                amount = 1
                conn = sqlite3.connect("projectdb.db")
                cursor = conn.cursor()
                sql = """
                        SELECT * FROM shop_ohk_orderprocess
                        WHERE table_index = ? and amount > 0 and menu_name = ?"""
                cursor.execute(sql,[ohkshop_tablex.get(),ordername])
                result = cursor.fetchone()
                conn.close()
                if result:
                    if ordername == result[1] :
                        newamount = int(result[3]) + 1
                        conn = sqlite3.connect("projectdb.db")
                        cursor = conn.cursor()
                        sql = """
                                UPDATE shop_ohk_orderprocess
                                SET amount = ?
                                WHERE menu_name = ? """
                        cursor.execute(sql,[newamount,ordername])
                        conn.commit()
                        conn.close()
                        messagebox.showinfo("Admin","Added to cart")    
                else :
                    conn = sqlite3.connect("projectdb.db")
                    cursor = conn.cursor()
                    sql = """
                            INSERT INTO shop_ohk_orderprocess 
                            values(?,?,?,?,?)"""
                    cursor.execute(sql,[ohkshop_tablex.get(),ordername,price,amount,statusx])
                    conn.commit()
                    conn.close()
                    messagebox.showinfo("Admin","Added to cart")    
                    conn = sqlite3.connect("projectdb.db")
                    cursor = conn.cursor()
                    sql = """
                                SELECT * FROM shop_ohk_orderprocess
                                WHERE table_index=? """
                    cursor.execute(sql,[ohkshop_tablex.get()])
                    result = cursor.fetchall()
                    nuborder = 0
                    for i,date in enumerate(result) :
                        nuborder = nuborder + 1
                    lenorder = StringVar()
                    lenorder.set(nuborder)
                    ohkshop_amount_order["text"] = lenorder.get()
            def ohkshop_click1(e) :
                if ohkshop_indexpage.get() == "1" :
                    ohkshop_frameone.destroy()
                elif ohkshop_indexpage.get() == "2" :
                    ohkshop_frametwo.destroy()
                elif ohkshop_indexpage.get() == "3" :
                    ohkshop_framethree.destroy()
                elif ohkshop_indexpage.get() == "4" :
                    ohkshop_framefour.destroy()
                elif ohkshop_indexpage.get() == "5" :
                    ohkshop_framefive.destroy()
                ohkshop_cate_1["image"] = ohkshop_cat_1
                ohkshop_cate_2["image"] = ohkshop_cat_2
                ohkshop_cate_3["image"] = ohkshop_cat_2
                ohkshop_cate_4["image"] = ohkshop_cat_2
                ohkshop_cate_5["image"] = ohkshop_cat_2
            def ohkshop_click2(e) :
                if ohkshop_indexpage.get() == "1" :
                    ohkshop_frameone.destroy()
                elif ohkshop_indexpage.get() == "2" :
                    ohkshop_frametwo.destroy()
                elif ohkshop_indexpage.get() == "3" :
                    ohkshop_framethree.destroy()
                elif ohkshop_indexpage.get() == "4" :
                    ohkshop_framefour.destroy()
                elif ohkshop_indexpage.get() == "5" :
                    ohkshop_framefive.destroy()
                ohkshop_cate_1["image"] = ohkshop_cat_2
                ohkshop_cate_2["image"] = ohkshop_cat_1
                ohkshop_cate_3["image"] = ohkshop_cat_2
                ohkshop_cate_4["image"] = ohkshop_cat_2
                ohkshop_cate_5["image"] = ohkshop_cat_2
            def ohkshop_click3(e) :
                if ohkshop_indexpage.get() == "1" :
                    ohkshop_frameone.destroy()
                elif ohkshop_indexpage.get() == "2" :
                    ohkshop_frametwo.destroy()
                elif ohkshop_indexpage.get() == "3" :
                    ohkshop_framethree.destroy()
                elif ohkshop_indexpage.get() == "4" :
                    ohkshop_framefour.destroy()
                elif ohkshop_indexpage.get() == "5" :
                    ohkshop_framefive.destroy()
                ohkshop_cate_1["image"] = ohkshop_cat_2
                ohkshop_cate_2["image"] = ohkshop_cat_2
                ohkshop_cate_3["image"] = ohkshop_cat_1
                ohkshop_cate_4["image"] = ohkshop_cat_2
                ohkshop_cate_5["image"] = ohkshop_cat_2
            def ohkshop_click4(e) :
                if ohkshop_indexpage.get() == "1" :
                    ohkshop_frameone.destroy()
                elif ohkshop_indexpage.get() == "2" :
                    ohkshop_frametwo.destroy()
                elif ohkshop_indexpage.get() == "3" :
                    ohkshop_framethree.destroy()
                elif ohkshop_indexpage.get() == "4" :
                    ohkshop_framefour.destroy()
                elif ohkshop_indexpage.get() == "5" :
                    ohkshop_framefive.destroy()
                ohkshop_cate_1["image"] = ohkshop_cat_2
                ohkshop_cate_2["image"] = ohkshop_cat_2
                ohkshop_cate_3["image"] = ohkshop_cat_2
                ohkshop_cate_4["image"] = ohkshop_cat_1
                ohkshop_cate_5["image"] = ohkshop_cat_2
            def ohkshop_click5(e) :
                if ohkshop_indexpage.get() == "1" :
                    ohkshop_frameone.destroy()
                elif ohkshop_indexpage.get() == "2" :
                    ohkshop_frametwo.destroy()
                elif ohkshop_indexpage.get() == "3" :
                    ohkshop_framethree.destroy()
                elif ohkshop_indexpage.get() == "4" :
                    ohkshop_framefour.destroy()
                elif ohkshop_indexpage.get() == "5" :
                    ohkshop_framefive.destroy()
                ohkshop_cate_1["image"] = ohkshop_cat_2
                ohkshop_cate_2["image"] = ohkshop_cat_2
                ohkshop_cate_3["image"] = ohkshop_cat_2
                ohkshop_cate_4["image"] = ohkshop_cat_2
                ohkshop_cate_5["image"] = ohkshop_cat_1
            def ohkshop_frame_one() : # 1
                global ohkshop_frameone
                ohkshop_indexpage.set("1")
                ohkshop_frameone = Frame(ohkshop_frame,bg="#FFFFFF")
                ohkshop_frameone.place(x=0,y=155,width=1000,height=545)
                # menu 1
                menu_1 = Label(ohkshop_frameone,image=ohk_menuset_1,bg="#FFFFFF")
                menu_1.place(x=0,y=20)
                # menu 2
                menu_2 = Label(ohkshop_frameone,image=ohk_menuset_2,bg="#FFFFFF")
                menu_2.place(x=200,y=20)
                # menu 3
                menu_3 = Label(ohkshop_frameone,image=ohk_menuset_3,bg="#FFFFFF")
                menu_3.place(x=400,y=20)
                # menu 4
                menu_4 = Label(ohkshop_frameone,image=ohk_menuset_4,bg="#FFFFFF")
                menu_4.place(x=600,y=20)
                # menu 5
                menu_5 = Label(ohkshop_frameone,image=ohk_menuset_5,bg="#FFFFFF")
                menu_5.place(x=800,y=20)
                # menu 6
                menu_6 = Label(ohkshop_frameone,image=ohk_menuset_6,bg="#FFFFFF")
                menu_6.place(x=0,y=285)
                # menu 7 
                menu_7 = Label(ohkshop_frameone,image=ohk_menuset_7,bg="#FFFFFF")
                menu_7.place(x=200,y=285)
                # menu 8
                menu_8 = Label(ohkshop_frameone,image=ohk_menuset_8,bg="#FFFFFF")
                menu_8.place(x=400,y=285)
                # menu 9
                menu_9 = Label(ohkshop_frameone,image=ohk_menuset_9,bg="#FFFFFF")
                menu_9.place(x=600,y=285)
                # menu 10
                menu_10 = Label(ohkshop_frameone,image=ohk_menuset_10,bg="#FFFFFF")
                menu_10.place(x=800,y=285)
                #
                mart_number_1 = Button(ohkshop_frameone,image=ohkshop_mart_photo,border=0,command=lambda:ohkshop_addtocartprocess("สเต็กซี่โครง","259"))
                mart_number_1.place(x=139,y=238)
                mart_number_2 = Button(ohkshop_frameone,image=ohkshop_mart_photo,border=0,command=lambda:ohkshop_addtocartprocess("เลดี้ ริบส์ โอ้กะจู๋","825"))
                mart_number_2.place(x=339,y=238)
                mart_number_3 = Button(ohkshop_frameone,image=ohkshop_mart_photo,border=0,command=lambda:ohkshop_addtocartprocess("สเต็กไก่สอดไส้ชีส","230"))
                mart_number_3.place(x=539,y=238)
                mart_number_4 = Button(ohkshop_frameone,image=ohkshop_mart_photo,border=0,command=lambda:ohkshop_addtocartprocess("ไส้กรอกย่างรวม","220"))
                mart_number_4.place(x=739,y=238)
                mart_number_5 = Button(ohkshop_frameone,image=ohkshop_mart_photo,border=0,command=lambda:ohkshop_addtocartprocess("สลัดแซลมอนซาซิมิ","150"))
                mart_number_5.place(x=939,y=238)
                mart_number_6 = Button(ohkshop_frameone,image=ohkshop_mart_photo,border=0,command=lambda:ohkshop_addtocartprocess("ชีสทอด","150"))
                mart_number_6.place(x=139,y=503)
                mart_number_7 = Button(ohkshop_frameone,image=ohkshop_mart_photo,border=0,command=lambda:ohkshop_addtocartprocess("ซุปฟักทองญี่ปุ่น","120"))
                mart_number_7.place(x=339,y=503)
                mart_number_8 = Button(ohkshop_frameone,image=ohkshop_mart_photo,border=0,command=lambda:ohkshop_addtocartprocess("สลัดเห็ดรวมกุ้งย่าง","200"))
                mart_number_8.place(x=539,y=503)
                mart_number_9 = Button(ohkshop_frameone,image=ohkshop_mart_photo,border=0,command=lambda:ohkshop_addtocartprocess("สเต็กแซลมอน","255"))
                mart_number_9.place(x=739,y=503)
                mart_number_10 = Button(ohkshop_frameone,image=ohkshop_mart_photo,border=0,command=lambda:ohkshop_addtocartprocess("แองเจิ้ลแฮร์ปูครีมไข่กุ้ง","220"))
                mart_number_10.place(x=939,y=503)
            def ohkshop_frame_two() : # 2
                global ohkshop_frametwo
                ohkshop_indexpage.set("2")
                ohkshop_frametwo = Frame(ohkshop_frame,bg="white")
                ohkshop_frametwo.place(x=0,y=155,width=1000,height=545)
                # menu 1
                menu_1 = Label(ohkshop_frametwo,image=ohk_menuset_11,bg="#FFFFFF")
                menu_1.place(x=0,y=20)
                # menu 2
                menu_2 = Label(ohkshop_frametwo,image=ohk_menuset_12,bg="#FFFFFF")
                menu_2.place(x=200,y=20)
                # menu 3
                menu_3 = Label(ohkshop_frametwo,image=ohk_menuset_13,bg="#FFFFFF")
                menu_3.place(x=400,y=20)
                # menu 4
                menu_4 = Label(ohkshop_frametwo,image=ohk_menuset_14,bg="#FFFFFF")
                menu_4.place(x=600,y=20)
                # menu 5
                menu_5 = Label(ohkshop_frametwo,image=ohk_menuset_15,bg="#FFFFFF")
                menu_5.place(x=800,y=20)
                # menu 6
                menu_6 = Label(ohkshop_frametwo,image=ohk_menuset_16,bg="#FFFFFF")
                menu_6.place(x=0,y=285)
                # menu 7 
                menu_7 = Label(ohkshop_frametwo,image=ohk_menuset_17,bg="#FFFFFF")
                menu_7.place(x=200,y=285)
                # menu 8
                menu_8 = Label(ohkshop_frametwo,image=ohk_menuset_18,bg="#FFFFFF")
                menu_8.place(x=400,y=285)
                # menu 9
                menu_9 = Label(ohkshop_frametwo,image=ohk_menuset_19,bg="#FFFFFF")
                menu_9.place(x=600,y=285)
                # menu 10
                menu_10 = Label(ohkshop_frametwo,image=ohk_menuset_20,bg="#FFFFFF")
                menu_10.place(x=800,y=285)
                #
                mart_number_1 = Button(ohkshop_frametwo,image=ohkshop_mart_photo,border=0,command=lambda:ohkshop_addtocartprocess("สเต็กทีโบน","395"))
                mart_number_1.place(x=139,y=238)
                mart_number_2 = Button(ohkshop_frametwo,image=ohkshop_mart_photo,border=0,command=lambda:ohkshop_addtocartprocess("ฟิช แอนด์ ชิพส์","195"))
                mart_number_2.place(x=339,y=238)
                mart_number_3 = Button(ohkshop_frametwo,image=ohkshop_mart_photo,border=0,command=lambda:ohkshop_addtocartprocess("สเต็กไก่","190"))
                mart_number_3.place(x=539,y=238)
                mart_number_4 = Button(ohkshop_frametwo,image=ohkshop_mart_photo,border=0,command=lambda:ohkshop_addtocartprocess("สเต็กแซลมอนซอสบีทรูท","265"))
                mart_number_4.place(x=739,y=238)
                mart_number_5 = Button(ohkshop_frametwo,image=ohkshop_mart_photo,border=0,command=lambda:ohkshop_addtocartprocess("พอร์คชอป เฟรนช์คัท","320"))
                mart_number_5.place(x=939,y=238)
                mart_number_6 = Button(ohkshop_frametwo,image=ohkshop_mart_photo,border=0,command=lambda:ohkshop_addtocartprocess("สเต็กแซลมอน","255"))
                mart_number_6.place(x=139,y=503)
                mart_number_7 = Button(ohkshop_frametwo,image=ohkshop_mart_photo,border=0,command=lambda:ohkshop_addtocartprocess("สเต็กไก่ย่าง","165"))
                mart_number_7.place(x=339,y=503)
                mart_number_8 = Button(ohkshop_frametwo,image=ohkshop_mart_photo,border=0,command=lambda:ohkshop_addtocartprocess("สเต็กปลาอัลมอนด์กรอบ","275"))
                mart_number_8.place(x=539,y=503)
                mart_number_9 = Button(ohkshop_frametwo,image=ohkshop_mart_photo,border=0,command=lambda:ohkshop_addtocartprocess("สเต็กแฮม","150"))
                mart_number_9.place(x=739,y=503)
                mart_number_10 = Button(ohkshop_frametwo,image=ohkshop_mart_photo,border=0,command=lambda:ohkshop_addtocartprocess("สเต็กปลาหิมะย่าง","225"))
                mart_number_10.place(x=939,y=503)
            def ohkshop_frame_three() : # 5
                global ohkshop_framethree
                ohkshop_indexpage.set("3")
                ohkshop_framethree = Frame(ohkshop_frame,bg="white")
                ohkshop_framethree.place(x=0,y=155,width=1000,height=545)
                # menu 1
                menu_1 = Label(ohkshop_framethree,image=ohk_menuset_21,bg="#FFFFFF")
                menu_1.place(x=0,y=20)
                # menu 2
                menu_2 = Label(ohkshop_framethree,image=ohk_menuset_22,bg="#FFFFFF")
                menu_2.place(x=200,y=20)
                # menu 3
                menu_3 = Label(ohkshop_framethree,image=ohk_menuset_23,bg="#FFFFFF")
                menu_3.place(x=400,y=20)
                # menu 4
                menu_4 = Label(ohkshop_framethree,image=ohk_menuset_24,bg="#FFFFFF")
                menu_4.place(x=600,y=20)
                # menu 5
                menu_5 = Label(ohkshop_framethree,image=ohk_menuset_25,bg="#FFFFFF")
                menu_5.place(x=800,y=20)
                # menu 6
                menu_6 = Label(ohkshop_framethree,image=ohk_menuset_26,bg="#FFFFFF")
                menu_6.place(x=0,y=285)
                # menu 7 
                menu_7 = Label(ohkshop_framethree,image=ohk_menuset_27,bg="#FFFFFF")
                menu_7.place(x=200,y=285)
                # menu 8
                menu_8 = Label(ohkshop_framethree,image=ohk_menuset_28,bg="#FFFFFF")
                menu_8.place(x=400,y=285)
                # menu 9
                menu_9 = Label(ohkshop_framethree,image=ohk_menuset_29,bg="#FFFFFF")
                menu_9.place(x=600,y=285)
                # menu 10
                menu_10 = Label(ohkshop_framethree,image=ohk_menuset_30,bg="#FFFFFF")
                menu_10.place(x=800,y=285)
                #
                mart_number_1 = Button(ohkshop_framethree,image=ohkshop_mart_photo,border=0,command=lambda:ohkshop_addtocartprocess("สปาเก็ตตี้มะเขือเทศ","150"))
                mart_number_1.place(x=139,y=238)
                mart_number_2 = Button(ohkshop_framethree,image=ohkshop_mart_photo,border=0,command=lambda:ohkshop_addtocartprocess("สปาเก็ตตี้พะแนงกุ้ง","175"))
                mart_number_2.place(x=339,y=238)
                mart_number_3 = Button(ohkshop_framethree,image=ohkshop_mart_photo,border=0,command=lambda:ohkshop_addtocartprocess("สปาเก็ตตี้คาโบนาร่า","165"))
                mart_number_3.place(x=539,y=238)
                mart_number_4 = Button(ohkshop_framethree,image=ohkshop_mart_photo,border=0,command=lambda:ohkshop_addtocartprocess("สปาเก็ตตี้ขี้เมาทะเล","225"))
                mart_number_4.place(x=739,y=238)
                mart_number_5 = Button(ohkshop_framethree,image=ohkshop_mart_photo,border=0,command=lambda:ohkshop_addtocartprocess("สปาเกตตี้ปูนิ่ม","250"))
                mart_number_5.place(x=939,y=238)
                mart_number_6 = Button(ohkshop_framethree,image=ohkshop_mart_photo,border=0,command=lambda:ohkshop_addtocartprocess("สปาเก็ตตี้ขี้เมาไก่โหระพา","199"))
                mart_number_6.place(x=139,y=503)
                mart_number_7 = Button(ohkshop_framethree,image=ohkshop_mart_photo,border=0,command=lambda:ohkshop_addtocartprocess("แองเจิ้ลแฮร์ปูครีมไข่กุ้ง","220"))
                mart_number_7.place(x=339,y=503)
                mart_number_8 = Button(ohkshop_framethree,image=ohkshop_mart_photo,border=0,command=lambda:ohkshop_addtocartprocess("แองเจิ้ลแฮร์เห็ดรวม","195"))
                mart_number_8.place(x=539,y=503)
                mart_number_9 = Button(ohkshop_framethree,image=ohkshop_mart_photo,border=0,command=lambda:ohkshop_addtocartprocess("สปาเก็ตตี้ต้มยำปูกุ้ง","285"))
                mart_number_9.place(x=739,y=503)
                mart_number_10 = Button(ohkshop_framethree,image=ohkshop_mart_photo,border=0,command=lambda:ohkshop_addtocartprocess("ฟูซิลลี่ทูน่าต้มยำแห้ง","270"))
                mart_number_10.place(x=939,y=503)
            def ohkshop_frame_four() : # 4
                global ohkshop_framefour
                ohkshop_indexpage.set("4")
                ohkshop_framefour = Frame(ohkshop_frame,bg="white")
                ohkshop_framefour.place(x=0,y=155,width=1000,height=545)
                # menu 1
                menu_1 = Label(ohkshop_framefour,image=ohk_menuset_31,bg="#FFFFFF")
                menu_1.place(x=0,y=20)
                # menu 2
                menu_2 = Label(ohkshop_framefour,image=ohk_menuset_32,bg="#FFFFFF")
                menu_2.place(x=200,y=20)
                # menu 3
                menu_3 = Label(ohkshop_framefour,image=ohk_menuset_33,bg="#FFFFFF")
                menu_3.place(x=400,y=20)
                # menu 4
                menu_4 = Label(ohkshop_framefour,image=ohk_menuset_34,bg="#FFFFFF")
                menu_4.place(x=600,y=20)
                # menu 5
                menu_5 = Label(ohkshop_framefour,image=ohk_menuset_35,bg="#FFFFFF")
                menu_5.place(x=800,y=20)
                # menu 6
                menu_6 = Label(ohkshop_framefour,image=ohk_menuset_36,bg="#FFFFFF")
                menu_6.place(x=0,y=285)
                # menu 7 
                menu_7 = Label(ohkshop_framefour,image=ohk_menuset_37,bg="#FFFFFF")
                menu_7.place(x=200,y=285)
                # menu 8
                menu_8 = Label(ohkshop_framefour,image=ohk_menuset_38,bg="#FFFFFF")
                menu_8.place(x=400,y=285)
                # menu 9
                menu_9 = Label(ohkshop_framefour,image=ohk_menuset_39,bg="#FFFFFF")
                menu_9.place(x=600,y=285)
                # menu 10
                menu_10 = Label(ohkshop_framefour,image=ohk_menuset_40,bg="#FFFFFF")
                menu_10.place(x=800,y=285)
                #
                mart_number_1 = Button(ohkshop_framefour,image=ohkshop_mart_photo,border=0,command=lambda:ohkshop_addtocartprocess("ชีสทอด","150"))
                mart_number_1.place(x=139,y=238)
                mart_number_2 = Button(ohkshop_framefour,image=ohkshop_mart_photo,border=0,command=lambda:ohkshop_addtocartprocess("ขนมปังกระเทียม","150"))
                mart_number_2.place(x=339,y=238)
                mart_number_3 = Button(ohkshop_framefour,image=ohkshop_mart_photo,border=0,command=lambda:ohkshop_addtocartprocess("ปังกระเทียมครีมชีส","190"))
                mart_number_3.place(x=539,y=238)
                mart_number_4 = Button(ohkshop_framefour,image=ohkshop_mart_photo,border=0,command=lambda:ohkshop_addtocartprocess("ยำถั่วพลูกุ้ง","189"))
                mart_number_4.place(x=739,y=238)
                mart_number_5 = Button(ohkshop_framefour,image=ohkshop_mart_photo,border=0,command=lambda:ohkshop_addtocartprocess("เปาะเปี๊ยะครีมชีสปูโรล","79"))
                mart_number_5.place(x=939,y=238)
                mart_number_6 = Button(ohkshop_framefour,image=ohkshop_mart_photo,border=0,command=lambda:ohkshop_addtocartprocess("โรลผักแซลมอนกุ้ง","95"))
                mart_number_6.place(x=139,y=503)
                mart_number_7 = Button(ohkshop_framefour,image=ohkshop_mart_photo,border=0,command=lambda:ohkshop_addtocartprocess("ซุปสวีทกรีนครีม","150"))
                mart_number_7.place(x=339,y=503)
                mart_number_8 = Button(ohkshop_framefour,image=ohkshop_mart_photo,border=0,command=lambda:ohkshop_addtocartprocess("ซุปหัวหอมใบไทม์","130"))
                mart_number_8.place(x=539,y=503)
                mart_number_9 = Button(ohkshop_framefour,image=ohkshop_mart_photo,border=0,command=lambda:ohkshop_addtocartprocess("ซุปข้าวโพด แครอท","130"))
                mart_number_9.place(x=739,y=503)
                mart_number_10 = Button(ohkshop_framefour,image=ohkshop_mart_photo,border=0,command=lambda:ohkshop_addtocartprocess("ซุปเห็ดสามอย่าง","120"))
                mart_number_10.place(x=939,y=503)
            def ohkshop_frame_five() : # 3
                global ohkshop_framefive
                ohkshop_indexpage.set("5")
                ohkshop_framefive = Frame(ohkshop_frame,bg="white")
                ohkshop_framefive.place(x=0,y=155,width=1000,height=545)
                # menu 1
                menu_1 = Label(ohkshop_framefive,image=ohk_menuset_41,bg="#FFFFFF")
                menu_1.place(x=0,y=20)
                # menu 2
                menu_2 = Label(ohkshop_framefive,image=ohk_menuset_42,bg="#FFFFFF")
                menu_2.place(x=200,y=20)
                # menu 3
                menu_3 = Label(ohkshop_framefive,image=ohk_menuset_43,bg="#FFFFFF")
                menu_3.place(x=400,y=20)
                # menu 4
                menu_4 = Label(ohkshop_framefive,image=ohk_menuset_44,bg="#FFFFFF")
                menu_4.place(x=600,y=20)
                # menu 5
                menu_5 = Label(ohkshop_framefive,image=ohk_menuset_45,bg="#FFFFFF")
                menu_5.place(x=800,y=20)
                # menu 6
                menu_6 = Label(ohkshop_framefive,image=ohk_menuset_46,bg="#FFFFFF")
                menu_6.place(x=0,y=285)
                # menu 7 
                menu_7 = Label(ohkshop_framefive,image=ohk_menuset_47,bg="#FFFFFF")
                menu_7.place(x=200,y=285)
                # menu 8
                menu_8 = Label(ohkshop_framefive,image=ohk_menuset_48,bg="#FFFFFF")
                menu_8.place(x=400,y=285)
                # menu 9
                menu_9 = Label(ohkshop_framefive,image=ohk_menuset_49,bg="#FFFFFF")
                menu_9.place(x=600,y=285)
                # menu 10
                menu_10 = Label(ohkshop_framefive,image=ohk_menuset_50,bg="#FFFFFF")
                menu_10.place(x=800,y=285)
                #
                mart_number_1 = Button(ohkshop_framefive,image=ohkshop_mart_photo,border=0,command=lambda:ohkshop_addtocartprocess("สลัดแซลมอนสาหร่าย","260"))
                mart_number_1.place(x=139,y=238)
                mart_number_2 = Button(ohkshop_framefive,image=ohkshop_mart_photo,border=0,command=lambda:ohkshop_addtocartprocess("สลัดธัญพืช","160"))
                mart_number_2.place(x=339,y=238)
                mart_number_3 = Button(ohkshop_framefive,image=ohkshop_mart_photo,border=0,command=lambda:ohkshop_addtocartprocess("เม็กซิกัน นาโช่","230"))
                mart_number_3.place(x=539,y=238)
                mart_number_4 = Button(ohkshop_framefive,image=ohkshop_mart_photo,border=0,command=lambda:ohkshop_addtocartprocess("สลัดแซลมอนย่าง","215"))
                mart_number_4.place(x=739,y=238)
                mart_number_5 = Button(ohkshop_framefive,image=ohkshop_mart_photo,border=0,command=lambda:ohkshop_addtocartprocess("สลัดเห็ดรวมกุ้งย่าง","200"))
                mart_number_5.place(x=939,y=238)
                mart_number_6 = Button(ohkshop_framefive,image=ohkshop_mart_photo,border=0,command=lambda:ohkshop_addtocartprocess("สลัดทูน่ายำแซ่บ","169"))
                mart_number_6.place(x=139,y=503)
                mart_number_7 = Button(ohkshop_framefive,image=ohkshop_mart_photo,border=0,command=lambda:ohkshop_addtocartprocess("สลัดปูอะโวคาโด","195"))
                mart_number_7.place(x=339,y=503)
                mart_number_8 = Button(ohkshop_framefive,image=ohkshop_mart_photo,border=0,command=lambda:ohkshop_addtocartprocess("สลัดเห็ดเทมปุระ","135"))
                mart_number_8.place(x=539,y=503)
                mart_number_9 = Button(ohkshop_framefive,image=ohkshop_mart_photo,border=0,command=lambda:ohkshop_addtocartprocess("สลัดหมูสับกุ้งสด","175"))
                mart_number_9.place(x=739,y=503)
                mart_number_10 = Button(ohkshop_framefive,image=ohkshop_mart_photo,border=0,command=lambda:ohkshop_addtocartprocess("สลัดคะน้าเบคอนกรอบ","190"))
                mart_number_10.place(x=939,y=503)
            def ohkshop_menuframe() :
                global ohkshop_cate_1 , ohkshop_cate_2 , ohkshop_cate_3 , ohkshop_cate_4 , ohkshop_cate_5 , ohkshop_indexmenubar
                ohkshop_menu_butt["state"] = "disabled"
                ohkshop_button_orders["state"] = "active"
                if ohkshop_indexmenubar.get() == "1" :
                    ohkshop_allorder.destroy()
                elif ohkshop_indexmenubar.get() == "0" :
                    pass
                ohkshop_indexmenubar.set("0")
                if ohkshop_indexpage.get() == "1" :
                    ohkshop_frameone.destroy()
                elif ohkshop_indexpage.get() == "2" :
                    ohkshop_frametwo.destroy()
                elif ohkshop_indexpage.get() == "3" :
                    ohkshop_framethree.destroy()
                elif ohkshop_indexpage.get() == "4" :
                    ohkshop_framefour.destroy()
                elif ohkshop_indexpage.get() == "5" :
                    ohkshop_framefive.destroy()
                ohkshop_frame_one()
                # category
                ohkshop_cate_1 = Button(ohkshop_frame,text="Recommand",image=ohkshop_cat_1,compound="center",fg="#FFFFFF",border=0,bg="#FFFFFF",activebackground="#FFFFFF",font="Calibri 13",command=ohkshop_frame_one)
                ohkshop_cate_1.place(relx=0.375,y=110)
                #
                ohkshop_cate_2 = Button(ohkshop_frame,text="Steak",image=ohkshop_cat_2,compound="center",fg="#FFFFFF",border=0,bg="#FFFFFF",activebackground="#FFFFFF",font="Calibri 13",command=ohkshop_frame_two)
                ohkshop_cate_2.place(relx=0.5,y=110)
                #
                ohkshop_cate_3 = Button(ohkshop_frame,text="Spaghetti",image=ohkshop_cat_2,compound="center",fg="#FFFFFF",border=0,bg="#FFFFFF",activebackground="#FFFFFF",font="Calibri 13",command=ohkshop_frame_three)
                ohkshop_cate_3.place(relx=0.875,y=110)
                #
                ohkshop_cate_4 = Button(ohkshop_frame,text="Appetizer",image=ohkshop_cat_2,compound="center",fg="#FFFFFF",border=0,bg="#FFFFFF",activebackground="#FFFFFF",font="Calibri 13",command=ohkshop_frame_four)
                ohkshop_cate_4.place(relx=0.75,y=110)
                #
                ohkshop_cate_5 = Button(ohkshop_frame,text="Salad",image=ohkshop_cat_2,compound="center",fg="#FFFFFF",border=0,bg="#FFFFFF",activebackground="#FFFFFF",font="Calibri 13",command=ohkshop_frame_five)
                ohkshop_cate_5.place(relx=0.625,y=110)
                # bind
                ohkshop_cate_1.bind("<Button-1>",ohkshop_click1)
                ohkshop_cate_2.bind("<Button-1>",ohkshop_click2)
                ohkshop_cate_3.bind("<Button-1>",ohkshop_click3)
                ohkshop_cate_4.bind("<Button-1>",ohkshop_click4)
                ohkshop_cate_5.bind("<Button-1>",ohkshop_click5)
            def ohkshop_orderframe() :
                global ohkshop_indexmenubar,ohkshop_allorder
                ohkshop_menu_butt["state"] = "active"
                ohkshop_button_orders["state"] = "disabled"
                if ohkshop_indexmenubar.get() == "0" :
                    pass
                elif ohkshop_indexmenubar.get() == "1" :
                    ohkshop_allorder.destroy()
                ohkshop_indexmenubar.set("1")
                #
                ohkshop_cate_1.place(relx=10)
                ohkshop_cate_2.place(relx=10)
                ohkshop_cate_3.place(relx=10)
                ohkshop_cate_4.place(relx=10)
                ohkshop_cate_5.place(relx=10)
                #
                ohkshop_allorder = Frame(ohkshop_frame,bg="#FFFFFF")
                ohkshop_allorder.place(x=0,y=150,width=1000,height=550)
                ohkshop_allorder.rowconfigure((0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20),weight=1)
                ohkshop_allorder.columnconfigure((0,1,2,3),weight=1)
                #
                def ohkshop_payment(Total,cusinfo) :
                    def paymentprocess(total) :
                        ans = messagebox.askquestion("Admin","Are you sure you want to make a payment?")    
                        if ans == "yes" :
                            if float(cusinfo[7]) >= total :
                                shoppoint = 0
                                shoppoint = (total/20)//1
                                Label(paymentframe,image=yayoishop_payment_3,bg="white").place(x=40,y=0)
                                Label(paymentframe,text="Bill",bg="#EAE8E9",font="Calibri 25").place(x=60,y=10)
                                data = time.datetime.now()
                                time_now = (data.strftime("%x"))
                                Label(paymentframe,text=time_now,bg="#EAE8E9",font="Calibri 16").place(x=380,y=20)
                                Label(paymentframe,text="Menu",bg="#EAE8E9",font="Calibri 16 bold").place(x=60,y=70)
                                Label(paymentframe,text="Amount",bg="#EAE8E9",font="Calibri 16 bold").place(x=280,y=70)
                                Label(paymentframe,text="Price",bg="#EAE8E9",font="Calibri 16 bold").place(x=400,y=70)
                                yaix = 120
                                for i,data in enumerate(orderresult):
                                    if i < 6 :
                                        if data[4] == "F" :
                                            Label(paymentframe,text=data[1][0:25],bg="#EAE8E9",font="Calibri 16").place(x=60,y=yaix)
                                            Label(paymentframe,text=data[3],bg="#EAE8E9",font="Calibri 16").place(x=300,y=yaix)
                                            Label(paymentframe,text=data[2],bg="#EAE8E9",font="Calibri 16").place(x=400,y=yaix)
                                            yaix = yaix + 50
                                        else :
                                            pass
                                newbalance = (float(cusinfo[7])-total)//1
                                newpoint = (float(cusinfo[6])+shoppoint)//1
                                conn=sqlite3.connect("projectdb.db")
                                cursor = conn.cursor()
                                sql = """
                                            UPDATE customer_information
                                            SET money_customer=?,point_customer=?
                                            WHERE id_customer=?"""
                                cursor.execute(sql,[newbalance,newpoint,cusinfo[0]])
                                conn.commit()
                                messagebox.showinfo("Admin","Payment Successfully")
                                Label(paymentframe,text="VAT",bg="#EAE8E9",font="Calibri 16").place(x=60,y=410)
                                Label(paymentframe,text="7 %",bg="#EAE8E9",font="Calibri 16").place(x=400,y=410)
                                Label(paymentframe,text="Point",bg="#EAE8E9",font="Calibri 16").place(x=60,y=450)
                                Label(paymentframe,text="%0.f"%(shoppoint),bg="#EAE8E9",font="Calibri 16").place(x=400,y=450)
                                Label(paymentframe,text="Total Cost",bg="#EAE8E9",font="Calibri 16 bold").place(x=60,y=490)
                                Label(paymentframe,text="%0.f"%(total),bg="#EAE8E9",font="Calibri 16 bold").place(x=400,y=490)
                                Button(paymentframe,text="Exit",bg="#EAE8E9",font="Calibri 16 bold",command=quit).place(x=890,y=480)
                                ohkshop_menu_butt["state"] = "disabled"
                                ohkshop_button_staff["state"] = "disabled"
                                sql = """
                                        DELETE FROM shop_ohk_orderprocess
                                        WHERE table_index=?"""
                                cursor.execute(sql,[table])   
                                conn.commit()
                                sql = """
                                        UPDATE shop_ohk_table
                                        SET status=?,name=?,amount=?
                                        WHERE table_no=? """
                                cursor.execute(sql,['free','','',table])
                                conn.commit()
                                conn.close()
                            else :
                                messagebox.showwarning("Admin","Not enough money in your wallet \n Please pay at the counter")   
                                ohkshop_menu_butt["state"] = "disabled"
                                ohkshop_button_staff["state"] = "disabled"
                                Button(paymentframe,text="Exit",bg="#EAE8E9",font="Calibri 16 bold",command=quit).place(x=890,y=480)
                                conn=sqlite3.connect("projectdb.db")
                                cursor = conn.cursor()
                                sql = """
                                        DELETE FROM shop_ohk_orderprocess
                                        WHERE table_index=?"""
                                cursor.execute(sql,[table])   
                                conn.commit()
                                sql = """
                                        UPDATE shop_ohk_table
                                        SET status=?,name=?,amount=?
                                        WHERE table_no=? """
                                cursor.execute(sql,['free','','',table])
                                conn.commit()
                                conn.close()
                        else :
                            pass 
                    # name
                    paymentframe = Frame(ohkshop_allorder,bg="#FFFFFF")
                    paymentframe.place(x=0,y=0,width=1000,height=550)
                    Label(paymentframe,image=yayoishop_payment_1,bg="white").place(x=40,y=0)
                    Label(paymentframe,image=yayoishop_payment_2,bg="white").place(x=510,y=0)
                    # widget
                    text_yourwallet = Label(paymentframe,text="Yourwallet",bg="#FFE6A7").place(x=60,y=10)
                    text_balance = Label(paymentframe,text="balance : %s"%(cusinfo[7]),bg="#FFE6A7").place(x=120,y=50)
                    text_point = Label(paymentframe,text="Point   : %s"%(cusinfo[6]),bg="#FFE6A7").place(x=120,y=90)
                    text_member = Label(paymentframe,text="membership : %s"%(cusinfo[5]),bg="#FFE6A7").place(x=120,y=130)
                    # 
                    text_Payout = Label(paymentframe,text="Payout",bg="#FFF2D0").place(x=60,y=210)
                    text_name = Label(paymentframe,text="Name : %s %s"%(cusinfo[1],cusinfo[2]),bg="#FFF2D0").place(x=120,y=260)
                    discount = 1
                    discountpercent = 0
                    if cusinfo[5] == "None" :
                        discount = 0.95
                        discountpercent = 5
                    elif cusinfo[5] == "Level1" :
                        discount = 0.9
                        discountpercent = 10
                    elif cusinfo[5] == "Level2" :
                        discount = 0.85
                        discountpercent = 15
                    text_tax = Label(paymentframe,text="Discount : %s Percent"%(discountpercent),bg="#FFF2D0").place(x=120,y=310)
                    total = (Total*discount*1.07)//1
                    text_total = Label(paymentframe,text="Total : %0.f Baht"%(total),bg="#FFF2D0").place(x=120,y=360)
                    text_point = Label(paymentframe,text="Point : %s"%((Totalx/20)//1),bg="#FFF2D0").place(x=120,y=410)
                    but_payment = Button(paymentframe,image=yayoishop_confirm,bg="#FFF2D0",fg="black",font="Calibri 16",border=0,command=lambda : paymentprocess(total))
                    but_payment.place(x=140,y=460)
                #
                Label(ohkshop_allorder,text="Status",bg="#FFFFFF").grid(row=0,column=0)
                Label(ohkshop_allorder,text="Menu",bg="#FFFFFF").grid(row=0,column=1)
                Label(ohkshop_allorder,text="Amount",bg="#FFFFFF").grid(row=0,column=2)
                Label(ohkshop_allorder,text="Price per unit",bg="#FFFFFF").grid(row=0,column=3)
                #
                conn = sqlite3.connect("projectdb.db")
                cursor = conn.cursor()
                sql = """
                        SELECT * FROM shop_ohk_orderprocess 
                        WHERE table_index =?
                        """
                cursor.execute(sql,[ohkshop_tablex.get()])
                orderresult= cursor.fetchall()
                conn.close()
                #
                Totalx = 0
                for i,data in enumerate(orderresult) :
                    if i < 10 :
                        if data[4] == "NF" : 
                            Label(ohkshop_allorder,image=yayoishop_red_status,bg="#FFFFFF").grid(row=i+1,column=0)
                            Label(ohkshop_allorder,text=data[1],bg="white").grid(row=i+1,column=1)
                            Label(ohkshop_allorder,text=data[3],bg="white").grid(row=i+1,column=2)
                            Label(ohkshop_allorder,text=data[2],bg="white").grid(row=i+1,column=3)
                        elif data[4] == "CF" : 
                            Label(ohkshop_allorder,image=yayoishop_red_status,bg="#FFFFFF").grid(row=i+1,column=0)
                            Label(ohkshop_allorder,text=data[1],bg="white").grid(row=i+1,column=1)
                            Label(ohkshop_allorder,text=data[3],bg="white").grid(row=i+1,column=2)
                            Label(ohkshop_allorder,text=data[2],bg="white").grid(row=i+1,column=3)
                        elif data[4] == "F" :
                            Label(ohkshop_allorder,image=yayoishop_green_status,bg="#FFFFFF").grid(row=i+1,column=0)
                            Label(ohkshop_allorder,text=data[1],bg="white").grid(row=i+1,column=1)
                            Label(ohkshop_allorder,text=data[3],bg="white").grid(row=i+1,column=2)
                            Label(ohkshop_allorder,text=data[2],bg="white").grid(row=i+1,column=3)
                            Totalx = Totalx + (int(data[3])*int(data[2]))
                conn = sqlite3.connect("projectdb.db")
                cursor = conn.cursor()
                sql = """
                            SELECT * FROM customer_information
                            WHERE firstname_customer=? """
                cursor.execute(sql,[customername])
                cusinfo = cursor.fetchone()
                Button(ohkshop_allorder,text="Pay out",image=yayoishop_yayoishop_payout,command=lambda:ohkshop_payment(Totalx,cusinfo),border=0,bg="white",activebackground="white").grid(row=20,column=1,columnspan=2)
            def staffcalling() :
                sql = """
                        UPDATE shop_ohk_table
                        SET staffcall=?
                        WHERE table_no=?"""
                cursor.execute(sql,["yes",ohkshop_tablex.get()])
                conn.commit()
            #
            ohkpicture()
            amt_table = "0"
            if ohkshop_tablex.get() == "1" or ohkshop_tablex.get() == "2" or ohkshop_tablex.get() == "3" :
                amt_table = "1-2"
            elif ohkshop_tablex.get() == "4" or ohkshop_tablex.get() == "5" or ohkshop_tablex.get() == "6":
                amt_table = "3-4"
            elif ohkshop_tablex.get() == "7" or ohkshop_tablex.get() == "8":
                amt_table = "5-6"
            ohkshop_frame = Frame(ohkroot,bg="#FFFFFF")
            ohkshop_frame.place(x=0,y=0,height=700,width=1000)
            Label(ohkshop_frame,image=ohk_header,bg="#FFFFFF").place(x=-2,y=-5)
            Label(ohkshop_frame,image=ohk_logo,bg="#FFFFFF").place(x=40,y=0)
            # table no
            ohkshop_table_no_wframe = Label(ohkshop_frame,image=ohkshop_showtable,bg="#E8C9AB")
            ohkshop_table_no_wframe.place(relx=0.519,y=15)
            ohkshop_text_no_people = Label(ohkshop_frame,text="Table No : %s \n %s people"%(ohkshop_tablex.get(),amt_table),bg="#FFEDD6",font="Calibri 16")
            ohkshop_text_no_people.place(relx=0.54,y=23)
            #
            ohkshop_order_wfame = Label(ohkshop_frame,image=yayoishop_whiteframe_2,bg="#E8C9AB")
            ohkshop_order_wfame.place(relx=0.7,y=15)
            ohkshop_chk_wfame = Label(ohkshop_frame,image=yayoishop_whiteframe_2,bg="#E8C9AB")
            ohkshop_chk_wfame.place(relx=0.8,y=15)
            ohkshop_staff_wfame = Label(ohkshop_frame,image=yayoishop_whiteframe_2,bg="#E8C9AB")
            ohkshop_staff_wfame.place(relx=0.9,y=15)
            #
            ohkshop_button_orders = Button(ohkshop_frame,image=yayoishop_but_orders,border=0,bg="#FBE5E5",activebackground="#FBE5E5",command=ohkshop_orderframe)
            ohkshop_button_orders.place(relx=0.814,y=27)
            #
            conn = sqlite3.connect("projectdb.db")
            cursor = conn.cursor()
            sql = """
                        SELECT * FROM shop_ohk_orderprocess
                        WHERE table_index=? """
            cursor.execute(sql,[ohkshop_tablex.get()])
            result = cursor.fetchall()
            nuborder = 0
            for i,date in enumerate(result) :
                nuborder = nuborder + 1
            lenorder = StringVar()
            lenorder.set(nuborder)
            #
            ohkshop_amount_order = Label(ohkshop_frame,border=0,bg="#FBE5E5",text=lenorder.get(),compound="center",font="bold")
            ohkshop_amount_order.place(relx=0.855,y=19)
            # relx=0.752,y=17
            ohkshop_button_staff = Button(ohkshop_frame,image=yayoishop_but_staff,border=0,bg="#FBE5E5",activebackground="#FBE5E5",command=staffcalling)
            ohkshop_button_staff.place(relx=0.92,y=26)
            # 1
            ohkshop_menu_butt = Button(ohkshop_frame,image=yayoishop_but_menu,border=0,bg="#FBE5E5",activebackground="#FBE5E5",command=ohkshop_menuframe)
            ohkshop_menu_butt.place(relx=0.72,y=28)
            ohkshop_menuframe()
    # call function
    allfunctionin_loginpage()
    allfunctionin_mainpage()
    allexitfuntion()
    photoimage_inloginpage()
    # call function picture
    main_picture()
    # start
    # โปรแกรมหลัก
    customerlogin()
# start
splash_win.after(600,Startprogram)
# End
mainloop()