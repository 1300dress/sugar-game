# SUGAR / HONEY / ICED TEA
## GAME BIBLE

**Version:** 0.1  
**Status:** Early Prototype

---

# 0. PROJECT RULE

이 문서는 `SUGAR / HONEY / ICED TEA`의
Creative Source of Truth다.

스토리, 캐릭터, 세계관, 비주얼, 게임 경험에 관한 결정은
이 문서를 기준으로 한다.

기술적 편의를 위해 확정된 스토리나 비주얼을
임의로 변경하지 않는다.

새로운 아이디어가 생겼을 경우
기존 설정을 조용히 덮어쓰지 않고
먼저 이 문서를 업데이트한다.

---

# 1. PROJECT

## Title

**SUGAR / HONEY / ICED TEA**

## Format

Browser-based interactive narrative / mini game

HTML / CSS / JavaScript 기반의
짧은 웹 인터랙티브 작품.

전통적인 의미의 게임보다는
작은 생명체를 움직이며
오브젝트와 기억을 발견하는
interactive short story에 가깝다.

---

# 2. CORE IDEA

세 가지 종류의 '단맛'을 통해
서로 다른 시기의 욕망, 사랑, 의존, 기억을 다룬다.

## SUGAR

**사춘기 / 청소년기**

달고 단순했던 최초의 욕망.

유년기의 기억과 슬픔.

오랫동안 가지고 놀아서
이제는 형태조차 닳아버린 것.

---

## HONEY

**20대 초반**

사랑과 육체성.

타인에게 강하게 매혹되는 경험.

달지만 끈적이고,
아름답지만 완전히 소유할 수 없는 것.

---

## ICED TEA

**20대 중후반 / 현재**

보다 인공적이고 일상적인 자극.

습관과 도피.

성인이 된 이후에도
계속해서 무언가를 필요로 하는 상태.

---

## Line across all three chapters

> I don't know which one is keeping me alive.

---

# 3. THIS IS NOT A GAME ABOUT WINNING

이 게임에는 기본적으로 다음 요소가 필요하지 않다.

- 점수
- 랭킹
- 경쟁
- 레벨업
- 전투
- 명확한 승리 조건
- 수집률을 채우는 행위 자체가 목적인 시스템

플레이어의 목적은

**잘하는 것**이 아니라

**머무르고, 걷고, 발견하는 것**이다.

보상은 숫자가 아니라

- 새로운 문장
- 기억
- 이미지
- 작은 변화
- 새로운 공간
- 사라지는 것

으로 주어진다.

---

# 4. PLAYER CHARACTER

플레이어는 한 마리의 개미다.

개미는 영웅이 아니다.

특별한 능력이 있는 것도 아니고
세계를 구하지도 않는다.

작고,
군집 속에 존재하며,
무언가를 찾고,
운반하고,
기억한다.

플레이어와 개미 사이에는
약간의 거리가 있어야 한다.

플레이어가 개미에게 완전히 감정이입하기보다는

**작은 생물을 관찰하고 있다는 감각**

역시 동시에 존재해야 한다.

---

# 5. THE ANT — VISUAL IDENTITY

현재 `sprites/`에 저장된
마스터 스프라이트의 개미 디자인을 기준으로 한다.

## Keywords

- monochrome
- muted sepia
- pixelated
- scanned print
- old zoological encyclopedia
- photocopy
- degraded image
- dust
- grain
- imperfect edges

개미를 일반적인 게임 마스코트처럼 만들지 않는다.

피해야 할 것:

- 과장된 표정
- 지나치게 큰 눈
- 귀여운 캐릭터화
- 매끈한 벡터 그래픽
- 과도한 squash & stretch
- 현대적인 polished pixel art

움직임은 약간 끊기거나 불완전해도 된다.

목표는

**게임 캐릭터가 움직인다**

보다

**오래된 도감에 인쇄된 생물이 갑자기 움직이기 시작한다**

에 가깝다.

---

# 6. VISUAL WORLD

세계 전체는
오래된 자료를 확대해서 들여다보는 것처럼 보인다.

