# ð· Enjoy Wining your Life ðº

## Start
Step 1: ngrok init<br>
Step 2: start reload your app `python /app/main.py`<br>
Step 3: modify webhook url of Line(https://developers.line.biz/zh-hant/), verify it<br>
Step 4: chat with Wine_Your_Life
<br><br>


### Function
1. Send me your location, and you would receive 3 bar within 1.5k
2. Text "Record", and record your Wine Life
3. Text "Show", and take a look at your Wine Life so far
<br><br>

### FSM picture
![alt text](https://github.com/Bonnie-entre/LineBot_WineYourLife/blob/main/fsm.png?raw=true)
<br><br>

### Using
- Google Map API
- Google Drive API
(save wine-your-life.json file in ~/.config/gspread)
- Google Sheet API
<br><br>

### Develope

in conda env,
`python -m uvicorn app.main:app --reload`

ps. use conda env LineBot in local env
<br><br>


### Learning

* ngrok æ¯ä»éº¼
https://learn.markteaching.com/ngrok-webhook/
https://ithelp.ithome.com.tw/articles/10235031

* 0.0.0.0 vs 127.0.0.1
On Unix systems, it's quite common to put 0.0.0.0 as the desired hostname/IP, which means "all network interfaces", in which case localhost/127.0.0.1 would work as well

    `127.0.0.1 æ¯ä¸ä¸ªç¯åå°åãå¹¶ä¸è¡¨ç¤ºâæ¬æºâã0.0.0.0ææ¯çæ­£è¡¨ç¤ºâæ¬ç½ç»ä¸­çæ¬æºâã 
    å¨å®éåºç¨ä¸­ï¼ä¸è¬æä»¬å¨æå¡ç«¯ç»å®ç«¯å£çæ¶åå¯ä»¥éæ©ç»å®å°0.0.0.0ï¼è¿æ ·æçæå¡è®¿é®æ¹å°±å¯ä»¥éè¿æçå¤ä¸ªipå°åè®¿é®æçæå¡ã 
    æ¯å¦ææä¸å°æå¡å¨ï¼ä¸ä¸ªå¤æ¾å°åA,ä¸ä¸ªåç½å°åBï¼å¦ææç»å®çç«¯å£æå®äº0.0.0.0ï¼é£ä¹éè¿åç½å°åæå¤ç½å°åé½å¯ä»¥è®¿é®æçåºç¨ãä½æ¯å¦ææä¹ç»å®äºåç½å°åï¼é£ä¹éè¿å¤ç½å°åå°±ä¸è½è®¿é®ã æä»¥å¦æç»å®0.0.0.0,ä¹æä¸å®å®å¨éæ£ï¼å¯¹äºåªéè¦åç½è®¿é®çæå¡ï¼å¯ä»¥åªç»å®åç½å°åã`
https://blog.csdn.net/u012814696/article/details/55098249

* Line Template message
åç¨®ï¼https://ithelp.ithome.com.tw/articles/10282102
https://ithelp.ithome.com.tw/articles/10195531
Flex Messageï¼https://ithelp.ithome.com.tw/articles/10243224
* Carousel å§æå¤å¯ä»¥æ¾ 12 å Bubble

* Google sheet
https://www.youtube.com/watch?v=bu5wXjz2KvU&t=347
    ```
    # worksheet_list = sh.worksheets()
    # print(worksheet_list)

    # values_list = wks_sh2.col_values(1)
    # print(values_list)

    # print("Rows: ", wks_sh2.row_count)
    # print("Cols: ", wks_sh2.col_count)
    # print(wks_sh2.get_all_values())

    # df = pd.DataFrame(sheet.get_all_records())
    # print(df)
    ```

* draw fsm
https://python.hotexamples.com/examples/transitions/Machine/get_graph/python-machine-get_graph-method-examples.html

<br><br>