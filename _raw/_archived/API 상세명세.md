# INAVI AIR API 상세 명세

> 출처: INAVI AIR API (Notion)
> 정리일: 2026-06-09
> 본 문서는 각 API의 Function / URL / Request(Header·Parameter) / Response 필드 스펙을 카테고리별로 정리한 것입니다.
> 각 페이지의 "더 불러오기" 항목을 모두 펼쳐 필드 누락 없이 수집했습니다.

---


# 1. 탐색

## 일반 경로 리스트 탐색

```
일반 경로 리스트 탐색
Function
일반 경로 리스트 탐색
URL
/findListRoute
Request Header
Request Parameter
parameter
type
requisite
description
searchOptions
List<String>
O
Agent 탐색 종류agt_recommend : 추천경로 (LGU+ 향으로는 “빠른길”)agt_short_time : 최소시간real_traffic_freeroad : 무료도로short_distance_priority : 최단거리highway_priority : 고속도로우선motorcycle : 이륜차 이용도로beginner : 초보자(편한길) (LGU+ 향으로는 “편한길”)recommendation : 엔진기반 추천경로(agt_recommend 대체)time_priority : 엔진기반 최소시간(agt_short_time 대체)
avoidSchoolZone
String
스쿨존 회피(searchOption)0:회피 안함(Default)1:회피
ignoreTimeRestrictedZone
String
시간제 통행 규제 무시 0: 무시안함(Default) 1: 무시
useHighwayProjectionStart
String
출발지 고속도로, 자동차전용, 도시고속 회피 0: 회피 안함(Default) 1: 회피
useHighwayProjectionEnd
String
목적지 고속도로, 자동차전용, 도시고속 회피 0: 회피 안함(Default) 1: 회피
mrVersion
String
O
MR version
searchType
String
O
탐색종류0: 일반탐색4: MYWAY(특정대교)5: 테마도로6: MYCCTV7: 통계탐색
directivity
boolean
목적지 방향성 탐색true : 사용false : 사용안함(default)
rotate
boolean
회전규제 고려 탐색true : 사용false : 사용안함(default)
dual
boolean
경로선 이원화(가상 분리된 경로선)true : 사용false : 사용안함(default)
forced
boolean
도로상 통행 제한지점 강제통과true : 사용false : 사용안함(default)
searchString
String
검색어(검색어가 사용되는 기능을 통한 탐색시)(Log)
inMethod
INTEGER
경로탐색을 호출한 기능(Log)0: 통합검색1: 최근검색어3: 즐겨찾기4: 이전목적지6: 타임머신7: AI를통한 호출(AI플래그와 타 플래그가 동시에 적용되는 시나리오에서는 구분자 '/'로 같이 보내주어야함)
routeOpt_sub
String
경로옵션(대교탐색/해안도로/구간비교/주행중탐색 인 경우만)(Log)
BRDG 대교탐색SHORE 해안도로REROUTE 주행중탐색
routeOpt_sub_name
String
대교탐색 인 경우 해당 대교의 이름(Log)
curPosType (LogApi = startPosType)
String
출발지가 GPS 3D Fix 시의 위치인지의 여부GPS(Log)
 GPS 에서 수신된 위치
OTHER GPS 에서 수신된 위치가 아닌 위치를 사용하거나 유저가 출발지를 지정한 경우
category
Array
선호주유소 카테고리 코드 리스트
┗ val
String
Category CodeC0100 : 주유소(default)
oil
String
유종0:ALL (default)1:휘발유2:고급휘발유3:경유4:LPG
startloc
Object
O
출발지 지점 정보
┣ lonx
String
O
출발지 경도, 정규화좌표 X값
┣ laty
String
O
출발지 위도, 정규화좌표 Y값
┣ pid
String
위치의 PID(startPos 에서는 PID 생략 가능)(Log)
┣ name
String
O
출발지 명칭
┣ mapid
String
O
출발지 도엽번호
┣ linkid
String
O
출발지 링크번호
┣ nodeid
String
O
출발지 노드번호
┣ direction
String
O
출발지 방향
┣ usingName
boolean
지점명칭 사용true : 사용(default)false : 사용안함
┣ usingHideViaLoc
boolean
숨김 경유지true : 사용false : 사용안함(default)
┣ viaLocStart
boolean
경유도로 시작true : 사용false : 사용안함(default)
┗ viaLocEnd
boolean
경유도로 종료true : 사용false : 사용안함(default)
endloc
Object
O
도착지 지점 정보
┣ lonx
String
O
도착지 경도, 정규화좌표 X값
┣ laty
String
O
도착지 위도, 정규화좌표 Y값
┣ pid
String
위치의 PID(endloc 에서는 PID 생략 가능)(Log)
┣ ctrIdx1
String
도착지 PID에 대한 CTR 검색 결과 idx1 정보(Log)
┣ ctrIdx2_1
String
도착지 PID에 대한 CTR 검색 결과 idx2-1 정보(Log)
┣ ctrIdx2_2
String
도착지 PID에 대한 CTR 검색 결과 idx2-2 정보(Log)
┣ ctrSortFlag
String
도착지 PID에 대한 CTR 검색 결과 sort flag 정보(Log)
정렬순서:DIST 거리순ACCU 정확도순
┣ name
String
O
도착지 명칭
┣ mapid
String
O
도착지 도엽번호
┣ linkid
String
O
도착지 링크번호
┣ nodeid
String
O
도착지 노드번호
┣ direction
String
O
도착지 방향
┣ usingName
boolean
지점명칭 사용true : 사용(default)false : 사용안함
┣ usingHideViaLoc
boolean
숨김 경유지true : 사용false : 사용안함(default)
┣ viaLocStart
boolean
경유도로 시작/종료true : 사용false : 사용안함(default)
┗ viaLocEnd
boolean
경유도로 종료true : 사용false : 사용안함(default)
vialocList
Array
경유지 지점 정보
┣ lonx
String
경유지 경도, 정규화좌표 X값
┣ laty
String
경유지 위도, 정규화좌표 Y값
┣ pid
String
위치의 PID(endloc 에서는 PID 생략 가능)(Log)
┣ ctrIdx1
String
도착지 PID에 대한 CTR 검색 결과 idx1 정보(Log)
┣ ctrIdx2_1
String
도착지 PID에 대한 CTR 검색 결과 idx2-1 정보(Log)
┣ ctrIdx2_2
String
도착지 PID에 대한 CTR 검색 결과 idx2-2 정보(Log)
┣ ctrSortFlag
String
도착지 PID에 대한 CTR 검색 결과 sort flag 정보(Log)
정렬순서:DIST 거리순ACCU 정확도순
┣ name
String
경유지 명칭
┣ mapid
String
경유지 도엽번호
┣ linkid
String
경유지 링크번호
┣ nodeid
String
경유지 노드번호
┣ direction
String
경유지 방향
┣ usingName
boolean
지점명칭 사용true : 사용(default)false : 사용안함
┣ usingHideViaLoc
boolean
숨김 경유지true : 사용false : 사용안함(default)
┣ viaLocStart
boolean
경유도로 시작/종료true : 사용false : 사용안함(default)
┗ viaLocEnd
boolean
경유도로 종료true : 사용false : 사용안함(default)
extensionList
Array
확장 리스트
┣ headerType
String
확장 리스트 타입1: 다중목적지 최적탐색2: 지나간 톨게이트3: 사용자정보5: 경유도로6: 유고회피7: 경로회피 13 : 교통정보 세부 설정
┣ routepoints
Array
다중목적지 리스트 (when headerType is 1)
┣ rpx
String
목적지 X좌표
┗ rpy
String
목적지 Y좌표
┣ tollList
Array
톨게이트 정보 리스트 (when headerType is 2)
┣ tolltype
String
톨게이트 Type
┗ tollidx
String
톨게이트 index
┣ userInput
Object
사용자 입력 정보 (when headerType is 3)
┣ height
String
높이(단위:Cm)
┣ weight
String
중량(단위:kg)
┣ hipass
boolean
하이패스 소지true: 소지false: 미소지
┣ over3
boolean
3인이상true: 3인이상false: 3인이하
┣ zonelimit
boolean
상수원 보호구역 진입 제한 차량true: 제한false: 미제한
┣ cartype
String
차종0: 1종(승용/승합/화물)1: 2종(승합/화물)2: 3종(승합/화물)3: 4종(화물)4: 5종(화물)5: 6종 경차
┣ dishigh
String
고속도로 통행료 할인0: 없음1: 50%할인2: 면제
┗ disjam
String
혼잡 통행료 할인0: 없음1: 50%할인2: 면제
┣ viaRoadList
Array
경유도로 리스트 (when headerType is 5)
┗ viaRoadlinkList
Array
경유도로 Link 리스트
┣ mapid
String
도엽 번호
┗ linkid
String
링크 번호
┣ eventList
Array
유고회피 리스트 (when headerType is 6)
┗ eid
String
유고정보 고유번호
┣ evasList
Array
경로회피 리스트 (when headerType is 7)
┣ mapid
String
도엽 번호
┣ linkid
String
링크 번호
┣ nodeid
String
노드 번호
┣ ext
String
부가 정보
┗ linkposition
String
링크 포지션
┗ trafficSetting
Object
교통정보 세부 설정탐색 (when headerType is 13)
　┗ trafficUnflag
boolean
교통정보 미사용 여부
true : 미사용 (삼성 중공업)
false : 사용 (Default)
timestamp
String
로그주행 탐색시작 시간
EX) 1689567848
Response Parameter
parameter
type
description
결과 없음
```

## 일반 경로 탐색

```
일반 경로 탐색
Function
일반 경로 탐색
URL
/findMultiRoute
Request Header
Request Parameter
parameter
type
requisite
description
searchOption
String
Agent 탐색 종류
해당 파라미터 사용 시 searchOptions null로 설정 해야 함

<일반>
agt_recommend : 추천경로 (LGU+ 향으로는 “빠른길”)
agt_short_time : 최소시간
real_traffic_freeroad : 무료도로
short_distance_priority : 최단거리
highway_priority : 고속도로우선
motorcycle : 이륜차 이용도로
beginner : 초보자(편한길) (LGU+ 향으로는 “편한길”)
recommendation : 엔진기반 추천경로(agt_recommend 대체)
time_priority : 엔진기반 최소시간(agt_short_time 대체)

<화물>
truck1 : 실시간 만차
truck1_freeroad : 실시간 만차 무료
truck2 : 실시간 공차
truck2_freeroad : 실시간 공차 무료
truck1_nationalway : 국도 만차
truck2_nationalway : 국도 공차
truck_empty: 트럭 공차시 추천 경로
truck_empty_freeroad: 트럭 공차시 무료 경로
truck_empty_nationalway: 트력 공차시 국도 위주 경로
truck_full: 트럭 만차시 추천 경로
truck_full_freeroad: 트럭 만차시 무료 경로
truck_full_nationalway: 트럭 만차시 국도 위주 경로
searchOption2
String
Agent 탐색 종류2
해당 파라미터 사용 시 searchOptions null로 설정 해야 함

<일반>
agt_recommend : 추천경로 (LGU+ 향으로는 “빠른길”)
agt_short_time : 최소시간
real_traffic_freeroad : 무료도로
short_distance_priority : 최단거리
highway_priority : 고속도로우선
motorcycle : 이륜차 이용도로
beginner : 초보자(편한길) (LGU+ 향으로는 “편한길”)
recommendation : 엔진기반 추천경로(agt_recommend 대체)
time_priority : 엔진기반 최소시간(agt_short_time 대체)

<화물>
truck1 : 실시간 만차
truck1_freeroad : 실시간 만차 무료
truck2 : 실시간 공차
truck2_freeroad : 실시간 공차 무료
truck1_nationalway : 국도 만차
truck2_nationalway : 국도 공차
truck_empty: 트럭 공차시 추천 경로
truck_empty_freeroad: 트럭 공차시 무료 경로
truck_empty_nationalway: 트력 공차시 국도 위주 경로
truck_full: 트럭 만차시 추천 경로
truck_full_freeroad: 트럭 만차시 무료 경로
truck_full_nationalway: 트럭 만차시 국도 위주 경로
searchOptions
Array<String>
Agent 리스트 탐색 종류
해당 파라미터 사용 시 searchOption, serchOption2 null로 설정 해야 함

<일반>
agt_recommend : 추천경로 (LGU+ 향으로는 “빠른길”)
agt_short_time : 최소시간
real_traffic_freeroad : 무료도로
short_distance_priority : 최단거리
highway_priority : 고속도로우선
motorcycle : 이륜차 이용도로
beginner : 초보자(편한길) (LGU+ 향으로는 “편한길”)
recommendation : 엔진기반 추천경로(agt_recommend 대체)
time_priority : 엔진기반 최소시간(agt_short_time 대체)

<화물>
truck1 : 실시간 만차
truck1_freeroad : 실시간 만차 무료
truck2 : 실시간 공차
truck2_freeroad : 실시간 공차 무료
truck1_nationalway : 국도 만차
truck2_nationalway : 국도 공차
truck_empty: 트럭 공차시 추천 경로
truck_empty_freeroad: 트럭 공차시 무료 경로
truck_empty_nationalway: 트력 공차시 국도 위주 경로
truck_full: 트럭 만차시 추천 경로
truck_full_freeroad: 트럭 만차시 무료 경로
truck_full_nationalway: 트럭 만차시 국도 위주 경로
avoidSchoolZone
String
스쿨존 회피(searchOption)0:회피 안함(Default)1:회피
avoidSchoolZone2
String
스쿨존 회피(searchOption2)0:회피 안함(Default)1:회피
ignoreTimeRestrictedZone
String
시간제 통행 규제 무시 0: 무시안함(Default) 1: 무시
useHighwayProjectionStart
String
출발지 고속도로, 자동차전용, 도시고속 회피 0: 회피 안함(Default) 1: 회피
useHighwayProjectionEnd
목적지 고속도로, 자동차전용, 도시고속 회피 0: 회피 안함(Default) 1: 회피
mrVersion
String
O
MR version
searchType
String
O
탐색종류
0: 일반탐색
4: MYWAY(특정대교)
5: 테마도로
6: MYCCTV
7: 통계탐색
directivity
boolean
목적지 방향성 탐색
true : 사용
false : 사용안함(default)
rotate
boolean
회전규제 고려 탐색
true : 사용
false : 사용안함(default)
dual
boolean
경로선 이원화(가상 분리된 경로선)
true : 사용
false : 사용안함(default)
forced
boolean
도로상 통행 제한지점 강제통과
true : 사용
false : 사용안함(default)
searchString
String
검색어(검색어가 사용되는 기능을 통한 탐색시)(Log)
inMethod
INTEGER
경로탐색을 호출한 기능(Log)
0: 통합검색
1: 최근검색어
3: 즐겨찾기
4: 이전목적지
6: 타임머신
7: AI를통한 호출(AI플래그와 타 플래그가 동시에 적용되는 시나리오에서는 구분자 '/'로 같이 보내주어야함)
8: 지도(위치지정)
9: 메인카드
10: 외부연동
11: 주변검색
12: 주소검색
13: 미정의
routeOpt_sub
String
경로옵션(대교탐색/해안도로/구간비교/주행중탐색 인 경우만)(Log)
BRDG 대교탐색
SHORE 해안도로
REROUTE 주행중탐색
routeOpt_sub_name
String
대교탐색 인 경우 해당 대교의 이름(Log)
curPosType (LogApi = startPosType)
String
출발지가 GPS 3D Fix 시의 위치인지의 여부(Log)
GPS GPS 에서 수신된 위치
OTHER GPS 에서 수신된 위치가 아닌 위치를 사용하거나 유저가 출발지를 지정한 경우
category
Array
선호주유소 카테고리 코드 리스트
┗ val
String
Category Code
C0100 : 주유소(default)
oil
String
유종
0: 휘발유
1: 고급휘발유
2: 경유
3: LPG
4: 전기(EV)
baseUrl
String
코드42 요청 URL
startloc
Object
O
출발지 지점 정보
┣ lonx
String
O
출발지 경도, 정규화좌표 X값
┣ laty
String
O
출발지 위도, 정규화좌표 Y값
┣ pid
String
위치의 PID(Log) (startPos 에서는 PID 생략 가능)
┣ name
String
O
출발지 명칭
┣ mapid
String
O
출발지 도엽번호
┣ linkid
String
O
출발지 링크번호
┣ nodeid
String
O
출발지 노드번호
┣ direction
String
O
출발지 방향
┣ angle
String
정북 기준 도로 진행 방향(코드42)
┣ usingName
boolean
지점명칭 사용
true : 사용(default)
false : 사용안함
┣ usingHideViaLoc
boolean
숨김 경유지
true : 사용
false : 사용안함(default)
┣ viaLocStart
boolean
경유도로 시작
true : 사용
false : 사용안함(default)
┗ viaLocEnd
boolean
경유도로 종료
true : 사용
false : 사용안함(default)
endloc
Object
O
도착지 지점 정보
┣ lonx
String
O
도착지 경도, 정규화좌표 X값
┣ laty
String
O
도착지 위도, 정규화좌표 Y값
┣ pid
String
위치의 PID(Log) (endloc 에서는 PID 생략 가능)
┣ ctrIdx1
String
도착지 PID에 대한 CTR 검색 결과 idx1 정보(Log)
┣ ctrIdx2_1
String
도착지 PID에 대한 CTR 검색 결과 idx2-1 정보(Log)
┣ ctrIdx2_2
String
도착지 PID에 대한 CTR 검색 결과 idx2-2 정보(Log)
┣ ctrSortFlag
String
도착지 PID에 대한 CTR 검색 결과 sort flag 정보(Log)
정렬순서
DIST: 거리순
ACCU: 정확도순
┣ name
String
O
도착지 명칭
┣ mapid
String
O
도착지 도엽번호
┣ linkid
String
O
도착지 링크번호
┣ nodeid
String
O
도착지 노드번호
┣ direction
String
O
도착지 방향
┣ usingName
boolean
지점명칭 사용
true : 사용(default)
false : 사용안함
┣ usingHideViaLoc
boolean
숨김 경유지
true : 사용
false : 사용안함(default)
┣ viaLocStart
boolean
경유도로 시작/종료
true : 사용
false : 사용안함(default)
┗ viaLocEnd
boolean
경유도로 종료
true : 사용
false : 사용안함(default)
vialocList
Array
경유지 지점 정보
┣ lonx
String
경유지 경도, 정규화좌표 X값
┣ laty
String
경유지 위도, 정규화좌표 Y값
┣ pid
String
위치의 PID(endloc 에서는 PID 생략 가능)(Log)
┣ ctrIdx1
String
도착지 PID에 대한 CTR 검색 결과 idx1 정보(Log)
┣ ctrIdx2_1
String
도착지 PID에 대한 CTR 검색 결과 idx2-1 정보(Log)
┣ ctrIdx2_2
String
도착지 PID에 대한 CTR 검색 결과 idx2-2 정보(Log)
┣ ctrSortFlag
String
도착지 PID에 대한 CTR 검색 결과 sort flag 정보(Log)
정렬순서
DIST: 거리순
ACCU: 정확도순
┣ name
String
경유지 명칭
┣ mapid
String
경유지 도엽번호
┣ linkid
String
경유지 링크번호
┣ nodeid
String
경유지 노드번호
┣ direction
String
경유지 방향
┣ usingName
boolean
지점명칭 사용
true : 사용(default)
false : 사용안함
┣ usingHideViaLoc
boolean
숨김 경유지
true : 사용
false : 사용안함(default)
┣ viaLocStart
boolean
경유도로 시작/종료
true : 사용
false : 사용안함(default)
┗ viaLocEnd
boolean
경유도로 종료
true : 사용
false : 사용안함(default)
extensionList
Array
확장 리스트
┣ headerType
String
확장 리스트 타입
1: 다중목적지 최적탐색
2: 지나간 톨게이트
3: 사용자정보
5: 경유도로
6: 유고회피
7: 경로회피
13 : 교통정보 세부 설정
　┣ routepoints
Array
다중목적지 리스트 (when headerType is 1)
　┣ rpx
String
목적지 X좌표
　┗ rpy
String
목적지 Y좌표
┣ tollList
Array
톨게이트 정보 리스트 (when headerType is 2)
　┣ tolltype
String
톨게이트 Type
　┗ tollidx
String
톨게이트 index
┣ userInput
Object
사용자 입력 정보 (when headerType is 3)
　┣ height
String
높이(단위:Cm)
　┣ weight
String
중량(단위:kg)
　┣ hipass
boolean
하이패스 소지
true: 소지
false: 미소지
　┣ over3
boolean
3인이상
true: 3인이상
false: 3인이하
　┣ zonelimit
boolean
상수원 보호구역 진입 제한 차량true: 제한false: 미제한
　┣ cartype
String
차종
0: 1종(승용/승합/화물)
1: 2종(승합/화물)
2: 3종(승합/화물)
3: 4종(화물)
4: 5종(화물)
5: 6종 경차
　┣ dishigh
String
고속도로 통행료 할인
0: 없음
1: 50%할인
2: 면제
　┣ carUsage
String
차량 용도
0: 일반(Default)
1: 택시 서비스 1(Onda)
2: 택시 서비스2 (i.M)
3: 타다 서비스 (VCNC)
4: Baemin 서비스(우아한 형제들)
5: Where 서비스(MXI)
　┗ disjam
String
혼잡 통행료 할인
0: 없음
1: 50%할인
2: 면제
┣ viaRoadList
Array
경유도로 리스트 (when headerType is 5)
　┣ viaRoadlinkList
Array
경유도로 Link 리스트
　┣ mapid
String
도엽 번호
　┗ linkid
String
링크 번호
┣ eventList
Array
유고회피 리스트 (when headerType is 6)
　┗ eid
String
유고정보 고유번호
┣ evasList
Array
경로회피 리스트 (when headerType is 7)
　┣ mapid
String
도엽 번호
　┣ linkid
String
링크 번호
　┣ nodeid
String
노드 번호
　┣ ext
String
부가 정보
더 불러오기
Response Parameter
parameter
type
description
결과 없음
더 불러오기
```

## 경로 재 탐색