## Reference feeling

- laboratory scan
- old zoological encyclopedia
- photocopied paper
- scanner texture
- dust
- film grain
- faded monochrome print
- pixel enlargement
- damaged archive

깨끗하고 현대적인 pixel-art world를 피한다.

완벽하게 정돈된 세계보다
조금 손상되고,
흐리고,
무언가 묻어 있는 세계가 좋다.

---

# 7. UI / TYPOGRAPHY

## Typography direction

- typewriter
- archival document
- specimen label
- old research material

텍스트는 UI가 설명해주는 것보다

**어딘가에서 발견한 기록**

처럼 느껴져야 한다.

피해야 할 것:

- 화려한 HUD
- 게임식 퀘스트 창
- XP bar
- 수집률 UI
- 과도한 버튼
- 불필요한 튜토리얼 문구

---

# 8. CHAPTER 01 — SUGAR

현재 가장 먼저 제작하는 챕터.

## Central Object

오래된 별사탕 한 알.

흙먼지가 묻어 있다.

오래 닳아서
멀리서 보면 개미알처럼 보일 수도 있다.

처음부터 이것이 무엇인지
명확하게 설명하지 않는다.

---

# 9. SUGAR — BASIC PROGRESSION

개미가 공간을 걷는다.

↓

무언가를 발견한다.

↓

그것이 오래된 별사탕이라는 사실이 서서히 드러난다.

↓

다른 개미들을 만난다.

↓

각 개미는 주인공에 대한
서로 다른 기억을 가지고 있다.

↓

그들의 기억은 완전히 일치하지 않는다.

↓

설탕에 대한 기억 역시 조금씩 달라진다.

↓

별사탕은 점점 닳거나 부서진다.

↓

마지막에는 작은 잔해만 남는다.

---

# 10. SUGAR — IMPORTANT LINE

> 슬픔이 다 닳아버린 후에는  
> 무엇을 가지고 놀아야 하나.

이 문장은 현재 SUGAR 챕터의
핵심적인 마지막 문장 후보다.

---

# 11. THE ANT SIBLINGS

주인공에게는 여러 마리의 개미 형제들이 있다.

현재 구상은 약 10마리.

숫자는 개발 과정에서 조정 가능하다.

이들은 주인공을 정확하게 이해하지 못했다.

하지만 악의를 가진 존재들은 아니다.

각자가 본 작은 단서만으로
주인공을 기억하고 있다.

그래서 같은 개미에 대한 기억이
서로 조금씩 다르다.

예:

> 난 네가 설탕을 싫어하는 줄 알았어.

또 다른 개미는

> 너는 항상 제일 마지막에 먹었잖아.

라고 기억할 수 있다.

또 다른 개미는

> 나는 네가 늘 꾀를 부리고 있는 줄 알았어.

라고 기억할 수도 있다.

## Core idea

**누구도 한 사람을 완전히 기억하지 못한다.**

---

# 12. HONEY

**STATUS: CONCEPT ONLY**

아직 본격적으로 구현하지 않는다.

꿀은

- 사랑
- 육체성
- 타인에게 강하게 끌리는 경험

을 상징한다.

## The Bee

꿀벌은 주인공에게
무언가를 직접 가르치는 존재가 아니다.

주인공이 스스로 느끼게 만드는 존재다.

꿀벌의 전체 모습을
쉽게 보여주지 않는 방향을 우선 고려한다.

가능한 표현:

- 날개
- 털
- 몸의 일부
- 움직임
- 그림자
- 가까운 클로즈업

기억 속에서

**가장 아름답지만 가장 완전하게 복원되지 않는 존재**

에 가깝다.

---

# 13. ICED TEA

**STATUS: CONCEPT ONLY**

20대 중후반.

성인이 된 이후의

- 반복적인 자극
- 습관
- 도피
- 의존

을 다룬다.

## The Moth

나방 아저씨가 등장한다.

Visual direction:

- 인간의 성인에 가까운 비율감
- 큰 빳빳한 날개
- 지친 모습
- 타락천사 같은 인상
- 연초를 피움
- 먼저 떠나는 존재

