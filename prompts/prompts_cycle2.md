# 2주기("진짜 대장이 되는 법", 메롱이·메추리 첫 등장) — 실제 사용 프롬프트 원문·생성 파라미터·레퍼런스 순서

모델: 이미지=`nano_banana_pro`(Higgsfield), 영상=`seedance_2_5`(mode: `omni_reference`, Higgsfield), 음성=`text2speech_v2`(variant: `elevenlabs`, Higgsfield)

## 0. 재사용 고정 자산(레퍼런스)
- 메롱이 표정시트 — media_id `8e334567-2f9d-4b69-9f4b-e66e1c0835fd`
- 메추리 표정시트 — media_id `8512a1da-71f4-4cf0-9d31-642266a844a4`
- 타원이 표정시트 — media_id `664ef077-063b-4ebe-a6f0-5fb847526aba`
- 몽글언덕 장소 컨셉 — media_id `1f8acd0c-17c8-4c65-924c-5df4f7847f07`
- 메롱이 턴어라운드(체형 비율 보정용 추가 레퍼런스) — media_id `147b121d-1e8d-4eeb-92c4-37d235ac7ad8`
- 음성: 메롱이=Zelda `b7aaea29-0c88-5925-90c0-8f66754cda53`, 메추리=Gracie `09878754-f20b-5330-9790-58a8027ab5b2`, 타원이=Miles `e18664a7-ee4f-5273-acf8-533eb24cd366`

## 1. 콘택트 시트(스틸) — `nano_banana_pro`, aspect_ratio 9:16, resolution 2k

### 블록1 (메롱이 질주) — 최초 승인
image_references: [메롱이 표정시트, 타원이 표정시트, 몽글언덕 컨셉]
```
3D matte clay mascot style, consistent with reference sheets. Scene on 몽글언덕(Monggeul Hill) background: lavender-to-soft-pink gradient sky with tiny stars and small ringed-planet silhouettes, smooth mint-green matte clay rolling hill, 2-3 rounded sage-green blob bushes, one cracked cream egg-shaped rock landmark, soft diffused lighting no hard shadows. FOREGROUND: 메롱이 (peach/skin-tone matte clay blob body, orange 'M' hairpin exactly like reference, orange spiral belly icon) captured mid-sprint, leaning far forward, both stubby arms swung back for speed, body blurred motion lines behind her, tongue stuck out to the side in a mischievous 'meerong' face with one eye winking shut exactly like her reference expression sheet tongue-out pose. BACKGROUND/SIDE: 타원이 (cream-yellow matte clay blob, pink 'M' hairpin, star-sparkle eyes, saturn belly icon) standing flat-footed, caught completely off guard, eyes wide as circles, mouth a small round 'o' of surprise, arms slightly raised in startled reflex. Vertical 9:16 composition, clear foreground/background depth, no text, no watermark.
```

### 블록2 (자랑/시큰둥) — 최초 승인
image_references: [메롱이 표정시트, 메추리 표정시트, 몽글언덕 컨셉]
```
3D matte clay mascot style, consistent with reference sheets. Scene on 몽글언덕(Monggeul Hill) background: lavender-to-soft-pink gradient sky with tiny stars and ringed-planet silhouettes, smooth mint-green matte clay hill, rounded sage-green blob bushes, cracked cream egg-shaped rock, soft diffused lighting. Two characters seated on the grass side by side, both at same eye level, medium shot: 메롱이 (peach/skin-tone matte clay blob, orange 'M' hairpin, orange spiral belly icon) flopped down cross-legged, panting happily, big excited open-mouth grin, cheeks flushed pink, leaning toward the other character eagerly, one arm gesturing proudly at herself. 메추리 (orange tiger-stripe matte clay blob, tiger-ear + forehead-stripe hair, paw-print belly icon, big round eyes) sitting with both short arms crossed over her chest, eyes half-lidded in a deadpan unimpressed stare, mouth a small flat neutral line, head tilted slightly, clearly unimpressed body language. Vertical 9:16 composition, no text, no watermark.
```