```
경로 재 탐색
Function
경로 재 탐색
URL
/findRouteAgain
Request Header
Request Parameter
parameter
type
requisite
description
searchOption
String
O
Agent 탐색 종류agt_recommend : 에이전트추천agt_short_time : 최소시간real_traffic : 빠르고real_traffic2 : 편하고real_traffic_comfortable : 더편하고real_traffic_freeroad : 무료도로short_distance_priority : 최단거리highway_priority : 고속도로우선motorcycle : 이륜차 이용도로beginner : 초보자recommendation : 엔진기반 추천경로time_priority : 엔진기반 최소시간* 추천, 최소시간은 스마트재탐색 사용안함으로 설정
searchOptionOrg
String
Agent 탐색 종류(사용자가 선택한 추천/최소 탐색 옵션)recommendation : 엔진기반 추천경로(agt_recommend 대체)time_priority : 엔진기반 최소시간(agt_short_time 대체)
avoidSchoolZone
String
스쿨존 회피0:회피 안함(Default)1:회피
ignoreTimeRestrictedZone
String
시간제 통행 규제 무시 0: 무시안함(Default) 1: 무시
useHighwayProjectionStart
String
출발지 고속도로, 자동차전용, 도시고속 회피 0: 회피 안함(Default) 1: 회피
useHighwayProjectionEnd
String
목적지 고속도로, 자동차전용, 도시고속 회피 0: 회피 안함(Default) 1: 회피
mrVersion
String
O
MR version
searchType
String
O
탐색종류1 : 일반재탐색2 : 교통재탐색3 : 이탈재탐색
smart
boolean
O
스마트재탐색 여부true : 사용false : 사용안함(default)
rid
String
O
경로파일 ID
remainTime
String
O
남은시간 (초)smart:true일 경우 remainTime이 일정 시간 이내이면 121(동일경로) 리턴 발생 할 수 있음
remainDistance
String
O
남은거리 (M)
currentPosition
String
O
경로파일에서 현재위치 링크인덱스
directivity
boolean
목적지 방향성 탐색true : 사용false : 사용안함(default)
rotate
boolean
회전규제 고려 탐색true : 사용false : 사용안함(default)
dual
boolean
경로선 이원화(가상 분리된 경로선)true : 사용false : 사용안함(default)
forced
boolean
도로상 통행 제한지점 강제통과true : 사용false : 사용안함(default)
category
Array
선호주유소 카테고리 코드 리스트
┗ val
String
Category CodeC0100 : 주유소(default)
oil
String
유종0:ALL (default)1:휘발유2:고급휘발유3:경유4:LPG
baseUrl
String
코드42 요청 URL
startloc
Object
O
출발지 지점 정보
┣ lonx
String
O
출발지 경도, 정규화좌표 X값
┣ laty
String
O
출발지 위도, 정규화좌표 Y값
┣ name
String
O
출발지 명칭
┣ mapid
String
O
출발지 도엽번호
┣ linkid
String
O
출발지 링크번호
┣ nodeid
String
O
출발지 노드번호
┣ direction
String
O
출발지 방향
┣ angle
String
정북 기준 도로 진행 방향(코드42)
┣ usingName
boolean
지점명칭 사용true : 사용(default)false : 사용안함
┣ usingHideViaLoc
boolean
숨김 경유지true : 사용false : 사용안함(default)
┣ viaLocStart
boolean
경유도로 시작/종료true : 사용false : 사용안함(default)
┗ viaLocEnd
boolean
경유도로 종료true : 사용false : 사용안함(default)
endloc
Object
O
도착지 지점 정보
┣ lonx
String
O
도착지 경도, 정규화좌표 X값
┣ laty
String
O
도착지 위도, 정규화좌표 Y값
┣ name
String
O
도착지 명칭
┣ mapid
String
O
도착지 도엽번호
┣ linkid
String
O
도착지 링크번호
┣ nodeid
String
O
도착지 노드번호
┣ direction
String
O
도착지 방향
┣ usingName
boolean
지점명칭 사용true : 사용(default)false : 사용안함
┣ usingHideViaLoc
boolean
숨김 경유지true : 사용false : 사용안함(default)
┣ viaLocStart
boolean
경유도로 시작/종료true : 사용false : 사용안함(default)
┗ viaLocEnd
boolean
경유도로 종료true : 사용false : 사용안함(default)
vialocList
Array
경유지 지점 정보
┣ lonx
String
경유지 경도, 정규화좌표 X값
더 불러오기
Response Parameter
parameter
type
description
result_code
String
결과 코드
result_msg
String
결과코드에 따른 메세지
option_type
String
Agent 탐색 종류agt_recommend : 에이전트추천agt_short_time : 최소시간real_traffic_freeroad : 무료도로short_distance_priority : 최단거리highway_priority : 고속도로우선motorcycle : 이륜차 이용도로*주의: 재탐색 시 rdata의 url을 통해 받은 탐색 파일에 명시 되어 있는 탐색 옵션을 재탐색 시 searchOption 항목에 전달 하여야 함
rid
String
경로 ID
rdata
String
경로 Data URI
gdata
String
안내 Data URI
tdata
String
교통정보 Data URI
poi
Object
최저가주유소 검색결과
┣ catecode
String
분류코드
┣ dpx
String
display X좌표(WGS84의 경우 longitude)
┣ dpy
String
display Y좌표(WGS84의 경우 latitude)
┗ oildata
Object
유가 데이터 정보
┣ g_price
Integer
휘발유 가격
┣ g_least
Integer
최저 휘발유 가격제공 Flag(0: 아님 1: 맞음)
┣ hg_price
Integer
고급휘발유 가격
┣ hg_least
Integer
최저 고급휘발유 가격제공 Flag(0: 아님 1: 맞음)
┣ d_price
Integer
경유 가격
┣ d_least
Integer
최저 경유 가격제공 Flag(0: 아님 1: 맞음)
┣ l_price
Integer
LPG 가격
┣ l_least
Integer
최저 LPG 가격제공 Flag(0: 아님 1: 맞음)
┗ updatetime
String
Update 시간
eventlist_cnt
Integer
유고정보 목록 개수
event_list
Array
유고정보 목록
┣ comment
String
부가 설명 (이벤트 설명)
┣ latitude
String
위도(WGS 84좌표, 10micro degree)
┣ longitude
String
경도(WGS 84좌표, 10micro degree)
┣ rtm_table_num
Integer
TPEG RTM Table 번호
┗ rtm_code_num
Integer
TPEG RTM Code 번호
vvms_cnt
Integer
VVMS 개수
vvms_list
Array
VVMS 리스트
┣ dpx
String
display X좌표(WGS84의 경우 longitude)
┣ dpy
String
display Y좌표(WGS84의 경우 latitude)
┣ id
String
도로정보 id
┣ mapid
String
MAP ID
┣ direction
Integer
0 : 경로역방향1 : 경로 진행방향
┗ linkid
String
LINK ID
smart_vvms_cnt
Integer
VVMS 개수
smart_vvms_list
Array
VVMS 리스트
┣ id
String
도로정보 id
┣ type
Integer
VVMS 타입 0:일반 1:홍수 2:산사태 3:호우
┣ d_level
String
VVMS 재난 레벨(type이 1,2,3일 때)
01:경보 발령 02:심각단계 발령
┣ vType
Integer
VVMS 음성 표출 타입0:미표출1:돌발2:사고
┣ m_x
String
메시지 display X좌표
┣ m_y
String
메시지 display Y좌표
┣ m_mapid
String
메시지 MAP ID
┣ m_linkid
String
메시지 LINK ID
┣ m_direction
Integer
메시지 DIRECTION0 : 경로 역방향1 : 경로 진행방향
┣ e_x
String
이벤트 display X좌표
┣ e_y
String
이벤트 display Y좌표
┣ e_mapid
String
이벤트 MAP ID
더 불러오기
```

## 요약결과 경로 탐색

```
요약결과 경로 탐색
Function
요약결과 경로 탐색
URL
/findSummaryRoute
Request Header
Request Parameter
parameter
type
requisite
description
searchOption
String
O
Agent 탐색 종류real_traffic : 빠르고
avoidSchoolZone
String
스쿨존 회피(searchOption)0:회피 안함(Default)1:회피
ignoreTimeRestrictedZone
String
시간제 통행 규제 무시 0: 무시안함(Default) 1: 무시
useHighwayProjectionStart
String
출발지 고속도로, 자동차전용, 도시고속 회피 0: 회피 안함(Default) 1: 회피
useHighwayProjectionEnd
String
목적지 고속도로, 자동차전용, 도시고속 회피 0: 회피 안함(Default) 1: 회피
mrVersion
String
O
MR version
searchType
String
O
탐색종류0: 일반탐색
directivity
boolean
목적지 방향성 탐색true : 사용false : 사용안함(default)
rotate
boolean
회전규제 고려 탐색true : 사용false : 사용안함(default)
dual
boolean
경로선 이원화(가상 분리된 경로선)true : 사용false : 사용안함(default)
forced
boolean
도로상 통행 제한지점 강제통과true : 사용false : 사용안함(default)
startloc
Object
O
출발지 지점 정보
┣ lonx
String
O
출발지 경도, 정규화좌표 X값
┣ laty
String
O
출발지 위도, 정규화좌표 Y값
┣ name
String
O
출발지 명칭
┣ mapid
String
O
출발지 도엽번호
┣ linkid
String
O
출발지 링크번호
┣ nodeid
String
O
출발지 노드번호
┣ direction
String
O
출발지 방향
┣ usingName
boolean
지점명칭 사용true : 사용(default)false : 사용안함
┣ usingHideViaLoc
boolean
숨김 경유지true : 사용false : 사용안함(default)
┣ viaLocStart
boolean
경유도로 시작true : 사용false : 사용안함(default)
┗ viaLocEnd
boolean
경유도로 종료true : 사용false : 사용안함(default)
endloc
Object
O
도착지 지점 정보
┣ lonx
String
O
도착지 경도, 정규화좌표 X값
┣ laty
String
O
도착지 위도, 정규화좌표 Y값
┣ name
String
O
도착지 명칭
┣ mapid
String
O
도착지 도엽번호
┣ linkid
String
O
도착지 링크번호
┣ nodeid
String
O
도착지 노드번호
┣ direction
String
O
도착지 방향
┣ usingName
boolean
지점명칭 사용true : 사용(default)false : 사용안함
┣ usingHideViaLoc
boolean
숨김 경유지true : 사용false : 사용안함(default)
┣ viaLocStart
boolean
경유도로 시작/종료true : 사용false : 사용안함(default)
┗ viaLocEnd
boolean
경유도로 종료true : 사용false : 사용안함(default)
vialocList
Array
경유지 지점 정보
┣ lonx
String
경유지 경도, 정규화좌표 X값
┣ laty
String
경유지 위도, 정규화좌표 Y값
┣ name
String
경유지 명칭
┣ mapid
String
경유지 도엽번호
┣ linkid
String
경유지 링크번호
┣ nodeid
String
경유지 노드번호
┣ direction
String
경유지 방향
┣ usingName
boolean
지점명칭 사용true : 사용(default)false : 사용안함
┣ usingHideViaLoc
boolean
숨김 경유지true : 사용false : 사용안함(default)
┣ viaLocStart
boolean
경유도로 시작/종료true : 사용false : 사용안함(default)
┗ viaLocEnd
boolean
경유도로 종료true : 사용false : 사용안함(default)
extensionList
Array
확장 리스트
┣ headerType
String
확장 리스트 타입1: 다중목적지 최적탐색2: 지나간 톨게이트3: 사용자정보5: 경유도로6: 유고회피7: 경로회피 13 : 교통정보 세부 설정
┣ routepoints
Array
다중목적지 리스트 (when headerType is 1)
더 불러오기
Response Parameter
parameter
type
description
result_code
String
결과 코드
result_msg
String
결과코드에 따른 메세지
distance
Integer
경로 길이(단위: M)
time
Integer
예상 소요 시간(단위: 초)
```

## 타임머신(시간예측)

```
타임머신(시간예측)
Function
타임머신(시간예측)
URL
/findStatRoute
Request Header
Request Parameter
parameter
type
requisite
description
searchOption
String
O
Agent 탐색 종류real_traffic : 빠르고
mrVersion
String
O
MR version
searchType
String
O
탐색종류7: 통계탐색
directivity
boolean
목적지 방향성 탐색true : 사용false : 사용안함(default)
rotate
boolean
회전규제 고려 탐색true : 사용false : 사용안함(default)
dual
boolean
경로선 이원화(가상 분리된 경로선)true : 사용false : 사용안함(default)
forced
boolean
도로상 통행 제한지점 강제통과true : 사용false : 사용안함(default)
startloc
Object
O
출발지 지점 정보
┣ lonx
String
O
출발지 경도, 정규화좌표 X값
┣ laty
String
O
출발지 위도, 정규화좌표 Y값
┣ pid
String
위치의 PID(startloc 에서는 PID 생략 가능)(Log)
┣ name
String
O
출발지 명칭
┣ mapid
String
O
출발지 도엽번호
┣ linkid
String
O
출발지 링크번호
┣ nodeid
String
O
출발지 노드번호
┣ direction
String
O
출발지 방향
┣ usingName
boolean
지점명칭 사용true : 사용(default)false : 사용안함
┣ usingHideViaLoc
boolean
숨김 경유지true : 사용false : 사용안함(default)
┣ viaLocStart
boolean
경유도로 시작/종료true : 사용false : 사용안함(default)
┗ viaLocEnd
boolean
경유도로 종료true : 사용false : 사용안함(default)
endloc
Object
O
도착지 지점 정보
┣ lonx
String
O
도착지 경도, 정규화좌표 X값
┣ laty
String
O
도착지 위도, 정규화좌표 Y값
┣ name
String
O
도착지 명칭
┣ pid
String
위치의 PID(endloc 에서는 PID 생략 가능)(Log)
┣ mapid
String
O
도착지 도엽번호
┣ linkid
String
O
도착지 링크번호
┣ nodeid
String
O
도착지 노드번호
┣ direction
String
O
도착지 방향
┣ usingName
boolean
지점명칭 사용true : 사용(default)false : 사용안함
┣ usingHideViaLoc
boolean
숨김 경유지true : 사용false : 사용안함(default)
┣ viaLocStart
boolean
경유도로 시작/종료true : 사용false : 사용안함(default)
┗ viaLocEnd
boolean
경유도로 종료true : 사용false : 사용안함(default)
vialocList
Array
경유지 지점 정보
┣ lonx
String
경유지 경도, 정규화좌표 X값
┣ laty
String
경유지 위도, 정규화좌표 Y값
┣ name
String
경유지 명칭
┣ pid
String
위치의 PID(vialocList 에서는 PID 생략 가능)(Log)
┣ mapid
String
경유지 도엽번호
┣ linkid
String
경유지 링크번호
┣ nodeid
String
경유지 노드번호
┣ direction
String
경유지 방향
┣ usingName
boolean
지점명칭 사용true : 사용(default)false : 사용안함
┣ usingHideViaLoc
boolean
숨김 경유지true : 사용false : 사용안함(default)
┣ viaLocStart
boolean
경유도로 시작/종료true : 사용false : 사용안함(default)
┗ viaLocEnd
boolean
경유도로 종료true : 사용false : 사용안함(default)
extensionList
Array
O
확장 리스트
┣ headerType
String
O
확장 리스트 타입1: 다중목적지 최적탐색2: 지나간 톨게이트3: 사용자정보4: 통계탐색5: 경유도로6: 유고회피7: 경로회피 13 : 교통정보 세부 설정
┣ routepoints
Array
다중목적지 리스트 (when headerType is 1)
┣ rpx
String
목적지 X좌표
더 불러오기
Response Parameter
parameter
type
description
result_code
String
결과 코드
result_msg
String
결과코드에 따른 메세지
time_count
Integer
예측시간 개수
time_list
Array
예측시간 리스트
┣ start_time
String
출발시간 (TimeStamp)
┗ end_time
String
도착시간 (TimeStamp)
```

## 경로 내 유고 정보

```
경로 내 유고 정보
Function
경로 내 유고 정보
URL
/routeRoadEvent
Request Header
Request Parameter
parameter
type
requisite
description
rid
String
O
경로 ID
version
String
O
Map version
Response Parameter
parameter
type
description
result_code
String
결과 코드
result_msg
String
결과코드에 따른 메세지
eventlist_cnt
Integer
유고정보 목록 개수
event_list
Array
유고정보 목록
┣ critical_rate
Integer
심각도 (0x00: 미확인)
┣ create_time
Integer
생성시간 – 메시지 생성시간(UTC)
┣ start_time
Integer
시작시간 – 이벤트 시작 시간(UTC)
┣ end_time
Integer
종료시간 – 이벤트 종료 시간(UTC)
┣ available_time
Integer
유효시간 (없을 경우 0x00)
┣ repeat_time
Integer
반복시간 (0~23 값을 사용, 없을 경우 0xff)
┣ repeat_minute
Integer
반복 분(0~9값을 사용, 없을 경우 0xff)
┣ day_of_week
Integer
요일정보 (월~일을 1bit단위로 셋팅)
┣ accident_count
Integer
사고건수 (사고가 아닌 경우 0x00)
┣ accident_vehicle_count
Integer
사고 차량 수 (사고가 아닌경우 0x00)
┣ speed_average
Integer
평균속도 (km/hour 속도) – 유형코드 5번 교통망 상태 이벤트에서 사용
┣ delay_time
Integer
지체시간 (초 단위) – 유형코드 5번 교통망 상태 이벤트에서 사용
┣ speed_limit
Integer
제한속도 (km/hour 속도) – 유형코드 5번 교통망 상태 이벤트에서 사용
┣ type_code
Integer
유고 유형코드
┣ accident_name
String
유고 정보 명칭
┣ interval
Integer
구간길이 (100m 단위의 길이)
┣ road_name
String
도로명
┣ road_interval_name
String
도로 구간명
┣ weather
Integer
날씨(TPEG RTM 29의 Code값)
┣ lane_info
Integer
차선정보 (TPEG RTM 테이블 10의 Code값)
┣ sight_distance
Integer
시야 거리(100m 단위)
┣ comment
String
부가 설명 (이벤트 설명)
┣ tpeg_link_id
Long
TPEG 링크 ID
┣ link_id_list
Array
영향 받는 링크 ID리스트
┗ link_id
String
영향 받는 링크 ID
┣ latitude
String
위도(WGS 84좌표, 10micro degree)
┣ longitude
String
경도(WGS 84좌표, 10micro degree)
┣ rtm_table_num
Integer
TPEG RTM Table 번호
┣ rtm_code_num
Integer
TPEG RTM Code 번호
┣ mrlinkinfo_list
Array
MR Link 목록
┣ mapid
Integer
Map ID
┗ linkid
Integer
Link ID
```

## 전체 유고 정보 조회

```
전체 유고 정보 조회
Function
전체 유고 정보 조회
URL
/fullRoadEvent
Request Header
Request Parameter
parameter
type
requisite
description
lutst
String
수신한 Last Update Time Stamp 값(기본값: 0)
version
String
O
Map version
Response Parameter
parameter
type
description
result_code
String
결과 코드
result_msg
String
결과코드에 따른 메세지
eventlist_cnt
Integer
유고정보 목록 개수
event_list
Array
유고정보 목록
┣ critical_rate
Integer
심각도 (0x00: 미확인)
┣ create_time
Integer
생성시간 – 메시지 생성시간(UTC)
┣ start_time
Integer
시작시간 – 이벤트 시작 시간(UTC)
┣ end_time
Integer
종료시간 – 이벤트 종료 시간(UTC)
┣ available_time
Integer
유효시간 (없을 경우 0x00)
┣ repeat_time
Integer
반복시간 (0~23 값을 사용, 없을 경우 0xff)
┣ repeat_minute
Integer
반복 분(0~9값을 사용, 없을 경우 0xff)
┣ day_of_week
Integer
요일정보 (월~일을 1bit단위로 셋팅)
┣ accident_count
Integer
사고건수 (사고가 아닌 경우 0x00)
┣ accident_vehicle_count
Integer
사고 차량 수 (사고가 아닌경우 0x00)
┣ speed_average
Integer
평균속도 (km/hour 속도) – 유형코드 5번 교통망 상태 이벤트에서 사용
┣ delay_time
Integer
지체시간 (초 단위) – 유형코드 5번 교통망 상태 이벤트에서 사용
┣ speed_limit
Integer
제한속도 (km/hour 속도) – 유형코드 5번 교통망 상태 이벤트에서 사용
┣ type_code
Integer
유고 유형코드
┣ accident_name
String
유고 정보 명칭
┣ interval
Integer
구간길이 (100m 단위의 길이)
┣ road_name
String
도로명
┣ road_interval_name
String
도로 구간명
┣ weather
Integer
날씨(TPEG RTM 29의 Code값)
┣ lane_info
Integer
차선정보 (TPEG RTM 테이블 10의 Code값)
┣ sight_distance
Integer
시야 거리(100m 단위)
┣ comment
String
부가 설명 (이벤트 설명)
┣ tpeg_link_id
Long
TPEG 링크 ID
┣ link_id_list
Array
영향 받는 링크 ID리스트
┗ link_id
String
영향 받는 링크 ID
┣ latitude
String
위도(WGS 84좌표, 10micro degree)
┣ longitude
String
경도(WGS 84좌표, 10micro degree)
┣ rtm_table_num
Integer
TPEG RTM Table 번호
┗ rtm_code_num
Integer
TPEG RTM Code 번호
```

## 경로 주변 부가 정보

```
경로 주변 부가 정보
Function
경로 주변 부가 정보
URL
/routeOtherInfo
Request Header
Request Parameter
parameter
type
requisite
description
rid
String
O
경로 ID
xpos
String
O
시작점 정규화 X 좌표
ypos
String
O
시작점 정규화 Y 좌표
cctvOn
Boolean
O
CCTV 정보true: 사용(default)false: 미사용
oilOn
Boolean
주유소 정보true: 사용(default)false: 미사용
evcOn
Boolean
전기차 중전소 정보true: 사용false: 미사용(default)
eventOn
Boolean
유고 정보true: 사용(default)false: 미사용
vvmsOn
Boolean
VVMS 정보true: 사용(default)false: 미사용
disasterOn
Boolean
재난 정보true: 사용(default)false: 미사용
disasterCarOn
Boolean
긴급출동 차량 위치 정보true: 사용(default)false: 미사용
category
Array
선호주유소 카테고리 코드 리스트
┗ val
String
Category CodeC0100 : 주유소(default)
oil
String
유종0:ALL (default)1:휘발유2:고급휘발유3:경유4:LPG
Response Parameter
parameter
type
description
result_code
String
결과 코드
result_msg
String
결과코드에 따른 메세지
cctv_cnt
Integer
CCTV 개수
cctv_list
Array
CCTV 리스트
┣ dpx
String
display X좌표(WGS84의 경우 longitude)
┣ dpy
String
display Y좌표(WGS84의 경우 latitude)
┣ mapid
String
맵 아이디
┣ linkid
String
링크 아이디
┣ direction
Integer
0 : 경로역방향, 1 : 경로 진행방향
┣ cctvdata
Object
CCTV 정보
┣ cctv_id
String
CCTV ID
┗ cctv_name
String
CCTV 명칭
oil_cnt
Integer
주유소 개수
oil_list
Array
주유소 리스트
┣ name1
String
정식명칭
┣ catecode
String
분류코드
┣ dpx
String
display X좌표(WGS84의 경우 longitude)
┣ dpy
String
display Y좌표(WGS84의 경우 latitude)
┣ mapid
String
맵 아이디
┣ linkid
String
링크 아이디
┣ direction
Integer
0 : 경로역방향, 1 : 경로 진행방향
┣ roadtype
String
도로타입
┗ oildata
Object
유가 데이터 정보
┣ g_price
Integer
휘발유 가격
┣ g_least
Integer
최저 휘발유 가격제공 Flag(0: 아님 1: 맞음)
┣ hg_price
Integer
고급휘발유 가격
┣ hg_least
Integer
최저 고급휘발유 가격제공 Flag(0: 아님 1: 맞음)
┣ d_price
Integer
경유 가격
┣ d_least
Integer
최저 경유 가격제공 Flag(0: 아님 1: 맞음)
┣ l_price
Integer
LPG 가격
┣ l_least
Integer
최저 LPG 가격제공 Flag(0: 아님 1: 맞음)
┗ updatetime
String
Update 시간
event_cnt
Integer
유고 개수
event_list
Array
유고 리스트
┣ dpx
String
display X좌표(WGS84의 경우 longitude)
┣ dpy
String
display Y좌표(WGS84의 경우 latitude)
┣ id
String
도로정보 id
┣ mapid
String
MAP ID
┣ linkid
String
LINK ID
┗ direction
Integer
0 : 경로역방향, 1 : 경로 진행방향
vvms_cnt
Integer
VVMS 개수
vvms_list
Array
VVMS 리스트
┣ dpx
String
display X좌표(WGS84의 경우 longitude)
┣ dpy
String
display Y좌표(WGS84의 경우 latitude)
┣ id
String
도로정보 id
┣ mapid
String
MAP ID
┣ linkid
String
LINK ID
┗ direction
Integer
0 : 경로역방향, 1 : 경로 진행방향
disaster_cnt
Integer
재난정보 개수
disaster_list
Array
재난정보 리스트
더 불러오기
```

## 대중교통 요약 길찾기

```
대중교통 요약 길찾기
Function
대중교통 요약 길찾기
URL
/summaryPath
Request Header
Request Parameter
parameter
type
requisite
description
list
Array
확장 리스트
┣ startPos
Object
출발지 정보
┣ dPosX
Double
출발지 좌표 X
┣ dPosY
Double
출발지 좌표 Y
┗ name
String
출발지 명칭
┣ endPos
Object
도착지 정보 (재탐색시 사용)
┣ dPosX
Double
도착지 좌표 X
┣ dPosY
Double
도착지 좌표 Y
┗ name
String
도착지 명칭(최근검색에서 사용)
┗ coordType
Integer
request/response 좌표 타입GEOGRAPHIC = 0(wgs84 고정값 0으로 채워보내시면됨)
Response Parameter
parameter
type
description
result_code
String
결과 코드
result_msg
String
결과코드에 따른 메세지
list
Array
출발지 정보(요청때 보낸 순서대로 리스트 정렬)
┣ huResult
Integer
휴빌론으로부터온 응답값(좌표체계 및 좌표값틀릴경우 정상으로안주는 케이스 존재)0 : 정상30 : 대중교통 서버의 서비스 지역이 아닙니다(아래값들 0으로 채워짐)1 : 비정상(비정상일경우 아래 값들 0으로 채워짐)
┣ routeArea
Integer
0 : 도시 내1 : 도시 간
┣ routeOpt
Integer
결과 수단별 타입(0:도보, 1:지하철, 2:버스, 3:버스+지하철, 4:기차, 5:고속버스, 6:항공, 7:시외버스)
┣ totalTime
Integer
총 소요시간 (분)
┗ totalDistance
Integer
전체 거리 (m)
```

## 탐색 유고정보 조회

```
탐색 유고정보 조회
Function
탐색 유고정보 조회
URL
/routingEvent
Request Header
Request Parameter
parameter
type
requisite
description
type
Integer
O
요청 타입0 : 전체 1 : 특정 링크
mrVersion
String
O
MR version
routeEveneList
List
O
※ 요청 타입이 1인 경우에만 존재
┣ mapid
Short
O
MAP ID
┣ linkid
Short
O
LINK ID
┗ direction
Short
O
Direction※ 0 : 정 1: 역
Response Parameter
parameter
type
description
result_code
String
결과 코드
result_msg
String
결과코드에 따른 메세지
request_type
Integer
요청 타입
info_count
Integer
유고정보 개수
link_count
Integer
요청링크 개수
resultLink_data
Object
요청링크 매칭 정보※ 요청 타입이 1인 경우에만 존재
┣ mapid
String
MAP ID
┣ linkid
String
LINK ID
┣ direction
String
Direction※ 0 : 정 1: 역
┣ existence
String
유고 존재 유무※ 0 : 없음 1: 있음
┗ seiral_number
String
유고 고유 번호
resultInfo_data
Object
유고 정보
┣ type
String
유고 타입
┣ seiral_number
String
유고 고유 번호
┣ start_date
String
시작시간(Timestamp - GMT)
┣ end_date
String
종료시간(Timestamp - GMT)
┣ latitude
String
경도좌표
┣ longitude
String
위도좌표
┣ roadname
String
도로명
┣ subject
String
제목
┣ detail_content
String
상세 설명
┣ preparing_person
String
작성자
┣ regulate_flag
String
통제유뮤0 : 통제없음 1 : 전면통제 2: 부분통제
┣ regulate_day
String
통제요일start_date ... end_date 기간 중 부분 통제 요일※ regulate_flag 가 부분통제일 경우에만 존재
┣ regulate_hour
String
통제시작 시간start_date ... end_date 기간 중 부분 통제 요일 중 통제 시작 시간※ regulate_flag 가 부분통제일 경우에만 존재
┣ regulate_time
String
통제시간(분)regulate_hour 시간으로 부터 regulate_tim(분)만큼 통제※ regulate_flag 가 부분통제일 경우에만 존재
┣ addtion_info
String
부가정보 (속도)전면통제가 아닌 경우의 링크 속도※ 전면통제의 경우 : 255(고정값)
┣ affect_count
String
Affect 링크 개수
┗ affect_list
List
Affect 링크 #0 ... #N※ Affrect 링크 개수만큼 존재
```


