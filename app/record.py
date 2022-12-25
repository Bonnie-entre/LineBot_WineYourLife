import gspread

def ShowMyRecords(usrId):
    sa = gspread.service_account(filename="./service_account.json")
    sh = sa.open("Wine_Your_Life_record")

    wks_sh1 = sh.worksheet("sheet_one")
    wks_sh2 = sh.worksheet("user_record")

    # sheet TWO
    # 'user_id', 'record_state', 'bar_name', 'date', 'score', 'comment', 'go_next_time'
    list_sh2_col_usr_id = wks_sh2.col_values(1)
    contents = []
    list_sh2_all = wks_sh2.get_all_values()
    for i in range(len(list_sh2_col_usr_id)):
        if(usrId==list_sh2_col_usr_id[i]):
            if(int(list_sh2_all[i][1])>=6):

                print("create one at row", i)
                #create tmplate
                bar_name = list_sh2_all[i][2]
                date = list_sh2_all[i][3]
                comment = list_sh2_all[i][5]
                next_time = list_sh2_all[i][6]
                star_img = []
                for i in range(int(list_sh2_all[i][4])):
                    star_img.append({
                            "type": "icon",
                            "size": "sm",
                            "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png"
                        }
                    )
                star_img.append({
                        "type": "text",
                        "text": "star",
                        "size": "sm",
                        "color": "#999999",
                        "margin": "md",
                        "flex": 0
                        }
                )
                
                _content = {
                            "type": "bubble",
                            "body": {
                                "type": "box",
                                "layout": "vertical",
                                "contents": [
                                {
                                    "type": "text",
                                    "text": bar_name,
                                    "weight": "bold",
                                    "size": "xl"
                                },
                                {
                                    "type": "box",
                                    "layout": "baseline",
                                    "margin": "md",
                                    "contents": star_img
                                    
                                },
                                {
                                    "type": "box",
                                    "layout": "vertical",
                                    "margin": "lg",
                                    "spacing": "sm",
                                    "contents": [
                                    {
                                        "type": "box",
                                        "layout": "baseline",
                                        "spacing": "sm",
                                        "contents": [
                                        {
                                            "type": "text",
                                            "text": "Last time",
                                            "color": "#aaaaaa",
                                            "size": "sm",
                                            "flex": 2
                                        },
                                        {
                                            "type": "text",
                                            "text": date,
                                            "wrap": True,
                                            "color": "#666666",
                                            "size": "sm",
                                            "flex": 5
                                        }
                                        ]
                                    },
                                    {
                                        "type": "box",
                                        "layout": "baseline",
                                        "spacing": "sm",
                                        "contents": [
                                        {
                                            "type": "text",
                                            "text": "Comments",
                                            "color": "#aaaaaa",
                                            "size": "sm",
                                            "flex": 2
                                        },
                                        {
                                            "type": "text",
                                            "wrap": True,
                                            "color": "#666666",
                                            "size": "sm",
                                            "flex": 5,
                                            "text": comment
                                        }
                                        ]
                                    },
                                    {
                                        "type": "box",
                                        "layout": "baseline",
                                        "spacing": "sm",
                                        "contents": [
                                        {
                                            "type": "text",
                                            "text": "Go again",
                                            "color": "#aaaaaa",
                                            "size": "sm",
                                            "flex": 2
                                        },
                                        {
                                            "type": "text",
                                            "text": next_time,
                                            "wrap": True,
                                            "color": "#666666",
                                            "size": "sm",
                                            "flex": 5
                                        }
                                        ]
                                    }
                                    ]
                                }
                                ]
                            },
                            "footer": {
                                "type": "box",
                                "layout": "vertical",
                                "spacing": "sm",
                                "contents": [
                                {
                                    "type": "box",
                                    "layout": "vertical",
                                    "contents": [],
                                    "margin": "sm"
                                }
                                ],
                                "flex": 0
                            }
                            }
                                
                contents.append(_content)
                # print("x")
    print("len", len(contents))
    return contents


