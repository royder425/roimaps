import folium
from branca.element import Figure
 
#  픽셀 크기 설정
# fig = Figure(width=50,height=100)
# 맵 함수 함수 이름 m
# m = folium.Map(
# 처음 시작하는 위치 위도 경도
#     location=[37.3525, 126.5943], 
# 처음 시작하는 위치 줌 배율
#     zoom_start=2.5, 
# )
# fig.add_child(m) 
 
fig = Figure(width=50,height=100)
m = folium.Map(
    location=[37.3525, 126.5943], 
    zoom_start=2.5, 
)
fig.add_child(m)


# # 위도 경도 마커 위치
# folium.Marker(독도,
# 팝업 상자 옵션 || # 링크
# popup=link+"36'>2022.05.22 국내 일주 울릉도(독도)</a>",
# 팝업 상자 문구
# tooltip='독도',
# 아이콘 이미지 설정
# icon=folium.CustomIcon(한국icon,                       
# icon_size=(30, 30))).add_to(m)


# 위도 경도 마커 위치
# folium.Marker([37.8184719,127.4502156],
# 팝업 상자 옵션
# ,popup=
# 글자 가로 출력
# "<html><head></head><body>
# 팝업 상자 길이 지정
# <div style='width: 150px'>
# 링크
# <a href='https://roitravel.tistory.com/10'>
# 팝업 상자 문구
# 2021.12 가평 여행</a>",
# 줄바꿈
# <br>

#링크 간소화 지정
link = "<html><head></head><body><div style='width: 170px'><a href='https://roitravel.tistory.com/"
link_1 ="</a><br><a href='https://roitravel.tistory.com/"
link_world = "<html><head></head><body><div style='width: 260px'><a href='https://roitravel.tistory.com/"
L = target='_blank'

#링크 1개 짜리
# link = 
 # 글자 가로 출력
# "<html><head></head><body>
 # 팝업 상자 길이 지정
# <div style='width: 170px'>
 # 링크
# <a href='https://roitravel.tistory.com/"
#링크 2개 이상
# link_1 ="</a>
# 줄바꿈
# <br>
# 링크
# <a href='https://roitravel.tistory.com/"

                  
#국내 도시별 좌표
가평=37.8184719,127.4502156
거제=34.8806427,128.6210824
경주=35.8266161,129.235988
광주=35.1557358,126.8354271
군산=35.9676772,126.7366293
남해군=34.8376721,127.8924234
단양=36.9941896,128.3877555
담양=35.291486,126.9952909
대전=36.3398175,127.3940486
독도=37.24293628,131.8668421
목포=34.8118351,126.3921664
무안=34.9904542,126.4816856
문경=36.6910006,128.1488468
부산=35.2100142,129.0688702
부안=35.7315661,126.7334651
부여=36.2463459,126.856897
서귀포시=33.2541205,126.560076
양평=37.5180465,127.5792445
울릉도=37.5063677,130.8571536
제주시=33.4996213,126.5311884
진주=35.205153,128.1297905
함평=35.1126823,126.5355523
제주도=33.3846216,126.5534925