# 2. 검색

## 구 주소 검색

```
구 주소 검색
Function
구 주소 검색
URL
/sire/searchOldAddr
Request Header
Request Parameter
parameter
type
requisite
description
cutflag
String
O
주소표현구분0 : 정식행정계 주소1 : 단축행정계 주소
coordtype
String
O
좌표형식0 : 정규화 좌표1 : WGS 842 : TM
startposition
String
O
시작위치0 : 첫번째 위치ex) 20 -> 21번째 결과부터 reqcount 만큼 조회
reqcount
String
O
요청개수
option
String
O
검색 option0 : admcode + jibun1 : addr + jibun
addr
String
행정명칭 (ex: 서울 서초구 양재동)
admcode
String
행정계 코드 (ex: 1165010200)
jibun
String
O
지번 (ex: 650)
mode
String
O
검색 mode1 : 법정동 우선 검색, 결과 없을 경우 행정동 검색2 : 법정동 검색 (행정동 검색 안함)3 : 법정동, 행정동 모두 검색
xpos
String
O
현재위치 x좌표
ypos
String
O
현재위치 y좌표
Response Parameter
parameter
type
description
result_code
String
결과 코드
result_msg
String
결과코드에 따른 메세지
totalcount
Integer
전체 검색결과 대상 개수
count
Integer
검색 결과 개수
adm
Array
주소검색결과 List
┣ posx
String
행정계 X좌표 (WGS84의 경우 longitude)
┣ posy
String
행정계 Y좌표 (WGS84의 경우 latitude)
┣ jposx
String
지번 X좌표 (WGS84의 경우 longitude)
┣ jposy
String
지번 Y좌표 (WGS84의 경우 latitude)
┣ accuracy
Integer
지번 정확도0 : 정확 검색1 : 호지번 확장2 : 모지번 확장3 : 행정계
┣ admtype
String
L : 법정동, A : 행정동
┣ admcode
String
행정코드
┣ address
String
주소
┣ jibun
String
지번
┣ roadname
String
새주소 도로명
┣ roadjibun
String
새주소 지번
┗ distance
Integer
거리
행정계 검색이 되었는데 좌표가 존재 하지 않는 경우 해당 행정계와 매칭되는 법정동의 좌표를 준다.
```

## 새 주소 검색

```
새 주소 검색
Function
새 주소 검색
URL
Request Header
Request Parameter
parameter
type
requisite
description
cutflag
String
O
주소표현구분0 : 정식행정계 주소1 : 단축행정계 주소
coordtype
String
O
좌표형식0 : 정규화 좌표1 : WGS 842 : TM
startposition
String
O
시작위치0 : 첫번째 위치ex) 20 -> 21번째 결과부터 reqcount 만큼 조회
reqcount
String
O
요청개수
option
String
O
검색 option1 : admcode + addr (ex: 26 + 진달래길(도로명 입력))2 : 새주소 명칭 (ex: 부산 진달래길)
addr
String
△
새 주소명(ex: 부산 진달래길 or 진달래길)
admcode
String
△
행정계 코드(ex: 26)
jibun
String
△
지번 (건물번호)ex) 3 (지번 검색하고 싶으면 입력, 없으면 주소검색만)
xpos
String
O
현재위치 x좌표
ypos
String
O
현재위치 y좌표
Response Parameter
parameter
type
description
result_code
String
결과 코드
result_msg
String
결과코드에 따른 메세지
totalcount
Integer
전체 검색결과 대상 개수
count
Integer
검색 결과 개수
adm
Array
주소검색결과 List
┣ posx
String
행정계 X좌표 (WGS84의 경우 longitude)
┣ posy
String
행정계 Y좌표 (WGS84의 경우 latitude)
┣ accuracy
Integer
지번 정확도0 : 정확 검색1 : 호지번 확장2 : 모지번 확장3 : 행정계
┣ admcode
String
행정코드
┣ address
String
주소
┣ jibun
String
지번
┣ roadname
String
새주소 도로명
┣ roadjibun
String
새주소 지번
┗ distance
Integer
거리
```

## 좌표로 주소 검색

```
좌표로 주소 검색
Function
좌표로 주소 검색
URL
/sire/revgeocoding
Request Header
Request Parameter
parameter
type
requisite
description
cutflag
String
O
주소표현구분0 : 정식행정계 주소1 : 단축행정계 주소
coordtype
String
O
좌표형식
0 : 정규화 좌표
startposition
String
O
시작위치0 : 첫번째 위치ex) 20 -> 21번째 결과부터 reqcount 만큼 조회
reqcount
String
O
요청개수
posx
String
O
X좌표
posy
String
O
Y좌표
w3wYn
String
W3W 연동 여부 (Default : N)
Y : 연동
N : 미 연동
Response Parameter
parameter
type
description
result_code
String
결과 코드
result_msg
String
결과코드에 따른 메세지
admcode
String
행정코드
x
String
X좌표 (WGS84의 경우 longitude)
y
String
Y좌표 (WGS84의 경우 latitude)
address
String
주소
cut_address
String
축약 주소
road_address
String
도로명 주소
cut_road_address
String
축약 도로명 주소
jibun
String
지번
bldnum
String
빌딩번호
address_type
String
주소 매핑 타입0 : 행정계1 : 새주소 폴리곤2 : 지적도 폴리곤3 : 인접지번4 : 행정계
w3wWords
String
w3w 단어 (미존재 케이스의 경우 “”)
```

## 하위 행정계 검색

```
하위 행정계 검색
Function
하위 행정계 검색
URL
/sire/searchSubAddr
Request Header
Request Parameter
parameter
type
requisite
description
cutflag
String
O
주소표현구분0 : 정식행정계 주소1 : 단축행정계 주소
coordtype
String
O
좌표형식0 : 정규화 좌표1 : WGS 842 : TM
option
String
O
검색 option1 : 행정 코드로 검색2 : 주소로 검색3 : 행정코드 -> 주소변환
startposition
String
O
무조건 0입력
reqcount
String
O
무조건 0입력
addr
String
△
주소명칭 (option 값이 2인경우)
admcode
String
△
행정계 코드 (option 값이 1, 3인경우)
Response Parameter
parameter
type
description
result_code
String
결과 코드
result_msg
String
결과코드에 따른 메세지
totalcount
Integer
전체 검색결과 대상 개수
count
Integer
검색 결과 개수
adm
Array
주소검색결과 List
┣ posx
String
X좌표 (WGS84의 경우 longitude)
┣ posy
String
Y좌표 (WGS84의 경우 latitude)
┣ admname
String
행정명
┣ admcode
String
행정코드
┣ address
String
주소
┗ hassub
Boolean
하위 행정계 존재여부
query에 "" 혹은 0을 입력하면 광역시도의 정보 조회
결과로 리턴+된 admcode를 사용하여 하위행정계 조회하여야 함
admcode : 광역시도 (2자리) 시,군,구(5자리), 읍면동(8자리) 리(10자리)
```

## 하위 행정계 도로명 검색

```
하위 행정계 도로명 검색
Function
하위 행정계 도로명 검색
URL
/sire/searchSubAddrRoadName
Request Header
Request Parameter
parameter
type
requisite
description
cutflag
String
O
주소표현구분0 : 정식행정계 주소1 : 단축행정계 주소
coordtype
String
O
좌표형식0 : 정규화 좌표1 : WGS 842 : TM
startposition
String
O
시작위치0 : 첫번째 위치ex) 20 -> 21번째 결과부터 reqcount 만큼 조회
reqcount
String
O
요청개수
admcode
String
O
행정코드ex) 11650 (구코드 5자리 입력) 세종시는 구가 없음으로 36두자리로
Response Parameter
parameter
type
description
result_code
String
결과 코드
result_msg
String
결과코드에 따른 메세지
totalcount
Integer
전체 검색결과 대상 개수
count
Integer
검색 결과 개수
road
Array
Road검색결과 List
┣ cid
Integer
도로명코드
┗ roadname
String
새주소 도로명
```

## POI 명칭 검색

```
POI 명칭 검색
Function
POI 명칭 검색
URL
/sire/searchPoiNumber
Request Header
Response Parameter
parameter
type
description
result_code
String
결과 코드
result_msg
String
결과코드에 따른 메세지
totalcount
Integer
전체 검색결과 대상 개수
count
Integer
검색 결과 개수
poitotalcount
Integer
Thinkware POI 전체 검색결과 대상 개수
poicount
Integer
Thinkware POI 검색 결과 개수
tel_poitotalcount
Integer
Tel POI 전체 검색결과 대상 개수
tel_poicount
Integer
Tel POI 검색 결과 개수
ucp_poitotalcount
Integer
User POI 전체 검색결과 대상 개수
ucp_poicount
Integer
User POI 검색 결과 개수
poi
Array
POI 검색결과 List 📙
POI_DATA_A
tel
Array
Tel POI 검색결과 List 📙
POI_DATA_A
ucp
Array
User POI 검색결과 List 📙
POI_DATA_A
POI_DATA_A
```

## SQE 통합검색

```
SQE 통합검색
Function
SQE 통합검색
URL
/sire/searchSQE
Request Header
Request Parameter
parameter
type
requisite
description
cutflag
String
O
주소표현구분0 : 정식행정계 주소1 : 단축행정계 주소
coordtype
String
O
좌표형식0 : 정규화 좌표1 : WGS 842 : TM
startposition
String
O
시작위치0 : 첫번째 위치ex) 20 -> 21번째 결과부터 reqcount 만큼 조회
reqcount
String
O
요청개수
depth
String
O
하위시설물 요구 depth0 : depth 사용 안함(검색결과 모두 표출) (Default)1 : 1 depth 만 요청(최상위 depth)2 : 2 depth 까지 요청3 : 3 depth 까지 요청
mode
String
O
검색 mode1 : poi 검색2 : adm 검색3 : poi+adm 검색 (Default)4 : poi+adm+tel+ucp 검색5 : tel db 검색6 : ucp 검색7 : poi+tel+adm 검색 (poi, tel 검색결과 Universal 제공)
query
String
O
검색어
subString
String
자동완성어 사용시에 사용자가 입력한 부분(ex : '주'를 입력한 이후 '주유소' 선택시, '주'가 subString)자동완성어/추천어재검색시에만 사용됨추천어재검색시에는 검색실패한 검색어가 subString이 됨AI연동시에는 uword(AI엔진이 인식한 단어) 가 subString이됨
autoSearchFlag
String
자동완성어 사용여부 flagY : 사용N : 미사용
spopt
String
O
공간검색 option0 : 공간검색 사용 안함 (Default)1 : Extent 검색2 : Range 검색3 : K-NN 검색 (x1, y1만 사용함) – 추후 지원 예정
radius
String
반경spopt가 2인 경우 사용 (Meter 단위)
admcode
String
행정코드행정코드 조건 검색
x1
String
X좌표spopt가 0인 경우 기준점 X좌표spopt가 1인 경우 Extent의 좌상단 X좌표spopt가 2,3인 경우 기준점 X좌표※ Range검색 및 K-NN의 경우 반드시 필요
y1
String
Y좌표spopt가 0인 경우 기준점 Y좌표spopt가 1인 경우 Extent의 좌상단 Y좌표spopt가 2,3인 경우 기준점 Y좌표※ Range검색 및 K-NN의 경우 반드시 필요
x2
String
X좌표spopt가 1인 경우 Extent의 우하단 X좌표spopt가 2,3인 경우 사용 안함
y2
String
Y좌표spopt가 1인 경우 Extent의 우하단 Y좌표spopt가 2,3인 경우 사용 안함
sortopt
String
O
정렬 option1 : 명칭순 정렬2 : 거리순 정렬 (좌표를 입력한 경우)3 : 이름매치 -> 거리순 정렬 (좌표를 입력한 경우)4 : 검색어 Weight 정렬 (엔진기준) (Default)5 : 검색어 Weight 정렬 + length (엔진기준)6 : 선호카테고리 우선 정렬7 : 최신데이터 순 정렬
favcatecode
String
선호카테고리선호카테고리 분류 코드(대/중/소 입력 가능)
neighboropt
String
주변검색 결과표현 option0 : Reference 정보 - 주변POI를 하위시설물 형태 depth로 표현(Default)- 각 Reference 당 검색되는 POI의 개수는 최대 20개로 제한1 : Reference정보+최상위 Reference의 검색결과 제공- Reference정보는 queryParse 파트로 제공- 검색결과는 poi 파트로 제공- Reference검색 결과인 경우 queryParse부분과 count정보등만 제공함(여러 개의 Reference가 검색되는 경우 queryParse 파트의 첫번째 Reference에 대한 검색결과를 제공한다)
sortoilprice
String
주유소 검색결과 유가순 정렬 option0 : 유가순 정렬 Option 사용안함 (Default)1 : 휘발유순 정렬2 : 고급휘발유순 정렬3 : 경유순 정렬4 : LPG 가격순
sflag
String
O
음성검색 구분 flagV : 음성T : 타이핑L : 최근검색어A : AI검색N : 구분안됨
searchType
String
O
통합검색/최근검색어/추천어재검색/위치주변통합검색/에어봇검색 {UNITED: 통합검색, RECENT: 최근검색어, SGST: 추천어재검색, NEARBY: 위치주변 통합검색, AIRBOT: 에어봇검색}
evcstatus
String
0 : 전기차 충전소 충전 가능 여부 Filter Option 사용안함(default)1 : 사용중2 : 사용 가능3 : 사용 불가
evctype
Array
전기차 충전소 충전 타입 필터 리스트
┗ val
String
0 : 전기차 충전소 충전 타입 여부 Filter Option 사용안함(default)1 : DC차데모2 : AC완속3 : DC콤보4 : AC급속3상
sortevcprice
String
0: 전기차 충전소 가격순 정렬 Option 사용안함(default)1: 가격순 정렬
Response Parameter
parameter
type
description
result_code
String
결과 코드
result_msg
String
결과코드에 따른 메세지
provider
String
검색결과 제공처SIRE: 검색엔진NAVER: 네이버
type
Integer
0 : 일반검색, 1 : Reference검색
totalcount
Integer
전체 검색결과 대상 개수
count
Integer
검색 결과 개수
poitotalcount
Integer
Thinkware POI 전체 검색결과 대상 개수
poicount
Integer
Thinkware POI 검색 결과 개수
tel_poitotalcount
Integer
Tel POI 전체 검색결과 대상 개수
tel_poicount
Integer
Tel POI 검색 결과 개수
ucp_poitotalcount
Integer
User POI 전체 검색결과 대상 개수
ucp_poicount
Integer
User POI 검색 결과 개수
admtotalcount
Integer
adm 전체 검색결과 대상 개수
admcount
Integer
adm 검색 결과 개수
reftotalcount
Integer
ref 전체 검색결과 대상 개수
refcount
Integer
ref 검색 결과 개수
recommandQuery
String
검색결과가 없는 경우 오타보정 결과 제공(NULL가능)
res_type
String
검색 결과 Type명칭, 카테고리, 주소, 전화번호 순(ex) NYNN: 명칭 No, 카테고리 YES, 주소 NO, 전화번호 NO
poi
Array
POI 검색결과 List📙
POI_DATA_A
tel
Array
Tel POI 검색결과 List📙
POI_DATA_A
ucp
Array
User POI 검색결과 List📙
POI_DATA_A
npoi
Array
NAVER POI 검색결과 List(provider가 NAVER일 경우만 존재)
┣ dpx
String
display X좌표(WGS84의 경우 longitude)
┣ dpy
String
display Y좌표(WGS84의 경우 latitude)
┣ routepoints
Array
탐색용 좌표 리스트
┣ rpx
String
탐색 X좌표(WGS84의 경우 longitude)
┗ rpy
String
탐색 Y좌표(WGS84의 경우 latitude)
┣ rpx
String
탐색 X좌표(WGS84의 경우 longitude)
┣ rpy
String
탐색 Y좌표(WGS84의 경우 latitude)
┣ name1
String
정식명칭
┣ address
String
주소
┣ roadname
String
새주소 도로명
┣ distance
Integer
좌표와의 거리 (해당시에만)
┗ tel
String
전화번호
adm
Array
ADM 검색결과 List
┣ type
String
검색 type
┣ posx
String
X좌표(WGS84의 경우 longitude)
┣ posy
String
Y좌표(WGS84의 경우 latitude)
┣ admcode
String
행정코드
┣ address
String
주소
┣ jibun
String
지번
┣ roadname
String
새주소 도로명
┣ roadjibun
String
새주소 지번
┣ accuracy
Integer
지번 정확도0 : 정확 검색1 : 호지번 확장2 : 모지번 확장
┗ distance
Integer
거리
queryParse
Object
Reference 검색이면서 neighboropt=1인 경우 제공됨
┣ ref
Array
reference 정보
┣ type
Integer
Reference Type(0 : POI, 1 : 구주소, 2 : 새주소, 3 : 가로명, 4 : 행정계, 5 : 현위치)
┣ id
Integer
Reference ID
┣ name
String
Reference 명칭
더 불러오기
```

## POI 상세정보 조회

```
POI 상세정보 조회
Function
POI 상세정보 조회
URL
/sire/searchPoiDetail
Request Header
Request Parameter
parameter
type
requisite
description
cutflag
String
O
주소표현구분0 : 정식행정계 주소1 : 단축행정계 주소
coordtype
String
O
좌표형식
0 : 정규화 좌표
startposition
String
O
시작위치0 : 첫번째 위치ex) 20 -> 21번째 결과부터 reqcount 만큼 조회
reqcount
String
O
요청개수
poiid
String
O
poi id구분자 "│"와 함께 입력 (복수개 가능 186개까지)ex) poiid=123│1234│234
simpleRes
String
O
멀티 입구점 결과만 받음. Y/N
w3wYn
String
W3W 연동 여부 (Default : N)
Y : 연동
N : 미 연동
Response Parameter
parameter
type
description
result_code
String
결과 코드
result_msg
String
결과코드에 따른 메세지
totalcount
Integer
POI 전체 검색결과 대상 개수
count
Integer
POI 검색 결과 개수
poiinfo
Array
POI 검색결과 List
┣ poiid
Integer
poi idsimpleRes가 Y인 경우 해당 결과만 반환 됨
┣ dpx
String
display X좌표(WGS84의 경우 longitude)
┣ dpy
String
display Y좌표(WGS84의 경우 latitude)
┣ rpx
String
탐색 X좌표(WGS84의 경우 longitude)
┣ rpy
String
탐색 Y좌표(WGS84의 경우 latitude)
┣ routepoints
Array
탐색용 좌표 리스트simpleRes가 Y인 경우 해당 결과만 반환 됨
┣ rpx
String
탐색 X좌표(WGS84의 경우 longitude)
┗ rpy
String
탐색 Y좌표(WGS84의 경우 latitude)
┣ name1
String
정식명칭
┣ name2
String
축약명칭
┣ name3
String
확장명칭1
┣ name4
String
확장명칭2
┣ admcode
String
행정코드
┣ address
String
주소
┣ jibun
String
지번
┣ roadname
String
새주소 도로명
┣ roadjibun
String
새주소 지번
┣ detailaddress
String
상세주소
┣ catecode
String
분류코드
┣ catename
String
분류명칭
┣ dp_catecode
String
DP 분류코드
┣ fulladdress
String
전체주소(행정주소+지번+상세주소)
┣ zip
String
우편번호
┣ homepage
String
홈페이지 url
┣ email
String
E-MAIL
┣ howtogo
String
교통편
┣ tel1
String
전화번호1
┣ tel2
String
전화번호2
┣ fax1
String
팩스번호1
┣ fax2
String
팩스번호2
┣ icode
String
ICODE
┣ badgeflag
Boolean
Badge 유무
┣ imagecount
Integer
poi 이미지 개수
┣ operation_value
String
영업시간
┣ closing_flag
Boolean
당일 휴무일 여부
┣ parking_value
String
주차정보
┣ etc_count
Integer
분류기타항목갯수
┣ etcinfo
Array
분류기타항목
┣ name
String
분류기타항목설명
┗ value
String
분류기타항목내용
┣ hasoildata
Boolean
유가 데이터 존재여부
┣ oildata
object
유가 데이터 정보
┣ g_price
Integer
휘발유 가격
┣ hg_price
Integer
고급휘발유 가격
┣ d_price
Integer
경유 가격
더 불러오기
```

## 주변 POI 검색

```
주변 POI 검색
Function
주변 POI 검색
URL
/sire/searchPoiAround
Request Header
Request Parameter
parameter
type
requisite
description
cutflag
String
O
주소표현구분0 : 정식행정계 주소1 : 단축행정계 주소
autoFlag
String
자동검색/수동검색 여부A : 자동M : 수동I: AI
coordtype
String
O
좌표형식0 : 정규화 좌표1 : WGS 842 : TM
startposition
String
O
시작위치0 : 첫번째 위치ex) 20 -> 21번째 결과부터 reqcount 만큼 조회
reqcount
String
O
요청개수
depth
String
O
하위시설물 요구 depth0 : depth 사용 안함(검색결과 모두 표출)1 : 1 depth 만 요청(최상위 depth)2 : 2 depth 까지 요청3 : 3 depth 까지 요청
catecode
String
O
Category Code
spopt
String
O
공간검색 option1 : Extent 검색2 : Range 검색3 : K-NN 검색 – 추후 지원 예정4 : Grade 정렬- 정렬 옵션이 유가(휘발유/고급휘발유/경유/LPG)인 경우 거리순 Grade부여.정렬 옵션이 평점순 정렬(망고플레이트)인 경우 평점순 Grade부여.이후 Grade내는 정렬옵션 순 재정렬. 단 Range검색입력 해야 함
windowsize
String
Grade당 POI개수(Fetch Count의 N배)- Grade정렬 옵션에서만 적용 됨.N >= 0인 자연수이며, 0 경우 1과 같이 동작. 파라메터 없는 경우 1로 동작N >= 1인 경우 Fetch * N개수 단위로 grade내 Max POI지정 함.
x1
String
X좌표spopt가 1인 경우 Extent의 좌상단 X좌표spopt가 2,3인 경우 기준점 X좌표
y1
String
Y좌표spopt가 1인 경우 Extent의 좌상단 Y좌표spopt가 2,3인 경우 기준점 Y좌표
x2
String
X좌표spopt가 1인 경우 Extent의 우하단 X좌표spopt가 2,3인 경우 사용 안함
y2
String
Y좌표spopt가 1인 경우 Extent의 우하단 Y좌표spopt가 2,3인 경우 사용 안함
radius
String
반경spopt가 2인 경우 사용 (Meter 단위)
sortopt
String
정렬 option1 : 거리순 (Default)2 : 명칭순3 : 휘발유 가격순 (주유소 검색시)4 : 고급휘발유 가격순 (주유소 검색시)5 : 경유 가격순 (주유소 검색시)6 : LPG 가격순 (주유소 검색시)7 : 망고플레이트 평점순
evcstatus
String
0 : 전기차 충전소 충전 가능 여부 Filter Option 사용안함(default)1 : 사용중2 : 사용 가능3 : 사용 불가
evctype
Array
전기차 충전소 충전 타입 필터 리스트
┗ val
String
0 : 전기차 충전소 충전 타입 여부 Filter Option 사용안함(default)1 : DC차데모2 : AC완속3 : DC콤보4 : AC급속3상
sortevcprice
String
0: 전기차 충전소 가격순 정렬 Option 사용안함(default)1: 가격순 정렬
Response Parameter
parameter
type
description
결과 없음
더 불러오기
```

## POI 하위시설물 조회

```
POI 하위시설물 조회
Function
POI 하위시설물 조회
URL
/sire/searchSubpoi
Request Header
Request Parameter
parameter
type
requisite
description
cutflag
String
O
주소표현구분0 : 정식행정계 주소1 : 단축행정계 주소
coordtype
String
O
좌표형식0 : 정규화 좌표1 : WGS 842 : TM
startposition
String
O
시작위치0 : 첫번째 위치ex) 20 -> 21번째 결과부터 reqcount 만큼 조회
reqcount
String
O
요청개수
poiid
String
O
POI ID (복수개 지원 안됨)
x1
String
현위치 또는 지도중심좌표. x, y좌표가 모두 NULL또는 0일 경우 거리 계산을 수행하지 않음.
y1
String
현위치 또는 지도중심좌표. x, y좌표가 모두 NULL또는 0일 경우 거리 계산을 수행하지 않음.
Request Parameter
parameter
type
description
result_code
String
결과 코드
result_msg
String
결과코드에 따른 메세지
totalcount
Integer
POI 전체 검색결과 대상 개수
count
Integer
POI 검색 결과 개수
poi
Array
POI 검색결과 List 📙
POI_DATA_B
POI_DATA_B
```

## Reference 주변 검색

