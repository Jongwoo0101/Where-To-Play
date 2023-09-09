# Where To Play ⁉️
![banner](https://github.com/Jongwoo0101/Where-To-Play/assets/96978536/937cba69-9b9c-4da9-8560-075ea69b5243)
현대해상 X 어썸스쿨 하이챌린지스쿨에서 진행하는 4조(*자료구조*) 프로젝트.   
➡️[사이트 바로가기](https://wheretoplay.kr)⬅️
🔥[발표자료 바로가기](https://www.canva.com/design/DAFsgPdSRWw/6qAxhTQyMFmUomuYKxUd3w/view?utm_content=DAFsgPdSRWw&utm_campaign=designshare&utm_medium=link&utm_source=publishsharelink)🔥   


[<img src="https://img.shields.io/badge/instagram-E4405F?style=flat&logo=instagram&logoColor=white"/>](https://www.instagram.com/wheretoplay.kr/)

<br />

# 조 이름은 왜 "자료구조" 인가요❓
> 여러가지 흩어져 있는 자료들을 형식별로 분류해서 체계적으로 분류해둔 것이 자료구조이듯이, 우리 조 또한 자료구조처럼 문제들을 체계적으로 분석하고 이를 체계적으로 해결해보자라는 의미를 담고 있습니다❗

<br />

## 👨‍👨‍👦‍👦 팀원 구성
| 이름 | 역할 |
|------|------|
| 조건희 | 뱅커/포토그래퍼 |
| 민현규 | 디자이너 |
| 원종우 | 마케터 |
| 한도윤 | 커뮤니케이터/발표 |

<br />

## 💡프로젝트 시작 계기
### 인식한 문제
> 운동장/체육관 사용을 원하는 사람들이 운동장을 찾고, 예약하는 서비스가 통합되어 있지 않아 주변 운동장을 일일히 알아보기 번거롭고, 시설의 사용 가능 여부가 실시간으로 제공되지 않음.
### 문제해결의 주요 키워드
> **"공공기관"**, **"예약 시스템"**, **"통합"**
### 해결책 1
> 카카오맵 API를 활용하여 실시간 지도 정보 서비스를 웹 페이지로 구축한다.
### 확장 가능성
- 일부 운동장과 예약 시스템 API를 구축하여 간단하게 사용할 수 있는 예약 시스템 또한 통합시킬 수 있음.
- 테마 지도를 만들어 운동장에 국한된 것이 아닌 다른 시설(카페, 맛집, 관광명소 etc..) 또한 동일한 시스템을 활용하여 확장할 수 있음.

<br />

## 🛠️ 핵심 기능
### 1. 개인별 맞춤 운동장 추천 시스템
- 회원가입 시, 닉네임/나이/전화번호(SMS인증)/우선순위(#청결, #교통편리, #넓은구장, #쾌적한시설 등 해시태그로 표기) 수집
- 수집한 우선순위를 바탕으로 운동장 추천
### 2. 실시간 정보 공유
- 구장 사정으로 인해 폐쇄, 이용이 불가능한 경우를 대비하기 위해 실시간 댓글 기능을 제공합니다!
### 3. 운동장 정보 등록/수정
- 언제든 바뀔 수 있는 운영 시간 등을 고려하여 사용자들이 수정할 수 있게 기능을 제공합니다! (신뢰성을 위해 회원만 가능)
### 4. 기여도에 따른 레벨 기능
- 운동장 등록 횟수, 출석 횟수, 댓글 갯수, 사진 등록 등의 활동 정보를 합산하여 레벨과 혜택을 제공합니다!

<br />

## 📝 프로젝트 기획
| 7.12(수) | 7.22(토) | 7.26(수) | 8.9(수) | 8.12(토) | 8.14(월) |
|------|------|------|------|------|------|
| **주/세부 기능 기획(완료)** | **프로토타입 제작(완료)** | **웹 개발(완료)** | **피드백** | **수정 및 보완** | **프로젝트 데드라인** |
| 주 기능 구성(완료) | 프로토타입 제작 협력 틀 선정(완료) | 프로토타입 기반 프론트앤드 제작(완료) | 베타 테스트(완료) | 수정 및 보완 |  |
| 세부 기능 구성(완료) | 피드백(완료) | 피드백(완료) | 디버깅(완료) | 피드백 기반 수정 및 보완(완료) |  |
| ~~기관/운동장 조사 및 연락(제거)~~ |  | 기능 구현(완료) | 사용자 요구사항 조합 |  |  |
| 화면 구성도 제작(완료) |  | 도메인 구매(완료) | 총정리(완료) |  |  |
| 플로우 차트 구성(완료) |  | 서버 선정 및 구매(완료) |  |  |  |
| 디자인 컨셉 구상(완료) |  | 배포(완료) |  |  |  |

<br />

## 📕 1차 회의 결과
전체의견 : 기존의 아이디어 였던 예약 서비스 통합이 아니라 주변 운동시설을 **보기좋은 형태로 만들어주는 서비스**로 변경하자!  

**팀원별 의견**
| 이름 | 의견 |
|------|------|
| 조건희 | 메인 홈페이지에서 지도를 띄워서 거기서 한번에 볼 수 있게끔 메인 맵 한 개를 구성 / 메인에 지도 하나를 배치 한 후 위치를 등록할 수 있는 기능 추가 / (위치등록 시스템)지도를 클릭해서 (포인트) 정보 제공 -> 마커 영역 헤드 부분에 주요 기능 / 카테고리를 운동장 말고 더 추가해도 됨.  |
| 민현규 | 사용자 칭호 기능 추가 |
| 원종우 | 강남구만 일시적으로 서비스 범위를 두자 / 메인 페이지는 우리 팀에 대한 설명을 제시하고 서비스에 대한 설명을 제시한 뒤 “시작하기” 버튼을 클릭하여 주변 운동장 찾기 서비스 웹페이지로 넘어가게끔 구성 |
| 한도윤 | 모바일 웹 둘 다  / 주변 가까운 운동장 찾기 서비스 기능 / 흙,잔디 구별 -> 위성지도 사용 / 유저와 반응 서비스 기능을 웹 상단에 배치 / 실시간 댓글(피드백) -> 예외로 간주 |

<br />

**📈 회의 결과**
- 마커 기능 등록
- 홈페이지 사이트 주소
- 사진 / 카테고리 (해시태그 - > 아이콘)
- 회원 (닉네임 수집, 아이디, 비밀번호, 생년월일, 성별, 활동레벨(칭호 -> 고급스러운 아이콘))

<br />

## 📙 2차 회의 결과
회의주제 : 기능 수정 및 추가  

**팀원별 진행상황**
| 이름 | 진행상황 |
|------|------|
| 조건희 | 프론트엔드 모바일 대응기능까지 [구현 완료](https://github.com/Jongwoo0101/Where-To-Play/commit/0833df210a2a8fbd4d0e83f6052d11e28aae2504)✅ / 운동장 찾기 -> 지도까지 띄우는 거 까지 구현 완료 / 로그인 구현 완료  |
| 민현규 | [피그마 프로토타입](https://www.figma.com/file/BBg7J7nI2HS4YmovKzNsHT/Main-Screen?type=design&node-id=0%3A1&mode=design&t=0OsBAJhNRSXeguH8-1) 제작 완료✅ |
| 원종우 | 피그마 기반 [프론트엔드 라이트 버전](https://github.com/Jongwoo0101/Where-To-Play/commit/d0890354d78eacb3fc0394947c812f6f9f40d6e3) 구현완료✅ |

<br />

**팀원별 의견**
| 이름 | 의견 |
|------|------|
| 조건희 | 우선순위 카테고리를 만들어서 텍스트타입 input 대신에 드롭다운 체크박스로 만들자 / 테마지도 -> 확장가능성 |
| 원종우 | 우선순위 추가와 테마지도 관련부분은 데드라인이 8월12일이므로 일단 보류하자 |

<br />

**📋 TODO**
| 이름 | TODO |
|------|------|
| 전체 | 우선순위 해시태그 각자 5개씩 생각하기 (추 후 개발할 때 사용될 예정) |
| 조건희 | 프론트 / 백엔드 나머지 구현 |
| 민현규 | 로고제작 |
| 원종우 | 깃허브 리드미 수정, 프론트엔드 협업 |

<br />

**📈 회의 결과**
- 우선순위 / 테마지도 부분은 일단 보류하자
- 추 후에 백엔드 개발이 완료되면 팀원들에게 관리할 수 있는 계정 지급 예정!

<br />

## ⏰ 1차 마감
**개발 진행상태** 
[![GitHub release](https://img.shields.io/github/release/Jongwoo0101/Where-To-Play.svg)](https://github.com/Jongwoo0101/Where-To-Play/releases/latest)
| 작업 완료 여부 | 작업 내용 |
|------|------|
| ✅  완료 | 로그인, 회원가입, 운동장 찾기, 운동장 등록 ([테마지도를 제외한 모든 기능 구현완료](https://github.com/Jongwoo0101/Where-To-Play/commit/4ef939012cda0064fb02e82b6742d5b43e0a80a6)) |
| ❌  미완료 | 테마지도 |

<br />

**역할별 진행상황**
| 역할 | 진행여부 |
|------|------|
| 뱅커/포토그래퍼 | 영수증/남은금액 정리하여 개인톡, 프로젝트 사진/회의 사진 정리하여 개인톡 ✅  |
| 디자이너 | 로고 디자인 ✅  |
| 마케터 | 웹사이트 홍보 (예정) |
| 커뮤니케이터 | 월요일에 프로젝트 완료 현황 개인톡 ✅  |

<br />

## 📊  프로젝트 결과 🎉
![IMG_5322](https://github.com/Jongwoo0101/Where-To-Play/assets/96978536/647e3a97-bc60-4355-a647-ef05529524ff)

<br />

## ⚙️ Used
<img src="https://img.shields.io/badge/vuejs-4FC08D?style=flat&logo=vuedotjs&logoColor=white"/> <img src="https://img.shields.io/badge/GitHub-181717?style=flat&logo=github&logoColor=white"/> <img src="https://img.shields.io/badge/django-092E20?style=flat&logo=django&logoColor=white"/>
- Vue의 컴포넌트 제작기능이 프로젝트에 적합하다고 판단하여 사용
- GitHub를 이용한 프로젝트 관리, 협업
- Python Django를 이용하여 간단한 DB 구축, 파이썬의 강력한 기능 활용

<br />

## ▶️ 실행
민감한 정보는 환경변수 설정으로 분리되어 있습니다. 개인의 어플리케이션 키로 변경/입력 후 다음 순서대로 실행하세요.
- Django key, Kakaomap API Key, Django 서버 포트

### 프론트엔드
```
cd frontend; npm run serve;
```

### 백엔드

#### SSL 인증서 X
```
cd ../backend; python manage.py runserver
```

#### SSL 인증서 O
```
cd ../backend; python manage.py runsslserver --certificate (cert_file) --key (key_file) 0.0.0.0:(port_number)
```