#나라별 좌표 설정
하노이=21.0277644,105.8341598
깟바=20.8,106.999722
하이퐁=20.8449115,106.6880841
아테네=37.9838096,23.7275388
테살로니키=40.6400629,22.9444191
소피아=42.6977082,23.3218675
스코페=41.9981294,21.4254355
티라나=41.3275459,19.8186982
포드고리차=42.4304196,19.2593642
두브로브니크=42.6506606,18.0944238
스플리트=43.5147118,16.4435148
자다르=44.119371,15.2313648
자그레브=45.8150108,15.981919
부다페스트=47.497912,19.040235
발라톤퓨레드=46.5739,17.5319
빈=48.2081743,16.3738189
그라츠=47.070714,15.439504
프라하=50.0755381,14.4378005
드레스덴=51.0504088,13.7372621
베를린=52.5200066,13.404954
브레멘=53.0792962,8.8016937
프랑크푸르트=50.1109221,8.6821267
암스테르담=52.3675734,4.9041389
파리=48.856614,2.3522219
보르도=44.837789,-0.57918
바르셀로나=41.3873974,2.168568
마드리드=40.4167754,-3.7037902
그라나다=37.1774605,-3.5984368
세비야=37.3890924,-5.9844589
리스본=38.7222524,-9.1393366
라고스=37.1073776,-8.6778582
포르토=41.1579438,-8.6291053
나폴리=40.8517983,14.26812
로마=41.9027835,12.4963655
플로렌스=43.7695604,11.2558136
피사=43.7228386,10.4016888
밀라노=45.4642035,9.189982
체르마트=46.0207133,7.749117
인터라켄=46.6863481,7.8632049
베른=46.9479739,7.4474468
리옹=45.764043,4.835659
클레르몽페랑=45.777222,3.087025
파리=48.856614,2.3522219
런던=51.5072178,-0.1275862
토론토=43.653226,-79.3831843
킹스턴=44.2311717,-76.4859544
몬트리올=45.5018869,-73.5673919
뉴욕=40.7127753,-74.0059728
샌프란시스코=37.7749295,-122.4194155
로스엔젤레스=34.0522342,-118.2436849
라스베가스=36.171563,-115.1391009
플라야델카르멘=20.6295586,-87.0738851
칸쿤=21.161908,-86.8515279
뉴욕=40.7127753,-74.0059728
에든버러=55.953252,-3.188267
런던=51.5072178,-0.1275862
자르뷔르켄=49.2362191,6.9960017
홍콩=22.3193039,114.1693611
마카오=22.198745,113.543873
후쿠오카=33.5901838,130.4016888
오사카=34.6937249,135.5022535
치앙마이=18.7883439,98.9853008
방콕=13.7563309,100.5017651
타이페이=25.0329636,121.5654268

#국기
베트남icon=r'C:\Users\home\Desktop\roimaps\png\베트남.png'
그리스icon=r'C:\Users\home\Desktop\roimaps\png\그리스.png'
불가리아icon=r'C:\Users\home\Desktop\roimaps\png\불가리아.png'
마케도니아icon=r'C:\Users\home\Desktop\roimaps\png\마케도니아.png'
알바니아icon=r'C:\Users\home\Desktop\roimaps\png\알바니아.png'
몬테네그로icon=r'C:\Users\home\Desktop\roimaps\png\몬테네그로.png'
크로아티아icon=r'C:\Users\home\Desktop\roimaps\png\크로아티아.png'
헝가리icon=r'C:\Users\home\Desktop\roimaps\png\헝가리.png'
오스트리아icon=r'C:\Users\home\Desktop\roimaps\png\오스트리아.png'
체코icon=r'C:\Users\home\Desktop\roimaps\png\체코.png'
독일icon=r'C:\Users\home\Desktop\roimaps\png\독일.png'
네덜란드icon=r'C:\Users\home\Desktop\roimaps\png\네덜란드.png'
프랑스icon=r'C:\Users\home\Desktop\roimaps\png\프랑스.png'
스페인icon=r'C:\Users\home\Desktop\roimaps\png\스페인.png'
포르투갈icon=r'C:\Users\home\Desktop\roimaps\png\포르투갈.png'
이탈리아icon=r'C:\Users\home\Desktop\roimaps\png\이탈리아.png'
스위스icon=r'C:\Users\home\Desktop\roimaps\png\스위스.png'
영국icon=r'C:\Users\home\Desktop\roimaps\png\영국.png'
캐나다icon=r'C:\Users\home\Desktop\roimaps\png\캐나다.png'
미국icon=r'C:\Users\home\Desktop\roimaps\png\미국.png'
멕시코icon=r'C:\Users\home\Desktop\roimaps\png\멕시코.png'
스코틀랜드icon=r'C:\Users\home\Desktop\roimaps\png\스코틀랜드.png'
한국icon=r'C:\Users\home\Desktop\roimaps\png\한국.png'
일본icon=r'C:\Users\home\Desktop\roimaps\png\일본.png'
홍콩icon=r'C:\Users\home\Desktop\roimaps\png\홍콩.png'
마카오icon=r'C:\Users\home\Desktop\roimaps\png\마카오.png'
태국icon=r'C:\Users\home\Desktop\roimaps\png\태국.png'
대만icon=r'C:\Users\home\Desktop\roimaps\png\대만.png'


#국내 일주
folium.Marker(부여,
              popup=link+"11'>2022.04.28 국내 일주 부여 1" + link_1 + "12'>2022.04.29 국내 일주 부여 2</a>",
              tooltip='부여',
              icon=folium.CustomIcon(한국icon, icon_size=(30, 30))).add_to(m)