```
Reference 주변 검색
Function
Reference 주변 검색
URL
/sire/searchReference
Request Header
Request Parameter
parameter
type
requisite
description
cutflag
String
O
주소표현구분0 : 정식행정계 주소1 : 단축행정계 주소
coordtype
String
O
좌표형식0 : 정규화 좌표1 : WGS 842 : TM
startposition
String
O
시작위치0 : 첫번째 위치ex) 20 -> 21번째 결과부터 reqcount 만큼 조회
reqcount
String
O
요청개수
depth
String
O
하위시설물 요구 depth0 : depth 사용 안함(검색결과 모두 표출) (Default)1 : 1 depth 만 요청(최상위 depth)2 : 2 depth 까지 요청3 : 3 depth 까지 요청
type
String
O
reference type0 : POI1 : 구주소2 : 새주소3 : 가로명4 : 행정계5 : 현위치
id
String
reference id (type=3인경우 필수입력)
posx
String
O
reference x좌표 (reference posx)
posy
String
O
reference y좌표 (reference posy)
admcode
String
referece admcode
keyword
String
△
검색 - 명칭 (검색어 - 명칭부분), catecode값이 없는 경우 필수
catecode
String
△
검색 - 분류코드 (검색어 - 분류코드), keyword값이 없는 경우 필수
radius
String
O
검색반경 (meter 단위)
curx
String
O
Reference검색의 경우 현위치 X좌표
cury
String
O
Reference검색의 경우 현위치 Y좌표
sortopt
String
정렬option1 : 명칭순 정렬2 : 거리순 정렬3 : 이름매치->거리순 정렬4 : 검색어 Weight 정렬 (엔진기준)(Default)5 : 검색어 Weight 정렬 + length(엔진기준)
sortoilprice
String
주유소 검색결과 유가순 정렬 option0 : 유가순 정렬 Option 사용안함 (Default)1 : 휘발유순 정렬2 : 고급휘발유순 정렬3 : 경유순 정렬4 : LPG 가격순
evcstatus
String
0 : 전기차 충전소 충전 가능 여부 Filter Option 사용안함(default)1 : 사용중2 : 사용 가능3 : 사용 불가
evctype
Array
전기차 충전소 충전 타입 필터 리스트
┗ val
String
0 : 전기차 충전소 충전 타입 여부 Filter Option 사용안함(default)1 : DC차데모2 : AC완속3 : DC콤보4 : AC급속3상
sortevcprice
String
0: 전기차 충전소 가격순 정렬 Option 사용안함(default)1: 가격순 정렬
Response Parameter
parameter
type
description
결과 없음
```

## 추천어 검색

```
추천어 검색
Function
추천어 검색
URL
/sire/searchProposer
Request Header
Request Parameter
parameter
type
requisite
description
query
String
O
검색어한글/영문/숫자 50Byte(한글 25자)
Response Parameter
parameter
type
description
result_code
String
결과 코드
result_msg
String
결과코드에 따른 메세지
count
Integer
추천 검색어 검색 결과 개수
keyword
Array
추천 검색어 결과 List
┣ keyword
String
검색어
┗ frequency
Integer
조회 빈도
```

## 경로 주변 다중 카테고리 검색

```
경로 주변 다중 카테고리 검색
Function
경로 주변 다중 카테고리 검색
URL
/sire/searchRouteAroundMulti
Request Header
Request Parameter
parameter
type
requisite
description
cutflag
String
O
주소표현구분0 : 정식행정계 주소1 : 단축행정계 주소
autoFlag
String
자동검색/수동검색 여부A : 자동M : 수동I : AI
coordtype
String
O
좌표형식0 : 정규화 좌표1 : WGS 842 : TM
startposition
String
O
시작위치0 : 첫번째 위치ex) 20 -> 21번째 결과부터 reqcount 만큼 조회
reqcount
String
O
요청개수
xpos
String
O
시작점 X 좌표
ypos
String
O
시작점 Y 좌표
category
Array
O
카테고리 코드 리스트
┗ val
String
O
Category Code
rid
String
O
경로 ID
sort
String
O
정렬0 : 거리순 (default)1 : 휘발유2 : 고급휘발유3 : 경유4 : LPG5 : 명칭순6 : PoiWeight7 : 망고플레이트 평점
direction
String
O
경로방향0:경로역방향1:경로정방향2:양방향 (default)
oil
String
유종0:ALL (default)1:휘발유2:고급휘발유3:경유4:LPG
distance
String
경로와 경로의 직교상 POI간의 유효거리 제한값0:default(서버내 정의값)10000보다 크면 default 값으로 설정함
evcstatus
String
0 : 전기차 충전소 충전 가능 여부 Filter Option 사용안함(default)1 : 사용중2 : 사용 가능3 : 사용 불가
evctype
Array
전기차 충전소 충전 타입 필터 리스트
┗ val
String
0 : 전기차 충전소 충전 타입 여부 Filter Option 사용안함(default)1 : DC차데모2 : AC완속3 : DC콤보4 : AC급속3상
sortevcprice
String
0: 전기차 충전소 가격순 정렬 Option 사용안함(default)1: 가격순 정렬
Response Parameter
parameter
type
description
결과 없음
경로 주변 POI 정보
```

## 교통정보 요약맵 검색

```
교통정보 요약맵 검색
Function
교통정보 요약맵 검색
URL
/sire/searchTism
Request Header
Request Parameter
parameter
type
requisite
description
code
String
코드명"depth1│depth2│depth3""고속도로│노선별고속도로│울산포항고속도로""수도권│고속도로│강남순환도시고속도로"code가 NULL: depth1 리스트 제공code가 2자리: code에 일치한 depth1 하위 리스트 제공code가 4자리: code에 일치한 depth2 하위 리스트 제공code가 7자리: code에 일치한 depth3 제공
Response Parameter
parameter
type
description
result_code
String
결과 코드
result_msg
String
결과코드에 따른 메세지
total_count
Integer
요약맵 검색 결과 개수
map_list
Array
요약맵 검색 결과 리스트
┣ name
String
요약맵 명칭
┣ image_id
String
이미지 ID(3-depth에서만 제공 / 1,2-depth는 NULL 리턴)
┣ depth
Integer
depth 분류 단계(1~3)
┣ code
String
code 명
┣ x1
String
Extent X1(3-depth에서만 제공 / 1,2-depth는 NULL 리턴)
┣ y1
String
Extent Y1(3-depth에서만 제공 / 1,2-depth는 NULL 리턴)
┣ x2
String
Extent X2(3-depth에서만 제공 / 1,2-depth는 NULL 리턴)
┣ y2
String
Extent Y2(3-depth에서만 제공 / 1,2-depth는 NULL 리턴)
┣ x3
String
Extent X3(3-depth에서만 제공 / 1,2-depth는 NULL 리턴)
┣ y3
String
Extent Y3(3-depth에서만 제공 / 1,2-depth는 NULL 리턴)
┣ x4
String
Extent X4(3-depth에서만 제공 / 1,2-depth는 NULL 리턴)
┣ y4
String
Extent Y4(3-depth에서만 제공 / 1,2-depth는 NULL 리턴)
┗ length
Integer
도로 길이
```

## CCTV용 고속도로 검색

```
CCTV용 고속도로 검색
Function
CCTV용 고속도로 검색
URL
/sire/searchRoad
Request Header
Request Parameter
parameter
type
requisite
description
keyword
String
검색어검색어가 고속도로 명칭에 exact 또는 partial 매치되는 경우, 매칭된 CCTV용 고속도로 데이터를 제공* keyword가 NULL인 경우, 전체 고속도로 데이터 리스트 리턴
Response Parameter
parameter
type
description
result_code
String
결과 코드
result_msg
String
결과코드에 따른 메세지
total_count
Integer
고속도로 검색 결과 개수
road_list
Array
고속도로 검색 결과 리스트
┣ road_id
Integer
고속도로 노선번호
┗ road_name
String
고속도로 명칭
```

## CCTV 검색

```
CCTV 검색
Function
CCTV 검색
URL
/sire/searchCctv
Request Header
Request Parameter
parameter
type
requisite
description
keyword
String
검색어검색어가 CCTV 명칭에 exact 매치되거나 partial 매치되는 경우, 매칭된 CCTV 데이터를 제공
road_id
String
고속도로 노선번호입력 시, 해당 노선번호의 CCTV 데이터 제공(CCTV용 고속도로 검색 결과의 노선번호 입력)
Response Parameter
parameter
type
description
result_code
String
결과 코드
result_msg
String
결과코드에 따른 메세지
total_count
Integer
CCTV 검색 결과 개수
cctv_list
Array
CCTV 검색 결과 리스트
┣ cctv_id
Integer
CCTV ID
┣ cctv_name
String
CCTV 명칭
┣ cctv_seq
Integer
동일 고속도로의 CCTV 위치 순서(1~n)* 고속도로 정보가 없는 경우 NULL
┣ road_id
Integer
CCTV가 위치한 고속도로 노선번호* 고속도로 정보가 없는 경우 NULL
┗ road_name
String
CCTV가 위치한 고속도로 명칭* 고속도로 정보가 없는 경우 NULL
```

## 대중교통 추천어 초성 검색

```
대중교통 추천어 초성 검색
Function
대중교통 추천어 초성 검색
URL
/multiSearchProposer
Request Header
Request Parameter
parameter
type
requisite
description
query
String
O
자동완성/초성문자
coordX
String
O
버스정류장 검색일경우현위치 중심좌표 x(UTM-K)
coordY
String
O
버스정류장 검색일경우현위치 중심좌표 y(UTM-K)
Response Parameter
parameter
type
description
result_code
String
결과 코드
result_msg
String
결과코드에 따른 메세지
sireResult
Object
sire 추천어 검색 결과(실패일경우 내려주지않음)
┣ count
Integer
추천 검색어 검색 결과 개수
┗ keyword
Array
추천 검색어 결과 List
┣ keyword
String
검색어
┗ frequency
Integer
조회 빈도
seamlessResult
Object
seamless 추천어 검색 결과(실패일경우 내려주지않음)
┣ busList
Array
버스노선 결과 리스트
┣ accuracy
Integer
검색 type
┣ busLineId
String
버스노선 ID(아로)
┣ locgovLineId
String
버스노선 ID(지자체)
┣ busLineNo
String
버스노선명
┣ busTypeCd
String
버스 유형
┣ busCityNm
String
버스노선 소재지역
┣ orgNm
String
버스 기점명
┗ dstNm
String
버스 종점명
┣ stationList
Array
버스정류소 결과 리스트
┣ stnId
Integer
버스 정류소 ID(아로)
┣ stnNo
String
버스 정류소 번호
┣ stnNm
String
버스 정류소 명
┣ addr
String
버스 정류소 주소
┣ x
Integer
X 좌표(UTM-K, 5179)
┣ y
Integer
Y 좌표(UTM-K, 5179)
┣ busNo
String
정차버스 \ (일반, 좌석, 마을, 직행좌석, 공항, 간선급행, 외곽, 간선, 지선, 순환, 광역, 급행, 농어촌, 급행간선)
┗ dist
Integer
거리(미터 단위)
┣ subwayList
Array
지하철 결과 리스트
┣ sbwyStnId
String
지하철 ID
┣ sbwyLineId
String
지하철 노선종류1(수도권1호선)2(수도권2호선)3(수도권3호선)4(수도권4호선)5(수도권5호선)6(수도권6호선)7(수도권7호선)8(수도권8호선)9(수도권9호선)100(수도권분당선)101(수도권공항철도)103(수도권중앙선)104(수도권경의선)108(수도권경춘선)109(수도권신분당선)21(인천1호선)31(대전1호선)41(대구1호선)42(대구2호선)51(광주1호선)71(부산1호선)72(부산2호선)73(부산3호선)74(부산4호선)79(김해경전철)
┗ stnNm
String
지하철역명
┗ totalList
Array
버스+버스정류장 결과 리스트
┣ type
String
버스:1, 버스정류장:2
┣ id
Integer
ID(아로ID)
┣ name
String
버스:버스번호버스정류장:정류장명
┣ stnid
Integer
버스:없음버스정류장:정류장번호
┣ sidonm
String
버스(정류장) 소재지역서울:12:부산3:대구4:인천5:광주6:대전7:울산8:세종시9:경기도10:강원도11:충청북도12:충청남도13:전라북도14:전라남도15:경상북도16:경상남도17:제주도
┣ sidocd
String
버스(정류장) 소재코드서울:12:부산3:대구4:인천5:광주6:대전7:울산8:세종시9:경기도10:강원도11:충청북도12:충청남도13:전라북도14:전라남도15:경상북도16:경상남도17:제주도
┣ x
Integer
버스 : 0(값없음)정류장 : X 좌표(UTM-K, 5179)
┗ y
Integer
버스 : 0(값없음)정류장 : Y 좌표(UTM-K, 5179)
```

## 최적 지적 검색

```
Add comment
최적 지적 검색
Function
최적 지적 검색
URL
/sire/optimalPosition
Request Header
Request Parameter
parameter
type
requisite
description
posx
String
O
정규화 X좌표
posy
String
O
정규화 Y좌표
type
Integer
O
최적 지점 속성
• Default : 0
• 0 : 전체
• 1 : 차량 입구점
• 2 : 택시 승하차 지점(건물)
• 3 : 택시 승하차 지점(단지)
• 4 : 택배 차량 하차 거점
• 5 : 보행자 입구점
• 6 : 배달 하차점(차량, 오토바이)
• 7 : 배달 하차점(자전거, 도보)
count
Integer
O
최대 결과 목록 수
Response Parameter
parameter
type
description
result_code
String
결과 코드
0 : 성공
903 : 조회 결과 없음
999 : 정의되지 않은 오류
result_msg
String
결과코드에 따른 메세지
entrypoints
Array
최적 지점 좌표 정보
┣ x
String
정규화 X좌표
┣ y
String
정규화 Y좌표
   ┗ type
Integer
EP 좌표 타입
• Default : 0
• 0 : 미지정
• 1 : 차량 입구점
• 2 : 택시 승하차 지점(건물)
• 3 : 택시 승하차 지점(단지)
• 4 : 택배 차량 하차 거점
• 5 : 보행자 입구점
• 6 : 배달 하차점(차량, 오토바이)
• 7 : 배달 하차점(자전거, 도보)
```


# 3. 즐겨찾기

## 즐겨찾기 추가

```
즐겨찾기 추가
Function
즐겨찾기 추가
URL
/regPointInsert
Request Header
Request Parameter
parameter
type
requisite
description
regPointData
Object
O
즐겨찾기 데이터
┣ name
String
O
즐겨찾기 이름
┣ type
String
O
즐겨찾기 타입10 : 집으로20 : 자주가는곳30 : 기본 즐겨찾기
┣ locationVX
String
O
위치보기좌표 X
┣ locationVY
String
O
위치보기좌표 Y
┣ routeX
String
O
탐색 x좌표
┣ routeY
String
O
탐색 y좌표
┣ ppoi
String
parent POI ID(parent POI ID값이 없을 경우 child POI ID값으로 채워줌)
┣ cpoi
String
child POI ID
┣ address
String
O
즐겨찾기 주소
┣ roadAddress
String
즐겨찾기 도로명 주소
┗ guideflag
String
음성 발성 여부
regPointLabelList
Array
삽입할 라벨 아이디(라벨 넣지않을거면 안보내도됩니다.)
┣ labelName
String
라벨이름 (LOG)
┗ labelId
String
라벨 ID
Response Parameter
parameter
type
description
결과 없음
```

## 즐겨찾기 업데이트

```
즐겨찾기 업데이트
Function
즐겨찾기 업데이트(이름변경)
URL
/regPointUpdate
Request Header
Request Parameter
parameter
type
requisite
description
regPointData
Object
O
즐겨찾기 데이터
┗ regId
String
O
즐겨찾기 ID
newRegPointData
Object
O
업데이트될 즐겨찾기 데이터
┣ name
String
O
즐겨찾기 이름
┣ type
String
O
즐겨찾기 타입10 : 집으로20 : 자주가는곳30 : 기본 즐겨찾기
┣ locationVX
String
O
위치보기좌표 X
┣ locationVY
String
O
위치보기좌표 Y
┣ routeX
String
O
탐색 x좌표
┣ routeY
String
O
탐색 y좌표
┣ ppoi
String
parent POI ID(parent POI ID값이 없을 경우 child POI ID값으로 채워줌)
┣ cpoi
String
child POI ID
┣ address
String
O
즐겨찾기 주소
┣ roadAddress
String
즐겨찾기 도로명 주소
┗ guideflag
String
음성 발성 여부
regPointLabelList
Array
삽입할 라벨 아이디(라벨 넣지않을거면 안보내도됩니다.)
┣ option
int
삽입 삭제 flag0 : 삭제 1: 삽입
┣ labelName
String
라벨이름 (LOG)N
┗ labelId
String
라벨 ID
Response Parameter
parameter
type
description
result_code
String
결과 코드
result_msg
String
결과코드에 따른 메세지
agentTs
Integer
서버 TS
```

## 즐겨찾기 삭제

```
즐겨찾기 삭제
Function
즐겨찾기 삭제
URL
/regPointDelete
Request Header
Request Parameter
parameter
type
requisite
description
regIdList
Array
O
삭제할 즐겨찾기ID 리스트
Response Parameter
parameter
type
description
result_code
String
결과 코드
result_msg
String
결과코드에 따른 메세지
agentTs
Integer
서버 TS
```

## 라벨 추가

```
라벨 추가
Function
라벨 추가
URL
/makeLabel
Request Header
Request Parameter
parameter
type
requisite
description
regPointLabel
Object
O
라벨정보
┣ labelName
String
O
라벨 이름
┣ labelId
String
O
라벨 ID(클라이언트 생성 ※default label 은 0 이므로 labelInsert 시에 0이아닌 값으로 만들어줘야함)
┗ labelColor
String
O
라벨색상
Response Parameter
parameter
type
description
result_code
String
결과 코드
result_msg
String
결과코드에 따른 메세지
agentTs
Integer
서버 TS
```

## 라벨 업데이트

```
라벨 업데이트
Function
라벨 업데이트
URL
/updateLabel
Request Header
Request Parameter
parameter
type
requisite
description
regPointLabel
Object
O
라벨정보
┗ labelId
String
O
라벨 이름
newRegPointLabel
Object
O
라벨정보
┣ labelName
String
O
변경할 라벨 이름
┗ labelColor
String
변경할 라벨 색상
Response Parameter
parameter
type
description
result_code
String
결과 코드
result_msg
String
결과코드에 따른 메세지
agentTs
Integer
서버 TS
```

## 라벨 삭제

```
라벨 삭제
Function
라벨삭제(라벨데이터 삭제 + 라벨삭제 (즐겨찾기 데이터는 모두 default 라벨화 됨))
URL
/deleteLabel
Request Header
Request Parameter
parameter
type
requisite
description
regPointLabel
Object
O
삭제할 라벨정보
┗ labelIdList
Array
O
삭제할 라벨 Id 리스트
Response Parameter
parameter
type
description
result_code
String
결과 코드
result_msg
String
결과코드에 따른 메세지
agentTs
Integer
서버 TS
```

## 라벨 데이터 추가

```
라벨 데이터 추가
Function
라벨 데이터 추가
URL
/insertRegToLabel
Request Header
Request Parameter
parameter
type
requisite
description
regPointLabelList
Array
O
삽입할 라벨안 즐겨찾기 정보 리스트
┣ labelId
String
O
라벨 ID
┗ regIdList
Array
O
삽입할 즐겨찾기 ID 리스트
Response Parameter
parameter
type
description
result_code
String
결과 코드
result_msg
String
결과코드에 따른 메세지
agentTs
Integer
서버 TS
```

## 라벨 데이터 삭제

```
라벨 데이터 삭제
Function
라벨 데이터 삭제
URL
/deleteLabelData
Request Header
Request Parameter
parameter
type
requisite
description
regPointLabelList
Object
O
삭제할 라벨안 즐겨찾기 정보
┣ labelId
String
O
라벨 ID
┗ regIdList
Array
O
삭제할 즐겨찾기 ID 리스트
Response Parameter
parameter
type
description
result_code
String
결과 코드
result_msg
String
결과코드에 따른 메세지
agentTs
Integer
서버 TS
```

## 라벨 데이터 모두 삭제

```
라벨 데이터 모두 삭제
Function
라벨 데이터 모두 삭제
URL
/resetLabel
Request Header
Request Parameter
parameter
type
requisite
description
regPointLabel
Object
O
삭제할 라벨안 즐겨찾기 정보
┗ labelId
String
O
라벨 ID
Response Parameter
parameter
type
description
result_code
String
결과 코드
result_msg
String
결과코드에 따른 메세지
agentTs
Integer
서버 TS
```

## 즐겨찾기 정보 동기화

```
즐겨찾기 정보 동기화
Function
즐겨찾기 정보 동기화
URL
/regPointsync
Request Header
Request Parameter
parameter
type
requisite
description
currentTs
Integer
O
클라이언트 현재 TS
justTsFlag
String
서버 TS만 내려받을지 여부0: 규격서에 명시된 리스폰스 다받음1: 서버TS만 내려받음
Response Parameter
parameter
type
description
result_code
String
결과 코드
result_msg
String
결과코드에 따른 메세지
sync
Boolean
false : 동기화 안맞음(서버데이터 내려줌) true : 에이전트와 서버 동기화상태
agentTs
Integer
서버 TS (요청시 justTsFlag 1 일경우 이것만 내려감)
regPointInfo
Array
즐겨찾기 list (sync가 false 일때만 내려감)
┣ name
String
즐겨찾기 이름
┣ ppoi
String
parent POI ID
┣ cpoi
String
child POI ID
┣ address
String
즐겨찾기 주소
┣ roadAddress
String
즐겨찾기 도로명 주소
┣ routeX
String
탐색 x좌표
┣ routeY
String
탐색 y좌표
┣ locationVX
String
위치보기 X좌표
┣ locationVY
String
위치보기 Y좌표
┣ type
String
즐겨찾기 타입10 : 집으로20 : 자주가는곳30 : 기본 즐겨찾기
┣ regId
String
즐겨찾기 ID
┣ guideflag
String
음성 발성 여부
┗ labelIdList
Array
등록되어 있는 라벨아이디0:default
labelInfo
Array
라벨정보 list (sync가 false 일때만 내려감)
┣ labelName
String
라벨이름
┣ labelColor
String
라벨 색상
┗ labelId
String
라벨Id
```

## 즐겨찾기 백업

```
즐겨찾기 백업
Function
즐겨찾기 백업
URL
/moveRegPoint
Request Header
Request Parameter
parameter
type
requisite
description
moveOption
String
O
이동방향1: 모바일(defaultPrivateKey) -> SNS(snsPrivateKey)2: SNS(snsPrivateKey) -> 모바일(defaultPrivateKey)3: 로그아웃시 NO눌럿을경우-> privateKey 즐겨찾기정보 삭제
Response Parameter
parameter
type
description
result_code
String
결과 코드
result_msg
String
결과코드에 따른 메세지
agentTs
Integer
서버 TS
```

## 즐겨찾기조회 통합회원 FivePin-AIR

```
즐겨찾기조회 통합회원 FivePin - AIR
Function
아이나비 통합회원 FivePin AIR즐겨찾기 조회
URL
/airRegpointUM
Request Header
Request Parameter
parameter
type
requisite
description
memCode
String
O
아이나비 통합회원 memberCode
Response Parameter
parameter
type
description
result_code
String
결과 코드
result_msg
String
결과코드에 따른 메세지
regPointInfo
Array
즐겨찾기 list (sync가 false 일때만 내려감)
┣ name
String
즐겨찾기 이름
┣ ppoi
String
parent POI ID
┣ cpoi
String
child POI ID
┣ address
String
즐겨찾기 주소
┣ roadAddress
String
즐겨찾기 도로명 주소
┣ routeX
String
탐색 x좌표
┣ routeY
String
탐색 y좌표
┣ locationVX
String
위치보기 X좌표
┣ locationVY
String
위치보기 Y좌표
┣ type
String
즐겨찾기 타입10 : 집으로20 : 자주가는곳30 : 기본 즐겨찾기
┣ regId
String
즐겨찾기 ID
┗ guideflag
String
음성 발성 여부
```

## 즐겨찾기추가 통합회원 FivePin-AIR

```
즐겨찾기추가 통합회원 FivePin - AIR
Function
즐겨찾기 추가
URL
/regPointInsertUM
Request Header
Request Parameter
parameter
type
requisite
description
regPointDataList
List
O
즐겨찾기 데이터
┣ name
String
O
즐겨찾기 이름
┣ type
String
O
즐겨찾기 타입10 : 집으로20 : 자주가는곳30 : 기본 즐겨찾기
┣ locationVX
String
O
위치보기좌표 X
┣ locationVY
String
O
위치보기좌표 Y
┣ routeX
String
O
탐색 x좌표
┣ routeY
String
O
탐색 y좌표
┣ ppoi
String
parent POI ID(parent POI ID값이 없을 경우 child POI ID값으로 채워줌)
┣ cpoi
String
child POI ID
┣ address
String
O
즐겨찾기 주소
┣ roadAddress
String
즐겨찾기 도로명 주소
┗ guideflag
String
음성 발성 여부
Response Parameter
parameter
type
description
결과 없음
```

## 즐겨찾기삭제 통합회원 FivePin-AIR

```
즐겨찾기삭제 통합회원 FivePin - AIR
Function
즐겨찾기 삭제
URL
/regPointDeleteUM
Request Header
Request Parameter
parameter
type
requisite
description
regIdList
Array
O
삭제할 즐겨찾기ID 리스트
Response Parameter
parameter
type
description
result_code
String
결과 코드
result_msg
String
결과코드에 따른 메세지
```

## 즐겨찾기업데이트 통합회원 FivePin-AIR

```
즐겨찾기업데이트 통합회원 FivePin - AIR
Function
즐겨찾기 업데이트(이름변경)
URL
/regPointUpdateUM
Request Header
Request Parameter
parameter
type
requisite
description
regPointData
Object
O
즐겨찾기 데이터
┗ regId
String
O
즐겨찾기 ID
newRegPointData
Object
O
업데이트될 즐겨찾기 데이터
┣ name
String
O
즐겨찾기 이름
┣ type
String
O
즐겨찾기 타입10 : 집으로20 : 자주가는곳30 : 기본 즐겨찾기
┣ locationVX
String
O
위치보기좌표 X
┣ locationVY
String
O
위치보기좌표 Y
┣ routeX
String
O
탐색 x좌표
┣ routeY
String
O
탐색 y좌표
┣ ppoi
String
parent POI ID(parent POI ID값이 없을 경우 child POI ID값으로 채워줌)
┣ cpoi
String
child POI ID
┣ address
String
O
즐겨찾기 주소
┣ roadAddress
String
즐겨찾기 도로명 주소
┗ guideflag
String
음성 발성 여부
Response Parameter
parameter
type
description
결과 없음
```