귀여운 곤충 캐릭터로 만들지 않는다.

조금 우습고,
조금 쓸쓸하며,
이미 너무 많은 것을 알고 있는 사람처럼 느껴져야 한다.

---

# 14. INTERACTION PHILOSOPHY

플레이어에게 모든 것을 설명하지 않는다.

가능하면 다음과 같은 직접적인 안내를 최소화한다.

> 여기로 가세요.

> 이것을 수집하세요.

> 3 / 5

> QUEST COMPLETE

플레이어가 조금 헤매는 것을 허용한다.

그러나 목표는 frustration이 아니다.

목표는 **wandering**이다.

플레이어의 질문이

> 뭘 해야 하지?

에서

> 저게 뭐지?

로 바뀌는 것이 이상적이다.

---

# 15. MOVEMENT

현재 고려하는 기본 조작:

### Move

WASD  
Arrow Keys

### Run

Shift + Movement

### Interact

E

### Mobile (touch)

- 화면을 누르고 있으면 개미가 그 방향으로 움직인다 (각도 제한 없음)
- 개미에서 멀리 누를수록 달린다 (화면 짧은 변의 약 1/3 이상)
- 개미를 짧게 탭하면 Interact
- 화면 버튼·조이스틱은 두지 않는다 (§7)
- 모바일에서는 이동 속도가 PC의 절반이다 (director decision)
- 별사탕 첫 등장 규칙(§30)은 PC와 같다

조작법은 가능한 한 단순하게 유지한다.

---

# 16. CURRENT SPRITE SYSTEM

Asset root:

`sprites/`

현재 animation groups:

- idle
- walk
- run
- turn
- interact
- dead
- front_walk (derived)
- back_walk (derived)

`front_walk` / `back_walk`는 새로 그린 그림이 아니다.
`tools/make_turn_walk.py`가 `turn_01` / `turn_02`의 다리 픽셀만
휘어서 만든 4프레임 걷기다. 몸통·더듬이·스캔 질감은 원본 그대로다.
위/아래로만 이동할 때 사용한다 (아래 = front, 위 = back).

Objects:

- sugar
- crumb
- star_candy

`preview/`의 GIF 파일은
개발 확인용이다.

실제 게임에서는 PNG frame을 사용한다.

---

# 17. SPRITE TECHNICAL RULES

기본 개미 방향은 LEFT.

오른쪽 이동 시
동일 스프라이트를 horizontal flip하여 사용한다.

CSS 사용 시 예:

`transform: scaleX(-1)`

Canvas 사용 시에도 동일한 방식으로 좌우 반전한다.

Pixel texture 보존:

`image-rendering: pixelated`

Canvas 사용 시:

`imageSmoothingEnabled = false`

---

# 18. SPRITE ANIMATION TIMING

권장값:

| Animation | Frame Interval |
|---|---:|
| idle | 400ms |
| walk | 130ms |
| run | 90ms |
| turn | 300ms |
| interact | 280ms |
| dead | 450ms |
| front_walk / back_walk | 130ms (Shift 90ms) |

`dead` animation은
마지막 frame에서 정지한다.

---

# 19. SPRITE ANCHORS

Animation group마다
원본 canvas 크기가 다르다.

따라서 캐릭터 위치는
이미지 좌상단이 아니라
BODY ANCHOR를 기준으로 렌더링한다.

| Group | Canvas | Anchor |
|---|---|---|
| idle | 285 × 161 | 172, 93 |
| walk | 223 × 147 | 136, 84 |
| run | 270 × 164 | 162, 95 |
| turn | 171 × 179 | 87, 105 |
| interact | 327 × 166 | 188, 95 |
| dead | 256 × 153 | 104, 101 |
| front_walk / back_walk | 171 × 179 | 87, 105 |

Player coordinate가 `(px, py)`라면

이미지의 좌상단 위치는 기본적으로:

`px - anchorX`

`py - anchorY`

를 기준으로 계산한다.