folium.Marker(대전,
              popup=link+"13'>2022.04.30 국내 일주 대전</a>",
              tooltip='대전',
              icon=folium.CustomIcon(한국icon, icon_size=(30, 30))).add_to(m)
folium.Marker(군산,
              popup=link+"14'>2022.05.01 국내 일주 군산</a>",
              tooltip='군산',
              icon=folium.CustomIcon(한국icon, icon_size=(30, 30))).add_to(m)
folium.Marker(부안,
              popup=link+"15'>2022.05.02 국내 일주 부안</a>",
              tooltip='부안',
              icon=folium.CustomIcon(한국icon, icon_size=(30, 30))).add_to(m)
folium.Marker(담양,
              popup=link+"16'>2022.05.03 국내 일주 담양</a>",
              tooltip='담양',
              icon=folium.CustomIcon(한국icon, icon_size=(30, 30))).add_to(m)
folium.Marker(광주,
              popup=link+"17'>2022.05.04 국내 일주 광주 1" + link_1 + "18'>2022.05.05 국내 일주 광주 2</a>",
              tooltip='광주',
              icon=folium.CustomIcon(한국icon, icon_size=(30, 30))).add_to(m)
folium.Marker(함평,
              popup=link+"19'>2022.05.06 국내 일주 함평, 무안</a>",
              tooltip='함평',
              icon=folium.CustomIcon(한국icon, icon_size=(30, 30))).add_to(m)
folium.Marker(무안,
              popup=link+"19'>2022.05.06 국내 일주 함평, 무안</a>",
              tooltip='무안',
              icon=folium.CustomIcon(한국icon, icon_size=(30, 30))).add_to(m)
folium.Marker(목포,
              popup=link+"21'>2022.05.07 국내 일주 목포</a>",
              tooltip='목포',
              icon=folium.CustomIcon(한국icon, icon_size=(30, 30))).add_to(m)
folium.Marker(제주도,
              popup=link+"22'>2022.05.08 국내 일주 제주 1" + link_1 + "23'>2022.05.09 국내 일주 제주 2" + link_1 + "24'>2022.05.10 국내 일주 제주 3" + link_1 + "25'>2022.05.11 국내 일주 제주 4" + link_1 + "26'>2022.05.12 국내 일주 제주 5" + link_1 + "27'>2022.05.13 국내 일주 제주 6</a>",
              tooltip='제주',
              icon=folium.CustomIcon(한국icon, icon_size=(30, 30))).add_to(m)
folium.Marker(남해군,
              popup=link+"28'>2022.05.14 국내 일주 남해군</a>",
              tooltip='남해군',
              icon=folium.CustomIcon(한국icon, icon_size=(30, 30))).add_to(m)
folium.Marker(진주,
              popup=link+"29'>2022.05.15 국내 일주 진주</a>",
              tooltip='진주',
              icon=folium.CustomIcon(한국icon, icon_size=(30, 30))).add_to(m)
folium.Marker(거제,
              popup=link+"30'>2022.05.16 국내 일주 거제</a>"
              ,tooltip='거제',
              icon=folium.CustomIcon(한국icon, icon_size=(30, 30))).add_to(m)
folium.Marker(부산,
              popup=link+"32'>2022.05.18 국내 일주 부산</a>",
              tooltip='부산',
              icon=folium.CustomIcon(한국icon, icon_size=(30, 30))).add_to(m)
folium.Marker(경주,
              popup=link+"33'>2022.05.19 국내 일주 경주 1" + link_1 + "34'>2022.05.20 국내 일주 경주 2</a>",
              tooltip='경주',
              icon=folium.CustomIcon(한국icon, icon_size=(30, 30))).add_to(m)
folium.Marker(독도,
              popup=link+"36'>2022.05.22 국내 일주 울릉도(독도)</a>",
              tooltip='독도',
              icon=folium.CustomIcon(한국icon, icon_size=(30, 30))).add_to(m)
folium.Marker(울릉도,
              popup=link+"37'>2022.05.23 국내 일주 울릉도</a>",
              tooltip='울릉도',
              icon=folium.CustomIcon(한국icon, icon_size=(30, 30))).add_to(m)
folium.Marker(문경,
              popup=link+"38'>2022.05.24 국내 일주 문경</a>",
              tooltip='문경',
              icon=folium.CustomIcon(한국icon, icon_size=(30, 30))).add_to(m)