# 4. 로그

## 공통 정보

```
공통 정보
💡
공통 정보로 보내지는 내용은 API 호출 시 보내는 CommonRequestHeader 의 정보를 통해 자동으로 생성되는 정보
Request Parameter
parameter
type
requisite
description
상태
Log
String
로그 내용
운영
Op
String
동작구분
운영
CUR_X/CUR_Y
String
현위치 X/Y 좌표
운영
Ad-ID
String
안드로이드 Ad-ID (iOS 계열은 NONE으로 고정)
운영
UniqKey
String
사용자 식별을 위한 고유키
운영
AppVer
String
App Version 정보
운영
OSVer
String
OS Version 구분
운영
DeviceName
String
디바이스 명칭
운영
Device
String
단말기 OS - Android / iOS / AppleCarplay / AndroidAuto
변경
ISP
String
통신사 구분 - AIR: AIR3 / TMONEY: 온다 택시 / SDK_AIR: (SDK_AIR/고객사Keycode)
변경
Time
String
로그가 발생한 시간
운영
Category
String
로그종류 식별 문자열 - AirEvent / AirStatEvent / AirExtEvent
운영
```

## 로그 전송(User Event)

```
로그 전송(User Event)
Function
로그 전송(User Event)
URL
/userEvent
Request Header
Request Parameter
parameter
type
requisite
description
상태
start_route_u
Object
안내시작(Log)
운영
┣ cur_x
String
현위치x(좌표는 TW Index 좌표)
운영
┣ cur_y
String
현위치y(좌표는 TW Index 좌표)
운영
┣ rid
String
경로 ID
운영
┣ length
String
경로길이 (단위 : M)
운영
┣ etime
String
목적지까지 걸리는 시간 (단위 : sec)
운영
┣ inmethod
String
경로탐색을 호출한 기능(통합검색, 최근검색어, 즐겨찾기, 이전목적지, 타임머신)
UNITED 통합검색
RECENT 최근검색어
FAV 즐겨찾기
PDEST 이전목적지
TM 타임머신
AI AI를통한 호출
MAP 지도(위치지정)
MAINCARD 메인카드
INTR 외부연동
NEARBY 주변검색
ADDR 주소검색
UNDEF 미정의
운영
┣ routeopt
String
안내시작으로 선택한 경로의 경로옵션(추천/최소시간/편한길/이륜차/고속우선/무료경로/최단거리 등)
SGST 추천경로 (LGU+ 향으로는 “빠른길”)
FAST 최소시간
BEGI 초보자(편한길) (LGU+ 향으로는 “편한길”)
2W 이륜차
HIGH 고속우선
FREE 무료경로
SHORT 최단거리
T1R (트럭) 실시간 만차
T1RF (트럭) 실시간 만차 무료
T2R (트럭) 실시간 공차
T2RF (트럭) 실시간 공차 무료
T1N (트럭) 국도 만차
T2N (트럭) 국도 공차
TES (트럭) 공차시 추천경로
TEF (트럭) 공차시 무료경로
TEN (트럭) 공차시 국도위주경로
TFS (트럭) 만차시 추천경로
TFF (트럭) 만차시 무료경로
TFN (트럭) 만차시 국도위주경로
운영
┣ routeopt2
String
경로옵션2(대교탐색/해안도로/구간비교/주행중탐색)BRDG 대교탐색SHORE 해안도로
운영
┣ opt2string
String
대교탐색 시 해당 대교의 이름
운영
┣ startpos
String
출발지 정보: X / Y / PID / 이름 (지역명칭 or POI 명칭) (좌표는 TW Index 좌표)
운영
┣ destpos
String
도착지 정보: X / Y / PID / 이름 (지역명칭 or POI 명칭) (좌표는 TW Index 좌표)
운영
┗ pasgpos
String
경유지 정보: X / Y / PID / 이름 (지역명칭 or POI 명칭) (좌표는 TW Index 좌표)
경유지가 없다면 공란으로 입력, 경유지가 두개이면 연속해서 입력
운영
cancel_route_u
Object
경로취소(Log)
운영
┣ cur_x
String
현위치x(좌표는 TW Index 좌표)
운영
┣ cur_y
String
현위치y(좌표는 TW Index 좌표)
운영
┣ rid
String
경로 ID
운영
┣ destpos
String
도착지 정보X / Y / PID / 이름 (지역명칭 or POI 명칭) (좌표는 TW Index 좌표)
운영
┣ rlength
String
남은 거리 (단위 : M)
운영
┣ opt
String
AI: AI를 통한 호출그외의 상황에서는 공백으로 보내주면됨
운영
┗ rtime
String
남은 시간 (단위 : sec)
운영
arrive_nearby_u
Object
목적지 접근 안내(Log)(경유지/히든경유지 접근안내 포함)
운영
┣ rid
String
경로 ID(Log)
운영
┣ rdist
String
남은 거리 (단위 : M)
운영
┣ rtime
String
남은 시간 (단위 : sec)
운영
┣ posinfo
String
경유지/목적지PASG 경유지DEST 목적지
운영
┣ objpos
String
도착지 정보 X / Y / PID / 이름 (지역명칭 or POI 명칭) (좌표는 TW Index 좌표)
운영
goal_notify_u
Object
도착안내 팝업(Log)
운영
┣ rid
String
경로 ID
운영
┣ length
String
경로 총 길이 (단위 : M)
운영
┣ time
String
주행 총 시간 (단위 : sec)
운영
┣ destpos
String
도착지 정보: X / Y / PID / 이름 (지역명칭 or POI 명칭) (좌표는 TW Index 좌표)
운영
┗ point
String
화면상에 보여준 마일리지 적립 포인트 값
운영
poi_share_u
Object
위치공유(Log)
운영
┣ name
String
POI 이름
운영
┣ pid
String
POI ID
운영
┗ shopt
String
공유 방식 구분 - SMS / COPY / KAKAO / LINE / BAND
운영
opt_blackbox_u
Object
블랙박스(Log)
운영
┗ opt
String
블랙박스 버튼 사용시 - ON: 녹화시작, OFF: 녹화종료
운영
app_entry_u
Object
앱 종료(Log)
운영
┗ opt
String
OFF로 String 값 고정
운영
stat_map_dw_u
Object
지도 다운로드(Log)
운영
┣ result
String
다운로드 결과 (OK/FAIL)
운영
┣ version
String
지도버전
운영
┣ mode
String
다운로드/스트리밍 (DW/STREAM)
운영
┗ etc
String
안전운행 데이터 버전
운영
carplay_u
Object
카플레이 설정(Log)
운영
┣ uiType
String
화면타입 (CarPlay_Map)
운영
┗ maptheme
String
지도테마 설정값(NORMAL / EXTREME3D)
+ 설정값 추가 (NORMAL / EXTREME3D / CARTOON / NATURE)
변경
maptheme_a
Object
맵테마설정
운영
더 불러오기
Response Parameter
parameter
type
description
result_code
String
결과 코드
result_msg
String
결과코드에 따른 메세지
```

## 주행로그 업로드

```
주행로그 업로드
Function
주행로그 업로드
URL
/uploadDrivingLog
Request Header
Request Parameter
parameter
type
requisite
description
data
File
O
Upload 할 File (Multipart로 파일을 전송한다.)
rtopt
String
O
경로 여부0 : 경로 없음1 : 경로 있음
sec
String
O
주행 시간(초단위 입력)
dist
String
O
주행 거리
mrVersion
String
O
MR Version (19.01a)
Response Parameter
parameter
type
description
result_code
String
결과 코드
result_msg
String
결과코드에 따른 메세지
```

## AI 로그 업로드

```
AI 로그 업로드
Function
AI 업로드
URL
/uploadAiLog
Request Header
Request Parameter
parameter
type
requisite
description
aclData
String
O
<ActTypeID>│<CallType>│<uword>│<ActTypeID>│<CallType>│<uword>│...갯수만큼 반복한다ActTypeID = AI 엔진에서 리턴된 액션 ID 값CallType = C or V (C = Click. 버튼으로 호출. V = Voice. 보이스로 호출)uword = AI 엔진에서 인식한 추가 String. 없다면 공백.
Response Parameter
parameter
type
description
result_code
String
결과 코드
result_msg
String
결과코드에 따른 메세지
```

## 에어연구소 로그 업로드

```
에어연구소 로그 업로드
Function
AI 업로드
URL
/uploadAirlabLog
Request Header
Request Parameter
parameter
type
requisite
description
properties
Array
Object
O
LogAPI 규격 프로퍼티 개수만큼 설정
┣ name
String
프로퍼티 이름
┗ value
String
프로퍼티 값
프로퍼티 목록
로그 API 규격 추가시 규격과 동일한 순서대로 전달 (유연한 설정 가능)
┣ airbot
String
에어봇 로그 - ON/OFF
┣ hudSetting
String
카플레이 연결시 HUD 길안내 - ON/OFF
┣ routeOpt
String
경로 안내 기본 옵션 설정 - SGST / FAST / FREE / MAINROAD / HIGHWAY / SHORT
┣ voiceCancel
String
기본 안내 음성 제거 - ON/OFF
┣ smartSig
String
똑똑한 신호등 - ON/OFF
┗ homeSetting
String
메인화면 설정 - ON/OFF
Response Parameter
parameter
type
description
result_code
String
결과 코드
result_msg
String
결과코드에 따른 메세지
Response Parameter
parameter
type
description
결과 없음
```


# 5. 이벤트

## 이벤트 조회

```
이벤트 조회
Function
이벤트 조회
URL
/event
Request Header
Request Parameter
Response Parameter
parameter
type
description
result_code
String
결과 코드
result_msg
String
결과코드에 따른 메세지
attEvent
Object
이벤트
┣ idx
String
이벤트 idx
┣ status
String
사용자 상태1: 응모전2: 응모후3: 응모중
┗ value
String
이벤트 값
```

## 행운상자 상품리스트 조회(Admin)

```
행운상자 상품리스트 조회(Admin)
Function
행운상자 상품리스트 조회(Admin)
URL
/getLuckyProductList
Request Header
Request Parameter
Response Parameter
parameter
type
description
result_code
String
결과 코드
result_msg
String
결과코드에 따른 메세지
productList
Array
등록가능한 상품리스트
┣ imageUrl
String
상품이미지 URL
┣ company
String
회사이름
┣ sellPrice
String
판매가격
┣ productName
String
상품명
┗ usePrice
String
소비자가격
```

## 행운상자 정보

```
행운상자 정보
Function
행운상자 정보
URL
/getLuckyBoxStatus
Request Header
Request Parameter
Response Parameter
parameter
type
description
result_code
String
결과 코드
result_msg
String
결과코드에 따른 메세지
luckyTimes
Integer
이번이벤트 1일 응모 가능 횟수
numberOfTimes
Integer
금일 응모한 횟수
isPossible
Boolean
응모가능여부 (횟수조건, 마일리지조건 or로 하여 최종판단하여 내려줌)
usePoint
Integer
1회응모에 드는 마일리지
remainMileage
Integer
응모에 사용가능 마일리지
impossibleReason
String
응모 불가 이유
```

## 행운상자 뽑기

```
행운상자 뽑기
Function
행운상자 뽑기
URL
/luckyBoxOpen
Request Header
Request Parameter
Response Parameter
parameter
type
description
result_code
String
결과 코드
result_msg
String
결과코드에 따른 메세지
isWin
boolean
당첨여부
giftImageUrl
String
상품 이미지 URL
luckyTimes
Integer
이번이벤트 1일 응모 가능 횟수
numberOfTimes
Integer
금일 응모한 횟수
isPossible
Boolean
응모가능여부 (횟수조건, 마일리지조건 or로 하여 최종판단하여 내려줌)
usePoint
Integer
1회응모에 드는 마일리지
remainMileage
Integer
응모에 사용가능 마일리지
```

## 행운상자 뽑기 이력 및 쿠폰리스트 조회(보관함)

```
행운상자 뽑기 이력 및 쿠폰리스트 조회(보관함)
Function
행운상자 기프트 리스트 조회(보관함)
URL
/luckyBoxList
Request Header
Request Parameter
Response Parameter
parameter
type
description
result_code
String
결과 코드
result_msg
String
결과코드에 따른 메세지
giftList
Array
상품리스트
┣ barcodeImageUrl
String
바코드 이미지 URL
┣ giftImageUrl
String
상품 이미지 URL
┣ company
String
회사명
┣ productName
String
상품명
┣ expireDate
String
만료일
┣ isExpired
Boolean
만료여부
┣ drawingDate
String
뽑은날짜
┗ extraInfo
String
상품명/설명/주의 등등 줄 수 있는 정보
```

## 에어 캐시 적립

```
에어 캐시 적립
Function
이벤트 페이지 에어 캐시 적립
URL
/event/cash/earn
Request Header
Request Parameter
parameter
type
requisite
description
eventID
String
O
이벤트 페이지 버튼에서 전달받은 ID
Response Parameter
parameter
type
description
result_code
String
결과 코드
0 : 성공
970 : 에어 캐시 정합성 체크 실패
980 : 기지급
999 : 정의 되지 않은 오류
result_msg
String
결과값에 따른 메세지
```

## 모바일 교환권 캐시 적립

```
모바일 교환권 캐시 적립
Function
이벤트 페이지 에어 캐시 적립
URL
/event/cash/voucherExchange
Request Header
Request Parameter
parameter
type
requisite
description
loginKey
String
O
암호화된 로그인 키(AES-128)
mobileVoucherCode
String
O
모바일 교환권 코드(16자리 난수)
Response Parameter
parameter
type
description
result_code
String
결과 코드
0 : 성공
970 : 에어 캐시 정합성 체크 실패
980 : 기지급
999 : 정의 되지 않은 오류
result_msg
String
결과값에 따른 메세지
```


# 6. 기타

## 외부 계정 연동 로그인

```
외부 계정 연동 로그인
Function
SNS 로그인
URL
/snsLogin
Request Header
Request Parameter
parameter
type
requisite
description
token
String
O
SNS 토큰통합로그인시 memberCd
snsType
String
O
SNS 타입f : 페이스북g : 구글k : 카카오k2 : 카카오(APIv2)n : 네이버a : 애플u : 통합로그인
appleAuthCode
String
애플인 경우 로그인 시 생성 되는 authorization_code
Response Parameter
parameter
type
description
result_code
String
결과 코드
result_msg
String
결과코드에 따른 메세지
snsType
String
snsType
snsKey
String
snsKey값
snsRegPopUpFlag
boolean
즐겨찾기 동기화 팝업 노출여부true : 팝업노출false : 팝업미노출위값들은 snsPrivateKey값의 ts가지고 판단하였음
birthday
String
생년월일 (입력해두지 않았을경우 null반환)
gender
String
성별 (입력해두지 않았을경우 null반환)
hipass
String
하이패스 옵션0: OFF1: ON
discount
String
국가유공자 및 장애인 할인0: OFF1: ON
car_type
String
차종0: 경차(1종 통행료 할인 적용)1: 1종(소형차)2: 2종(중형차)3: 3종(대형차)4: 4종(대형화물차)5: 5종(특수화물차)6: 이륜차
car_mark
String
자차마크0: 기본1: 흰색세단2: 빨간스포츠카3: 하늘색SUV4: 노란스포츠카5: 경찰차6: 소방차7: 파란색트럭8 : 봉고차9: 초록 해치백10 : 파란버스11 : 파란오토바이12 : 빨간오토바이
oil_type
String
유종0: 휘발유1: 고급휘발유2: 경유3: LPG4: 전기차 충전소
oil_station
String
선호주유소 (중복 설정시 "_"구분자로 전송 *전체선택시 -> 0, 이경우 이외 다른값 전달 금지)0: 전체1: SK2: S-OIL3: 현대 OilBank4: GS5: E-1선호 충전기(중복 설정시 "_"구분자로 전송)0: DC차데모1:AC급속3상2:DC콤보3:AC완속
total_distance
Long
총 주행 거리
total_point
Long
총 적립 포인트
gender
String
성별M: 남자F : 여자
birthday
String
생년월일EX(1988.12.30) -> YYYY.MM.DD
carNum
String
차량번호EX(16더0726, 223라1832)
birthTime
String
태어난시간(ex : 1930)모름 : DNK
sL
String
음력 양력양력 : S음력 : L음력윤달 : LI
tutoComplete
boolean
튜토리얼 완료여부
driveLineColor
String
주행선 색상 (환경설정 -> 지도설정 -> 주행선 색상)
0 : traffic
1 : red
2 : orange
3 : yellow
4 : green
5 : blue (Default)
6 : indigo
onAirBenefits
String
맞춤형 온에어 혜택 (Default ON)
0 : OFF
1 : ON
defaultRouteOption
String
추천  경로 옵션 설정 (0 ~ 5)
0 : 에어추천 (Default)
1 : 가장 빠름
2: 무료도로
3: 큰길 위주
4: 고속도로 위주
5 : 최단 거리
issueReport
String
제보하기 개선 (Default OFF)
0 : OFF
1 : ON
onlyCamera
String
Only 카메라 모드 (Default OFF)
0 : OFF
1 : ON
realTimeTraffic
String
실시간 교통 신호 안내 (Default ON)
0 : OFF
1 : ON
mainRecentPlaces
String
메인화면 최근장소 더보기 (Default OFF)
0 : OFF
1 : ON
mbSpdEnfrc
String
이동식 과속 단속 (Default : ON)
0 : OFF
1: ON
bxtSpEnfrc
String
박스형 과속 단속 (Default : ON)
0 : OFF
1: ON
crckdIntrv
String
끼어들기 단속 (Default : OFF)
0 : OFF
1: ON
ovrldCntrl
String
과적 단속 (Default : OFF)
0 : OFF
1: ON
trfclCmr
String
교통정보 수집 카메라(Default : ON)
0 : OFF
1: ON
sharpCurve
String
급커브 구간 (Default : ON)
0 : OFF
1: ON
acdntBndln
String
사고다발 구간 (Default : ON)
0 : OFF
1: ON
speedBump
String
과속 방지턱 (Default : ON)
0 : OFF
1: ON
chlEldRsr
String
어린이/노인 보호구역 (Default : ON)
0 : OFF
1: ON
wldlfSnctr
String
야생동물 보호구역 (Default : ON)
0 : OFF
1: ON
rlrdCrsng
String
철도 건널목 (Default : ON)
0 : OFF
1: ON
fallStSect
String
낙석 구간 (Default : OFF)
0 : OFF
1: ON
entrnGrtrr
String
녹색교통지역 진입 (Default : ON)
0 : OFF
1: ON
```

## 외부 계정 연동 가입여부 확인

```
외부 계정 연동 가입여부 확인
Function
외부 계정 연동 가입여부 확인
URL
/snsCheck
Request Header
Request Parameter
parameter
type
requisite
description
snsId
String
O
통합로그인시 memberCd(현재는 통합회원만 지원)
snsType
String
O
SNS 타입f : 페이스북g : 구글k : 카카오n : 네이버a L 애플u : 통합로그인
Response Parameter
parameter
type
description
result_code
String
결과 코드
result_msg
String
결과코드에 따른 메세지
```

## 외부 계정 연동 통합회원 전환 로그인

```
외부 계정 연동 통합회원 전환 로그인
Function
SNS 연동 통합회원 전환 로그인
URL
/snsTransLogin
Request Header
Request Parameter
parameter
type
requisite
description
memberCd
String
O
아이나비 memberCd
Response Paramete
parameter
type
description
result_code
String
결과 코드
result_msg
String
결과코드에 따른 메세지
snsType
String
snsType
snsKey
String
snsKey값
```

## 외부 계정 연동 로그아웃

```
외부 계정 연동 로그아웃
Function
SNS 로그아웃
URL
/snsLogout
Request Header
Request Parameter
parameter
type
requisite
description
buttonFlag
boolean
O
팝업버튼 플래그값YES : trueNO : false
Response Parameter
parameter
type
description
result_code
String
결과 코드
result_msg
String
결과코드에 따른 메세지
```

## 외부 계정 연동 정보입력

```
외부 계정 연동 정보입력
Function
SNS 정보입력
URL
/snsMemberInfoInsert
Request Header
Request Parameter
parameter
type
requisite
description
gender
String
성별M: 남자F : 여자
birthday
String
생년월일EX(1988.12.30) -> YYYY.MM.DD
Response Parameter
parameter
type
description
result_code
String
결과 코드
result_msg
String
결과코드에 따른 메세지
```

## 외부 계정 연동 회원탈퇴

```
외부 계정 연동 회원탈퇴
Function
SNS 회원탈퇴
URL
/signout
Request Header
Request Parameter
parameter
type
requisite
description
buttonFlag
boolean
O
팝업버튼 플래그값YES : trueNO : false
snsType
String
O
SNS 타입f : 페이스북g : 구글k : 카카오n : 네이버u: 통합회원
Response Parameter
parameter
type
description
result_code
String
결과 코드
result_msg
String
결과코드에 따른 메세지
```

## 확대도 정보 조회

```
확대도 정보 조회
Function
확대도 정보 조회확대도 ID(extid)는 한글을 포함하므로 Encoding(utf-8)을 하여 전송한다.결과의 data_url 사용 시에도 마지막 extid 부분은 Encoding(utf-8)하여 전송한다.
URL
/extendedMap
Request Header
Request Parameter
parameter
type
requisite
description
extid
String
O
확대도 ID
type
String
확대도 tyepieg : 기존 이미지mp4 : 영상 이미지
Response Parameter
parameter
type
description
result_code
String
결과 코드
result_msg
String
결과값에 따른 메세지
data_url
String
확대도 Data URL
extid
String
조회한 3D확대도 ID
type
String
요청한 확대도 tyepieg : 기존 이미지mp4 : 영상 이미지
```

## 신규 DP 확대도 정보 조회

