# GAAW Model Replication Package

생성형 AI 애니메이션의 캐릭터 일관성 유지를 위한 게이트형 자산고정 워크플로우 모델
*A Gated Asset-Lock Workflow Model for Character Consistency in Generative AI Animation*

위 논문의 재현 패키지입니다. 2·3주기 프롬프트와 생성 파라미터, 레퍼런스 순서, 보정·재시도 이력, 1주기-A 승인 기록, 표 4(보조 정량 지표)의 산정 코드와 입력 이미지를 수록합니다.

## 저장소 구성

```
.
├── prompts/
│   ├── prompts_cycle2.md   # 2주기("진짜 대장이 되는 법", 6블록) 콘택트 시트·음성·영상 프롬프트 + 반려 이력
│   └── prompts_cycle3.md   # 3주기("기록보관소", 4블록) 콘택트 시트·음성·영상 프롬프트
├── records/
│   ├── cycle1a_contact_sheet_approval.md  # 1주기-A 콘택트 시트 최종 승인 기록
│   └── cycle1a_video_approval.md          # 1주기-A 영상 최종 승인·음성 교체 기록
├── ssim_clip_analysis.py   # 표 4 보조 정량 지표 산정 코드 (CLIP ViT-B/32, OpenAI 사전학습 가중치)
├── crops/                  # CLIP 이미지-레퍼런스 유사도 입력(캐릭터 크롭 5장)
│   ├── ref.png              # 캐릭터 턴어라운드 레퍼런스(정면) 크롭
│   ├── b3_before.png        # 블록3(발끈/정색) 수정 전 스틸 크롭
│   ├── b3_after.png         # 블록3 수정 후 스틸 크롭
│   ├── b6_before.png        # 블록6(어깨동무) 수정 전 스틸 크롭
│   └── b6_after.png         # 블록6 수정 후 스틸 크롭
├── full_frames/            # SSIM·CLIP 텍스트 유사도 입력(콘택트 시트 원본 4장)
│   ├── b3_before_full.png
│   ├── b3_after_full.png
│   ├── b6_before_full.png
│   └── b6_after_full.png
├── requirements.txt
├── NOTICE.md                # 자료 종류별 이용 조건(코드/이미지/프롬프트·기록이 서로 다름 — 반드시 확인)
└── LICENSE-CODE             # ssim_clip_analysis.py에만 적용되는 MIT 라이선스
```

## 수록 범위와 한계

- **1주기 프롬프트 원문은 포함되지 않습니다.** 1주기-A(성장서사 티저)·1주기-B(리빌챌린지)는 2·3주기와 같은 수준의 원문 로그가 보존되어 있지 않습니다. 논문 IV장 1절과 표 3에 밝힌 대로 1주기 수치는 파일·로그 기반 사후 재구성에 의한 최소치입니다. 1주기-A는 `records/`의 승인 기록을 수록하며, 1주기-B는 별도 승인 문서가 없습니다.
- **원시 타임스탬프 로그는 포함되지 않습니다.** 생성 시도·재시도·반려 기록은 `prompts/`에 서술되어 있으나, 표 3의 생성 호출 활성 시간을 산출한 요청별 타임스탬프 원본은 수록되어 있지 않습니다.
- **일부 프롬프트는 축약되어 있습니다.** `prompts_cycle2.md`의 영상 프롬프트는 최종 승인본 위주로 기재했고, 콘택트 시트 블록3 v1·v2와 블록6 v1, 영상 블록5는 전문이 아닌 축약 또는 요약입니다.
- **레퍼런스 원본 시트는 ID로 기재됩니다.** 표정 시트·장소 컨셉은 Higgsfield `media_id`로 표기되며, 이 ID는 플랫폼 계정 밖에서 내려받을 수 없습니다.
- **생성 결과 자체의 재현은 보장되지 않습니다.** 상용 플랫폼의 모델 갱신에 따라 같은 프롬프트로도 다른 결과가 산출될 수 있습니다(논문 V장 2절).

## 재현 방법

저장소 루트에서 실행합니다.

```bash
pip install -r requirements.txt
python ssim_clip_analysis.py
```

CLIP 이미지-레퍼런스 유사도와 CLIP 텍스트 유사도가 위 명령으로 산정됩니다. SSIM은 ffmpeg가 별도로 필요합니다.

```bash
ffmpeg -i full_frames/b3_before_full.png -i full_frames/b3_after_full.png -lavfi ssim -f null -
ffmpeg -i full_frames/b6_before_full.png -i full_frames/b6_after_full.png -lavfi ssim -f null -
```

## 논문 표 4 결과 (참고용)

| 블록 | SSIM(전체 구도, 수정 전↔후) | CLIP 이미지-레퍼런스 유사도(전→후) | CLIP 텍스트 유사도 차이(크기차이−크기유사, 전→후) |
|---|---|---|---|
| 블록3(발끈/정색) | 0.9095 | 0.8773 → 0.8668 | −0.0222 → −0.0173 |
| 블록6(어깨동무) | 0.9158 | 0.8008 → 0.7969 | −0.0217 → −0.0153 |

해석은 논문 IV장 3절을 참고하세요. 두 블록에 한정된 산정이지만, 항목별 이진 대조에서 반려된 상대 체형 결함이 레퍼런스 대비 CLIP 유사도에는 드러나지 않았으며, 이는 게이트 2를 자동 유사도 점수가 아닌 항목별 이진 대조로 운영한 근거입니다.

## 이용 조건

코드·이미지·프롬프트와 기록에 서로 다른 조건이 적용됩니다. 반드시 [NOTICE.md](NOTICE.md)를 먼저 확인하세요.

## 인용

```
이수연, "생성형 AI 애니메이션의 캐릭터 일관성 유지를 위한 게이트형 자산고정 워크플로우 모델," 한국콘텐츠학회논문지, 게재 확정, 2026.
```