#국내 여행
folium.Marker(단양,
              popup=link+"8'>2021.07 단양 여행</a>",
              tooltip='단양',
              icon=folium.CustomIcon(한국icon, icon_size=(30, 30))).add_to(m)
folium.Marker(가평,
              popup=link+"10'>2021.12 가평 여행</a>",
              tooltip='가평',
              icon=folium.CustomIcon(한국icon, icon_size=(30, 30))).add_to(m)
folium.Marker(양평,
              popup=link+"41'>2022.07 양평 여행</a>",
              tooltip='양평',
              icon=folium.CustomIcon(한국icon, icon_size=(30, 30))).add_to(m)

#링크 여러개개 해외(베트남 여행)
folium.Marker(하노이,
              popup=link+"42'>2022.07.17 베트남 하노이 1" + link_1 + "43'>2022.07.18 베트남 하노이 2</a>" + link_1 + "44'>2022.07.19 베트남 하노이 3</a>",
              tooltip='하노이',
              icon=folium.CustomIcon(베트남icon, icon_size=(30, 30))).add_to(m)
folium.Marker(깟바,
              popup=link+"45'>2022.07.19 베트남 깟바 1" + link_1 + "46'>2022.07.20 베트남 깟바 2</a>" + link_1 + "47'>2022.07.21 베트남 깟바 3</a>",
              tooltip='깟바',
              icon=folium.CustomIcon(베트남icon, icon_size=(30, 30))).add_to(m)
folium.Marker(하이퐁,
              popup=link+"49'>2022.07.21 베트남 하이퐁 1" + link_1 + "50'>2022.07.22 베트남 하이퐁 2</a>" + link_1 + "51'>2022.07.23 베트남 하이퐁 3</a>",
              tooltip='하이퐁',
              icon=folium.CustomIcon(베트남icon, icon_size=(30, 30))).add_to(m)

#세계 여행
#일본
folium.Marker(후쿠오카,
              popup=link_world+"7'>2018.03 후쿠오카 여행",
              tooltip='후쿠오카',
              icon=folium.CustomIcon(일본icon, icon_size=(30, 30))).add_to(m)
folium.Marker(오사카,
              popup=link_world+"4'>2014.12 오사카 여행",
              tooltip='오사카',
              icon=folium.CustomIcon(일본icon, icon_size=(30, 30))).add_to(m)
#태국
folium.Marker(방콕,
              tooltip='방콕',
              icon=folium.CustomIcon(태국icon, icon_size=(30, 30))).add_to(m)
folium.Marker(치앙마이,
              tooltip='치앙마이',
              icon=folium.CustomIcon(태국icon, icon_size=(30, 30))).add_to(m)
#대만
folium.Marker(타이페이,
              tooltip='타이페이',
              icon=folium.CustomIcon(대만icon, icon_size=(30, 30))).add_to(m)
#홍콩
folium.Marker(홍콩,
              popup=link_world+"3'>2013.10 홍콩, 마카오 여행",
              tooltip='홍콩',
              icon=folium.CustomIcon(홍콩icon, icon_size=(30, 30))).add_to(m)
#마카오
folium.Marker(마카오,
              popup=link_world+"3'>2013.10 홍콩, 마카오 여행",
              tooltip='마카오',
              icon=folium.CustomIcon(마카오icon, icon_size=(30, 30))).add_to(m)
#그리스
folium.Marker(아테네,
              popup=link_world+"53'>2022.08.20 세계 여행 그리스 아테네 1" + link_1 + "54'>2022.08.21 세계 여행 그리스 아테네 2</a>",
              tooltip='아테네',
              icon=folium.CustomIcon(그리스icon, icon_size=(30, 30))).add_to(m)
folium.Marker(테살로니키,
              popup=link_world+"55'>2022.08.22 세계 여행 그리스 테살로니키",
              tooltip='테살로니키',
              icon=folium.CustomIcon(그리스icon, icon_size=(30, 30))).add_to(m)
#불가리아
folium.Marker(소피아,
              popup=link_world+"57'>2022.08.24 세계 여행 불가리아 소피아",
              tooltip='소피아',
              icon=folium.CustomIcon(불가리아icon, icon_size=(30, 30))).add_to(m)