이 규칙은 animation group이 전환될 때
개미의 몸이 튀는 것을 방지하기 위해 중요하다.

---

# 20. OBJECT ASSETS

현재 objects:

### Sugar

- sugar_01.png
- sugar_02.png
- sugar_03.png

### Crumbs

- crumb_01.png
- crumb_02.png
- crumb_03.png
- crumb_04.png
- crumb_05.png
- crumb_06.png
- crumb_07.png
- crumb_08.png

### Star Candy

- star_candy.png

오브젝트 역시
현재 추출된 원본 pixel / scan texture를 유지한다.

임의로 다시 그리지 않는다.

---

# 21. SOUND DIRECTION

**STATUS: NOT FINAL**

현재 방향성:

- 작은 마찰음
- 종이
- 흙
- 아주 작은 발소리
- room tone
- distant mechanical noise
- tape hiss

전형적인 게임 효과음은 피한다.

음악 없이도 작품이 성립할 수 있어야 한다.

---

# 22. EMOTIONAL TARGET

이 작품은 플레이어에게

> 슬퍼하세요.

> 감동하세요.

> 이것은 트라우마입니다.

라고 말하지 않는다.

대신 플레이가 끝난 뒤

**무언가를 정확하게 이해하지 못했는데도  
조금 오래 생각나는 상태**

를 목표로 한다.

작고,

이상하고,

조금 우습고,

조금 외롭고,

이상하게 아름다운 것.

---

# 23. CREATIVE RULES

## DO

- 여백을 둔다.
- 설명하지 않는 순간을 남긴다.
- 작은 디테일을 중요하게 다룬다.
- 기억의 불완전함을 허용한다.
- 이상한 순간을 그대로 둔다.
- 플레이어가 관찰하게 한다.
- 이미지와 행동으로 이야기한다.
- 침묵도 하나의 연출로 사용한다.

## DON'T

- 모든 상징을 설명한다.
- 감정을 과장한다.
- 캐릭터를 지나치게 귀엽게 만든다.
- 일반적인 RPG 문법을 무작정 넣는다.
- 점수와 보상으로 플레이를 강제한다.
- 플레이어에게 계속 무엇을 해야 하는지 말한다.
- 기술적 편의를 이유로 확정된 비주얼을 임의 변경한다.

---

# 24. TEAM

## SUBIN
### Director / Author

최종 의사결정권자.

담당:

- 원작
- 아이디어
- 취향
- creative judgment
- 최종 선택
- playtest
- 작품이 "내 것 같다 / 아니다"에 대한 판단

---

## ChatGPT
### Creative Director / Game Designer

담당:

- 세계관
- storytelling
- narrative structure
- game experience design
- interaction concept
- dialogue
- character development
- visual direction
- image / asset development
- UX / direction
- Claude 전달용 implementation spec 작성

확정되지 않은 설정을
임의로 canon으로 만들지 않는다.

---

## Claude
### Lead Developer / Technical Operator

담당:

- HTML
- CSS
- JavaScript
- sprite implementation
- animation system
- input
- collision
- camera
- asset integration
- debugging
- performance
- repository maintenance
- GitHub deployment

Claude는 확정된

- 스토리
- 대사
- 캐릭터
- 비주얼
- 게임 경험

을 임의로 변경하지 않는다.

구현상 변경이 필요하다면
먼저 문제와 가능한 대안을 제시한다.

---

# 25. WORKFLOW

기본 제작 흐름:

SUBIN

↓

idea / feeling / feedback

↓

CHATGPT

creative development  
game design  
visual development  
narrative design

↓

IMPLEMENTATION SPEC

↓

CLAUDE

technical implementation  
test  
debug

↓

GITHUB

commit  
deploy

↓

SUBIN

playtest

↓

다시 반복

---

# 26. SOURCE OF TRUTH

## Creative Source of Truth

`GAME_BIBLE.md`

## Executable Source of Truth

GitHub repository의 최신 정상 작동 버전.

코드와 creative direction이 충돌한다고 해서
코드를 기준으로 기획을 자동 변경하지 않는다.