### 블록3 (발끈/정색) v1 — 반려(체형 비율)
image_references: [메롱이 표정시트, 메추리 표정시트, 몽글언덕 컨셉]
```
(v1: 위 블록2와 동일한 3종 레퍼런스, 메롱이 체형 크기 별도 지정 없음 — 결과물에서 메롱이가 메추리보다 작게 산출되어 반려)
```

### 블록3 v2 — 재반려(턴어라운드 미참조)
image_references: [메롱이 표정시트, 메추리 표정시트, 몽글언덕 컨셉]
```
3D matte clay mascot style, consistent with reference sheets. ... IMPORTANT BODY SIZE: 메롱이 has a noticeably LARGER, bulkier, rounder body than 메추리 — her head and torso are visibly bigger in volume than 메추리's, she is the physically biggest character on screen (matching her character-sheet trait of being unusually large-bodied), NOT smaller or same size. 메롱이 flinched back slightly, shoulders raised defensively, eyebrows angled up in a flustered protest, mouth open mid-argument, cheeks blushing red with embarrassment. 메추리 leaning back with arms still crossed, eyes narrowed sternly, eyebrows drawn down in a serious scolding look (calm and firm, not shouting), small flat frown, one hand slightly raised near her own face mid-sigh. Vertical 9:16 composition, no text, no watermark.
```
(사용자가 "메롱이는 캐릭터 시트 참고해서 다시 만들어줘"라고 지적 — 체형은 커졌으나 비율 자체가 턴어라운드와 다름)

### 블록3 v3 — 최종 승인
image_references: [메롱이 턴어라운드, 메롱이 표정시트, 메추리 표정시트, 몽글언덕 컨셉]
```
3D matte clay mascot style. Scene on 몽글언덕(Monggeul Hill): lavender-to-soft-pink gradient sky, tiny stars, ringed-planet silhouettes, smooth mint-green matte clay hill, rounded sage-green blob bushes, cracked cream egg-shaped rock, soft diffused lighting. 메롱이 MUST match her turnaround reference sheet exactly: very large round bobble-head (head is clearly bigger in proportion than body, roughly matching the turnaround sheet's head-to-body ratio), short round torso, short stubby arms held slightly away from body, short stubby legs, peach/skin-tone matte clay, orange 'M'-shaped hairpin (two connected loops), orange spiral belly icon centered on lower torso. Her overall body volume (head+torso combined) is noticeably BIGGER than 메추리's — she is the physically largest character in the scene. Two characters seated facing each other: 메롱이 (matching description above) flinched back slightly, shoulders raised defensively, eyebrows angled up in a flustered protest, mouth open mid-argument, cheeks blushing red. 메추리 (orange tiger-stripe matte clay blob, tiger-ear + forehead-stripe hair, paw-print belly icon, clearly smaller/more compact body than 메롱이) leaning back with arms crossed, eyes narrowed sternly, small flat frown, one hand slightly raised near her face mid-sigh. Vertical 9:16 composition, no text, no watermark.
```

### 블록4 (울컥/도망) — 최초 승인
image_references: [메롱이 표정시트, 몽글언덕 컨셉]
```
3D matte clay mascot style, consistent with reference sheet. Scene on 몽글언덕(Monggeul Hill) background: lavender-to-soft-pink gradient sky with tiny stars and ringed-planet silhouettes, smooth mint-green matte clay hill, rounded sage-green blob bushes, cracked cream egg-shaped rock, soft diffused lighting. Single character full shot: 메롱이 (peach/skin-tone matte clay blob body, orange 'M' hairpin exactly like reference, orange spiral belly icon) alone, body already half-turned away as if about to run off, head turned back toward camera, face crumpling with a choked-up wounded expression: eyebrows pinched upward in the middle, eyes glassy and welling with tears, mouth pressed into a wobbling frown, one stubby arm half-raised toward her own face. Motion blur starting at her turned-back foot suggesting she is about to bolt. Vertical 9:16 composition, no text, no watermark.
```