#북 마케도니아
folium.Marker(스코페,
              popup=link_world+"58'>2022.08.26 세계 여행 북 마케도니아 스코페",
              tooltip='스코페',
              icon=folium.CustomIcon(마케도니아icon, icon_size=(30, 30))).add_to(m)
#알바니아
folium.Marker(티라나,
              popup=link_world+"59'>2022.08.27~28 세계 여행 알바니아 티라나",
              tooltip='티라나',
              icon=folium.CustomIcon(알바니아icon, icon_size=(30, 30))).add_to(m)
#몬테네그로
folium.Marker(포드고리차,
              popup=link_world+"60'>2022.08.29 세계 여행 몬테네그로 포드고리차",
              tooltip='포드고리차',
              icon=folium.CustomIcon(몬테네그로icon, icon_size=(30, 30))).add_to(m)
#크로아티아
folium.Marker(두브로브니크,
              popup=link_world+"61'>2022.08.30 세계 여행 크로아티아 두브로브니크 1" + link_1 + "62'>2022.08.31 세계 여행 크로아티아 두브로브니크 2</a>",
              tooltip='두브로브니크',
              icon=folium.CustomIcon(크로아티아icon, icon_size=(30, 30))).add_to(m)
folium.Marker(스플리트,
              popup=link_world+"63'>2022.09.02 세계 여행 크로아티아 스플리트",
              tooltip='스플리트',
              icon=folium.CustomIcon(크로아티아icon, icon_size=(30, 30))).add_to(m)
folium.Marker(자다르,
              popup=link_world+"64'>2022.09.03 세계 여행 크로아티아 자다르",
              tooltip='자다르',
              icon=folium.CustomIcon(크로아티아icon, icon_size=(30, 30))).add_to(m)
folium.Marker(자그레브,
              popup=link_world+"65'>2022.09.04~06 세계 여행 크로아티아 자그레브",
              tooltip='자그레브',
              icon=folium.CustomIcon(크로아티아icon, icon_size=(30, 30))).add_to(m)
#헝가리
folium.Marker(부다페스트,
              popup=link_world+"66'>2022.09.07 세계 여행 헝가리 부다페스트 1" + link_1 + "67'>2022.09.08 세계 여행 헝가리 부다페스트 2" + link_1 + "68'>2022.09.09 세계 여행 헝가리 부다페스트 3</a>",
              tooltip='부다페스트',
              icon=folium.CustomIcon(헝가리icon, icon_size=(30, 30))).add_to(m)
folium.Marker(발라톤퓨레드,
              popup=link_world+"69'>2022.09.09~10 세계 여행 헝가리 발라톤퓨레드",
              tooltip='발라톤퓨레드',
              icon=folium.CustomIcon(헝가리icon, icon_size=(30, 30))).add_to(m)
#오스트리아
folium.Marker(빈,
              popup=link_world+"70'>2022.09.10 세계 여행 오스트리아 빈 1" + link_1 + "71'>2022.09.11 세계 여행 오스트리아 빈 2" + link_1 + "72'>2022.09.12 세계 여행 오스트리아 빈 3</a>",
              tooltip='빈',
              icon=folium.CustomIcon(오스트리아icon, icon_size=(30, 30))).add_to(m)
folium.Marker(그라츠,
              popup=link_world+"73'>2022.09.13 세계 여행 오스트리아 그라츠",
              tooltip='그라츠',
              icon=folium.CustomIcon(오스트리아icon, icon_size=(30, 30))).add_to(m)
#체코
folium.Marker(프라하,
              popup=link_world+"74'>2022.09.14 세계 여행 체코 프라하 1" + link_1 + "75'>2022.09.15 세계 여행 체코 프라하 2"+ link_1 + "76'>2022.09.16 세계 여행 체코 프라하 3"+ link_1 + "77'>2022.09.17 세계 여행 체코 프라하 4</a>",
              tooltip='프라하',
              icon=folium.CustomIcon(체코icon, icon_size=(30, 30))).add_to(m)
#독일
folium.Marker(드레스덴,
              popup=link_world+"78'>2022.09.18 세계 여행 독일 드레스덴 1" + link_1 + "79'>2022.09.19 세계 여행 독일 드레스덴 2</a>",
              tooltip='드레스덴',
              icon=folium.CustomIcon(독일icon, icon_size=(30, 30))).add_to(m)
