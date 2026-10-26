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
| 빈 종이 | 0.6초 |
| 타이틀 | 2.2초 |
| 뚝 끊겨 사라짐 (빈 종이) | 1.3초 |
| `@1300dress` | 2.1초 |
| 픽셀 디졸브, 개미 등장 | 1초 |
