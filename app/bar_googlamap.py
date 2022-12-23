from config import settings

import requests

from linebot.models import MessageTemplateAction, CarouselColumn, CarouselTemplate, URITemplateAction, TemplateSendMessage

def bar_search(latitude_in, longitude_in):
    
    url_nearSearch = f'https://maps.googleapis.com/maps/api/place/nearbysearch/json?location={latitude_in},{longitude_in}&radius=1500&type=bar&keyword=酒&key={settings.GOOGLE_MAP_API_KEY}'
    payload = {}
    headers = {}
    response_nearSearch = requests.request("GET", url_nearSearch, headers=headers, data=payload)
    r = response_nearSearch.json()

    num = len(r['results'])

    # make msg_send
    contents=dict()
    contents['type']='carousel'
    _columns=[]

    bar_imag_addr = [
        "https://media.vogue.com.tw/photos/626224c1d18a414283599107/2:3/w_2560%2Cc_limit/BARHOME2.jpg",
        "https://image.cache.storm.mg/styles/smg-800x533-fp/s3/media/image/2022/08/16/20220816-030826_U23429_M785333_7180.JPG?itok=Sl31bIXh",
        "https://media.gq.com.tw/photos/5dbc268ecfb8d000081c005b/master/pass/2019071953952917.jpg"
    ]
    print("Numbers of bar within 500km:", num)
    if(num>3):
        num=3
    if(num):
        # for i in range(num):
        for i in range(num):
            place_id = r['results'][i]['place_id']
            
            url_placeDetail = f'https://maps.googleapis.com/maps/api/place/details/json?place_id={place_id}&key={settings.GOOGLE_MAP_API_KEY}'
            payload = {}
            headers = {}
            response_placeDetail = requests.request("GET", url_placeDetail, headers=headers, data=payload)
            r_placeDetail = response_placeDetail.json()
            
            name = r_placeDetail['result']['name']
            if(len(name)>40):
                name = name[0:30]
            try:
                weekday_text_o = r_placeDetail['result']['current_opening_hours']['weekday_text']
            except:
                weekday_text_o=''
            weekday_text=''
            for we in weekday_text_o:    
                weekday_text += we + '\n'
            try:
                website = r_placeDetail['result']['website']
            except:
                website = "None"
            try:
                rating = str(r_placeDetail['result']['rating'])    
            except:
                rating =''
            try:
                url_map = r_placeDetail['result']['url']
            except:
                url_map=""
            print(name)
            col = CarouselColumn(
                        thumbnail_image_url=bar_imag_addr[i],
                        title = name,
                        text = "Rating: "+ rating, #+"\nTel:"+formatted_phone_number,
                        actions=[
                            MessageTemplateAction(
                                label = 'Time',
                                text = weekday_text
                            ),
                            MessageTemplateAction(
                                label='Website',
                                text=website,
                            ),
                            URITemplateAction(
                                label='Map',
                                uri=url_map
                            )
                        ]
                    )
                    
            _columns.append(col)
    
    
    Carousel_template = TemplateSendMessage(
        alt_text='Carousel template',
        template=CarouselTemplate(
            columns=_columns
        )
    )        
    return Carousel_template
    
# bar_search(24.993533, 121.461588)   #Banqua
# bar_search(22.994821,120.196452)    #Tainan