folium.Marker(베를린,
              popup=link_world+"80'>2022.09.20 세계 여행 독일 베를린 1" + link_1 + "81'>2022.09.21 세계 여행 독일 베를린 2" + link_1 + "82'>2022.09.22 세계 여행 독일 베를린 3</a>",
              tooltip='베를린',
              icon=folium.CustomIcon(독일icon, icon_size=(30, 30))).add_to(m)
folium.Marker(브레멘,
              popup=link_world+"83'>2022.09.23 세계 여행 독일 브레멘",
              tooltip='브레멘',
              icon=folium.CustomIcon(독일icon, icon_size=(30, 30))).add_to(m)
folium.Marker(프랑크푸르트,
              popup=link_world+"84'>2022.09.24~25 세계 여행 독일 프랑크푸르트",
              tooltip='프랑크푸르트',
              icon=folium.CustomIcon(독일icon, icon_size=(30, 30))).add_to(m)
folium.Marker(자르뷔르켄,
              tooltip='자르뷔르켄',
              icon=folium.CustomIcon(독일icon, icon_size=(30, 30))).add_to(m)
#네덜란드
folium.Marker(암스테르담,
              popup=link_world+"85'>2022.09.26 세계 여행 네덜란드 암스테르담 1" + link_1 + "86'>2022.09.27 세계 여행 네덜란드 암스테르담 2</a>",
              tooltip='암스테르담',
              icon=folium.CustomIcon(네덜란드icon, icon_size=(30, 30))).add_to(m)
# 프랑스
folium.Marker(파리,
              popup=link_world+"87'>2022.09.28 세계 여행 프랑스 파리 1" + link_1 + "88'>2022.09.29 세계 여행 프랑스 파리 2" + link_1 + "89'>2022.09.30 세계 여행 프랑스 파리 3"+ link_1 + "118'>2022.11.10 세계 여행 프랑스 파리 4"+ link_1 + "119'>2022.11.11 세계 여행 프랑스 파리 5"+ link_1 + "120'>2022.11.12 세계 여행 프랑스 파리 6</a>",
              tooltip='파리',
              icon=folium.CustomIcon(프랑스icon, icon_size=(30, 30))).add_to(m)
folium.Marker(보르도,
              popup=link_world+"90'>2022.10.01~02 세계 여행 프랑스 보르도",
              tooltip='보르도',
              icon=folium.CustomIcon(프랑스icon, icon_size=(30, 30))).add_to(m)
folium.Marker(리옹,
              popup=link_world+"116'>2022.11.06 세계 여행 프랑스 리옹",
              tooltip='리옹',
              icon=folium.CustomIcon(프랑스icon, icon_size=(30, 30))).add_to(m)
folium.Marker(클레르몽페랑,
              popup=link_world+"117'>2022.11.08 세계 여행 프랑스 클레르몽페랑",
              tooltip='클레르몽페랑',
              icon=folium.CustomIcon(프랑스icon, icon_size=(30, 30))).add_to(m)
# 스페인
folium.Marker(바르셀로나,
              popup=link_world+"91'>2022.10.04 세계 여행 스페인 바르셀로나",
              tooltip='바르셀로나',
              icon=folium.CustomIcon(스페인icon, icon_size=(30, 30))).add_to(m)
folium.Marker(마드리드,
              popup=link_world+"92'>2022.10.05~06 세계 여행 스페인 마드리드",
              tooltip='마드리드',
              icon=folium.CustomIcon(스페인icon, icon_size=(30, 30))).add_to(m)
folium.Marker(그라나다,
              popup=link_world+"93'>2022.10.07~09 세계 여행 스페인 그라나다",
              tooltip='그라나다',
              icon=folium.CustomIcon(스페인icon, icon_size=(30, 30))).add_to(m)
folium.Marker(세비야,
              popup=link_world+"94'>2022.10.10~11 세계 여행 스페인 세비야",
              tooltip='세비야',
              icon=folium.CustomIcon(스페인icon, icon_size=(30, 30))).add_to(m)
# 포르투갈
folium.Marker(리스본,
              popup=link_world+"95'>2022.10.12~14 세계 여행 포르투갈 리스본",
              tooltip='리스본',
              icon=folium.CustomIcon(포르투갈icon, icon_size=(30, 30))).add_to(m)
folium.Marker(라고스,
              popup=link_world+"96'>2022.10.13 세계 여행 포르투갈 라고스",
              tooltip='라고스',
              icon=folium.CustomIcon(포르투갈icon, icon_size=(30, 30))).add_to(m)