### 블록5 (발견/솔직) — 최초 승인
image_references: [메롱이 표정시트, 타원이 표정시트, 몽글언덕 컨셉]
```
3D matte clay mascot style, consistent with reference sheets. Scene on 몽글언덕(Monggeul Hill) background near a rounded sage-green blob bush used as a hiding spot: lavender-to-soft-pink gradient sky with tiny stars and ringed-planet silhouettes, smooth mint-green matte clay hill, cracked cream egg-shaped rock, soft diffused lighting. 타원이 (cream-yellow matte clay blob, pink 'M' hairpin, star-sparkle eyes, saturn belly icon) crouching down and leaning in beside the bush, head tilted, one eyebrow raised, warm genuinely curious open expression, gentle small smile, clearly just found someone. 메롱이 (peach/skin-tone matte clay blob, orange 'M' hairpin, orange spiral belly icon) curled up small behind the bush, shoulders hunched up to her ears, body scrunched inward trying to look smaller, cheeks blushing pink with embarrassment, eyes looking down and away avoiding eye contact, small awkward closed-mouth smile. Vertical 9:16 composition, no text, no watermark.
```

### 블록6 (어깨동무) v1 — 반려(그룹 구도 접지)
image_references: [메롱이 표정시트, 메추리 표정시트, 타원이 표정시트, 몽글언덕 컨셉]
```
3D matte clay mascot style, consistent with reference sheets. ... Three characters in one group shot: 메추리 has popped up from behind, standing between and slightly behind 메롱이 and 타원이, both short arms stretched out slinging over their shoulders, head tilted with a confident sly smirking grin. 메롱이 on one side, startled upward, eyes wide circles, small round open mouth of surprise. 타원이 on the other side, equally startled, eyes wide, small round open mouth of surprise, both frozen mid-reaction with no dialogue. Vertical 9:16 composition, no text, no watermark.
```
(사용자가 "6번 구도 이질감 들어 다시 생성해줘" — 메추리가 접지 없이 공중에 뜬 것처럼 보임)

### 블록6 v2 — 최종 승인
image_references: [메롱이 턴어라운드, 메롱이 표정시트, 메추리 표정시트, 타원이 표정시트, 몽글언덕 컨셉]
```
3D matte clay mascot style. Scene on 몽글언덕(Monggeul Hill): lavender-to-soft-pink gradient sky, tiny stars, ringed-planet silhouettes, smooth mint-green matte clay hill, rounded sage-green blob bushes, cracked cream egg-shaped rock, soft diffused lighting. IMPORTANT: ALL THREE PAIRS OF FEET FIRMLY PLANTED ON THE SAME GROUND LEVEL (no floating, no character elevated above the others in a way that looks pasted-in) — 메추리 stands directly behind and between 메롱이 and 타원이, on the same hill surface just slightly further back, her body naturally overlapping/tucked behind theirs for depth. Both of 메추리's short arms are bent and physically DRAPED ACROSS 메롱이's and 타원이's shoulders/backs (real physical contact, not floating in the air to the sides), head leaning forward between them with a confident sly smirk. 메롱이 (peach/skin-tone blob, MUST match her turnaround reference: very large round bobble-head, noticeably bigger body than 메추리 and 타원이, orange 'M' hairpin, orange spiral belly icon) on one side, startled upward, eyes wide circles, small round open mouth of surprise. 타원이 (cream-yellow blob, pink 'M' hairpin, star-sparkle eyes, saturn belly icon, similar modest size to 메추리) on the other side, equally startled, eyes wide, small round open mouth of surprise. All three characters' feet cast consistent shadows on the same ground plane. Vertical 9:16 composition, no text, no watermark.
```

## 2. 음성(오디오) — `text2speech_v2`, variant `elevenlabs`, voice_type `preset`

