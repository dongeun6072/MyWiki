---
title: >-
    iNavi SDK Android 개요, 개발 환경, 세팅, 권한, 난독화
category: references
project: orbis-sdk
tags: [navisdk, android, setup, proguard, permissions, visibility/internal]
aliases: [iNavi SDK Android 개발 가이드 세팅 방법, SDK 권한 목록, SDK Interface, Proguard]
relationships:
  - target: "[[orbis-sdk]]"
    type: related_to
  - target: "[[navisdk-api-coverage-and-domestic-sdk-guide]]"
    type: related_to
sources:
  - url:https://inavisystems.atlassian.net/wiki/spaces/INaviAIR/pages/305430571
summary: >-
    국내향 iNavi SDK(Android) 개요, Appkey 발급 절차, 개발 환경, Gradle/Manifest/Layout 세팅, 필수 권한, 난독화, SDK 생명주기와 좌표계 규칙.
provenance:
  extracted: 0.92
  inferred: 0.05
  ambiguous: 0.03
base_confidence: 0.62
lifecycle: draft
lifecycle_changed: 2026-10-26
tier: supporting
created: 2026-10-26T13:00:00+09:00
updated: 2026-10-26T13:00:00+09:00
---

# iNavi SDK Android 개요, 개발 환경, 세팅, 권한, 난독화

iNavi SDK Android 개발 가이드의 앞부분(개요, Appkey 발급, 개발 환경, SDK 세팅 방법, SDK 권한 목록, SDK Interface 규칙)을 옮긴 문서이다. 코드 예시는 [[inavi-sdk-android-scenario-examples]], 함수별 상세는 [[inavi-sdk-android-controller-init-map-search]] 이후 페이지를 본다. 전체 목차는 [[inavi-sdk-android-guide-hub]], 국내 SDK 전반은 [[navisdk-api-coverage-and-domestic-sdk-guide]].

## 개요
- 본 문서는 Android 기반 플랫폼에서 구동되는 "아이나비 내비게이션 SDK"(이하 SDK) 연동에 대한 기술 문서이다.

## Appkey 발급
- SDK를 사용하기 위해서는 우선 Appkey 발급이 필요하다. 규격서를 제공한 제휴 사업 담당자를 통해 별도 요청해야 한다.
- 실제 AppKey 값은 문서에 기재되지 않는다(Manifest 예시에서도 `AppKey` 자리표시자만 사용).

## 개발 환경
| 항목 | 값 |
|---|---|
| 개발 도구 | Android Studio 3.5 이상 |
| 개발 언어 | Android, Kotlin |
| targetSdkVersion | 28 (Android 9, P OS) |
| minSdkVersion | 21 (Android 5.0, LOLLIPOP OS) |

- 0.0.22 이전에는 minSdkVersion 19였고 0.0.22에서 21로 올라갔다([[inavi-sdk-android-revision-history]]).

## SDK 세팅 방법

### 1. SDK 저장소 추가 (Root Project build.gradle)
```
//Root Project build.gradle
allprojects {
    repositories {
        // ~~maven { url '<<URL>>' }~~   (기존 저장소, 취소선 처리됨)
        // 기존 저장소 변경, SDK 버전 상관 없이 반드시 해당 URL 적용 필요
        maven { url '<<URL>>' }
    }
}
```
- 실제 저장소 URL은 원본에 있으나 이 위키에는 옮기지 않았다(원본에 있음, 미수록). 0.6.2(2023-10-17)에서 저장소 URL이 변경되었고, 어느 SDK 버전이든 새 URL을 써야 한다.
- 저장소 이력: 0.0.20에서 Bintray → Artifactory, 0.6.2에서 URL 재변경.

### 2. SDK 의존성 추가 (App build.gradle)
```
// App build.gradle
dependencies {
    //SDK 의존성
    implementation 'com.inavisys.navisdk:inavi-navigation-sdk:version'
    //SDK가 사용하는 Library 의존성 추가
    implementation 'com.google.code.gson:gson:2.8.5'
    // SDK v0.6.0 이하 버전은 16.0.0 사용
    // implementation 'com.google.android.gms:play-services-location:16.0.0'
    // SDK v0.6.0 부터 반영
    implementation 'com.google.android.gms:play-services-location:21.0.01'
    // APP 내에서 ConstraintLayout 사용 시 2.0 이상 사용 하여야 함 (SDK-0.0.28 이후 버전 부터)
    implementation 'androidx.constraintlayout:constraintlayout:2.1.4'
}
```
- 원문에는 `play-services-location:21.0.01`로 적혀 있다(SHI 사본은 `21.0.1`). 오타 가능성이 있다 ^[ambiguous]

`gradle.properties`
```xml
android.useAndroidX=true // SDK v0.6.0 부터 필수
```