def TextMsgReply(usrId, record_include, line_msg):
    sa = gspread.service_account(filename="./service_account.json")
    sh = sa.open("Wine_Your_Life_record")

    wks_sh1 = sh.worksheet("sheet_one")
    wks_sh2 = sh.worksheet("user_record")

    # sheet ONE
    # usr_id, record_state
    sh1_id_col = -1
    list_sh1_col_usr_id = wks_sh1.col_values(1)
    list_sh1_all = wks_sh1.get_all_values()
    for i in range(len(list_sh1_col_usr_id)):
        if(list_sh1_col_usr_id[i]==usrId):
            sh1_id_col = i + 1
            sh1_record_state = int(list_sh1_all[sh1_id_col-1][1])
            print("find at ", sh1_id_col)
            print("state ", sh1_record_state)
            break


    if(sh1_id_col==-1):
        if(record_include):
            wks_sh1.append_row([usrId, "0"])
            sh1_record_state = 0
            print("start modify sheet2")
        else:
            wks_sh1.append_row([usrId, "6"])
            sh1_record_state = 6
            # ReplyText="reply normal"
            ReplyText = line_msg

    else:
        if(record_include!=-1):     #if("record" in event.text):
            sh1_record_state = 0
            wks_sh1.update('B'+str(sh1_id_col), '0')
            print("start modify sheet2")
        elif(sh1_record_state<6):
            # flag_modify_sh2 = 1
            print("keep modify sheet2")
        elif(sh1_record_state>=6):           #other msg reply
            # ReplyText = "reply others, maybe chatgpt" 
            ReplyText = line_msg
            print("reply others, maybe chatgpt")

    print("state ", sh1_record_state)


    # sheet TWO
    # 'user_id', 'record_state', 'bar_name', 'date', 'score', 'comment', 'go_next_time'
    sh2_modified_row = -1
    if(sh1_record_state==0):
        wks_sh2.append_row([usrId, "1"])
        wks_sh1.update('B'+str(sh1_id_col), '1')
        print("create new record")
        ReplyText="what's the bar name?"
    elif(sh1_record_state<6):
        print("find right modified last time")
        list_sh2_col_usr_id = wks_sh2.col_values(1)
        list_sh2_all = wks_sh2.get_all_values()
        for i in range(len(list_sh2_col_usr_id)):
            if(usrId==list_sh2_col_usr_id[i]):
                if(int(list_sh2_all[i][1])<6):
                    sh2_modified_row = i+1
                    break
        
        if(sh1_record_state==1):
            wks_sh1.update('B'+str(sh1_id_col), '2')
            wks_sh2.update('B'+str(sh2_modified_row), '2')
            wks_sh2.update('C'+str(sh2_modified_row), line_msg) #name
            ReplyText = "which date did you go?"
        elif(sh1_record_state==2):
            wks_sh1.update('B'+str(sh1_id_col), '3')
            wks_sh2.update('B'+str(sh2_modified_row), '3')
            wks_sh2.update('D'+str(sh2_modified_row), line_msg) #date
            ReplyText = "how many start would you like to give to this bar?"
        elif(sh1_record_state==3):
            wks_sh1.update('B'+str(sh1_id_col), '4')
            wks_sh2.update('B'+str(sh2_modified_row), '4')
            wks_sh2.update('E'+str(sh2_modified_row), line_msg) #star
            ReplyText = "Comment something for this bar. (if none, type none~)"
        elif(sh1_record_state==4):
            wks_sh1.update('B'+str(sh1_id_col), '5')
            wks_sh2.update('B'+str(sh2_modified_row), '5')
            wks_sh2.update('F'+str(sh2_modified_row), line_msg) #comment
            ReplyText = "Last question: whould you like to go next time?"
        elif(sh1_record_state==5):
            wks_sh1.update('B'+str(sh1_id_col), '6')
            wks_sh2.update('B'+str(sh2_modified_row), '6')
            wks_sh2.update('G'+str(sh2_modified_row), line_msg) #next time
            ReplyText = "Added bar record Successfully!!"
        else:
            "err"

    return ReplyText