| 순서 | 화자 | voice_id | 대사 |
|---|---|---|---|
| 1 | 메롱이(Zelda) | b7aaea29-0c88-5925-90c0-8f66754cda53 | "메~~롱!!" |
| 2 | 메롱이(Zelda) | b7aaea29-0c88-5925-90c0-8f66754cda53 | "나 방금 완전 센 거 했다! 봤어?" |
| 3 | 메추리(Gracie) | 09878754-f20b-5330-9790-58a8027ab5b2 | "...메롱 한 거? 너 필살기 그거 하나잖아." (429 레이트리밋 1회 재시도 후 성공) |
| 4 | 메롱이(Zelda) | b7aaea29-0c88-5925-90c0-8f66754cda53 | "이, 이번엔 진짜 세게 했다고!" |
| 5 | 메추리(Gracie) | 09878754-f20b-5330-9790-58a8027ab5b2 | "처음 보는 애한테 그러는 거 아니야. 그거 안 무섭고, 안 멋있어." |
| 6 | 메롱이(Zelda) | b7aaea29-0c88-5925-90c0-8f66754cda53 | "...몰라!" (0.88초 — audio_references 최소 길이 미달로 영상 생성 시 제외) |
| 7 | 타원이(Miles) | e18664a7-ee4f-5273-acf8-533eb24cd366 | "너 진짜 세 보이고 싶었던 거야, 추리처럼?" |
| 8 | 메롱이(Zelda) | b7aaea29-0c88-5925-90c0-8f66754cda53 | "...어. 근데 나는 메롱밖에 못하잖아." |
| 9 | 메추리(Gracie) | 09878754-f20b-5330-9790-58a8027ab5b2 | "그래서 내가 방법 하나 가르쳐줄게 — 대장은 세 보이는 게 아니라, 쫄지 않는 거야. 메롱 그거, 나한테 한번 해봐." |

블록2·3·5는 각각 순서 2+3, 4+5, 7+8을 ffmpeg WAV concat(0.3초 무음 간격)으로 병합.

## 3. 영상 — `seedance_2_5`, mode `omni_reference`, aspect_ratio 9:16, resolution 480p, generate_audio false

(최종 승인본 프롬프트만 기재. 블록1·2·3·6은 사용자 피드백에 따라 v2 재생성됨 — 아래는 v2/최종 버전)

### 블록1 v2 (duration 4초, audio_references = 순서1 "메~~롱!!")
start_image: 블록1 콘택트 시트 승인본
```
메롱이 is actively SPRINTING, not standing still — her legs cycle in a continuous running stride (alternating legs kicking forward and back, feet lifting off the ground each stride), her body bounces slightly with each step, both arms pump back and forth in a running motion, and she visibly TRAVELS a large distance across the frame from her starting position near the left toward off-screen right, with a motion-blur trail stretching behind her the whole time. This running motion continues for the ENTIRE shot, not just the first second — she never stands still or freezes mid-pose. Around 0:00-0:01 while saying '메~~롱!!' her mouth is OPEN: wide rounded oval shape with her pink tongue sticking out to the side, then her mouth CLOSES into a playful smirk as she keeps sprinting past 타원이 and continues running until she exits the frame on the right edge. 타원이 stays planted in place the whole shot, no dialogue, eyes snap wide into circles and mouth opens into a small round 'o' of surprise partway through, tracking 메롱이 with her eyes as she runs past. Audio starts at 0:00, do not stretch to fill duration. No text, no watermark, no camera cuts, single continuous shot, camera fixed.
```

### 블록2 v2 (duration 7초, audio_references = 순서2+3 병합)
start_image: 블록2 콘택트 시트 승인본
```
Two characters seated side by side, exactly as in the start image: 메롱이 (peach/skin-tone blob, orange 'M' hairpin) is positioned on SCREEN LEFT. 메추리 (orange tiger-stripe blob, tiger ears) is positioned on SCREEN RIGHT. Audio starts at 0:00, do not stretch to fill duration. SEGMENT A (first half of audio, line: '나 방금 완전 센 거 했다! 봤어?'): ONLY the SCREEN-LEFT character 메롱이 opens her mouth and moves her lips (big rounded open mouth shape, visible soft pink interior, no thick lips), bobbing her head excitedly and gesturing one hand at her own chest. During this entire segment the SCREEN-RIGHT character 메추리's mouth stays completely CLOSED and still (flat deadpan line, arms crossed, no lip movement at all). SEGMENT B (second half of audio, line: '...메롱 한 거? 너 필살기 그거 하나잖아.'): the mouth movement SWITCHES — now ONLY the SCREEN-RIGHT character 메추리 opens her mouth and moves her lips (small flat oval shape, deadpan tilt of her head), while the SCREEN-LEFT character 메롱이's mouth CLOSES completely and stays still (satisfied closed grin, no lip movement) for the rest of the shot. The mouth-moving character must switch exactly once, in sync with the audio switching speakers. No text, no watermark, single continuous shot, camera fixed.
```
(v1은 화면 좌/우 위치를 명시하지 않아 메추리 대사 구간에도 메롱이 입이 움직이는 오귀속 발생 — 논문 IV장 3절 패턴 (6))