```
신규 DP 확대도 정보 조회
Function
신규 DP 확대도 정보 조회확대도 ID(extid)는 한글을 포함하므로 Encoding(utf-8)을 하여 전송한다.결과의 data_url 사용 시에도 마지막 extid 부분은 Encoding(utf-8)하여 전송한다.
URL
/extendedNewMap
Request Header
Request Parameter
parameter
type
requisite
description
extid
String
O
확대도 ID
type
String
확대도 tyepieg : 기존 이미지mp4 : 영상 이미지
Response Paramete
parameter
type
description
result_code
String
결과 코드
result_msg
String
결과값에 따른 메세지
data_url_new
String
신규 DP엔진 확대도 Data URL
extid
String
조회한 3D확대도 ID
type
String
요청한 확대도 tyepieg : 기존 이미지mp4 : 영상 이미지
`
```

## 방면 음성 정보 조회

```
방면 음성 정보 조회
안상언
2024. 09. 12. (편집됨)
•  (2024-09-11 기준 개발 서버 반영) [Request Parameter] - [type] 4: 신규 발랄한 음성 추가
Function
방면 음성 정보 조회방면음성 정보 ID(vid)는 한글을 포함하므로 Encoding(utf-8)하여 전송한다.결과의 data_url 사용 시에도 마지막 vid 부분은 Encoding(utf-8)하여 전송한다.
URL
/directionVoice
Request Header
Request Parameter
parameter
type
requisite
description
vid
String
O
방면 음성 ID
type
String
음성 타입 1 : 부드러운 음성 2 : 발랄한 음성 3 : 신규 부드러운 음성 4: 신규 발랄한 음성
Response Parameter
parameter
type
description
result_code
String
결과 코드
result_msg
String
결과값에 따른 메세지
vid
String
조회한 방면 음성 ID
data_url
String
음성 파일 Data URL
playtime
String
음성 실행 시간
```

## 고속도로 휴게소 주유소 정보 조회

```
고속도로 휴게소 주유소 정보 조회
Function
고속도로 휴게소 주유소 정보 조회
URL
/searchOilStation
Request Header
Request Parameter
parameter
type
requisite
description
serviceid
String
O
서비스 ID1063 : 휴게소 주유소 검색
count
String
O
salist 개수
salist
Array
O
휴게소 명칭 리스트
┗ saname
String
O
휴게소 명칭
Response Parameter
parameter
type
description
result_code
String
결과 코드
result_msg
String
결과코드에 따른 메세지
total_num
Integer
전체 검색 결과 개수
search_num
Integer
검색 결과 개수
oslist
Array
휴게소 쥬우소 목록
┣ id
Integer
OPWID
┣ pole
Integer
POLE
┣ x
Integer
정규화 X좌표
┣ y
Integer
정규화 Y좌표
┣ update_date
Integer
변경날짜 YYYYMMDD
┣ update_time
Integer
변경시간 HHMMSS
┣ hg_price
Integer
고급 휘발유
┣ g_price
Integer
휘발유
┣ k_price
Integer
경유
┣ d_price
Integer
등유
┣ l_price
Integer
LPG
┣ saname
String
휴게소 명칭
┗ name
String
OPW 이름
evlist
Array
휴게소 전기차 충전소 목록
┗ saname
String
휴게소 명칭
```

## 환경 설정 저장

```
환경 설정 저장
Function
환경설정 저장
URL
/saveConfig
Request Header
Request Parameter
parameter
type
requisite
description
hipass
String
O
하이패스 옵션0: OFF1: ON
discount
String
O
국가유공자 및 장애인 할인0: OFF1: ON
car_type
String
O
차종0: 경차(1종 통행료 할인 적용)1: 1종(소형차)2: 2종(중형차)3: 3종(대형차)4: 4종(대형화물차)5: 5종(특수화물차)6: 이륜차
oil_type
String
O
유종0: 휘발유1: 고급휘발유2: 경유3: LPG4: 전기차 충전소
oil_station
String
O
선호주유소 (중복 설정시 "_"구분자로 전송 *전체선택시 -> 0, 이경우 이외 다른값 전달 금지)0: 전체1: SK2: S-OIL3: 현대 OilBank4: GS5: E-1선호 충전기(중복 설정시 "_"구분자로 전송)0: DC차데모1:AC급속3상2:DC콤보3:AC완속
car_mark
String
O
자차마크0: 기본1: 흰색세단2: 빨간스포츠카3: 하늘색SUV4: 노란스포츠카5: 경찰차6: 소방차7: 파란색트럭8 : 봉고차9: 초록 해치백10 : 파란버스11 : 파란오토바이12 : 빨간오토바이
push_status
String
O
PUSH 수신 동의 여부0: OFF1: ON
bbox
String
O
블랙박스 설정상태0: OFF1: ON(LOG)N
mapSetting
String
O
지도다운로드설정DW : 다운로드STREAM: 스트리밍(LOG)N
bboxAOF
String
O
블랙박스 상시녹화 ON/OFF(LOG)N
aIStatus
String
O
AI기능 활성화 ON/OFF0: OFF1: ON(LOG)N
aIVCFlag
String
O
AI보이스호출 사용 ON/OFF0: OFF1: ON2: 선택안함(LOG)N
aIVCString
String
O
0: 지니야1: 기가지니2: 선택안함
gender
String
성별M: 남자F : 여자
birthday
String
생년월일EX(1988.12.30) -> YYYY.MM.DD
carNum
String
차량번호EX(16더0726, 223라1832)
tutoComplete
boolean
O
튜토리얼 완료여부
birthTime
String
태어난시간(ex : 1930)모름 : DNK
sL
String
음력 양력양력 : S음력 : L음력윤달 : LI
cash_push_status
String
에어 캐시 PUSH 수신 동의 여부
0 : 미동의
1 : 동의
driveLineColor
String
주행선 색상 (환경설정 -> 지도설정 -> 주행선 색상)
0 : traffic
1 : red
2 : orange
3 : yellow
4 : green
5 : blue (Default)
6 : indigo
onAirBenefits
String
맞춤형 온에어 혜택 (Default ON)
0 : OFF
1 : ON
defaultRouteOption
String
추천  경로 옵션 설정 (0 ~ 5)
0 : 에어추천 (Default)
1 : 가장 빠름
2: 무료도로
3: 큰길 위주
4: 고속도로 위주
5 : 최단 거리
issueReport
String
제보하기 개선 (Default OFF)
0 : OFF
1 : ON
onlyCamera
String
Only 카메라 모드 (Default OFF)
0 : OFF
1 : ON
realTimeTraffic
String
실시간 교통 신호 안내 (Default ON)
0 : OFF
1 : ON
mainRecentPlaces
String
메인화면 최근장소 더보기 (Default OFF)
0 : OFF
1 : ON
mbSpdEnfrc
String
이동식 과속 단속 (Default : ON)
0 : OFF
1: ON
bxtSpEnfrc
String
박스형 과속 단속 (Default : ON)
0 : OFF
1: ON
crckdIntrv
String
끼어들기 단속 (Default : OFF)
0 : OFF
1: ON
ovrldCntrl
String
과적 단속 (Default : OFF)
0 : OFF
1: ON
trfclCmr
String
교통정보 수집 카메라(Default : ON)
0 : OFF
1: ON
sharpCurve
String
급커브 구간 (Default : ON)
0 : OFF
1: ON
acdntBndln
String
사고다발 구간 (Default : ON)
0 : OFF
1: ON
speedBump
String
과속 방지턱 (Default : ON)
0 : OFF
1: ON
chlEldRsr
String
어린이/노인 보호구역 (Default : ON)
0 : OFF
1: ON
wldlfSnctr
String
야생동물 보호구역 (Default : ON)
0 : OFF
1: ON
rlrdCrsng
String
철도 건널목 (Default : ON)
0 : OFF
1: ON
fallStSect
String
낙석 구간 (Default : OFF)
0 : OFF
1: ON
entrnGrtrr
String
녹색교통지역 진입 (Default : ON)
0 : OFF
1: ON
Response Parameter
parameter
type
description
result_code
String
결과 코드
result_msg
String
결과값에 따른 메세지
```

## 대교 리스트 조회

```
대교 리스트 조회
Function
대교 리스트 조회
URL
/bridgeList
Request Header
Request Parameter
Response Parameter
parameter
type
description
result_code
String
결과 코드
result_msg
String
결과값에 따른 메세지
bridge_list
Array
대교 리스트
┣ name
String
대교 이름
┣ up_x
String
상행 X좌표(정규화)
┣ up_y
String
상행 Y좌표(정규화)
┣ down_x
String
하행 X좌표(정규화)
┗ down_y
String
하행 Y좌표(정규화)
```

## 최근 목적지 리스트 조회

```
최근 목적지 리스트 조회
Function
최근 목적지 리스트 조회
URL
/latelyPoiListSelect
Request Header
Request Parameter
Response Parameter
parameter
type
description
result_code
String
결과 코드
result_msg
String
결과값에 따른 메세지
lately_poi_list
List
최근 목적지 리스트
┣ name
String
목적지 이름
┣ rpx
String
탐색 X좌표
┣ rpy
String
탐색 Y좌표
┣ dpx
String
Display X좌표
┣ dpy
String
Display Y좌표
┣ poi
String
POI ID
┣ address
String
지번 주소
┣ road_address
String
도로명 주소
┣ ts
String
Timestamp
┣ catecode
String
목적지 CATECODE
┗ cnt
int
목적지 탐색 횟수
```

## 최근 목적지 리스트 등록

```
최근 목적지 리스트 등록
Function
최근 목적지 리스트 등록
URL
/latelyPoiListInsert
Request Header
Request Parameter
parameter
type
requisite
description
lately_poi_list
List
O
최근 목적지 리스트
┣ name
String
O
목적지 이름
┣ rpx
String
O
탐색 X좌표
┣ rpy
String
O
탐색 Y좌표
┣ dpx
String
Display X좌표
┣ dpy
String
Display Y좌표
┣ poi
String
POI ID
┣ address
String
지번 주소
┣ road_address
String
도로명 주소
┣ ts
String
O
Timestamp
┣ catecode
String
목적지 CATECODE
┗ cnt
int
O
목적지 탐색 횟수
Response Parameter
parameter
type
description
result_code
String
결과 코드
result_msg
String
결과값에 따른 메세지
```

## 유고, VVMS, 수해 정보 상세 조회

```
유고, VVMS, 수해 정보 상세 조회
Function
유고, VVMS 아이디를 이용하여 상세 정보를 조회
URL
/roadEventDetail
Request Header
Request Parameter
parameter
type
requisite
description
id
String
O
유고 or VVMS or 수해 ID
eventType
Integer
O
0: VVMS, 1: 유고, 2: 수해
Response Parameter
parameter
type
description
result_code
String
결과 코드
result_msg
String
결과값에 따른 메세지
id
String
유고 or VVMS or 수해 ID
comment
String
상세 유고 or VVMS or 수해 정보
```

## CCTV 상세 조회

```
CCTV 상세 조회
Function
CCTV 아이디를 이용하여 상세 정보를 조회
URL
/cctvInfo
Request Header
Request Parameter
parameter
type
requisite
description
cctvList
Array<String>
O
CCTV ID 리스트
Response Parameter
parameter
type
description
result_code
String
결과 코드
result_msg
String
결과값에 따른 메세지
cctv_cnt
Integer
CCTV 개수
cctv_list
Array
CCTV 정보 리스트
┣ cctv_id
String
CCTV ID
┣ cctv_name
String
CCTV 명칭
┣ nosun
String
도로명
┣ offer
String
CCTV 데이터 제공처
┣ thumbnail_url
String
썸네일 이미지 URL
┣ stream_url
String
CCTV Stream URL
┗ time
String
업데이트 시간 (YYYYMMDDHHMISS)
```

## 재난, 긴급출동차량 위치 상세조회

```
재난, 긴급출동차량 위치 상세조회
Function
재난, 긴급출동차량 위치 상세 정보를 조회
URL
/emergencyDetail
Request Header
Request Parameter
parameter
type
requisite
description
id
String
O
재난 혹인 긴급출동차량 위치 정보 아이디
type
Integer
O
2 : 재난정보, 3 : 긴급출동차량 위치
Response Parameter
parameter
type
description
result_code
String
결과 코드
result_msg
String
결과값에 따른 메세지
emergency_text
String
상세정보 (현재는 고정문구로 서비스)
```

## 주행 이력 그룹 리스트 조회

```
주행 이력 그룹 리스트 조회
Function
주행 이력 그룹 리스트 조회
URL
/drivingHisGroupList
Request Header
Request Parameter
parameter
type
requisite
description
type
String
1: 총 마일리지, 총 주행거리만 표출0: 리스트 포함 전체 표출기본값: 0
Response Parameter
parameter
type
description
result_code
String
결과 코드
result_msg
String
결과값에 따른 메세지
total_distance
Long
총 주행 거리
total_point
Long
총 적립 포인트
days
List
현재 달 주행 이력 일별 리스트
┣ date
String
년.월.일(초단위Timestamp)
┣ distance
Long
주행 거리(단위 m)
┗ point
Long
마일리지
months
List
현재 달을 제외한 주행 이력 월별 리스트
┣ date
String
년.월(초단위Timestamp)
┣ distance
Long
주행 거리(단위 m)
┗ point
Long
마일리지
```

## 주행 이력 일별 리스트 조회

```
주행 이력 일별 리스트 조회
Function
주행 이력 일별 리스트 조회
URL
/drivingHisDayList
Request Header
Request Parameter
parameter
type
requisite
description
date
String
O
조회 년.월(초단위Timestamp)
Response Parameter
parameter
type
description
result_code
String
결과 코드
result_msg
String
결과값에 따른 메세지
total_distance
Long
조회 월 총 주행 거리
total_point
Long
조회 월 총 적립 포인트
days
List
조회 월 주행 이력 일별 리스트
┣ date
String
년.월.일(초단위Timestamp)
┣ distance
Long
주행 거리(단위 m)
┗ point
Long
마일리지
```

## 주행 이력 일 상세 리스트 조회

```
주행 이력 일 상세 리스트 조회
Function
주행 이력 일 상세 리스트 조회
URL
/drivingHisDayListDetail
Request Header
Request Parameter
parameter
type
requisite
description
date
String
O
조회 년.월.일(초단위Timestamp)
Response Parameter
parameter
type
description
result_code
String
결과 코드
result_msg
String
결과값에 따른 메세지
details
List
조회 날짜 주행 이력 날짜 상세 리스트
┣ reg_id
String
주행 이력 고유 ID
┣ start_addr
String
출발 주소
┣ end_addr
String
도착 주소
┣ start_dt
String
출발 시간(초단위Timestamp)
┣ end_dt
String
도착 시간(초단위Timestamp)
┣ distance
Long
주행 거리(단위 m)
┗ point
Long
마일리지
```

## 주행 이력 그룹 리스트 조회 FivePin-AIR

```
주행 이력 그룹 리스트 조회 FivePin - AIR
Function
주행 이력 그룹 리스트 조회 -FIVE PIN
URL
/drivingHisGroupListUM
Request Header
Request Parameter
parameter
type
requisite
description
memCode
String
O
통합회원 멤버코드
Response Parameter
parameter
type
description
result_code
String
결과 코드
result_msg
String
결과값에 따른 메세지
total_distance
Long
총 주행 거리
days
List
현재 달 주행 이력 일별 리스트
┣ date
String
년.월.일(초단위Timestamp)
┗ distance
Long
주행 거리(단위 m)
months
List
현재 달을 제외한 주행 이력 월별 리스트
┣ date
String
년.월(초단위Timestamp)
┗ distance
Long
주행 거리(단위 m)
```

## 주행 이력 일 상세 리스트 조회 FivePin-AIR

```
주행 이력 일 상세 리스트 조회 FivePin - AIR
Function
주행 이력 일 상세 리스트 조회
URL
/drivingHisDayListDetailUM
Request Header
Request Parameter
parameter
type
requisite
description
memCode
String
O
아이나비 통합회원 멤버코드
date
String
O
조회 년.월.일(초단위Timestamp)
Response Parameter
parameter
type
description
result_code
String
결과 코드
result_msg
String
결과값에 따른 메세지
details
List
조회 날짜 주행 이력 날짜 상세 리스트
┣ reg_id
String
주행 이력 고유 ID
┣ start_addr
String
출발 주소
┣ end_addr
String
도착 주소
┣ start_dt
String
출발 시간(초단위Timestamp)
┣ end_dt
String
도착 시간(초단위Timestamp)
┗ distance
Long
주행 거리(단위 m)
```

## 주행 이력별 상세 좌표 조회 FivePin-AIR

```
주행 이력별 상제 좌표 조회 FivePin - AIR
Function
주행 이력별 좌표 조회 -Five Pin
URL
/drivingHisCoordUM
Request Header
Request Parameter
parameter
type
requisite
description
regId
String
O
주행 regId
Response Parameter
parameter
type
description
result_code
String
결과 코드
result_msg
String
결과값에 따른 메세지
userLocInfo
Object
유저 주행정보
┣ id
String
주행 regId
┗ locTraces
List
주행좌표 리스트
┣ lat
String
출발지 위도, 정규화좌표 Y값(TW INDEX)
┣ lng
String
출발지 경도, 정규화좌표 X값(TW INDEX)
┣ speed
Integer
속도
┗ insert_time
String
입력시간
```

## 주행 이력 삭제

```
주행 이력 삭제
Function
주행 이력 삭제
URL
/drivingHisDelete
Request Header
Request Parameter
parameter
type
requisite
description
date_months
List<String>
삭제 년.월(초단위Timestamp)
date_days
List<String>
삭제 년.월.일(초단위Timestamp)
reg_ids
List<String>
삭제 주행 이력 ID
Response Parameter
parameter
type
description
result_code
String
결과 코드
result_msg
String
결과값에 따른 메세지
```

## 마일리지 이력 등록

```
마일리지 이력 등록
Function
마일리지 이력 등록(LogApi 전용)
URL
/mileageHisInsert
Request Header
Request Parameter
parameter
type
requisite
description
start_addr
String
출발 주소
end_addr
String
도착 주소
start_x
String
출발 좌표x (정규화)
start_y
String
출발 좌표x (정규화)
end_x
String
도착 좌표x (정규화)
end_y
String
도착 좌표x (정규화)
start_dt
String
출발 시간(초단위Timestamp)
end_dt
String
도착 시간(초단위Timestamp)
distance
Long
주행 거리(단위 m)
point
Long
O
마일리지
type
String
O
D : 주행 이력 마일리지E : 기타 마일리지
title
String
O
제목(예 : 가입 기념 마일리지)
Response Parameter
parameter
type
description
result_code
String
결과 코드
result_msg
String
결과값에 따른 메세지
```

## 혼잡 차선 조회

```
혼잡 차선 조회
Function
혼잡 차선 KS Link ID 조회
URL
/confusionLane
Request Header
Request Parameter
parameter
type
requisite
description
mrVer
String
O
요청 MR Version
mrlinks
Array
O
요청 MRLink 정보 리스트
┣ mapid
Integer
O
도로 MapID
┣ linkid
Integer
O
도로 LinkID
┗ direction
Integer
O
도로 Direction
Response Parameter
parameter
type
description
result_code
String
결과 코드
result_msg
String
결과값에 따른 메세지
kslinks
Array
응답 KSLink 정보 리스트
┣ mapid
Integer
도로 MapID
┣ linkid
Integer
도로 LinkID
┣ direction
Integer
도로 Direction
┣ speed
Integer
속도
┗ kslinkid
Integer
도로 KS LinkID
```

## KT 종료 마이그레이션 파일 정보 조회

```
KT 종료 마이그레이션 파일 정보 조회
Function
KT 종료 마이그레이션 파일 정보 조회
URL
/snsInfoMigrationFile
Request Header
Request Parameter
Response Parameter
parameter
type
description
result_code
String
결과 코드
result_msg
String
결과값에 따른 메세지
file_name
String
파일 이름
file_value
String
파일 내용
```

## KT 종료 마이그레이션 정보 조회

```
KT 종료 마이그레이션 정보 조회
Function
KT 종료 마이그레이션 파일 정보 조회
URL
/snsInfoMigrationData
Request Header
Request Parameter
Response Parameter
parameter
type
description
result_code
String
결과 코드
result_msg
String
결과값에 따른 메세지
sns_key
String
sns_key
data
String
마이그레이션 Data
```

## 제보하기 간소화

```
제보하기 간소화
Function
에어3 주행 중 원터치로 제보하기
URL
/simpleReport
Request Header
Request Parameter
parameter
type
requisite
description
category
String
O
제보하기 카테고리CAM : 카메라 정보 틀림ROU : 경로 오류DES : 목적지 위치 오류
┣ nowLoc
Object
O
현재 위치 정보
┣ x
String
O
현재 좌표 X (6자리 정규화 좌표)
┣ y
String
O
현재 좌표 Y (6자리 정규화 좌표)
┣ startLoc
Object
출발지 정보(category가 ROU 일때 필수)
┣ x
String
출발지 좌표 X (6자리 정규화 좌표)
┣ y
String
출발지 좌표 Y (6자리 정규화 좌표)
┗ name
String
출발지명
┣ desLoc
Object
목적지 정보(category가 ROU, DES 일때 필수)
┣ x
String
목적지 좌표 X (6자리 정규화 좌표)
┣ y
String
목적지 좌표 Y (6자리 정규화 좌표)
┗ name
String
목적지명
searchOption
String
Agent 탐색 종류(category가 ROU 일때 사용)agt_recommend : 추천경로 (LGU+ 향으로는 “빠른길”)agt_short_time : 최소시간real_traffic_freeroad : 무료도로short_distance_priority : 최단거리highway_priority : 고속도로우선motorcycle : 이륜차 이용도로beginner : 초보자(편한길) (LGU+ 향으로는 “편한길”)recommendation : 엔진기반 추천경로(agt_recommend 대체)time_priority : 엔진기반 최소시간(agt_short_time 대체)
Response Parameter
parameter
type
description
결과 없음
```

## AIR SOS

```
AIR SOS
Function
SOS 정보를 도로관리기관에 전달
URL
/roadAcdntNotiSos
Request Header
Request Parameter
parameter
type
requisite
description
sosInfo
Array
SOS 정보
┣ evntType
String
O
이벤트 type01 : SOS02 : 급감속
┣ evntLoctX
String
O
정규화좌표 X값(8자리)
┣ evntLoctY
String
O
정규화좌표 Y값(8자리)
┣ vhclAngl
String
O
차량 정북기준 각도(0~359)
┣ roadNm
String
O
도로 이름
┣ mrVer
String
O
요청 MR Version
┣ mrlink
Object
O
요청 MRLink 정보 리스트
┣ mapid
Integer
O
도로 MapID
┣ linkid
Integer
O
도로 LinkID
┗ direction
Integer
O
도로 Direction
┗ naviCd
String
O
내비사 코드02 : 아이나비(Defalut)
Response Parameter
parameter
type
description
result_code
String
결과 코드
result_msg
String
결과코드에 따른 메세지
```

## 회원탈퇴

```
회원탈퇴
Function
통합 회원탈퇴
URL
/integratedSignout
Request Header
Request Parameter
Response Parameter
parameter
type
description
result_code
String
결과 코드
result_msg
String
결과코드에 따른 메세지
```


# 7. RRIS

## 현재 위치 업로드

```
현재 위치 업로드
Function
재 위치 업로드
URL
/rris/data/currentLoc
Request Header
Request Parameter
parameter
type
requisite
description
x
String
O
X좌표
y
String
O
Y좌표
coordType
String
O
좌표 타입W : WGS84R : 탐색 좌표S : 검색 좌표
myInfo
Object
그룹주행이 아닐경우 오브젝트 안보내면됨
├ groupId
String
O
그룹아이디
├ remainDistance
String
O
목적지까지 남은거리
├ remainTime
String
O
목적지까지 남은시간단위 : 초
├ desX
String
O
목적지 X좌표 (TW index)
├ desY
String
O
목적지 Y좌표 (TW index)
├ desPoi
String
목적지 POIID
├ desName
String
목적지 이름
├ snsId
String
snsID(sns사용자일 경우)
├ snsType
String
snsTypeg:구글, k:카카오, f:페이스북, n:네이버(sns사용자일 경우)
┗ allowList
List
위치공유를 허용할 상대방의 privateKey리스트 (항상 최신 스냅샷을 보내야함)
rrisObject
Object
rris Object rris 아닐경우 오브젝트 안보내도됨
├ mapVer
String
O
지도 버전
├ speed
Integer
O
현재 주행 속도(km/h)
├ bearing
Integer
O
진행 각도
┗ link
Object
O
현재 도로 mr link 정보
├ mapId
Integer
O
mapId
├ linkId
Integer
O
linkId
├ nodeId
Integer
O
nodeId
┗ direction
Integer
O
direction
Response Parameter
parameter
type
description
result_code
String
결과 코드
result_msg
String
결과값에 따른 메세지
groupId
String
그룹ID(그룹주행관련한 요청이 아닐경우 안채워짐)
groupMembers
Array
그룹멤버 정보 (그룹주행관련한 요청이 아닐경우 안채워짐)
├ privateKey
String
그룹멤버 프라이빗키
├ mdn
String
암호화된 mdn
├ snsId
String
snsId(sns유저일 경우)
├ snsName
String
snsName(sns유저일 경우)
├ snsImageUrl
String
snsImageUrl(sns유저일 경우)
├ remainDistance
String
목적지까지 남은거리
├ remainTime
String
목적지까지 남은시간
├ updateTime
String
최근 수정시간밀리세컨드
├ status
String
그룹 참여 상황D:주행중 G: 도착
├ x
String
현재X 좌표
├ y
String
현재Y 좌표
├ allowFlag
boolean
나를 상대방이 허용했는지 여부 (이플래그를보고 좌표,목적지까지 남은거리 남은시간이 없는경우 위치없음인지 허용이 아닌지 판단)
├ iAllowFlag
boolean
내가 상대방을 허용했는지 Flag
├ isLeader
boolean
그룹방장 여부
┗ isMe
boolean
자기자신인지 여부
```

## 경로 파일 정보 업로드

```
프로덕트개발부문의 게스트이십니다. 전체 사용 권한을 얻으려면 멤버가 되거나 내 워크스페이스를 탐색하세요.
멤버십을 요청하세요.
워크스페이스 추가하기
경로 파일 정보 업로드
Function
경로 파일 정보 업로드
URL
/rris/data/saveRoute
Request Header
Request Parameter
parameter
type
requisite
description
mapVer
String
O
지도 버전
rid
String
O
탐색 파일 ID
dataUri
String
O
탐색 파일 URL
Response Parameter
parameter
type
description
result_code
String
찾을 수 없음
result_msg
String
결과값에 따른 메세지
```

## 이벤트 위치 업로드

```
프로덕트개발부문의 게스트이십니다. 전체 사용 권한을 얻으려면 멤버가 되거나 내 워크스페이스를 탐색하세요.
멤버십을 요청하세요.
워크스페이스 추가하기
이벤트 위치 업로드
Function
이벤트 위치 업로드
URL
/rris/event/upEmergency
Request Header
Request Parameter
parameter
type
requisite
description
eventId
String
O
이벤트 ID100: 구급차
longitude
String
O
longitude
latitude
String
O
latitude
coordType
String
O
좌표 타입W : WGS84
Response Parameter
parameter
type
description
result_code
String
결과 코드
result_msg
String
결과값에 따른 메세지
```


# 8. 에어 캐시

## 에어 캐시 정보 조회

```
에어 캐시 정보 조회
Function
에어 캐시 정보 조회
URL
/cashInfo
Request Header
Request Parameter
parameter
type
requisite
description
Response Parameter
parameter
type
description
result_code
String
결과 코드
result_msg
String
결과값에 따른 메세지
randomCashYn
String
랜덤 캐시 지급 가능 여부
Y : 지급 가능
N : 지급 불가
noneSavedCashYn
String
미적립 캐시 존재 여부
Y : 존재
N : 미존재
noneSavedCashValidDt
String
미적립 캐시 유효 기간 표출 문구
EX ) 24시간
myAirCashInfo
Object
나의 에어캐시 정보
┣ totalAirCash
Integer
나의 총 에어 캐시
┣ todaySavedCash
Integer
오늘 주행을 통해 적립된 캐시
┣ todayOnAirSavedCash
Integer
오늘 온에어를 통해 적립된 캐시
┣ todayDrivingDistance
Integer
오늘 주행 거리(m)
┣ maxDrivingDistance
Integer
최대 주행 거리(m)
┣ maxCash
Integer
최대 적립 캐시
┣ saveableAirCash
Integer
적립 가능한 캐시
┗ offerWall
1
Boolean
오퍼월 활성 여부
true: 활성화
false: 비활성화
rouletteInfo
Object
룰렛 관련 정보
┣ totalAirMile
Integer
나의 총 에어 마일리지
┣ convertedCash
Integer
전환된 에어 캐시
┗ roulettePeriod
String
룰렛 기간
```

## 에어 캐시 적립하기

```
에어 캐시 적립하기
Function
에어 캐시 적립하기
URL
/cashSave
Request Header
Request Parameter
parameter
type
requisite
description
결과 없음
Response Parameter
parameter
type
description
result_code
String
결과 코드
970 : 에어 캐시 정합성 체크 실패
(캐시 어뷰징 의심)
result_msg
String
결과값에 따른 메세지
randomCashYn
String
랜덤 캐시 지급 가능 여부
Y : 지급 가능
N : 지급 불가
noneSavedCashYn
String
미적립 캐시 존재 여부
Y : 존재
N : 미존재
myAirCashInfo
Object
나의 에어캐시 정보
┣ totalAirCash
Integer
나의 총 에어 캐시
┣ todaySavedCash
Integer
오늘 주행을 통해 적립된 캐시
┣ todayOnAirSavedCash
Integer
오늘 온에어를 통해 적립된 캐시
┣ todayDrivingDistance
Integer
오늘 주행 거리(m)
┣ maxDrivingDistance
Integer
최대 주행 거리(m)
┣ maxCash
Integer
최대 적립 캐시
┣  saveableAirCash
Integer
적립 가능한 캐시
┗ offerWall
오퍼월 활성 여부
true: 활성화
false: 비활성화
```

## 구매 상품 카탈로그 조회

```
구매 상품 카탈로그 조회
Function
구매 상품 카탈로그 조회
URL
/productList
Request Header
Request Parameter
parameter
type
requisite
description
결과 없음
Response Parameter
parameter
type
description
result_code
String
결과 코드
result_msg
String
결과코드에 따른 메세지
productList
Array
구매 가능한 상품리스트
┣ productName
String
상품명
┣ productCode
String
상품 코드
┣ imageUrl
String
상품이미지 URL
┣ company
String
회사이름
┣ sellPrice
Integer
판매가격
┣ discountPrice
Integer
할인 판매 가격 (discountFlag가 true일 경우에만 유효한 데이터)
┗ discountFlag
boolean
할인 판매 가격 적용 여부 플래그
true : 할인 판매 가격 적용
false : 할인 판매 가격 미적용
 totalAirCash
