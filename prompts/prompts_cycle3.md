# 3주기("기록보관소", 메모리 첫 등장) — 실제 사용 프롬프트 원문·생성 파라미터·레퍼런스 순서

모델: 이미지=`nano_banana_pro`(Higgsfield), 영상=`seedance_2_5`(mode: `omni_reference`, Higgsfield), 음성=`text2speech_v2`(variant: `elevenlabs`, Higgsfield)

## 0. 재사용 고정 자산(레퍼런스)
- 메추리 표정시트 — media_id `8512a1da-71f4-4cf0-9d31-642266a844a4` (2주기에서 업로드한 것을 재사용)
- 몽글언덕 장소 컨셉 — media_id `1f8acd0c-17c8-4c65-924c-5df4f7847f07` (동일)
- 메모리 표정시트(신규 업로드) — media_id `fd9a6b57-8dec-46d2-9b39-87ebd6968421`
- 음성: 메추리=Gracie `09878754-f20b-5330-9790-58a8027ab5b2`, 메모리=Helena `3c2b83c0-2e0a-5ae8-998a-a5fe71b7eccd`

## 1. 콘택트 시트(스틸) — `nano_banana_pro`, aspect_ratio 9:16, resolution 2k

### 블록1 (혼자 불안)
image_references: [메추리 표정시트]
```
3D matte clay mascot style, consistent with reference sheets. Scene on 몽글언덕(Monggeul Hill) background: lavender-to-soft-pink gradient sky with tiny stars and ringed-planet silhouettes, smooth mint-green matte clay hill, rounded sage-green blob bushes, cracked cream egg-shaped rock, soft diffused lighting. Single character alone in a corner of the frame, off to one side, smaller in the composition to emphasize solitude: 메추리 (orange tiger-stripe matte clay blob, tiger-ear + forehead-stripe hair, paw-print belly icon) sitting hunched over with knees pulled up to her chest, arms wrapped around her own knees, shoulders drawn in small and anxious, eyes glancing sideways nervously (not making eye contact with camera), small worried frown — a visible contrast to her usual confident posture. Lots of empty background space around her to emphasize being alone. Vertical 9:16 composition, no text, no watermark.
```

### 블록2 (메모리 등장)
image_references: [메추리 표정시트, 메모리 표정시트, 몽글언덕 컨셉]
```
3D matte clay mascot style, consistent with reference sheets. Scene on 몽글언덕(Monggeul Hill) background: lavender-to-soft-pink gradient sky with tiny stars and ringed-planet silhouettes, smooth mint-green matte clay hill, rounded sage-green blob bushes, cracked cream egg-shaped rock, soft diffused lighting. Two characters, both feet firmly planted on the same ground level (no floating): 메추리 (orange tiger-stripe matte clay blob, tiger-ear + forehead-stripe hair, paw-print belly icon) positioned on SCREEN LEFT, still sitting but now turned and startled, eyes wide, mouth open mid-gasp, one hand raised defensively. 메모리 (gray/silver metallic matte clay blob, translucent blue-purple lego-block hair ornament, glossy marble-like reflective eyes, circuit-pattern cheek tattoos, CPU-chip belly icon) positioned on SCREEN RIGHT, standing calmly just having walked/stepped into frame from the side (clearly walking in on her own two feet, not floating or teleporting), a soft warm glow emanating from her CPU belly icon, gentle knowing smile, similar modest body size to 메추리 (not oversized). Vertical 9:16 composition, no text, no watermark.
```

