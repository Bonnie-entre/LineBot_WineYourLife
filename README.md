## Start

Step 1: ngrok init
Step 2: start reload your app `python /app/main.py`
Step 3: modify webhook url of Line(https://developers.line.biz/zh-hant/), verify it
Step 4: chat with Wine_Your_Life
<br><br>


### Function
1. 傳送定位，給予方圓 3km 內的 3個酒吧資訊
2. 為去過的酒吧做紀錄
3. 查詢個人酒吧紀錄
<br>

### FSM picture
![alt text](https://github.com/Bonnie-entre/LineBot_WineYourLife/blob/main/fsm.png?raw=true)
<br>

### Using
- Google Map API
- Google Drive API
(save wine-your-life.json file in ~/.config/gspread)
- Google Sheet API
<br>

### Develope

in conda env,
`python -m uvicorn app.main:app --reload`

ps. use conda env LineBot in local env
<br>


### Learning

* ngrok 是什麼
https://learn.markteaching.com/ngrok-webhook/
https://ithelp.ithome.com.tw/articles/10235031

* 0.0.0.0 vs 127.0.0.1
On Unix systems, it's quite common to put 0.0.0.0 as the desired hostname/IP, which means "all network interfaces", in which case localhost/127.0.0.1 would work as well

`127.0.0.1 是一个环回地址。并不表示“本机”。0.0.0.0才是真正表示“本网络中的本机”。 
在实际应用中，一般我们在服务端绑定端口的时候可以选择绑定到0.0.0.0，这样我的服务访问方就可以通过我的多个ip地址访问我的服务。 
比如我有一台服务器，一个外放地址A,一个内网地址B，如果我绑定的端口指定了0.0.0.0，那么通过内网地址或外网地址都可以访问我的应用。但是如果我之绑定了内网地址，那么通过外网地址就不能访问。 所以如果绑定0.0.0.0,也有一定安全隐患，对于只需要内网访问的服务，可以只绑定内网地址。`
https://blog.csdn.net/u012814696/article/details/55098249

* Line Template message
各種：https://ithelp.ithome.com.tw/articles/10282102
https://ithelp.ithome.com.tw/articles/10195531
Flex Message：https://ithelp.ithome.com.tw/articles/10243224

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