### 블록3 v2 (duration 7초, audio_references = 순서4+5 병합, start_image = 블록3 v3 콘택트 시트)
```
Two characters seated facing each other, exactly as in the start image: 메롱이 (peach/skin-tone blob, LARGE bulky bobble-head body, orange 'M' hairpin) is on SCREEN LEFT and is clearly the physically bigger character. 메추리 (orange tiger-stripe blob, visibly smaller/more compact body, tiger ears) is on SCREEN RIGHT. Keep 메롱이 noticeably bigger-bodied than 메추리 throughout the whole shot — do not shrink her relative size at any frame. Audio starts at 0:00, do not stretch to fill duration. SEGMENT A (first half of audio, line: '이, 이번엔 진짜 세게 했다고!'): ONLY the SCREEN-LEFT character 메롱이 opens her mouth into a flustered wobbling oval shape and moves her lips, small jerky defensive head movements, reddening cheeks. During this the SCREEN-RIGHT character 메추리's mouth stays CLOSED and still. SEGMENT B (second half of audio, line: '처음 보는 애한테 그러는 거 아니야. 그거 안 무섭고, 안 멋있어.'): mouth movement SWITCHES — now ONLY SCREEN-RIGHT 메추리 opens her mouth into a small firm oval shape and moves her lips with a slow stern head shake, while SCREEN-LEFT 메롱이's mouth CLOSES completely and stays still in a tense flat line. Eyes stay narrowed sternly on 메추리 throughout. No text, no watermark, single continuous shot, camera fixed.
```

### 블록4 (duration 5초, audio_references 없음 — 대사 0.88초로 최소 길이 미달, 동작 지시문으로만 타이밍 대체)
start_image: 블록4 콘택트 시트 승인본
```
Audio starts at 0:00, do not stretch to fill duration. 메롱이 face keeps crumpling, eyes welling further, mouth OPENS briefly into a small quivering wavering oval shape to say '...몰라!', immediately after finishing the line her mouth CLOSES shut, then she spins her body around and sprints off toward the background with motion-blur trailing behind her until she exits frame. No text, no watermark, single continuous shot.
```
(원래 audio_references와 함께 duration 4·5초로 제출 시도했으나 422 오류 반복 — 오디오 레퍼런스 제외 후 성공)

### 블록5 (duration 8초, audio_references = 순서7+8 병합)
start_image: 블록5 콘택트 시트 승인본
```
(블록2/3와 유사한 SEGMENT A/B 좌우 위치 명시 구조 — 타원이 SCREEN LEFT, 메롱이 SCREEN RIGHT로 지정, 순서7 구간엔 타원이만, 순서8 구간엔 메롱이만 입 움직임)
```

### 블록6 v2 (duration 8초, audio_references = 순서9, start_image = 블록6 v2 콘택트 시트)
```
Three characters exactly as in the start image: 메추리 stands directly behind and between 메롱이 and 타원이, both her arms physically draped across their shoulders the whole shot (real contact, not floating), all three characters' feet stay planted on the same ground level throughout, no floating or elevation change. 메추리 keeps her confident sly smirk expression, mouth OPENS into a wide confident open shape (visible soft interior, no thick lips) delivering the full line '그래서 내가 방법 하나 가르쳐줄게 — 대장은 세 보이는 게 아니라, 쫄지 않는 거야. 메롱 그거, 나한테 한번 해봐.' with animated head tilts, then mouth CLOSES into the sly smirk at the end. 메롱이 and 타원이 stay frozen in their startled silent reaction the whole shot: no lip movement, mouths stay in a small round 'o' of surprise, only subtle blinking. Audio starts at 0:00, do not stretch to fill duration. No text, no watermark, single continuous shot, camera fixed.
```

전 영상 생성에서 Higgsfield가 "IN THE DARK" 프리셋을 추천하며 최초 제출을 차단하는 현상이 여러 차례 발생하여 `declined_preset_id`를 추가해 재제출하였다(품질 반려와 별개, 논문 IV장 1절 표 3 주 참고).