### 3. SDK 환경 세팅
App build.gradle - ndk abiFilters 추가
```
android {
    defaultConfig {
        ndk {
            abiFilters "arm64-v8a", "armeabi-v7a"
        }
    }
}
```
App build.gradle - 컴파일 옵션 추가
```
android {
    compileOptions {
        sourceCompatibility JavaVersion.VERSION_1_8
        targetCompatibility JavaVersion.VERSION_1_8
    }
}
```
AndroidManifest.xml - http 허용
```
<manifest>
    <application
        android:usesCleartextTraffic="true">
    </application>
</manifest>
```
AndroidManifest.xml - Apache.http.legacy 허용
```
<manifest>
    <application
        <uses-library android:name="org.apache.http.legacy" android:required="false"/>
    </application>
</manifest>
```
AndroidManifest.xml - AppKey 등록
```
<manifest>
    <application
        <meta-data android:name="com.inaviair.sdk.appkey" android:value="AppKey"/>
    </application>
</manifest>
```
- `android:value`에 발급받은 AppKey를 넣는다(값은 미수록).

### 4. SDK 난독화 옵션 세팅 (proguard-rules.pro)
```
-keep class com.inaviair.sdk.** { *; }
```
- 개정이력: 0.0.5 Proguard 옵션 추가, 0.0.6 통신 관련 난독화 예외처리 및 App 난독화 가이드 추가.

### 5. SDK Layout 세팅
지도를 표출할 Layout(xml) 파일에 아래 두 View를 추가한다.
- 지도 View: `com.inaviair.sdkEngine.MapAdapter`
- 주행화면 View: `com.inaviair.sdkEngine.MapLayer`
```
<androidx.constraintlayout.widget.ConstraintLayout
        android:layout_width="match_parent"
        android:layout_height="match_parent">
        <androidx.constraintlayout.widget.ConstraintLayout
            android:layout_width="match_parent"
            android:layout_height="match_parent">
            <!-- 지도 View -->
            <com.inaviair.sdkEngine.MapAdapter
                android:id="@+id/mapAdapter"
                android:layout_width="match_parent"
                android:layout_height="match_parent"
                android:visibility="visible"
                />
            <!-- 주행화면 View -->
            <com.inaviair.sdkEngine.MapLayer
                android:id="@+id/mapLayer"
                android:layout_width="match_parent"
                android:layout_height="match_parent"
                android:visibility="visible"
                />
        </androidx.constraintlayout.widget.ConstraintLayout>
</androidx.constraintlayout.widget.ConstraintLayout>
```
- 이 두 View의 리소스 ID를 `initLayout`에 전달한다.

## SDK 권한 목록
앱에서 필수로 권한을 획득해야 한다.

### 1. SDK 사용을 위한 필수 권한(앱이 런타임에 획득)
```
Manifest.permission.ACCESS_FINE_LOCATION
Manifest.permission.ACCESS_COARSE_LOCATION
Manifest.permission.READ_EXTERNAL_STORAGE
Manifest.permission.WRITE_EXTERNAL_STORAGE
```
- 위치 권한이 없으면 맵매칭 엔진 초기화 실패(코드 3052)가 날 수 있다([[inavi-sdk-android-error-codes]]).

### 2. SDK 내부에 선언되어 있는 Permission 목록
| 분류 | 권한 |
|---|---|
| 통신 | `INTERNET`, `ACCESS_NETWORK_STATE`, `ACCESS_WIFI_STATE`, `CHANGE_WIFI_STATE` |
| 위치 | `ACCESS_FINE_LOCATION`, `ACCESS_COARSE_LOCATION`, `ACCESS_LOCATION_EXTRA_COMMANDS` |
| 저장소 | `READ_EXTERNAL_STORAGE`, `WRITE_EXTERNAL_STORAGE` |

(모두 `android.permission.` 접두의 `<uses-permission>` 선언)

## SDK Interface 규칙
1. SDK 생명주기
   - SDK 생명주기는 Application 생명주기와 동일하게 사용하는 것을 권장한다.
   - SDK의 내비게이션 지도 및 주행화면은 앱 실행시 최초 실행되는 Activity에서 구현한다.
   - `loadNaviLibrary`, `initLayout`, `initalizeNavi`, `destroyNavi`는 앱 실행당 1회만 호출한다.
2. 모든 기능은 `INaviController` 클래스로 사용한다.
   - `INaviController`는 Singleton 객체이다.
   - 비동기 처리는 SDK가 Callback으로 제공한다.
3. 좌표계
   - SDK는 위경도 좌표를 사용하며 DD(십진수 도) 방식이다.
   - 예) 서울역 위도 37.553173, 경도 126.972471

## Related
- [[inavi-sdk-android-guide-hub]] — 이 가이드 묶음 목차
- [[navisdk-api-coverage-and-domestic-sdk-guide]] — 국내 SDK 가이드 개요
- [[orbis-sdk]] — SDK 프로젝트 허브
- [[orbis-navisdk-architecture-and-flutter-plan]] — SDK 구조

## Sources
- Confluence "iNavi SDK Android 개발 가이드" (pageId 305430571) — 가져온 날짜 2026-10-26, 로컬 스냅샷 없음