folium.Marker(포르토,
              popup=link_world+"97'>2022.10.15 세계 여행 포르투갈 포르투 1" + link_1 + "98'>2022.10.16 세계 여행 포르투갈 포르투 2" + link_1 + "99'>2022.10.17 세계 여행 포르투갈 포르투 3</a>",
              tooltip='포르토',
              icon=folium.CustomIcon(포르투갈icon, icon_size=(30, 30))).add_to(m)
# 이탈리아
folium.Marker(나폴리,
              popup=link_world+"101'>2022.10.20 세계 여행 이탈리아 나폴리",
              tooltip='나폴리',
              icon=folium.CustomIcon(이탈리아icon, icon_size=(30, 30))).add_to(m)
folium.Marker(로마,
              popup=link_world+"102'>2022.10.21 세계 여행 이탈리아 로마 1" + link_1 + "103'>2022.10.22 세계 여행 이탈리아 로마 2" + link_1 + "104'>2022.10.23 세계 여행 이탈리아 로마 3" + link_1 + "105'>2022.10.24 세계 여행 이탈리아 로마 4</a>",
              tooltip='로마',
              icon=folium.CustomIcon(이탈리아icon, icon_size=(30, 30))).add_to(m)
folium.Marker(플로렌스,
              popup=link_world+"106'>2022.10.25 세계 여행 이탈리아 플로렌스(피렌체) 1" + link_1 + "108'>2022.10.27 세계 여행 이탈리아 플로렌스(피렌체) 2</a>",
              tooltip='플로렌스',
              icon=folium.CustomIcon(이탈리아icon, icon_size=(30, 30))).add_to(m)
folium.Marker(피사,
              popup=link_world+"107'>2022.10.26 세계 여행 이탈리아 피사",
              tooltip='피사',
              icon=folium.CustomIcon(이탈리아icon, icon_size=(30, 30))).add_to(m)
folium.Marker(밀라노,
              popup=link_world+"109'>2022.10.28~29 세계 여행 이탈리아 밀라노",
              tooltip='밀라노',
              icon=folium.CustomIcon(이탈리아icon, icon_size=(30, 30))).add_to(m)
# 스위스
folium.Marker(체르마트,
              popup=link_world+"110'>2022.10.30 세계 여행 스위스 체르마트 1" + link_1 + "111'>2022.10.31 세계 여행 스위스 체르마트 2</a>",
              tooltip='체르마트',
              icon=folium.CustomIcon(스위스icon, icon_size=(30, 30))).add_to(m)
folium.Marker(인터라켄,
              popup=link_world+"112'>2022.11.01 세계 여행 스위스 인터라켄 1" + link_1 + "113'>2022.11.02 세계 여행 스위스 인터라켄 2</a>",
              tooltip='인터라켄',
              icon=folium.CustomIcon(스위스icon, icon_size=(30, 30))).add_to(m)
folium.Marker(베른,
              popup=link_world+"114'>2022.11.03 세계 여행 스위스 인터라켄 베른" + link_1 + "115'>2022.11.04 세계 여행 스위스 베른</a>",
              tooltip='베른',
              icon=folium.CustomIcon(스위스icon, icon_size=(30, 30))).add_to(m)
# 영국
folium.Marker(런던,
              popup=link_world+"121'>2022.11.14 세계 여행 영국 런던 1" + link_1 + "122'>2022.11.15 세계 여행 영국 런던 2</a>",
              tooltip='런던',
              icon=folium.CustomIcon(영국icon, icon_size=(30, 30))).add_to(m)
# 캐나다
folium.Marker(토론토,
              popup=link_world+"123'>2022.11.16 세계 여행 캐나다 토론토 1" + link_1 + "124'>2022.11.17 세계 여행 캐나다 토론토 2</a>",
              tooltip='토론토',
              icon=folium.CustomIcon(캐나다icon, icon_size=(30, 30))).add_to(m)
folium.Marker(킹스턴,
              popup=link_world+"125'>2022.11.18~19 세계 여행 캐나다 킹스턴</a>",
              tooltip='킹스턴',
              icon=folium.CustomIcon(캐나다icon, icon_size=(30, 30))).add_to(m)