### 블록3 (기록 재생)
image_references: [메추리 표정시트, 메모리 표정시트, 몽글언덕 컨셉]
```
3D matte clay mascot style, consistent with reference sheets. Scene on 몽글언덕(Monggeul Hill) background: lavender-to-soft-pink gradient sky with tiny stars and ringed-planet silhouettes, smooth mint-green matte clay hill, rounded sage-green blob bushes, cracked cream egg-shaped rock, soft diffused lighting. Two characters both seated facing each other, feet/bodies grounded on the same hill surface: 메추리 (orange tiger-stripe matte clay blob, tiger-ear + forehead-stripe hair, paw-print belly icon) on SCREEN LEFT, posture softened, looking down uncertainly with a small vulnerable expression, shoulders slightly hunched. 메모리 (gray/silver metallic matte clay blob, translucent blue-purple lego-block hair ornament, glossy marble-like reflective eyes, circuit-pattern cheek tattoos, CPU-chip belly icon, similar modest body size to 메추리) on SCREEN RIGHT, calm and warm expression, one hand resting on her own glowing CPU belly icon (icon lit up brighter than normal, small soft light rays), as if replaying a memory. Vertical 9:16 composition, no text, no watermark.
```

### 블록4 (자신감 회복)
image_references: [메추리 표정시트, 메모리 표정시트, 몽글언덕 컨셉]
```
3D matte clay mascot style, consistent with reference sheets. Scene on 몽글언덕(Monggeul Hill) background: lavender-to-soft-pink gradient sky with tiny stars and ringed-planet silhouettes, smooth mint-green matte clay hill, rounded sage-green blob bushes, cracked cream egg-shaped rock, soft diffused lighting. Two characters standing side by side, both feet firmly planted on the same ground level: 메추리 (orange tiger-stripe matte clay blob, tiger-ear + forehead-stripe hair, paw-print belly icon) on SCREEN LEFT, back to her confident posture — standing tall, arms crossed proudly, small determined smile. 메모리 (gray/silver metallic matte clay blob, translucent blue-purple lego-block hair ornament, glossy marble-like reflective eyes, circuit-pattern cheek tattoos, CPU-chip belly icon, similar modest body size to 메추리) on SCREEN RIGHT, standing beside her with a playful sly smile, CPU belly icon glowing again faintly. Vertical 9:16 composition, no text, no watermark.
```

## 2. 음성(오디오) — `text2speech_v2`, variant `elevenlabs`, voice_type `preset`

| 순서 | 화자 | voice_id | 대사 | 실측 길이 |
|---|---|---|---|---|
| 1 | 메추리(Gracie) | 09878754-f20b-5330-9790-58a8027ab5b2 | "누, 누구야?!" | 1.28초 |
| 2 | 메모리(Helena) | 3c2b83c0-2e0a-5ae8-998a-a5fe71b7eccd | "괜찮아, 기록하러 온 거야." | 2.08초 |
| 3 | 메추리(Gracie) | 09878754-f20b-5330-9790-58a8027ab5b2 | "나 진짜 잘한 거 맞아...?" | 1.60초 |
| 4 | 메모리(Helena) | 3c2b83c0-2e0a-5ae8-998a-a5fe71b7eccd | "이미 여기 다 기록돼 있어. 네가 까먹었을 뿐이야." | 3.20초 |
| 5 | 메추리(Gracie) | 09878754-f20b-5330-9790-58a8027ab5b2 | "...그럼 이것도 기록해놔." | 1.60초 |
| 6 | 메모리(Helena) | 3c2b83c0-2e0a-5ae8-998a-a5fe71b7eccd | "어, 방금 것도 벌써 기록 중이야." | 2.08초 |

블록2·3·4는 각각 순서 1+2, 3+4, 5+6을 ffmpeg WAV concat(0.3초 무음 간격)으로 병합 → block2_final.mp3(3.66초), block3_final.mp3(5.10초), block4_final.mp3(3.98초).

## 3. 영상 — `seedance_2_5`, mode `omni_reference`, aspect_ratio 9:16, resolution 480p, generate_audio false

### 블록1 (duration 4초, audio_references 없음 — 대사 없는 무언 블록)
start_image: 블록1 콘택트 시트 승인본
```
메추리 stays hunched over, knees pulled to chest, no dialogue. Subtle idle motion: slow anxious breathing, eyes darting side to side nervously, occasional small twitch of her tail, one hand tightening its grip around her knee. Camera fixed, no cuts. Keep the exact same background and her exact same position/scale as the start image throughout. No text, no watermark.
```