Integer
나의 총 에어 캐시
```

## 구매 상품 카탈로그 상세 정보 조회

```
구매 상품 카탈로그 상세 정보 조회
Function
구매 상품 카탈로그 상세 정보 조회
URL
/productDetail
Request Header
Request Parameter
parameter
type
requisite
description
productCode
String
O
상품 코드
Response Parameter
parameter
type
description
result_code
String
결과 코드
result_msg
String
결과코드에 따른 메세지
productDetail
Object
상품 상세 정보
┣ productName
String
상품명
┣ imageUrl
String
상품이미지 URL
┣ company
String
회사이름
┣ sellPrice
Integer
판매가격
┣ discountPrice
Integer
할인 판매 가격 (discountFlag가 true일 경우에만 유효한 데이터)
┣ discountFlag
boolean
할인 판매 가격 적용 여부 플래그
true : 할인 판매 가격 적용
false : 할인 판매 가격 미적용
┗  useNote
String
유의 사항
 totalAirCash
Integer
나의 총 에어 캐시
mdn
String
쿠폰 수신 암호화 MDN
```

## 쿠폰 구매하기

```
쿠폰 구매하기
Function
쿠폰 구매하기
URL
/couponPurchase
Request Header
Request Parameter
parameter
type
requisite
description
productCode
String
O
상품 코드
mdn
String
O
암호화 된 MDN
Response Parameter
parameter
type
description
result_code
String
결과 코드
501 : 에어 캐시 부족
970 : 에어 캐시 정합성 체크 실패
(캐시 어뷰징 의심)
result_msg
String
결과코드에 따른 메세지
 totalAirCash
Integer
나의 총 에어 캐시
```

## 쿠폰함 조회

```
쿠폰함 조회
Function
쿠폰함 조회
URL
/couponBox
Request Header
Request Parameter
parameter
type
requisite
description
결과 없음
Response Parameter
parameter
type
description
result_code
String
결과 코드
result_msg
String
결과코드에 따른 메세지
giftList
Array
상품리스트
┣ giftImageUrl
String
상품 이미지 URL
┣ company
String
회사명
┣ productName
String
상품명
┣ trId
String
트랜잭션 ID (재발송 시 필요)
┣ expireDate
String
만료일
┗  isExpired
Boolean
만료여부
```

## 쿠폰함 상세 정보 조회

```
쿠폰함 상세 정보 조회
Function
쿠폰 상세 정보 조회
URL
/couponBoxDetail
Request Header
Request Parameter
parameter
type
requisite
description
trId
String
O
트랜잭션 ID
Response Parameter
parameter
type
description
result_code
String
결과 코드
result_msg
String
결과코드에 따른 메세지
gift
Object
상품리스트
┣ giftImageUrl
String
상품 이미지 URL
┣ company
String
회사명
┣ productName
String
상품명
┣ trId
String
트랜잭션 ID (재발송 시 필요)
┣ drawingDate
String
발급일
┣ expireDate
String
만료일
┣ isExpired
Boolean
만료여부
┣ isResend
Boolean
재전송 가능여부
┣ useNote
String
유의 사항
┗ mdn
String
쿠폰 수신한 암호화 MDN
```

## 쿠폰 재발송

```
쿠폰 재발송
Function
쿠폰 재발송
URL
/couponResend
Request Header
Request Parameter
parameter
type
requisite
description
trId
String
O
트랜잭션 ID
Response Parameter
parameter
type
description
result_code
String
결과 코드
920인 경우, result_msg를 통해 메시지 표출
result_msg
String
결과코드에 따른 메세지
```

## 적립내역

```
적립내역
Function
적립 내역
URL
/airCashHistory
Request Header
Request Parameter
parameter
type
requisite
description
결과 없음
Response Parameter
parameter
type
description
result_code
String
결과 코드​
result_msg
String
결과코드에 따른 메세지
currentMonth
Integer
현재 월(1 ~ 12)
ex) 6
useableAirCash
Integer
사용 가능한 에어 캐시
exipiredAirCash
Integer
소멸 예정 에어 캐시
expiredAirCashPopMsg
Object
소멸 예정 캐시 팝업
┣ title
String
제목
ex) 소멸 예정 캐시
┗ contents
String
내용
ex) 약관에 따라 ~ 소멸 예정 캐시 부터 사용 됩니다.
airCashHistoryList
Array
적립 내역 리스트
┣ date
String
날짜 (MM.dd)
ex) 05.08
┣ type
String
항목 (적립 OR 사용)
ex) 적립
┣ detail
String
항목 상세 내역
ex) 주행 거리 적립
┗ cash
Integer
적립 OR 사용 항목 캐시
ex)
적립 case : 20
사용 case : -100
```

## 룰렷 게임

```
룰렛 게임
Function
룰렛 게임
URL
/roulette
Request Header
Request Parameter
parameter
type
requisite
description
type
String
O
룰렛 타입
P : 프리미엄
S : 스페셜
B : 보너스
Response Parameter
parameter
type
description
result_code
String
결과 코드
502 : 에어 마일 관련 에러
(에어 마일이 부족하거나 1000 마일 이상 보유자가 보너스 룰렛을 시도했을 때)
970 : 에어 캐시 정합성 체크 실패
(캐시 어뷰징 의심)
result_msg
String
결과값에 따른 메세지
winningCash
Integer
당첨 캐시
totalAirMile
Integer
에어 마일리지
convertedCash
Integer
전환된 에어 캐시
```

## 적립 스탬프 조회

```
적립 스탬프 조회
Function
적립 스탬프 조회
URL
/stampHistory
Request Header
Request Parameter
parameter
type
requisite
description
결과 없음
Response Parameter
parameter
type
description
result_code
String
결과 코드
0 : 성공
920 : 이벤트 종료 사유 등으로 서버 메세지 표출
999 : 정의 되지 않은 오류
result_msg
String
결과코드에 따른 메세지
currentMonth
Integer
현재 월(1 ~ 12)
ex) 6
stampCount
Integer
랜덤 캐시 지급을 위해 한달에 모아야 하는 스탬프 갯수
Default : 9
baseDay
String
적립 스탬프 기준 일
Ex) “한 달”
randomCashYn
String
랜덤 캐시 지급 가능 여부
Y : 지급 가능
N : 지급 불가
stampNotiMsg
String
스탬프 안내 문구

EX)
• 스탬프는 최대 1일 1개 제공되며, 매월 1일 초기화 됩니다.
• 추가 캐시 지급이 완료되면 스탬프는 처음부터 다시시작됩니다.
• 미적립 캐시는 3일간 유효하며 이후엔 자동 소멸됩니다.
• 캐시 유효기간 및 적립스탬프는 아이나비 에어의 정책에 따라 변경될 수 있습니다.
stampList
Array
스탬프 리스트
┣ date
String
날짜 (MM-dd)
ex) 04-19
┣ status
String
적립 상태 여부
S : 적립 상태
N : 미적립 상태
┣ cash
Integer
적립된 캐시 OR 적립 가능한 캐시
┗ randomCash
Integer
적립 된 랜덤 캐시
- 랜덤 캐시 전환 후 초기화 이전 표출 될 랜덤 캐시
- stampLIst 마지막 값만 유효하며 나머지 값들은 0
- 랜덤캐시 전환 이력이 없는 경우 모두 0
stampStartNumber
Integer
스탬프 배경 숫자 변경을 위한 시작 값 (해당 회차 기준 시작 숫자)
ex)
1회차 : 1
2회차 : 10
3회차 : 19
4회차 : 28
```

## 스탬프 완성(랜덤 캐시 지급)

```
스탬프 완성(랜덤 캐시 지급)
Function
스탬프 완성(랜덤 캐시 지급)
URL
/stampComplete
Request Header
Request Parameter
parameter
type
requisite
description
결과 없음
Response Parameter
parameter
type
description
result_code
String
결과 코드
0 : 성공
970 : 에어 캐시 정합성 체크 실패 (캐시 어뷰징 의심)
999 : 정의 되지 않은 오류
result_msg
String
결과코드에 따른 메세지
randomCash
Integer
추가 지급 된 랜덤 캐시
```

## 캐시 스탬프 적립

```
캐시 스탬프 적립 (구 미적립 캐시 스탬프 적립)
Function
캐시 스탬프 적립 (구 미적립 캐시 스탬프 적립)
URL
/cashStampSave
Request Header
Request Parameter
parameter
type
requisite
description
date
String
O
적립할 캐시 스탬프의 미적립 날짜 (MM-dd)
적립 스탬프 조회 의 date 🧭
스탬프 완성(랜덤 캐시 지급) 의 date
EX) 04-01
cashRenewal
String
에어 캐시 고도화 버전 여부
Y : 에어 캐시 고도화 버전
Response Parameter
parameter
type
description
result_code
String
결과 코드
0 : 성공
970 : 에어 캐시 정합성 체크 실패 (캐시 어뷰징 의심)
971 : 유효하지 않은 캐시 스탬프 date (이미 소멸 된 캐시 의심)
 ⇒ 해당 에러를 받을 경우,  🧭
적립 스탬프 조회 호출하여 데이터 구성 필요
999 : 정의 되지 않은 오류
result_msg
String
결과코드에 따른 메세지
cash
Integer
캐시 고도화 이전 : 해당 날짜에 적립 된 스탬프의 캐시
캐시 고도화 이후 : 현재 적립 되는 캐시
```

## 에어 캐시 및 스탬프 정보 조회

```
에어 캐시 및 스탬프 정보 조회
Function
에어 캐시 및 스탬프 정보 조회
URL
/cashStampInfo
Request Header
Request Parameter
parameter
type
requisite
description
결과 없음
Response Parameter
parameter
type
description
result_code
String
결과 코드
0 : 성공
999 : 정의 되지 않은 오류
result_msg
String
결과코드에 따른 메세지
noneSavedCashValidDt
String
미적립 캐시 유효 기간 표출 문구
EX ) 24시간
myAirCashInfo
Object
나의 에어캐시 정보
┣ totalAirCash
Integer
나의 총 에어 캐시
┣ todaySavedCash
Integer
오늘 주행을 통해 적립된 캐시
┣ todayOnAirSavedCash
Integer
오늘 온에어를 통해 적립된 캐시
┣ todayDrivingDistance
Integer
오늘 주행 거리(m)
┣ maxDrivingDistance
Integer
최대 주행 거리(m)
┣ maxCash
Integer
최대 적립 캐시
┗ offerWall
Boolean
오퍼월 활성 여부
true: 활성화
false: 비활성화
currentMonth
Integer
현재 월(1 ~ 12)
ex) 6
stampCount
Integer
랜덤 캐시 지급을 위해 한달에 모아야 하는 스탬프 갯수
Default : 9
stampNotiMsg
String
스탬프 하단 안내 문구

EX)
• 스탬프는 최대 1일 1개 제공되며, 매월 1일 초기화 됩니다.
• 추가 캐시 지급이 완료되면 스탬프는 처음부터 다시시작됩니다.
• 미적립 캐시는 3일간 유효하며 이후엔 자동 소멸됩니다.
• 캐시 유효기간 및 적립스탬프는 아이나비 에어의 정책에 따라 변경될 수 있습니다.
stampList
Array
스탬프 리스트
┣ date
String
날짜 (MM-dd)
ex) 04-19
┗ status
String
적립 상태 여부
S : 적립 상태
N : 미적립 상태
A : 적립/미적립 모두 보유 상태
stampStartNumber
Integer
스탬프 해당 회차 기준 시작 숫자
ex)
1회차 : 1
2회차 : 10
3회차 : 19
4회차 : 28
storyMsg
String
표출 스토리 문구
ex)
주행 적립하면
9회차에 캐시 룰렛 도착!
rouletteButtonActive
String
룰렛 버튼 활성화/비활성화 여부
Y : 활성화
N : 비활성화
rouletteButtonMsg
String
룰렛 버튼 표출 문구
ex) 캐시 룰렛 도착!
skpEventInfo
Object
SKP 이벤트 관련 정보(2023년 12월 31일 이후 제거 예정)
┣ url
String
SKP URL
ex)  https://www.inavisys.com/
┗date
String
날짜 (yyyyMMdd)
ex)20231231
```

## 에어 캐시 스탬프 룰렷 게임

```
에어 캐시 스탬프 룰렛 게임
Function
에어 캐시 스탬프 룰렛 게임
URL
/cashStampRouletteGame
Request Header
Request Parameter
parameter
type
requisite
description
결과 없음
Response Parameter
parameter
type
description
result_code
String
결과 코드
0 : 성공
970 : 에어 캐시 정합성 체크 실패 (캐시 어뷰징 의심)
972 : 에어캐시 스탬프 룰렛 이용권 미존재
999 : 정의 되지 않은 오류
result_msg
String
결과코드에 따른 메세지
cash
Integer
당첨 캐시
```

## 에어 캐시 스탬프 룰렷 이용권 조회

```
에어 캐시 스탬프 룰렛 이용권 조회
Function
에어 캐시 스탬프 룰렛 이용권 조회
URL
/cashStampRouletteTicket
Request Header
Request Parameter
parameter
type
requisite
description
결과 없음
Response Parameter
parameter
type
description
result_code
String
결과 코드
0 : 성공
999 : 정의 되지 않은 오류
result_msg
String
결과코드에 따른 메세지
count
Integer
이용권 횟수
```


# 9. w3w

## 3단어 추천어 검색

```
3단어 추천어 검색
Function
3단어 추천어 검색 (w3w)
URL
/w3w/autoSuggest
Request Header
Request Parameter
parameter
type
requisite
description
words
String
O
w3w 추천어 검색을 위한 .으로 구분 된 세 단어
EX)
- 닮은.조언.ㄱ
- 닮은.조언.감사
posx
String
O
현재 위치 정규화 X 좌표
EX) 160337
posy
String
O
현재 위치 정규화 Y 좌표
EX) 501885
Response Parameter
parameter
type
description
result_code
String
결과 코드
0 : 성공
610 : w3w 추천어 검색 파라미터 오류
903 : 조회 결과 없음
999 : 정의 되지 않은 오류
result_msg
String
결과값에 따른 메세지
autoSuggestList
Array
w3w 추천어 검색 결과 리스트
┣ words
String
w3w 추천어
┣ admcode
String
행정코드
2023-06-21 패치로 인해 Empty String 리턴
┣ x
String
정규화 X 좌표
EX) 160337
2023-06-21 패치로 인해 Empty String 리턴
┣ y
String
정규화 Y 좌표
EX) 501885
2023-06-21 패치로 인해 Empty String 리턴
┣ address
String
주소
2023-06-21 패치로 인해 Empty String 리턴
┣ cut_address
String
표출 주소
┣ road_address
String
도로명 주소
2023-06-21 패치로 인해 Empty String 리턴
┣ cut_road_address
String
축약 도로명 주소
2023-06-21 패치로 인해 Empty String 리턴
┣ jibun
String
지번
2023-06-21 패치로 인해 Empty String 리턴
┣ bldnum
String
빌딩번호
2023-06-21 패치로 인해 Empty String 리턴
┣ address_type
String
주소 매핑 타입0 : 행정계1 : 새주소 폴리곤2 : 지적도 폴리곤3 : 인접지번4 : 행정계
2023-06-21 패치로 인해 Empty String 리턴
┗ distanceToFocusKm
Integer
현재 지점에서의 거리 (km)
```

## w3w 단어 검색

```
w3w 단어 검색
Function
w3w 단어 검색
URL
/w3w/wordSearch
Request Header
Request Parameter
parameter
type
requisite
description
words
String
O
w3w 추천어 검색을 위한 .으로 구분 완성 된 세 단어
EX)
- 닮은.조언.감사
Response Parameter
parameter
type
description
result_code
String
결과 코드
0 : 성공
610 : w3w 단어 검색 파라미터 오류  (EX : 닮.조.감)
903 : 조회 결과 없음
999 : 정의 되지 않은 오류
result_msg
String
결과값에 따른 메세지
admcode
String
행정코드
x
String
정규화 X 좌표
EX) 160337
y
String
정규화 Y 좌표
EX) 501885
address
String
주소
cut_address
String
축약 주소
road_address
String
도로명 주소
cut_road_address
String
축약 도로명 주소
jibun
String
지번
bldnum
String
빌딩번호
address_type
String
주소 매핑 타입0 : 행정계1 : 새주소 폴리곤2 : 지적도 폴리곤3 : 인접지번4 : 행정계
```


# 10. 캐시버튼

## 에어 캐시 전환

```
에어 캐시 전환
안상언
2024. 08. 14. (편집됨)
[Request Parameter] - [version] 추가 (아바티 API 변경에 따른 기존 아바티 API, 신규 아바티 API 호출 구분 파라미터)
안상언
2024. 08. 22. (편집됨)
[Request Parameter] - [basicToken] 추가 (아바티 API 변경에 따른 신규 아바티 API 호출에 필요한 Header Authorization 추가)
Function
에어 캐시 전환 (캐시버튼 캐시 → 에어 캐시 전환)
URL
/cashButton/cashConversion
Request Header
Request Parameter
parameter
type
requisite
description
transactionID
String
O
캐시버튼 SDK에서 전달받은 요청ID
basicToken
String
verrsion v3의 호출 시, 필수
아바티 API 호출에 필요한 Header 내 Authorization
version
String
아바티 호출 API 구분자
null: /shop/exchange/verify
v3: /shop/exchange/verifyV3
Response Parameter
parameter
type
description
result_code
String
결과 코드
0 : 성공
630 : 캐시버튼 연동 오류
970 : 에어 캐시 정합성 체크 실패
(캐시 어뷰징 의심)
999 : 정의 되지 않은 오류
result_msg
String
결과값에 따른 메세지
```


# 11. HUD

## S/N 인증

```
S/N 인증
Function
S/N 인증
URL
/authSerialNumber
Request Header
Request Parameter
parameter
type
requisite
description
serialNumber
String
O
시리얼 번호
hudType
String
hudType (null인 경우 iHUD, 신규 앱인경우 해당 값을 채워 전송)
EX) air
Response Parameter
parameter
type
description
result_code
String
결과 코드
0 : 성공
200 : 인증되지 않은 시리얼 번호
result_msg
String
결과값에 따른 메세지
```


# 12. 신호등

## 방향코드

```
방향코드
Definition
대구 신호등 방향 코드를 정의 합니다.
방향

코드

북

10

동

20

남

30

서

40

북동

50

남동

60

남서

70

북서