충돌을 먼저 확인하고
Director가 최종 결정한다.

---

# 27. DEVELOPMENT PRINCIPLE

한 번에 모든 것을 만들지 않는다.

작은 기능 하나를 구현한다.

브라우저에서 직접 확인한다.

정상 작동하면 다음 단계로 넘어간다.

현재 개발 순서:

1. Sprite assets repository에 추가
2. idle animation
3. walk animation
4. left / right movement
5. horizontal flip
6. run
7. world visual
8. star candy
9. interaction
10. first memory encounter
11. SUGAR vertical slice

---

# 28. CURRENT PRIORITY

지금 목표는 완성된 게임이 아니다.

첫 번째 목표는 단 하나다.

> **MAKE THE ANT ALIVE FIRST.**

우리 개미가
브라우저 안에서 살아 움직이게 만든다.

Everything else can wait.

---

# 29. TITLE SEQUENCE

**STATUS: CONFIRMED (intro draft 2)**

Director decisions:

- 타이틀은 `SUGAR / HONEY / ICED TEA`.
- 세 단어는 **동등한 위계**로 읽혀야 한다. 어느 하나를 크게 / 작게 하지 않는다.
- 읽는 사람이 부담스러울 정도로 크게 뜬다.
- 타이포 방향: 오락실 픽셀 글자를 종이에 인쇄된 것처럼 바랜 세피아로 처리한다
  (`intro_concepts.html` 10 WORN 기준: 단말기 글꼴, 잉크 빠짐, 1px 어긋난 잔상).
- 순서: 타이틀 → 창작자명 `@1300dress` 짧게 → 디졸브되며 개미가 보인다.
- 배치: 세 단어를 같은 크기로 세 줄 쌓는다 (`SUGAR /` `HONEY /` `ICED TEA`).

| 순서 | 길이 |
|---|---:|
| 빈 종이 (음악 시작) | 0.764초 — 음악 0.764초의 소리에 타이틀이 맞물린다 |
| 타이틀 | 2.2초 |
| 뚝 끊겨 사라짐 (빈 종이) | 1.3초 |
| `@1300dress` | 2.1초 |
| 픽셀 디졸브, 개미 등장 | 1초 |

---

# 30. STAR CANDY — FIRST APPEARANCE

**STATUS: CONFIRMED (director decision)**

- 개미가 **도합 3초 이상** 움직이면 (멈춘 시간은 세지 않음),
  새로 드러나는 방향의 바닥에서 별사탕 한 알이 보인다.
- 별사탕은 하나뿐이다.

Implementation (`index.html` STAR CANDY):

- 3초가 되는 순간 개미가 향하는 쪽 화면 바로 바깥에 놓는다.
- 아직 화면에 보이지 않았는데 개미가 방향을 크게 틀면
  새 방향의 화면 바깥으로 옮긴다 (화면 밖이라 보이지 않는다).
- 한 번 화면에 들어오면 그 자리에 고정된다.
- 개미 몸이 별사탕에 닿으면 개미가 별사탕을 등에 지고 다닌다 (director decision).
  옆모습은 배 위에 얹고 앞모습은 머리 뒤로 살짝 보이며 뒷모습은 등 위에 보인다.
  위치는 `CARRY` 표에서 동작별로 조정한다.
- 닿았는지는 더듬이와 다리 끝을 뺀 몸통 기준으로 판단한다.
- 드러난 영역을 기록하지 않는다. 상태는 숫자 몇 개뿐이라 메모리가 늘지 않는다.

---

# 31. MUSIC — SUGAR CHAPTER

**STATUS: CONFIRMED (director decision)**

- 곡: Restaurant chatter — itinerantmonk108, Freesound #874243, **CC0**
  (출처 표기 의무 없음, 상업적 사용 가능). https://freesound.org/s/874243/
- 첫 입장부터 SUGAR 챕터가 끝날 때까지만 나온다.
- 타이틀은 음악 시작 후 0.764초에 뜬다 (인트로 시간은 음악의 재생 위치를 따른다).

Implementation:

- 파일: `audio/restaurant_chatter.m4a` (원본 WAV 35MB → AAC 모노 96kbps 약 3MB).
- 스트리밍 재생 (`<audio>` 2개). 통째로 메모리에 풀지 않는다.
- 음량 0.5. 시작 0.15초만 짧게 페이드인 (클릭음 방지).
- 루프: 끝나기 2초 전부터 2초 크로스페이드. 두 번째 바퀴부터는 2초 지점에서
  시작해 0.8초의 타이틀 신호음이 반복되지 않게 한다.
- 브라우저가 소리 자동 재생을 막으면 빈 종이에 `PRESS ANY KEY`를 띄우고,
  첫 키/클릭에 음악과 인트로를 함께 시작한다.
- 음악이 1.5초 넘게 멈추면 인트로는 화면 시계로 이어서 진행한다.
- 탭을 숨기면 일시정지, 돌아오면 이어서 재생.
- 챕터 끝: `stopMusic(ms)`로 페이드아웃 (아직 연결 전).

---

# 32. THE ANT SIBLINGS — A to J

**STATUS: DRAFT (director review)**

§11의 형제 개미 열 마리. 내부 이름은 알파벳 A–J.

새로 그리지 않는다. 모두 마스터 walk 스프라이트에서
다리를 자르고 더듬이를 닳게 하고 인쇄를 바래게 해서 만든다.

## 뽑는 방법

`tools/make_siblings.py`가 seed로 두 숫자를 랜덤하게 뽑는다.

- **SIZE** 0.62–1.28 (주인공 = 1)
- **IMPAIRMENT 장애도** 0–1

나머지는 이 둘에서 나온다.

- 속도: 클수록 빠르고 장애도가 높을수록 느리다
- 걸음 프레임 수와 프레임별 유지 시간:
  0–0.15 고른 4프레임 / –0.35 한 걸음 건너뛰는 3프레임 /
  –0.55 한 번 걸리는 5프레임 / –0.75 절룩이는 6프레임 / 그 이상 끄는 2프레임
- 잃은 다리: 0.3 미만 0개 / 0.65 미만 1개 / 그 이상 2개 (앞·가운데·뒷다리 중)
- 더듬이: intact / worn / stubs
- 인쇄 바램과 잉크 농도는 따로 랜덤
- 움직임 규칙 10가지를 한 마리에 하나씩, 겹치지 않게 준다
  (크기와 장애도에 어울리는 규칙을 먼저 고른다)

현재 seed 2833 (크기와 장애도가 고르게 퍼지는 seed로 골랐다).
seed를 바꾸면 열 마리가 모두 다시 뽑힌다.

## 결과

| | SIZE | 장애도 | SPEED | 프레임 | 다리 | 더듬이 | 규칙 |
|---|---:|---:|---:|---:|---|---|---|
| A | 1.12 | 0.09 | 173 | 4 | 6/6 | intact | pace — 같은 구간을 왔다 갔다 한다 |
| B | 0.89 | 0.54 | 94 | 5 | 5/6 앞 | intact | circle — 한 자리를 크게 맴돈다 |
| C | 0.74 | 0.62 | 79 | 6 | 5/6 가운데 | worn | freeze — 다가가면 그 자리에 굳는다 |
| D | 0.70 | 0.80 | 69 | 2 | 4/6 앞·뒤 | worn | veer — 똑바로 가려 하지만 한쪽으로 휜다 |
| E | 0.93 | 0.84 | 84 | 2 | 4/6 가운데·앞 | stubs | wander — 정한 곳 없이 헤맨다 |
| F | 1.25 | 0.98 | 78 | 2 | 4/6 가운데·앞 | stubs | stop_go — 몇 걸음 가다 멈춘다 |
| G | 1.04 | 0.36 | 126 | 5 | 5/6 뒤 | intact | straight — 곧게 간다 |
| H | 0.64 | 0.03 | 116 | 4 | 6/6 | intact | zigzag — 갈지자로 간다 |
| I | 0.81 | 0.86 | 65 | 2 | 4/6 가운데·앞 | worn | retreat — 다가가면 뒷걸음친다 |
| J | 1.08 | 0.21 | 154 | 3 | 6/6 | intact | follow — 거리를 두고 따라온다 |