folium.Marker(몬트리올,
              popup=link_world+"126'>2022.11.20~21 세계 여행 캐나다 몬트리올 1" + link_1 + "127'>2022.11.22 세계 여행 캐나다 몬트리올 2" + link_1 + "128'>2022.11.23~24 세계 여행 캐나다 몬트리올 3</a>",
              tooltip='몬트리올',
              icon=folium.CustomIcon(캐나다icon, icon_size=(30, 30))).add_to(m)
# 미국
folium.Marker(뉴욕,
              popup=link_world+"129'>2022.11.24~25 세계 여행 미국 뉴욕 1" + link_1 + "130'>2022.11.26 세계 여행 미국 뉴욕 2" + link_1 + "131'>2022.11.27 세계 여행 미국 뉴욕 3" + link_1 + "132'>2022.11.28~29 세계 여행 미국 뉴욕 4" + link_1 + "149'>2022.12.19~20 세계 여행 미국 뉴욕 5" + link_1 + "150'>2022.12.21~22 세계 여행 미국 뉴욕 6" + link_1 + "151'>2022.12.23 세계 여행 미국 뉴욕 7" + link_1 + "152'>2022.12.24 세계 여행 미국 뉴욕 8" + link_1 + "153'>2022.12.25 세계 여행 미국 뉴욕 9</a>",
              tooltip='뉴욕',
              icon=folium.CustomIcon(미국icon, icon_size=(30, 30))).add_to(m)
folium.Marker(샌프란시스코,
              popup=link_world+"133'>2022.11.30 세계 여행 미국 샌프란시스코 1" + link_1 + "134'>2022.12.01 세계 여행 미국 샌프란시스코 2" + link_1 + "135'>2022.12.02 세계 여행 미국 샌프란시스코 3</a>",
              tooltip='샌프란시스코',
              icon=folium.CustomIcon(미국icon, icon_size=(30, 30))).add_to(m)
folium.Marker(로스엔젤레스,
              popup=link_world+"136'>2022.12.04 세계 여행 미국 LA 1" + link_1 + "137'>2022.12.05 세계 여행 미국 LA 2" + link_1 + "138'>2022.12.06 세계 여행 미국 LA 3</a>",
              tooltip='로스엔젤레스',
              icon=folium.CustomIcon(미국icon, icon_size=(30, 30))).add_to(m)
folium.Marker(라스베가스,
              popup=link_world+"139'>2022.12.07 세계 여행 미국 라스베이거스 1" + link_1 + "140'>2022.12.08 세계 여행 미국 라스베이거스 2" + link_1 + "141'>2022.12.09 세계 여행 미국 라스베이거스 3</a>",
              tooltip='라스베가스',
              icon=folium.CustomIcon(미국icon, icon_size=(30, 30))).add_to(m)
# 멕시코
folium.Marker(플라야델카르멘,
              popup=link_world+"142'>2022.12.10 세계 여행 멕시코 플라야 델 카르멘 1" + link_1 + "143'>2022.12.11 세계 여행 멕시코 플라야 델 카르멘 2" + link_1 + "144'>2022.12.12 세계 여행 멕시코 플라야 델 카르멘 3"+ link_1 + "145'>2022.12.13~15 세계 여행 멕시코 플라야 델 카르멘 4</a>",
              tooltip='플라야 델 카르멘',
              icon=folium.CustomIcon(멕시코icon, icon_size=(30, 30))).add_to(m)
folium.Marker(칸쿤,
              popup=link_world+"146'>2022.12.15 세계 여행 멕시코 칸쿤 1" + link_1 + "147'>2022.12.16~17 세계 여행 멕시코 칸쿤 2" + link_1 + "148'>2022.12.18 세계 여행 멕시코 칸쿤 3</a>",
              tooltip='칸쿤',
              icon=folium.CustomIcon(멕시코icon, icon_size=(30, 30))).add_to(m)
# 스코틀랜드
folium.Marker(에든버러,
              popup=link_world+"154'>2022.12.26~27 세계 여행 스코틀랜드 에든버러 1" + link_1 + "155'>2022.12.28 세계 여행 스코틀랜드 에든버러 2" + link_1 + "156'>2022.12.29~30 세계 여행 스코틀랜드 에든버러 3</a>",
              tooltip='에든버러',
              icon=folium.CustomIcon(스코틀랜드icon, icon_size=(30, 30))).add_to(m)


m.get_root().html.add_child(folium.Element("""
<style>
.folium-popup {
  max-width: 1000px;
}
</style>
"""))

m


m.save('index.html')