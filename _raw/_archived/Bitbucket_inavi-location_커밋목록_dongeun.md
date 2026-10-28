# Bitbucket inavi-location 커밋 목록 (본인 작성분)

- 저장소: Bitbucket mobility-tech/inavi-location (로컬 clone `Android/inavi-location`)
- 필터: `git log --all --no-merges --author=dongeun`, stash 항목 제외
- 수집일: 2026-10-28, 총      219건, 기간 2026-04-09 ~ 2026-10-15
- 형식: `해시|작성일|커밋 메시지` (최신순). 메시지 원문이며 diff는 검증하지 않았다.

```
3bd2fa0|2026-10-15|✨ SamsungLifeService 에 세션 삭제 API(deleteSession) 추가
1546178|2026-10-15|✨ 데모 앱 세션 화면에 Delete 버튼 추가
6d1118d|2026-10-15|🔧 release 버전 1.0.3으로 상향
2869a2f|2026-10-15|✨ 데모 앱 세션 화면에 Delete 버튼 추가
aed6833|2026-10-15|✨ SamsungLifeService 에 세션 삭제 API(deleteSession) 추가
853a095|2026-10-15|⬇️ Kotlin 2.0.0 / AGP 8.7.1 다운그레이드
7004872|2026-08-20|📝 로컬 AAR 연동 가이드 문서 추가
76c2fde|2026-08-20|🔧 로컬 전달용 AAR 빌드 스크립트 추가
0adf1e1|2026-07-03|Logger 표출하도록 수정
504369a|2026-06-25|📝 SDK 가이드에 pause/resume/duration API 및 포그라운드 종료 동작 반영
3fc6333|2026-06-25|🔧 release 버전 1.0.1로 상향
0c81655|2026-06-25|🔥 raw 활동 라벨/신뢰도 UI 표출 테스트 코드 제거
e8fcfc4|2026-06-25|🚧 raw 활동 라벨/신뢰도 UI 표출 (테스트)
018e5fb|2026-06-25|🔥 끝자락 집계 제외 설계·계획 문서 삭제
9333918|2026-06-25|💄 Pause 세션을 라이브 표시로 전환 (Android·iOS)
d99379e|2026-06-25|🐛 끝자락 집계 제외 철회, 종료 시점 마커 스냅샷으로 활동시간 보존
d40b10a|2026-06-25|🐛 iOS Pause 시 세션 해제 후 보정된 trackingResult로 전환
82d2838|2026-06-24|🐛 iOS 트래킹 API 변경 대응 (resumeTracking·stopped 재개 판정)
c54d7ef|2026-06-24|🐛 stop/pause 동시 호출 시 종료 플래그 오기록 방지
e0c7fd5|2026-06-24|🐛 getTrackingResult 끝자락 구간 집계 제외
090489d|2026-06-24|📝 TrackingResult 끝자락 집계 제외 설계·계획 문서 추가
a41d410|2026-06-24|💄 세션 화면 Resume 활성 조건을 stopped 상태로 변경
237f81e|2026-06-24|✨ stop/pause 분리 및 종료 세션 재개 차단
36d3585|2026-06-24|🗃️ tracking_sessions에 stopped 컬럼 추가 (DB v3)
3173c90|2026-06-24|📝 세션 종료 플래그(stopped) 설계 문서 추가
31d6a7c|2026-06-22|🐛 reset() 시 duration 상태 미정리로 오래된 값 노출 문제 해결
0efe225|2026-06-19|🔧 난독화 시 내부 클래스 재패키징 규칙 추가
4f151ce|2026-06-18|✨ 트래킹·리스너 전체 초기화 reset() API 추가
f63363d|2026-06-18|📝 onTaskRemoved 프로세스 정리 설계/구현 계획 문서 추가
1267550|2026-06-18|🐛 스와이프 종료 시 프로세스 정리로 재시작 데이터 잔존 문제 해결
a6bee76|2026-06-10|Location accuarcy, fresh 필드 추가
2260cf3|2026-05-15|📝 [SLDR-30] PDF 가이드 현행화
d54f847|2026-05-14|📝 [SLDR-30] Android 필요 권한에 ACCESS_COARSE_LOCATION 추가
96105a5|2026-05-14|🔧 Android Demo 서브모듈 커밋 포인터 업데이트
b70659a|2026-05-14|🔧 Android Demo 서브모듈 추가
29c5db9|2026-05-14|📝 [SLDR-30] 가이드 버전·iOS 최소 버전·의존성 버전·데모 앱 링크 업데이트
74b317e|2026-05-14|📝 [SLDR-30] PDF 코드 블록 긴 줄 잘림 수정
7374c09|2026-05-14|📝 [SLDR-30] SDK 명칭·권한·의존성 가이드 정정
6b46530|2026-05-14|📝 [SLDR-30] 가이드 PDF 업데이트 (한글 폰트 적용)
0ed7ecf|2026-05-14|📝 [SLDR-30] iOS SPM 의존성 추가 가이드 작성
b7fd130|2026-05-14|📝 [SLDR-30] Android Maven 저장소 및 의존성 추가 가이드 작성
ed3480c|2026-05-13|✨ [SLDR-30] 걸음수/케이던스 UI 표시 추가 및 iOS 재개 다이얼로그 수정
ef78d84|2026-05-13|✨ [SLDR-30] 걸음수/케이던스 데이터 계층 추가
771ed5d|2026-05-13|🔧 [SLDR-30] Artifactory 저장소를 navigation에서 sdk로 변경
afc442f|2026-05-13|🚀 [SLDR-30] SDK 릴리스 버전 1.0.0으로 올림
ac3ba59|2026-05-12|🔧 [SLDR-30] Room DB 버전 1로 초기화
957defa|2026-05-12|🔧 [SLDR-30] useRemoteDeps 플래그 추가
9f25a24|2026-05-12|🔧 [SLDR-30] samsunglife 배포 설정 및 공개 API 전이 의존성 노출
7eded61|2026-05-12|🔧 [SLDR-30] core:tracking 내부 구현 은닉 및 배포 설정
6dc3b55|2026-05-12|🔧 [SLDR-30] core:database 배포 설정 및 ProGuard 규칙 추가
e54da51|2026-05-12|🔧 [SLDR-30] core:common 배포 설정 및 Kotlin 메타데이터 보존
583e1ea|2026-05-12|🔧 [SLDR-30] SDK 모듈 Artifactory 배포 환경 구성
be4d990|2026-05-12|📝 [SLDR-30] 삼성생명 SDK 연동 가이드 문서 추가
5148611|2026-05-12|🔧 [SLDR-30] minSdk 24 → 26 상향
6153fa8|2026-05-12|💄 [SLDR-30] CurrentPoint 전환에 따른 현재 포인트 UI 텍스트 정리
10a5fc4|2026-05-12|✨ [SLDR-30] setCurrentPointListener 공개 타입을 CurrentPoint로 분리
17dce01|2026-05-11|🐛 [SLDR-30] ON_FOOT 활동을 RUNNING/WALKING 서브 액티비티로 올바르게 분기
d66632e|2026-05-07|🔥 [SLDR-30] onActivityDetected 미사용 파라미터 제거
08e341d|2026-05-07|🐛 [SLDR-30] 세션 재시작 시 이전 위치 타임스탬프로 인한 대기시간 오산 수정
44d7514|2026-05-07|🐛 [SLDR-30] Android/iOS 세션 화면 표출 사양 통일 및 버그 수정
7bf1ec2|2026-05-07|📝 [SLDR-30] 오픈소스 라이센스 고지 문서 추가
7a67e5c|2026-05-06|♻️ [SLDR-30] observeCurrentMotion 제거 및 setUiDataListener 리네임
b7c693f|2026-05-06|♻️ [SLDR-30] SDK 공개 API 정리 및 리스너 네이밍 개선
d813653|2026-05-06|♻️ [SLDR-30] observeSessions → getSessionIds 스냅샷 API 전환
9fff5fa|2026-05-06|📝 [SLDR-30] 센서 가용성 확인 API 문서화
d38b5ca|2026-05-06|📝 [SLDR-30] 세션 조회/삭제 공개 API 문서화
b3bb715|2026-05-06|📝 [SLDR-30] 트래킹 세션 관련 공개 API 문서화
d2f4104|2026-05-06|📝 [SLDR-30] 배포 가이드 문서용 공개 API 문서화
6407d4f|2026-05-06|♻️ [SLDR-30] applicationInit → initialize 리네임 및 디버그 빌드 로그 비활성화
4e13c1a|2026-05-06|🔧 [SLDR-30] samsunglife BuildConfig 생성 활성화 및 isDebugBuild expect/actual 구현
817f2bc|2026-05-06|🐛 startTracking/restartTracking 반환 타입을 develop 머지 전으로 원복
185eeaf|2026-05-06|🐛 iOS startTracking 반환값 Long? nil 체크로 성공 판단
23ca1c1|2026-05-06|🐛 iOS CMMotion 권한 거부 시 조기 리턴 추가
1aa7f3d|2026-05-06|♻️ bindActivity 제거 — startLocationUpdate 내부 bind로 통합
f90febc|2026-05-06|🚚 applicationInit을 Application 클래스로 이전
3d4db05|2026-04-30|🐛 iOS CMMotion 권한 요청을 startActivityUpdates 표준 패턴으로 교체
6862d74|2026-04-30|♻️ SamsungLifeService.startTracking — Long? 반환 및 불필요한 Dispatcher 래핑 제거
7212d3f|2026-04-30|🐛 kermit을 api로 노출 — core:tracking 빌드 에러 수정
42875b4|2026-04-30|🔧 JFrog Artifactory AAR 배포 인프라 설정
7cfb5e7|2026-04-30|🐛 startLocationUpdate 호출 전 위치 권한 확인 및 요청 — iOS
26eaef0|2026-04-30|🐛 startLocationUpdate 호출 전 위치 권한 확인 및 요청 — Android
db36e1c|2026-04-30|♻️ startLocationUpdate에 activity 파라미터 추가 — bind 책임 TrackingService 내부로 이전
8b154a1|2026-04-30|♻️ 샘플 앱에서 OS 권한 요청 직접 처리
c977929|2026-04-30|♻️ 권한 요청 책임 분리 — :core/:samsunglife에서 제거, 체크 전용 API로 정비
9d26810|2026-04-29|💄 앱 아이콘 및 이름 적용
5609851|2026-04-28|🔥 모션 상태 dwell/candidate 메커니즘 제거
683892e|2026-04-28|✨ [SLDR-44] 모션 활동 원천 라벨 디버그 노출
e1d7aa2|2026-04-28|🐛 [SLDR-44] iOS CMMotionActivity 동시 발화 매핑 보정
4d32cea|2026-04-28|📝 모션 상태 판정 방식 변경 설계 문서 추가
38eb26f|2026-04-27|🐛 추적 중 sparse 이벤트 공백이 excluded로 잘못 누적되는 문제 수정
6049284|2026-04-27|🔥 미사용 worktree 마커 파일 삭제
5fc84c4|2026-04-27|🎨 runSession 지역 변수 오타 수정 (Holer → Holder)
a743701|2026-04-27|🐛 runSession 중복 실행 가드 추가
09a5f6d|2026-04-27|🐛 DB/IO 작업을 Default Dispatcher로 이동
43ffc65|2026-04-27|✨ iOS에서 미종료 세션 클릭 시 재개 다이얼로그 표시
a62520e|2026-04-27|✨ Android에서 미종료 세션 클릭 시 재개 다이얼로그 표시
9333342|2026-04-27|🐛 추적 공백 시간을 excluded로 분리 누적
d107e9a|2026-04-27|✨ 세션 재시작(restartTracking) API 추가
7c55c55|2026-04-27|[SLDR-18] ✨ 구간별 첫 구간 대비 페이스 차이 계산
8f48f0a|2026-04-27|♻️ DerivedMetricsCalculator를 session 패키지 기반으로 재구성
ddf8f78|2026-04-24|♻️ 실시간 지표 6개 Flow를 UIData 단일 Flow로 통합
4c83071|2026-04-24|♻️ TrackingEngine에 Motion·Foreground 위임 및 startTracking coroutineScope 재구성
63e6fac|2026-04-24|✨ core/common에 nowMillis 유틸 함수 추가
3f7327c|2026-04-24|🚚 internal 패키지 3개 홀더를 Tracking 접두사로 rename 및 네이밍 정리
f04066c|2026-04-24|🚚 CoordinateProjection을 RouteCoordinateProjection으로 rename 및 네이밍 정리
0035e12|2026-04-24|🚚 MinuteCadenceTracker를 TrackingMinuteCadenceTracker로 rename 및 네이밍 통일
2ed2691|2026-04-24|🚚 CalorieCalculator를 TrackingCalorieCalculator로 rename 및 네이밍 개선
f1f2bed|2026-04-24|♻️ TrackingMovement의 Ms/Millis 접두사 통일 및 지역 변수 네이밍 정리
45b454e|2026-04-24|🚚 AltitudeAccumulator를 TrackingAltitudeAccumulator로 rename 및 네이밍 통일
0289782|2026-04-24|🔥 미사용 TrackingCalculator/TrackingPace/SectionElevationTracker 제거
83667f6|2026-04-23|♻️ LapCalculator를 TrackingLapCalculator로 rename 및 네이밍 통일
1bcc2ba|2026-04-23|♻️ DistanceCalculator를 TrackingDistanceCalculator로 rename 및 네이밍 통일
6a30d1c|2026-04-23|✨ core/common에 toRadians 확장 함수 추가
07c5367|2026-04-23|💄 세션 화면에 계산중인 상태 표시 (Android/iOS)
93527a8|2026-04-23|✨ MovementStats에 현재 계산 상태(currentStateName) 노출
9c2ff86|2026-04-23|🔧 Claude Code kotlin-refactor 스킬 추가
c8113f0|2026-04-23|[SLDR-16] ✨ 이동 페이스 계산 및 표시
24fe825|2026-04-22|[SLDR-34] 🐛 권한 승인 후에만 포그라운드 서비스 시작
8b6dc15|2026-04-22|[SLDR-34] 🚚 POST_NOTIFICATIONS 권한을 앱 모듈로 이동
0b929d7|2026-04-22|Merge branch 'develop' into feature/SLDR-34-aos-포그라운드-서비스-구현
180b19f|2026-04-22|✨ 앱에 Foreground 서비스 연동 및 알림 권한 요청
d942879|2026-04-22|✨ SamsungLifeService에 Foreground 서비스 API 공개
7b6c764|2026-04-22|✨ TrackingService에 Foreground 서비스 제어 메서드 추가
8be19a7|2026-04-22|✨ Foreground 서비스 Provider/Config expect-actual 추가
b4248ca|2026-04-22|[SLDR-16] 💄 iOS 데이터 탭에 이동 페이스 표시
118af6f|2026-04-22|[SLDR-16] 💄 데이터 탭에 이동 페이스 표시
4b366dd|2026-04-22|[SLDR-16] ✨ 이동(러닝+걷기) 평균 페이스 계산·노출
b8d1d96|2026-04-21|🔧  TrackingEngine, TrackingService 리팩토링
7ab3c63|2026-04-21|🔧 iOS altitudeDeadband·sectionInterval 기본값 조정
0ecaef2|2026-04-21|🔥 iOS 데이터 탭 상승/하강 고도 표시 제거
e54316c|2026-04-21|🔧 페이스 디버그용 elapsedMs/distance 원시값 Flow 노출
a6d1836|2026-04-21|🔧 altitudeDeadbandMeters 기본값을 0.3m로 하향
a5553b0|2026-04-21|[SLDR-13] ✨ 현재 포인트에 활동 인식 상태 표시
fa0a43b|2026-04-21|[SLDR-13] 💄 데이터 탭 움직임 통계를 쌓는 형태로 개편
a1f9e22|2026-04-21|[SLDR-13] 🎨 MotionProvider 활동 인식 호출부 포맷 정리
f28c92a|2026-04-21|[SLDR-13] ✨ 활동 판정에 신뢰도 필터·히스테리시스·보행속도 교차검증 추가
8181000|2026-04-21|[SLDR-13] ✨ UI에 기타 상태 누적 시간 표시
7801cef|2026-04-21|[SLDR-13] ✨ 기타(excluded) 누적 시간을 모델·저장소에 전파
c1bda74|2026-04-21|[SLDR-13] 🗃️ 세션 테이블에 기타(excluded) 누적 시간 컬럼 추가 (DB v10)
08775c1|2026-04-21|[SLDR-13] ✨ UI에 러닝/걷기/대기 실시간 통계 표시
984f408|2026-04-21|[SLDR-13] ✨ TrackingService에 movementStatsFlow 실시간 통계 연동
d2f9d58|2026-04-21|[SLDR-13] ✨ MotionProvider에 활동 인식 구현 (Android + iOS)
95647e5|2026-04-21|[SLDR-13] 🗃️ 세션에 러닝/걷기/대기 집계 컬럼 추가 (DB v9)
b53e0a8|2026-04-21|[SLDR-13] ✨ 러닝/걷기/대기 집계 TrackingMovement와 MovementStats 모델 추가
9b5e022|2026-04-20|[SLDR-15] 🐛 TrackingPace 코드 리뷰 피드백 반영
534e069|2026-04-20|[SLDR-15] 🐛 merge 후 남은 conflict 마커 제거
bcf8b2d|2026-04-20|[SLDR-15] 🔥 쓰이지 않는 실시간 bestPaceFlow/observeBestPace 제거
f0e33df|2026-04-20|[SLDR-15] 🐛 iOS 평균 페이스 옵셔널 체이닝 제거
0e700ef|2026-04-20|[SLDR-15] 💄 현재 포인트에서 최고 페이스 표시 제거
040ba85|2026-04-20|[SLDR-15] 📝 TrackingService 평균/최고 페이스 플랜 문서 추가
99d3102|2026-04-20|[SLDR-15] 💄 Android/iOS 앱에 평균/최고 페이스 표시
8b1eba0|2026-04-20|[SLDR-15] ✨ SamsungLifeService에 페이스 Flow 구독 API 추가
82e300d|2026-04-20|[SLDR-15] ✨ TrackingService에 평균/최고 페이스 통합
77a0bbf|2026-04-20|[SLDR-15] ✨ 평균/최고 페이스 계산기 TrackingPace 추가
a8a057b|2026-04-20|[SLDR-15] 🗃️ TrackingSession에 평균/최고 페이스 컬럼 추가
bcc1588|2026-04-17|[SLDR-29] ♻️ SamsungLifeService.startTracking을 Main 디스패처로 실행
f761845|2026-04-17|[SLDR-29] ♻️ TrackingService.startTracking을 Default 디스패처로 실행
b77aff0|2026-04-17|[SLDR-29] ✨ 활동 인식(모션) 권한 요청 추가
42cb87b|2026-04-17|♻️ collect 블록 변수 섀도잉 제거 및 필터 포인트 일관 적용
a795f5a|2026-04-17|🐛 TrackingEngine stop에서 job을 실제로 취소하도록 수정
78d77fb|2026-04-17|♻️ TrackingService 인터페이스 분리
3015b2d|2026-04-17|♻️ Tracking 오케스트레이션을 Service/Engine으로 분리
7e8f243|2026-04-17|✨ LocationPoint/TrackingSession Repository 신규 추가
2ea583c|2026-04-16|[SLDR-8] 💄 경로 이미지 배경을 투명으로 변경
09a1ca9|2026-04-16|[SLDR-8] ♻️ LocationTracker 세션 기록 로직 분리 및 가독성 개선
a2b9e07|2026-04-16|[SLDR-8] ✨ TrackingResult GPS 추적 결과 데이터 모델 추가
f207caf|2026-04-16|[SLDR-8] ♻️ 공통 LatLng 모델 도입 및 PermissionRepository 인터페이스 분리
edb92e0|2026-04-16|[SLDR-8] 💄 iOS ContentView를 Android SessionScreen UI 구조로 통일
82adc52|2026-04-16|[SLDR-8] 🗃️ DB 스키마 버전 업그레이드
cdb912c|2026-04-16|[SLDR-12] 💄 세션 목록에 총 시간 표시
a30e0ec|2026-04-16|[SLDR-12] ✨ 세션 총 시간(duration) 저장 기능 추가
bbde347|2026-04-16|[SLDR-12] 🔧 스키마 변경 시 DB 자동 재생성 설정
199521d|2026-04-16|[SLDR-8] 🔧 Xcode 프로젝트 설정 변경
338faaf|2026-04-16|[SLDR-8] 🎨 SessionScreen 변수명 가독성 개선
26d1680|2026-04-15|[SLDR-8] ♻️ LocationTracker 불필요한 public API 제거 및 필터 가독성 개선
e6f1ea0|2026-04-15|[SLDR-8] 🔥 RouteImageConfig 미사용 companion object 제거
b5280bd|2026-04-15|[SLDR-8] ♻️ LocationTracker 상태 관리 간소화 및 세션 종료 안전성 개선
f7e3579|2026-04-15|[SLDR-8] 🚚 RoutePoint, RouteImageConfig를 model 패키지로 이동
38f95fe|2026-04-15|[SLDR-8] 🚚 LocationSample을 LocationPoint로 리네이밍
3210a32|2026-04-15|[SLDR-8] ♻️ Component에 CoroutineScope 추가 및 DI 간소화
df0b4fd|2026-04-15|[SLDR-8] 🔧 Coroutine 의존성을 core:common으로 통합
6bc73ea|2026-04-15|[SLDR-8] ♻️ Koin 초기화를 samsunglife 모듈로 이전 및 database DI 구조 변경
45ba369|2026-04-15|[SLDR-8] ♻️ 자체 Time 유틸을 kotlinx-datetime Clock으로 교체
e88d181|2026-04-15|[SLDR-8] 🎨 SamsungLifeService 불필요한 공백 제거
e4f7ff5|2026-04-15|[SLDR-8] ✨ Compose 기반 세션 화면 구현 및 ViewBinding 레이아웃 제거
ce7d51f|2026-04-15|[SLDR-8] 🔧 Compose 빌드 설정 및 의존성 추가
62ac3ba|2026-04-14|[SLDR-8] 🔧 iOS 빌드 스크립트에 java 버전 로그 추가 및 DEVELOPMENT_TEAM 변경
f7b59fa|2026-04-14|[SLDR-8] ♻️ TrackingRepository를 Flow로 노출하고 SamsungLifeService를 리스너 파사드로 전환
604ff52|2026-04-14|[SLDR-8] ♻️ LocationService를 TrackingRepository로 교체하고 tracking 내부 패키지 재편
136ef4b|2026-04-14|[SLDR-8] 📝 AGENTS.md 모듈 구조·의존성 그래프 갱신
52d8225|2026-04-14|[SLDR-8] ✨ samsunglife 파사드 모듈 추가 및 앱을 해당 모듈 기반으로 전환
07a8d93|2026-04-14|[SLDR-8] 🚚 core:location을 core:tracking 모듈로 이동하고 패키지 재편성
fef63a4|2026-04-14|[SLDR-8] ♻️ core:database 패키지를 core.database로 이동
ce0a8f1|2026-04-14|[SLDR-8] ♻️ core:common 패키지를 core.common으로 이동하고 permission API 통합
7c8daa7|2026-04-14|[SLDR-8] ✨ core:common에 DeviceInfo 추상화 및 플랫폼 DI 추가
eda9209|2026-04-14|[SLDR-8] 🏗️ 서브모듈 패키지 구조 정규화
35b8899|2026-04-13|[SLDR-8] ♻️ MotionPermission, PermissionResult 파일 분리
16d1945|2026-04-13|[SLDR-8] 🔥 미사용 의존성 제거
e5d58fa|2026-04-13|[SLDR-8] ✨ LocationService 초기화 및 권한 요청 앱 연동
ad76e26|2026-04-13|[SLDR-8] ✨ 위치 권한 요청 기능 구현
b71ab51|2026-04-13|[SLDR-8] 🔧 moko-permissions 의존성 및 위치 권한 설정 추가
fe52cdf|2026-04-13|📝 AI Agent 표준 가이드 문서 추가
f55bd93|2026-04-10|🔧 [SLDR-2] Claude Code 스킬 이름 수정 및 MCP 설정 추가
c4e881e|2026-04-10|🔧 [SLDR-2] Claude Code 프로젝트 스킬 설정 추가
cab0391|2026-04-10|✨ [SLDR-2] Koin/Kermit 기반 Component 베이스 클래스 추가
7e0678a|2026-04-10|🔥 [SLDR-2] core:common KMP 템플릿 코드 삭제
45bece5|2026-04-10|⬆️ [SLDR-2] core:common에 Kermit, Koin 의존성 추가
5461924|2026-04-10|✨ [SLDR-2] core:gpx 모듈 추가
ab14353|2026-04-10|✨ [SLDR-2] core:location 모듈 추가
0c3839c|2026-04-10|🏗️ [SLDR-2] shared → core 멀티모듈 구조 전환
781d2ef|2026-04-10|✨ [SLDR-2] XML 기반 Android app 모듈 추가
e396eb2|2026-04-10|🔧 [SLDR-2] Compose 의존성 제거 및 빌드 설정 변경
86b605c|2026-04-10|🔥 [SLDR-2] composeApp 모듈 삭제
020e79e|2026-04-10|📝 README 추가
037105e|2026-04-10|✨ iOS 앱 모듈 추가
4680696|2026-04-10|✨ Android Compose 앱 모듈 추가
a7d26f0|2026-04-10|✨ shared 모듈 추가
68d734f|2026-04-10|🔧 KMP 프로젝트 빌드 환경 설정
cd349c8|2026-04-09|Initial commit
```