SPEED는 world px/s (주인공 걷기 155).

## 파일

- `sprites/siblings/<A–J>/walk_01..04.png`
- `sprites/siblings/siblings.json` — 게임이 읽는 모든 숫자 (손으로 고치지 않는다)
- `sprites/preview/siblings_sheet.png` — 메인컷 시안 (`tools/make_siblings_sheet.py`, Pillow 필요)

아직 게임에는 넣지 않았다. 만나는 과정은 다음 단계.

---

# 33. MEETING THE SIBLINGS — TALK

**STATUS: CONFIRMED (director decision)**

- 별사탕을 등에 진 뒤 도합 3초를 걸으면 A가 나타난다.
  별사탕처럼 진행 방향 화면 바로 바깥에 놓이고 화면에 들어오면 그 자리가 집이 된다.
- 형제는 A → J 순서로 한 마리씩 만난다.
- 형제를 클릭(폰은 탭)하면 그 형제의 대화 세트가 01 → 02 → 03 순서로 하나씩 나온다.
- **대화는 둘이 옆에 붙어 마주볼 때만 시작된다.** 주인공이 옆모습으로 그 형제 쪽을 보고,
  높이가 거의 같고(24px 안), 두 몸 사이 틈이 -12~34px일 때.
  - 조건이 안 맞을 때 형제를 클릭하면 대화 대신 평소처럼 그쪽으로 걸어간다.
  - 바로 옆인데 반대쪽을 보고 있으면 클릭이 주인공을 그 형제 쪽으로 돌려세운다 (대화는 다음 클릭).
  - 주인공이 바로 옆에 오면 형제는 멈춰서 주인공 쪽을 본다. 움직이는 형제와도 만날 수 있게.
  - I(retreat)는 계속 뒷걸음치다 집에서 180px 넘게 밀리면 몰려서 멈춘다.
- 세트 안의 줄은 한 호흡씩 천천히 나온다 (줄 사이 0.9초 + 글자당 0.055초). 클릭해도 빨라지지 않는다.
- 한 세트가 사라진 뒤 5초 동안은 말을 걸어도 대답하지 않는다.
- 한 세트가 끝나면 그 형제는 이리저리 방향을 틀며 3~5초 동안 자리를 떠났다가
  자기 움직임 규칙으로 돌아오며 원래 자리 쪽으로 온다 (director decision).
  상수: `SIB_AWAY_MIN` `SIB_AWAY_MAX` `SIB_AWAY_TURN`
- 03까지 다 들은 형제는 더 대답하지 않는다.
- 주인공은 대답하지 않는다. 듣기만 한다.
- 03까지 다 듣고 그 글이 사라진 뒤 2초를 더 걸으면 다음 형제가 나타난다.
- 말하는 동안 형제는 멈춰서 주인공 쪽을 본다. 끝나면 자기 움직임 규칙(§32)으로 돌아간다.
- I의 03도 다른 형제와 같은 규칙을 따른다 (ChatGPT 제안인 "떠날 때만"은 보류).
- 대사 원문: `data/siblings_dialogue.json` (ChatGPT Dialogue Study 02 그대로)

## 대사 표시

**확정: 1 ink (말풍선 없음)** (director decision). 나머지 셋은 다시 볼 때를 위해 코드에 남겨 둔다.

시안 4종:

`sprites/preview/talk_styles.png`

| | 이름 | 형태 |
|---|---|---|
| 1 | ink (기본값) | 말풍선 없음. 종이에 바로 찍힌 타자 글씨 |
| 2 | label | 말풍선 없음. 표본 라벨처럼 위아래 선과 핀으로 개미에 연결 |
| 3 | slip | 말풍선. 바닥에 놓인 찢어진 종이 쪽지 |
| 4 | outline | 말풍선. 1비트 잉크 테두리와 계단 꼬리 |