### 블록2 (duration 5초, audio_references = block2_final.mp3)
start_image: 블록2 콘택트 시트 승인본
```
Two characters exactly as in the start image: 메추리 (orange tiger-stripe blob) on SCREEN LEFT, 메모리 (gray/silver metallic blob, glowing CPU belly icon) on SCREEN RIGHT, both feet grounded on the same hill surface throughout — 메모리 does not float or teleport, she stands naturally. Audio starts at 0:00, do not stretch to fill duration. SEGMENT A (first part of audio, line: '누, 누구야?!'): ONLY SCREEN-LEFT 메추리 opens her mouth into a startled gasping shape and moves her lips, eyes wide, one hand raised defensively. SCREEN-RIGHT 메모리's mouth stays CLOSED and still (calm gentle smile, no lip movement). SEGMENT B (second part of audio, line: '괜찮아, 기록하러 온 거야.'): mouth movement SWITCHES — now ONLY SCREEN-RIGHT 메모리 opens her mouth into a small warm oval shape and moves her lips with a gentle head tilt, while SCREEN-LEFT 메추리's mouth CLOSES and stays still, still wide-eyed and wary. No text, no watermark, single continuous shot, camera fixed.
```

### 블록3 (duration 6초, audio_references = block3_final.mp3)
start_image: 블록3 콘택트 시트 승인본
```
Two characters exactly as in the start image: 메추리 (orange tiger-stripe blob) on SCREEN LEFT, 메모리 (gray/silver metallic blob) on SCREEN RIGHT, both seated and grounded, similar modest body size to each other throughout. Audio starts at 0:00, do not stretch to fill duration. SEGMENT A (first part of audio, line: '나 진짜 잘한 거 맞아...?'): ONLY SCREEN-LEFT 메추리 opens her mouth into a small hesitant wavering shape and moves her lips, looking down uncertainly. SCREEN-RIGHT 메모리's mouth stays CLOSED (warm patient smile, no lip movement), her CPU belly icon glowing steadily brighter with soft pulsing light. SEGMENT B (second part of audio, line: '이미 여기 다 기록돼 있어. 네가 까먹었을 뿐이야.'): mouth movement SWITCHES — now ONLY SCREEN-RIGHT 메모리 opens her mouth into a calm reassuring shape and moves her lips, her belly icon pulsing in sync with her speech, while SCREEN-LEFT 메추리's mouth CLOSES and stays still, listening with slowly widening eyes. No text, no watermark, single continuous shot, camera fixed.
```

### 블록4 (duration 5초, audio_references = block4_final.mp3)
start_image: 블록4 콘택트 시트 승인본
```
Two characters exactly as in the start image: 메추리 (orange tiger-stripe blob) on SCREEN LEFT, 메모리 (gray/silver metallic blob) on SCREEN RIGHT, both standing side by side, feet grounded, similar modest body size to each other throughout. Audio starts at 0:00, do not stretch to fill duration. SEGMENT A (first part of audio, line: '...그럼 이것도 기록해놔.'): ONLY SCREEN-LEFT 메추리 opens her mouth into a confident determined shape and moves her lips, arms crossed proudly, small smile. SCREEN-RIGHT 메모리's mouth stays CLOSED (playful smirk, no lip movement). SEGMENT B (second part of audio, line: '어, 방금 것도 벌써 기록 중이야.'): mouth movement SWITCHES — now ONLY SCREEN-RIGHT 메모리 opens her mouth into a playful sly shape and moves her lips, belly icon flickering faintly, while SCREEN-LEFT 메추리's mouth CLOSES into a confident closed smile, no lip movement. No text, no watermark, single continuous shot, camera fixed.
```

블록2·3·4 제출 시 Higgsfield가 "IN THE DARK" 프리셋을 추천하며 최초 제출을 차단하는 현상이 발생하여(품질 반려 아님, 논문 IV장 1절의 플랫폼 운영 실패 범주이며 표 3 집계에서는 확인 절차로서 제외), `declined_preset_id: "24bae836-2c4a-48e0-89b6-49fcc0b21612"`를 추가해 동일 프롬프트로 재제출하였다. 4개 블록 모두 재제출 포함 각 1회씩 성공(품질 반려 0건).