80
```

## 전체 신호등 정보 조회

```
전체 신호등 정보 조회
Function
전체 신호등 정보 조회
URL
/trafficLightList
Request Header
Request Parameter
parameter
type
requisite
description
Response Parameter
parameter
type
description
result_code
String
결과 코드
0 : 성공
result_msg
String
결과값에 따른 메세지
ver
String
대구 신호등 전체 리스트 버전 정보
ex) ver0.1
info_list
Array
대구 신호등 전체 리스트 JSON 데이터
┣ nodeID
Long
신호등 Node ID
ex) 1570062500
┣ nodeType
Byte
Node 형태
1 : 교차로 중심
2 : 안내 신호등
┣ nodeName
String
Node 명칭
ex) “국가산단04”
┣ compassCode
Byte
방향코드
┣ longitude
Integer
경도
ex) 272693
┣ latitude
Integer
위도
ex) 306482
┣ angle
Integer
진입 각도
EX) 0
┗ mapID
Integer
Map ID
ex) 4101
```

## 신호등 상태 조회

```
신호등 상태 조회
Function
신호등 상태 조회
URL
/trafficLightStatus
Request Header
Request Parameter
parameter
type
requisite
description
nodeID
String
O
신호등 Node Id (Node ID)
compassCode
String
O
신호등 방향 코드 (compassCode)
방향코드
Response Parameter
parameter
type
description
result_code
String
결과 코드
0 : 성공
result_msg
String
결과값에 따른 메세지
info_list
Array
신호등 상태 정보 리스트
┣ operationInfo
String
신호등 운영 정보
EX) 정상, 전이, 감응, 소등, 점멸, 수동
┣ wrongInfo
String
신호등 이상 정보
EX) 정상, SCU 통신 이상, 센터 통신 이상, 모순 이상
┣ opIdx
Integer
신호등 운영 주기  (신호등 운영 사이클에 대한 진행 시간을 초로 표기한 값)
진행 시간 : 초
┣ roadType
String
신호등의 종류
EX) 미지정, 직진, 좌회전, 보행자, 자전거, 우회전, 버스, 유턴
┣ seeTime
Integer
신호 상태 표출 시간
┣ remainTime
Integer
신호 상태 잔여 시간
┣ color
String
신호등 색상
EX) 소등, 적색 점등, 황색 점등, 녹색 점등, 적색 점멸, 황색 점멸, 녹색 점멸
┣ varTime
String
신호등 시간의 가변 유무
┗  timeStmp
Integer
정보가 들어온 시간 Time Stamp
```

## 보행자 신호등 정보 조회

```
보행자 신호등 정보 조회
Function
보행자 신호등 정보 조회
URL
/trafficLightWalker
Request Header
Request Parameter
parameter
type
requisite
description
nodeID
String
O
신호등 Node Id (Node ID)
Response Parameter
parameter
type
description
result_code
Byte
결과 코드
0 : 성공 1 : 데이터 없음 2 : 서버 응답 없음
result_msg
String
결과값에 따른 메세지
nodeID
Long
요청한 NodeID
listCnt
Integer
보행자 신호등 정보 리스트 개수
info_list
Array
신호등 상태 정보 리스트
┣ bearingCode
Integer
방향 코드
┣ trafLighAnomInfo
Integer
신호등 이상 정보
EX) 정상, SCU 통신 이상, 센터 통신 이상, 모순 이상
┣ signlExtnYn
Integer
신호 상태의 연장 여부
┣ wtrmsCrosngYn
Integer
무단 횡단자 존재 여부
┣ leftBearingCode
Integer
왼쪽 신호등 방향 코드
┣ leftWalkerYN
Integer
왼쪽 신호등의 보행자 여부
┣ leftAwaiteYN
Integer
왼쪽 신호등 대기자 여부
┣ rightBearingCode
Integer
오른쪽 신호
┣ rightWalkerYN
Integer
오른쪽 신호등 보행자 여부
┣ rightAwaiterYN
Integer
오른쪽 신호등 대기자 여부
┣ remainingTime
Integer
신호 상태 잔여 시간
┣ pedSignalState
String
신호등 색상
R: 적색등
G: 녹색등
GF : 녹색 깜빡임
┗  timeStmp
Integer
정보가 들어온 시간
EX) 1689560090
```


# 13. 음성광고

## 하루 최대 수신 광고 수

```
하루 최대 수신 광고 수
Function
하루 최대 수신 광고 수
URL
/onAirDailyCount
Request Header
Request Parameter
parameter
type
requisite
description
결과 없음
Response Parameter
parameter
type
description
result_code
String
결과 코드
0 : 성공
result_msg
String
결과값에 따른 메세지
count
Integer
당일 광고 재생 가능 수 (0인 경우 당일 수신 가능한 광고 모두 수신 한 상태)
```

## 온에어 음성 파일 조회

```
온에어 음성 파일 조회
Function
온에어 음성 파일 조회
URL
/onAirVoiceFileInfo
Request Header
Request Parameter
parameter
type
requisite
description
hashTag
String
URL 인코딩 된 해시 태그
EX)
%ED%95%B4%EC%8B%9C%ED%83%9C%EA%B7%B8
Response Parameter
parameter
type
description
result_code
String
결과 코드
0 : 성공
403 : 조회 조건에 해당하는 온에어 음성 정보 미존재
result_msg
String
결과값에 따른 메세지
todayAdPlayable
Boolean
당일 광고 재생 가능 여부
true : 재생 가능
false : 재생 불가 (하루에 들을수 있는 최대 광고 갯수 초과)
onAirFile
Object
온에어 음성파일 정보
┣ url
String
온에어 음성 파일 URL
┣ playTime
Integer
재생 시간
┣ onAirId
String
음성 파일 고유 ID
┗  onAirHashId
Integer
음성 파일 해시 값
```

## 온에어 수신 시작

```
온에어 수신 시작
Function
온에어 수신 시작
URL
/onAirListenStart
Request Header
Request Parameter
parameter
type
requisite
description
onAirId
String
O
수신 시작 음성 파일 고유 ID
Response Parameter
parameter
type
description
result_code
String
결과 코드
0 : 성공
result_msg
String
결과값에 따른 메세지
onAirTrid
String
트랜잭션 ID
```

## 온에어 수신 완료

```
온에어 수신 완료
Function
온에어 수신 완료
URL
/onAirListenFinish
Request Header
Request Parameter
parameter
type
requisite
description
onAirId
String
O
수신 완료 된 음성 파일 고유 ID
onAirTrid
String
O
수신 시작 시 응답 받은 트랜잭션 ID
Response Parameter
parameter
type
description
result_code
String
결과 코드
0 : 성공
401 : 수신하지 않은 온에어 정보
402 : 이미 수신 완료한 온에어 정보
970 : 에어 캐시 정합성 체크 실패
(캐시 어뷰징 의심)
result_msg
String
결과값에 따른 메세지
```


# 14. 메인화면-AIR

## 날씨정보

```
날씨정보
Function
날씨정보
URL
/weather
Request Header
Request Parameter
parameter
type
requisite
description
coordinations
Array
날씨 정보를 받고싶은 위치의 좌표
┣ x
String
O
날씨정보를 받고싶은 위치의 x좌표, wgs84 X값
┗ y
String
O
날씨정보를 받고싶은 위치의 y좌표, wgs84 Y값
Response Parameter
parameter
type
description
result_code
String
결과 코드
result_msg
String
결과코드에 따른 메세지
weatherList
Array
날씨정보
┣x
String
요청된 wgs84 X값
┣y
String
요청된 wgs84 Y값
┣obs_time
String
관측시간
┣wind_dir
String
풍향 (한글표기 16방향)
┣wind_speed
String
풍속 (m/s)
┣temperature
String
현재기온
┣rel_humidity
String
상대습도
┣ wti_code
String
날씨 매칭 코드해당 정보로 아이콘 표출1 맑음 2 구름 많음 3 흐림 4 비5 눈 6 눈비 7 소나기 10 뇌우13 흐리고 비 14 흐리고 눈15 흐리고 눈비 22 미세먼지
┣wx
String
현재날씨
┗precipitation
String
강수량
```

## 통합메인화면

```
통합메인화면
Function
통합메인화면
URL
/mainPageData
Request Header
Request Parameter
parameter
type
requisite
description
currentLocX
String
O
정규화 X값
currentLocY
String
O
정규화 Y값
oilCateCode
String
O
사용자의 선호 주유소 catecode(Default:C0100)Category Code
oilSortopt
String
O
정렬 옵션1 : 거리순2 : 명칭순3 : 휘발유 가격순(주유소 검색시)4 : 고급휘발유 가격순(주유소 검색시)5 : 경유 가격순(주유소 검색시)6 : LPG 가격순(주유소 검색시)7 : 평점 순 정렬(2016.11월 기준 망고플레이트 데이터에 한함)Default : 3
requestType
Array
O
요청할 정보들
InterestingPlaceWeather
MyAirMileage
TodayAccumulateMileage
NearHotPlace
NearHotPlaces
NearLowestOil
NearLowestOils
MyDrivingScore
LastDrivingRecord
AirMileU
lbsLuckyBox
todaysFortune
AirCash
isWiget
boolean
O
현재 IOS만 필수값위젯여부
weatherCoordinations
Array
날씨정보 요청할때 추가로 더 보고싶은곳(ex:도착지) 에대한 좌표
┣ x
String
정규화 X값
┗ y
String
정규화 Y값
Response Parameter
parameter
type
description
결과 없음
```

## 오늘의운세 날짜유효성체크

```
오늘의운세 날짜유효성체크
Function
오늘의운세 날짜유효성 체크
URL
/fortuneBirthCheck
Request Header
Request Parameter
parameter
type
requisite
description
birthday
String
O
생년월일EX(19881230) -> YYYYMMDD
Response Parameter
parameter
type
description
result_code
String
결과 코드
result_msg
String
결과값에 따른 메세지
lunar
boolean
음력날짜 존재여부
sLunar
boolean
윤달 음력날짜 존재여부
```


# 15. 그룹주행-AIR

## 그룹만들기

```
그룹만들기
Function
그룹 만들기
URL
/makeGroup
Request Header
Request Parameter
parameter
type
requisite
description
destiName
String
도착지 이름
destiPoiId
String
도착지 poiId
destiX
String
O
도착 좌표x (정규화)
destiY
String
O
도착 좌표y (정규화)
Response Parameter
parameter
type
description
result_code
String
결과 코드
result_msg
String
결과코드에 따른 메세지
groupId
String
그룹아이디
shortenURL
String
숏URL(기능 구현 후 검토 예정)
```

## 현재 위치 업로드

```
현재 위치 업로드
Function
현재 위치 업로드
URL
/rris/data/currentLoc
Request Header
Request Parameter
parameter
type
requisite
description
x
String
O
X좌표
y
String
O
Y좌표
coordType
String
O
좌표 타입W : WGS84R : 탐색 좌표S : 검색 좌표
myInfo
Object
그룹주행이 아닐경우 오브젝트 안보내면됨
├ groupId
String
O
그룹아이디
├ remainDistance
String
O
목적지까지 남은거리
├ remainTime
String
O
목적지까지 남은시간단위 : 초
├ desX
String
O
목적지 X좌표 (TW index)
├ desY
String
O
목적지 Y좌표 (TW index)
├ desPoi
String
목적지 POIID
├ desName
String
목적지 이름
├ snsId
String
snsID(sns사용자일 경우)
├ snsType
String
snsTypeg:구글, k:카카오, f:페이스북, n:네이버(sns사용자일 경우)
┗ allowList
List
위치공유를 허용할 상대방의 privateKey리스트 (항상 최신 스냅샷을 보내야함)
rrisObject
Object
rris Object rris 아닐경우 오브젝트 안보내도됨
├ mapVer
String
O
지도 버전
├ speed
Integer
O
현재 주행 속도(km/h)
├ bearing
Integer
O
진행 각도
┗ link
Object
O
현재 도로 mr link 정보
├ mapId
Integer
O
mapId
├ linkId
Integer
O
linkId
├ nodeId
Integer
O
nodeId
┗ direction
Integer
O
direction
Response Parameter
parameter
type
description
결과 없음
```

## 그룹나가기

```
그룹나가기
Function
그룹 나가기
URL
/groupUpdate
Request Header
Request Parameter
parameter
type
requisite
description
groupId
그룹ID
status
O
String
나가기 : E (지금은 나가기만 하기떄문에 E로 전달해주시면됩니다)
Response Parameter
parameter
type
description
result_code
String
결과 코드
result_msg
String
결과코드에 따른 메세지
```

## 위치제공사실조회

```
위치제공사실조회
Function
위치제공사실조회
URL
/groupDrivingHis
Request Header
Request Parameter
Response Parameter
parameter
type
description
result_code
String
결과 코드
result_msg
String
결과값에 따른 메세지
his
Array
위치제공사실조회 이력(최근1달간)
├ positioningMdn
String
측위자(자신의 위치를 조회 한 사람) 암호화된 MDN
├ startDate
String
시작시점(YYYYMMDDHHMISS)
├ endDate
String
종료시점(YYYYMMDDHHMISS)
├ count
String
측위횟수
```


# 16. 오픈POI-AIR

## 오픈POI만들기

```
오픈POI만들기
Function
오픈POI만들기
URL
/makeOpenPoi
Request Header
Request Parameter
parameter
type
requisite
description
mode
String
O
오픈POI이름 접속경로POI : 장소검색등록SHARE : 위치공유등록
name
String
O
오픈POI이름
ilon
String
O
출발지 경도, 정규화좌표 X값
ilat
String
O
출발지 위도, 정규화좌표 Y값
private_key
String
O
오픈POI만드는 유저의 private_key
start_dt
String
O
OPENPOI 표시 시작시간
end_dt
String
O
OPENPOI 표시 종료시간
Response Parameter
parameter
type
description
result_code
String
결과 코드
result_msg
String
결과코드에 따른 메세지
openPoiId
String
오픈Poi아이디
```

## 오픈POI 상세조회

```
오픈POI 상세조회
Function
오픈POI상세조회
URL
/getOpenPoi
Request Header
Request Parameter
parameter
type
requisite
description
name
String
O
오픈POI이름
openPoiId
String
O
오픈Poi아이디
Response Parameter
parameter
type
description
result_code
String
결과 코드
result_msg
String
결과코드에 따른 메세지
openPoi
Object
오픈Poi정보
┣ name
String
오픈POI이름
┣ ilon
String
출발지 경도, 정규화좌표 X값
┣ ilat
String
출발지 위도, 정규화좌표 Y값
┣ start_dt
String
OPENPOI 표시 시작시간
┣ end_dt
String
OPENPOI 표시 종료시간
┗ openPoiId
String
오픈Poi 아이디
```

## 오픈POI 검색

```
오픈POI 검색
Function
오픈POI 검색
URL
/searchOpenPoi
Request Header
Request Parameter
parameter
type
requisite
description
query
String
O
검색하고자 하는 OPENPOI이름(초성검색 안됨)
Response Parameter
parameter
type
description
result_code
String
결과 코드
result_msg
String
결과코드에 따른 메세지
openPoi
Array
openPoi정보
┣ name
String
검색 결과이름
┗ openPoiId
String
오픈Poi 아이디
```


# 17. AIR 서비스

## 이용 약관 조회(AIR)

```
이용 약관 조회(AIR)
Function
이용약관 조회Request Header 중 개인키, 인증키 값 없이 호출
URL
/clauseCheck
Request Header
Request Parameter
Response Parameter
parameter
type
description
result_code
String
결과 코드
result_msg
String
결과값에 따른 메세지
total_ver
String
이용약관 통합 버전
url_list
Array
이용약관 리스트 (기존 약관 리스트)
┣ url_name
String
이용약관 번호termNew1 : 개인정보 처리방침 [필수]termNew2 : 서비스 및 위치정보 이용약관 [필수]termNew3 : 개인정보 수집 동의 [필수]termNew4 : 만 14세 이상 이용 동의 [필수]termNew5 : 정보 및 광고수신 동의 [선택]
┗ url_path
String
이용약관 URL
url_list_v2
Array
이용약관 리스트 (신규 약관 리스트)
┣ url_name
String
이용약관 번호termLatest1 : 서비스 및 위치정보 이용약관 [필수]termLatest2 : 개인정보 수집·이용 동의 [필수]termLatest3 : 만 14세 이상 이용 동의 [필수]termLatest4 : 개인정보 제3자 제공 동의 [선택]termLatest5 : 정보 및 광고수신 동의 [선택]termLatest6 : 개인정보 처리방침
┗ url_path
String
이용약관 URL
```

## 이용 약관 동의 및 개인 키 생성(AIR)

```
이용 약관 동의 및 개인 키 생성(AIR)
Function
이용약관 동의 및 개인키 생성Request Header 중 개인키, 인증키 값 없이 호출
URL
/clauseAgree
Request Header
Request Parameter
parameter
type
requisite
description
device_id
String
O
단말 고유 값Android : IMEIiOS : UUID
ip
String
단말 IP (iOS일 경우만)
mymenu_status
String
O
마이메뉴 동의 여부0 : 동의안함1 : 동의함
ad_status
String
O
광고 수신 동의 여부0 : 동의안함1 : 동의함
prov_status
String
O
개인정보 3자 제공 동의 여부0 : 동의안함1 : 동의함
Response Parameter
parameter
type
description
result_code
String
결과 코드
result_msg
String
결과값에 따른 메세지
private_key
String
개인키
company
String
통신사KT / SKT / LGU / ETC
```

## 지도 다운로드 정보 조회(AIR)

```
지도 다운로드 정보 조회(AIR)
Function
지도 다운로드 정보 조회Request Header 중 인증키 값 없이 호출
URL
/mapDownloadInfo
Request Header
Request Parameter
parameter
type
requisite
description
smr_ver
String
SMR Version (Map Version)
SMR :  도로 정보
smdc_ver
String
SMDC Version
SMDC : 배경 dp (타일 별 정보, 새로운 도역 정보)
Response Parameter
parameter
type
description
result_code
String
결과 코드
result_msg
String
결과값에 따른 메세지
map_info
Object
MAP 버전 정보
┣ map_status
String
업데이트 여부"T" : 업데이트 필요"F" : 업데이트 불필요
┣ smr_ver
String
최신 SMR Version(Map Version)
┣ smr_url
String
SMR 데이터 URL
┣ smdc_ver
String
SMDC Version
┣ smdc_url
String
SMDC 데이터 URL
┣ init_dataSet
String
초기 데이터 XML
┣ init_serverUrl
String
초기 데이터 URL
┣ full_dataSet
String
전체 데이터 XML
┗ full_serverUrl
String
전체 데이터 URL
gp_info
Object
안전운행 데이터 정보
┣ gp_ver
String
최신 안전운행 데이터 버전
┣ gp_url
String
안전운행 데이터 URL
┣ gp_extractPath
String
안전운행 데이터 압축해제 경로
┗ gp_fileSize
String
안전운행 데이터 파일 크기
aero_info
Object
항공 지도 정보
┣ aero_url
String
항공 지도 URL
┣ data_set
String
항공 지도 data set
┗ server_url
String
항공 지도 server URL
```

## 서비스 메인(AIR)

```
서비스 메인(AIR)
안상언
2024. 08. 14. (편집됨)
•  [Response] - [gen_ai_flag] 추가
•  [Response] - [gen_ai_max_token] 추가
•  [Response] - [cp_hud_flag] 추가
👍
2
답글 2개 더 보기
김
김희정
2025. 09. 08.
• [Response] - [airbotAuthKey] 추가
Function
서비스 메인 Request Header 중 인증키 값 없이 호출하며, 이후 다른 I/F 호출시 결과로 받은 인증키값 사용
URL
/serviceGate
Request Header
Request Parameter
parameter
type
requisite
description
reg_id
String
O
push id (Android) or device token (iOS)
app_ver
String
O
App Version
smr_ver
String
O
SMR Version (Map Version)
smdc_ver
String
O
SMDC Version
gp_ver
String
O
안전운행 Version
clause_ver
String
O
약관 Version
channel
String
유입 경로NOR : 정상실행
Response Parameter
parameter
type
description
결과 없음
더 불러오기
```


# 18. AIR 나의주행

## 나의주행 주간요약바(AIR)

```
나의주행 주간요약바(AIR)
Function
나의주행 주간요약 바
URL
/weeklyMyHabit
Request Header
Request Parameter
Response Parameter
parameter
type
description
result_code
String
결과 코드
result_msg
String
결과값에 따른 메세지
weeklyHabitList
List
최근 1주일간 주행 습관 리스트
┣ date
String
년.월.일
┗ habitList
List
해당날짜 습관 리스트
┣ count
String
일일 발생 갯수
┗ habit
String
행위1: 차선이탈10: 전방추돌경고100: 급감속101: 급가속
```

## 나의주행 일별 리스트(AIR)

```
나의주행 일별 리스트(AIR)
Function
나의주행 일별 리스트
URL
/myDailyDrivingList
Request Header
Request Parameter
parameter
type
requisite
description
date
String
O
조회하고자 하는 날짜(default : 당일)
Response Parameter
parameter
type
description
result_code
String
결과 코드
result_msg
String
결과값에 따른 메세지
drivingList
List
주행리스트
┣ drivingId
String
주행Id
┣ day
String
주행날짜
┗ timeRange
String
시간범위
```

## 나의주행 상세(AIR)

```
나의주행 상세(AIR)
Function
나의주행 상세
URL
/drivingHabitDetail
Request Header
Request Parameter
parameter
type
requisite
description
drivingId
String
O
주행ID
Response Parameter
parameter
type
description
result_code
String
결과 코드
result_msg
String
결과값에 따른 메세지
distance
String
주행거리
timeTaken
String
주행시간 Min
pointList
List
주행 좌표 리스트
┣ x
String
x좌표 (TWCoord)
┣ y
String
y좌표 (TWCoord)
┗ habit
Object
해당주행내 습관
┣ address
String
주소
┣ time
String
해당좌표 지나갈때 시간
┣ firstSpeed
String
habit이 급가속 급감속일때만 내려줌 아닐씨 emptyString처음속도
┣ secondSpeed
String
habit이 급가속 급감속일때만 내려줌 아닐씨 emptyString바뀐속도
┗ habit
String
행위1: 차선이탈10: 전방추돌경고100: 급감속101: 급가속
```

## 나의주행 월별 리스트(AIR)

```
나의주행 월별 리스트(AIR)
Function
나의주행 월별 리스트
URL
/monthlyMyDriving
Request Header
Request Parameter
parameter
type
requisite
description
date
String
O
조회하고자 하는 년월
Response Parameter
parameter
type
description
result_code
String
결과 코드
result_msg
String
결과값에 따른 메세지
monthlyDrivingList
List
월간 주행 리스트
┣ x
String
x좌표 (TWCoord)
┣ y
String
y좌표 (TWCoord)
┣ drivingId
String
주행Id
┣ day
String
주행날짜
┗ timeRange
String
시간범위
```


# 19. LOG-AIR

## 제보하기

```
제보하기
Function
제보하기 로그전송
URL
/reportLog
Request Header
Request Parameter
parameter
type
requisite
description
category
String
O
제보하기 화면 카테고리MAP : 지도문제TRAFFIC : 교통CAMERA : 카메라ACCIDENT : 사고PLACE : 장소등록ETC : 기타
index
String
O
카테고리별 세부항목 (세부항목이 가변적이므로 index 번호로 입력) (0... )
Response Parameter
parameter
type
description
result_code
String
결과 코드
result_msg
String
결과코드에 따른 메세지
```


# 20. 삼성중공업 SDK

## 이동불가 구역/출입금지 구역 정보 조회

```
이동불가 구역/출입금지 구역 정보 조회
Function
이동불가 구역/출입금지 구역 정보 조회
URL
/shiSdk/getTFlimitInfo
Request Header
Request Parameter
parameter
type
requisite
description
결과 없음
Response Parameter
parameter
type
description
result_code
String
결과 코드
0 : 성공
903 : 조회결과 없음
999 : 정의되지 않은 오류
result_msg
String
결과코드에 따른 메세지
limitList
Array
이동불가/출입금지 구역 정보 리스트
┣ lon
String
WGS 84 경도 (EX : 127.11077678260982)
┣ lat
String
WGS 84 위도 (EX : 37.40219377747615)
┣ nodeid
String
node 아이디 (EX : 1234)
┣ mapid
String
지도 아이디 (EX : 1234)
┣ linkid
String
링크 아이디 (EX : 1234)
┣ dir
String
방향 코드 (EX : 0)
┣ limitStdt
String
제한시작일자 (EX : 20230630)
┣ limitSttm
String
제한시작시간 (EX : 0700)
┣ limitFndt
String
제한종료일자 (EX : 20230630)
┣ limitFntm
String
제한종료시간 (EX : 0930)
┗ weightType
String
중량 타입
0 : 중량 상관 없이 회피 탐색 (Default)
1 : 4톤 미만 차량에 대해 회피 탐색
2 : 4톤 이상 차량에 대해 회피 탐색
```

## 운행금지시간 정보 조회

```
운행금지시간 정보 조회
Function
운행금지시간 정보 조회
URL
/shiSdk/getDrivStopInfo
Request Header
Request Parameter
parameter
type
requisite
description
결과 없음
Response Parameter
parameter
type
description
result_code
String
결과 코드
0 : 성공
903 : 조회결과 없음
999 : 정의되지 않은 오류
result_msg
String
결과코드에 따른 메세지
stopList
Array
운행금지시간 정보 리스트
┣ zoneId
String
구역 정보 (EX : "zone02_01" //공장내 운행금지)
┣ limitSttm
String
제한시작시간 (EX : 0650)
┗ limitFntm
String
제한종료시간 (EX : 0730)
```

## 중대재해 발생 구역 정보 조회

```
중대재해 발생 구역 정보 조회
Function
중대재해 발생 구역 정보 조회
URL
/shiSdk/getDisasterInfo
Request Header
Request Parameter
parameter
type
requisite
description
결과 없음
Response Parameter
parameter
type
description
result_code
String
결과 코드
0 : 성공
903 : 조회결과 없음
999 : 정의되지 않은 오류
result_msg
String
결과코드에 따른 메세지
disasterList
Array
중대재해 발생 구역 정보 리스트
┣ lon
String
WGS 84 경도 (EX : 127.11077678260982)
┣ lat
String
WGS 84 위도 (EX : 37.40219377747615)
┣ mapid
String
지도 아이디 (EX : 1234)
┣ linkid
String
링크 아이디 (EX : 1234)
┣ dir
String
방향 코드 (EX : 0)
┣ etcFlag
String
중대재해 코드 (EX : 01)
(01: 사망 , 02 : 위험 , 03)
┣ viewFlag
String
화면표시 Y/N (EX : Y)
┗ soundFlag
String
음향표시 Y/N (EX: Y)
```

## SHI GPS Data 전송

```
SHI GPS Data 전송
Function
SHI GPS Data 전송
URL
/shiSdk/sendShiGps
Request Header
Request Parameter
parameter
type
requisite
description
paramList
ArrayList
O
GPS 정보 리스트
┣ userId
String
O
사용자 ID
┣ speed
Integer
O
속도
┣ lat
double
O
위도
┣ lon
double
O
경도
┣ angle
double
O
정북기준각도
┣ overSpeedYn
String
O
속도위반여부 (Y/N)
┣ pathVolnYn
String
O
경로위반여부 (Y/N)
┣ limitLocEntrYn
String
O
제한구역진입여부 (Y/N)
┣ mapId
String
O
MapID 해당 위경도에 맞는 실제 ID 값
┣ linkId
String
O
linkID 해당위경도에 맞는 실제 ID 값
┣ dir
String
O
방향코드
┗ timeStamp
String
unix timestamp(초단위) → “2023-11-23 발행 SDK 부터 적용”
Response Parameter
parameter
type
description
result_code
String
결과 코드
0 : 성공
999 : 정의되지 않은 오류
result_msg
String
결과코드에 따른 메세지
```

## 일단 정지 구역 정보 조회

```
일단 정지 구역 정보 조회
Function
일단 정지 구역 정보 조회
URL
/shiSdk/getStopAreaInfo
Request Header
Request Parameter
parameter
type
requisite
description
결과 없음
Response Parameter
parameter
type
description
result_code
String
결과 코드
0 : 성공
903 : 조회결과 없음
999 : 정의되지 않은 오류
result_msg
String
결과코드에 따른 메세지
stopAreaList
Array
일단 정지 구역 정보 리스트
┣ mapid
String
맵 ID
EX ) 4379
┣ linkid
String
링크 ID
EX) 64
┗ dir
String
방향 코드
EX) 1
```


# 21. 통계

## 전체 사용자 조회

```
전체 사용자 조회
Function
전체 사용자 조회
URL
/statistics/totalUser
Request Header
Response Parameter
parameter
type
description
totalLoginUserCount
Integer
로그인 사용자 수
totalNoLoginUserCount
Integer
미로그인 사용자 수
```

## 월별 신규 가입 유저

```
월별 신규 가입 유저
Function
월별 신규 가입 유저
URL
/statistics/newUser
Request Header
Request Parameter
parameter
type
requisite
description
year
String
O
조회하고자 하는 년도
month
String
O
조회하고자 하는 월
Response Parameter
parameter
type
description
monthlyNewUserCount
String
월별 건수
```

## 월별 주행이력

```
월별 주행이력
Function
월별 주행이력
URL
/statistics/drivingHistory
Request Header
Request Parameter
parameter
type
requisite
description
year
String
O
조회하고자 하는 년도
month
String
O
조회하고자 하는 월
Response Parameter
parameter
type
description
monthlyLoginUserDrivingHistoryCount
String
월별 로그인 사용자 주행 건수
monthlyNoLoginUserDrivingHistoryCount
String
월별 미로그인 사용자 주행 건수
```

## 월별 캐쉬 적립 사용자

```
월별 캐쉬 적립 사용자
Function
월별 캐쉬 적립 사용자
URL
/statistics/cashedUser
Request Header
Request Parameter
parameter
type
requisite
description
year
String
O
조회하고자 하는 년도
month
String
O
조회하고자 하는 월
Response Parameter
parameter
type
description
monthlyCashedUserCount
String
월별 캐쉬 지급 받은 사용자 수
```


# 22. 오르다(ORDA)

## [ORDA] 가까운 스탬프 조회

```
[ORDA] 가까운 스탬프 조회
Function
가까운 스탬프 정보 조회
URL
/orda/stamp
Request Header
Request Parameter
이름
타입
필수
설명
x
String
필수
APP 현재 위치 X(WGS84)
y
String
필수
APP 현재 위치 Y(WGS84)
Response
이름
타입
Nullable
설명
result_code
String
false
결과 코드

0: 성공
921: 오르다 서버 연동 오류
result_msg
String
false
응답 문구
linkUrl
String
false
Orda 앱연동 백링크 URL
stamp
Object
true
Stamp 객체
Stamp 객체
Response Parameter
이름
타입
Nullable
설명
id
String
false
스탬프 식별값
tourId
String
false
투어 ID
tourName
String
false
투어명
name
String
false
스탬프 이름
address
String
true
주소
imageUrl
String
true
스태프 이미지 URL
x
String
false
스탬프 위치 X(WGS84)
y
String
false
스탬프 위치 Y(WGS84)
distance
Integer
true
현재 위치로부터 거리 (단위: M)
```


# 23. 제보하기

## 제보하기 등록

```
제보하기
제보하기 등록
```