주소 끝에 `#ink` `#label` `#slip` `#outline`을 붙여 바꿔 볼 수 있다.
글은 형제 위에 놓고 자리가 없거나 주인공을 가리면 아래로 옮긴다.

---

# 34. ENCOUNTER — THE HERO'S THOUGHT

**STATUS: CONFIRMED (director decision)**

형제를 처음 만나는 순간 주인공이 잠깐 멈춰 그 형제를 보며 떠올리는 두 문장.
대화가 아니다. 형제는 듣지 못한다. 튜토리얼도 아니다.
슬픈 기억과 우스운 기억을 구분하지 않고 담담하게.

- 형제가 처음 화면 안에 들어오고 1초 뒤에 최초 1회만 자동으로 일어난다 (director decision).
  그 순간 형제가 화면 밖으로 잠깐 나가 있으면 다시 보일 때 시작한다.
- 주인공은 저절로 멈추고 그 형제 쪽으로 돌아선다. 바라보는 형제도 잠시 멈춘다.
- 0.3초 → 첫 문장(이름) 1.1초 → 사라짐 → 0.5초 → 두 번째 문장(기억) 1.5초 + 글자당 0.04초 → 사라짐
- 두 문장은 주인공 위 같은 자리에 하나씩만. 형제 대사와 같은 타자 글씨. 버튼이나 선택지 없음.
- 끝나면 바로 다시 움직일 수 있다. 누르고 있던 키나 손가락도 그대로 이어진다.
- 동시에 둘 이상 일어나지 않고 형제의 대화(§33) 중에는 시작되지 않는다.
- 독백 중에는 형제를 클릭해도 대화가 시작되지 않는다. 독백이 끝난 뒤 마주보고 말을 건다.
- 대사 원문: `data/siblings_encounter.json` (최종 채택본. 단어와 문장 구조를 바꾸지 않는다. 문장부호는 물음표만.)

| | 이름 | 첫 문장 | 두 번째 문장 |
|---|---|---|---|
| A | Jack | That's Jack | Our big brother |
| B | Jules | There's Jules | He stole my breakfast yesterday |
| C | Timmy | That's Timmy | He tried to jump off the wall again |
| D | Dex | There's Dex | He punched Jack last Tuesday |
| E | Ollie | There's Ollie | He spent all morning watching a dead beetle |
| F | Alfie | That's Alfie | He thinks everyone hates him |
| G | Max | There's Max | He challenged a bird to a race once |
| H | Milo | That's Milo | He still leaves food out for our dead brother |
| I | Finn | That's Finn | He'll walk away if I get any closer |
| J | Toby | That's Toby | He still thinks I know where we're going |

조정용 상수 (`index.html` ENCOUNTER): `ENCOUNTER_DELAY` `ENCOUNTER_PAUSE`
`ENCOUNTER_FIRST_HOLD` `ENCOUNTER_GAP` `ENCOUNTER_SECOND_HOLD` `ENCOUNTER_PER_CHAR` `ENCOUNTER_FADE`

---

# 35. FAVICON / LINK PREVIEW

- 파비콘: 마스터 개미 앞모습(`turn_01`)의 머리 부분을 종이색 바탕에. 16px에서도 눈이 보인다.
  `icons/favicon.ico` (16·32·48) · `icons/favicon-32.png` · `icons/apple-touch-icon.png` (180) · `icons/icon-512.png`
- 링크 미리보기 (카카오톡 등): `icons/og-image.jpg` 1200×630.
  실제 게임 화면으로 만들었다. 별사탕을 진 개미 + 인트로와 같은 낡은 잉크 타이틀 + @1300dress.
- 제목: SUGAR / HONEY / ICED TEA · 설명: Chapter 01 — SUGAR
- 미리보기 이미지와 주소는 절대 경로다. 저장소 이름이나 주소가 바뀌면 `index.html` 머리의 og 태그를 같이 고친다.
- 카카오톡은 미리보기를 캐시한다. 바꾼 뒤 예전 모습이 나오면 Kakao Developers의 공유 디버거에서 캐시를 지운다.
