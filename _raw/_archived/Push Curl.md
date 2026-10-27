

[일반 push]

curl -X POST \
 https://fcm.googleapis.com/fcm/send \
 -H 'authorization: key=[FCM_SERVER_KEY_REMOVED]' \
 -H 'cache-control: no-cache' \
 -H 'content-type: application/json;charset=UTF-8' \
 -H 'postman-token: [REMOVED]' \
 -d '{"data":{"nt":"FCM PUSH TITLE","pt":"popup_title","pc":"popup_content","type":"D","subtype":"CI","url":"","collapskey":"HJ_TYPE"},"to":"[FCM_DEVICE_TOKEN_REMOVED]"}
'


curl -X POST \
 https://fcm.googleapis.com/fcm/send \
 -H 'authorization: key=[FCM_SERVER_KEY_REMOVED]' \
 -H 'cache-control: no-cache' \
 -H 'content-type: application/json;charset=UTF-8' \
 -H 'postman-token: [REMOVED]' \
 -d '{"data":{"nt":"FCM PUSH TITLE","pt":"팝업 타이틀","pc":"팝업콘텐츠팝업콘텐츠 팝업콘텐츠 팝업콘텐츠팝업콘텐츠 ","type":"E","subtype":"CI","url":"","collapskey":"HJ_TYPE"},"to":"[FCM_DEVICE_TOKEN_REMOVED]"}
'


curl -X POST https://fcm.googleapis.com/fcm/send \
-H 'authorization: key=[FCM_SERVER_KEY_REMOVED]' \
-H 'cache-control: no-cache' \
-H 'content-type: application/json;charset=UTF-8' \
-H 'postman-token: [REMOVED]' \
-d '{"data":{"nt":"FCM PUSH TITLE","pt":"popup_title","pc":"popup_content","type":"E","collapskey":"HJ_TYPE","subtype":"CI"},"to":"[FCM_DEVICE_TOKEN_REMOVED]"}'




[탐색용 push]

curl -X POST \
 https://fcm.googleapis.com/fcm/send \
 -H 'authorization: key=[FCM_SERVER_KEY_REMOVED]' \
 -H 'cache-control: no-cache' \
 -H 'content-type: application/json;charset=UTF-8' \
 -H 'postman-token: [REMOVED]' \
 -d '{"data":{"nt":"FCM PUSH TITLE","pt":"popup_title","pc":"popup_content","type":"S","payType":"A","status":"4","collapskey":"HJ_TYPE", "iu":"[HOST](602 kB)","callId":"922959","startLoc": {
        "x": "45760675",
        "y": "13463829",
        "poiid": "",
        "name": "팅크웨어"
    },
  "endLoc": {
        "x": "45731002",
        "y": "13497630",
        "poiid": "4522133",
        "name": "강남역"
    },
    "viaLocs": [{
        "x": "45765625",
        "y": "13459212",
        "poiid": "",
        "name": "이매촌한신"
    }]},
    "to":"[FCM_DEVICE_TOKEN_REMOVED]"}
'



curl -X POST \
 https://fcm.googleapis.com/fcm/send \
 -H 'authorization: key=[FCM_SERVER_KEY_REMOVED]' \
 -H 'cache-control: no-cache' \
 -H 'content-type: application/json;charset=UTF-8' \
 -H 'postman-token: [REMOVED]' \
 -d '{"data":{"nt":"FCM PUSH TITLE","pt":"popup_title","pc":"popup_content","type":"X","status":"4","collapskey":"HJ_TYPE", "iu":"[HOST](602 kB)","callId":"922959","startLoc": {
        "x": "45760675",
        "y": "13463829",
        "poiid": "",
        "name": "팅크웨어"
    },
  "endLoc": {
        "x": "45731002",
        "y": "13497630",
        "poiid": "4522133",
        "name": "강남역"
    },
    "viaLocs": [{
        "x": "45765625",
        "y": "13459212",
        "poiid": "",
        "name": "이매촌한신"
    }]},
    "to":"[FCM_DEVICE_TOKEN_REMOVED]"}
'




