"""
논문 표 4 보조 정량 지표(SSIM · CLIP 유사도) 산정 코드
대상: 블록3(발끈/정색), 블록6(어깨동무) — IV장 3절 패턴 (7)·(8)로 반려 후 보정된 2주기 블록

요구 패키지: torch, open_clip_torch, pillow
  pip install torch open_clip_torch pillow
SSIM은 별도로 ffmpeg(>=4.x, --enable-libavfilter의 ssim 필터 포함)가 필요합니다.

사용된 크롭 이미지는 이 저장소의 crops/ 폴더에 함께 포함되어 있습니다.
  crops/ref.png        — 메롱이 턴어라운드 레퍼런스(정면) 크롭
  crops/b3_before.png  — 블록3 수정 전 스틸의 메롱이 크롭
  crops/b3_after.png   — 블록3 수정 후 스틸의 메롱이 크롭
  crops/b6_before.png  — 블록6 수정 전 스틸의 메롱이 크롭(얼굴 위주)
  crops/b6_after.png   — 블록6 수정 후 스틸의 메롱이 크롭(얼굴 위주)

전체 구도 이미지는 full_frames/ 폴더에 포함되어 있습니다. 저장소 루트에서 실행하세요.
"""

import torch
import torch.nn.functional as F
import open_clip
from PIL import Image

MODEL_NAME = "ViT-B-32"
PRETRAINED = "openai"


def load_clip():
    model, _, preprocess = open_clip.create_model_and_transforms(MODEL_NAME, pretrained=PRETRAINED)
    tokenizer = open_clip.get_tokenizer(MODEL_NAME)
    model.eval()
    return model, preprocess, tokenizer


def embed_image(model, preprocess, path):
    im = preprocess(Image.open(path).convert("RGB")).unsqueeze(0)
    with torch.no_grad():
        f = model.encode_image(im)
        return f / f.norm(dim=-1, keepdim=True)


def embed_text(model, tokenizer, text):
    tok = tokenizer([text])
    with torch.no_grad():
        f = model.encode_text(tok)
        return f / f.norm(dim=-1, keepdim=True)


def run_image_reference_similarity(model, preprocess):
    """CLIP 이미지-이미지 유사도: 캐릭터 크롭 vs 레퍼런스 시트 크롭"""
    ref = embed_image(model, preprocess, "crops/ref.png")
    pairs = {
        "block3_before": "crops/b3_before.png",
        "block3_after": "crops/b3_after.png",
        "block6_before": "crops/b6_before.png",
        "block6_after": "crops/b6_after.png",
    }
    print("\n[CLIP 이미지-레퍼런스 유사도]")
    for name, path in pairs.items():
        v = embed_image(model, preprocess, path)
        sim = F.cosine_similarity(ref, v).item()
        print(f"  {name}: {sim:.4f}")


def run_text_relation_similarity(model, preprocess, tokenizer):
    """CLIP 텍스트-이미지 유사도: 크기차이 vs 크기유사 관계 진술 프롬프트"""
    t_large = embed_text(model, tokenizer,
                          "a noticeably larger, bigger-bodied character standing next to a smaller character")
    t_similar = embed_text(model, tokenizer,
                            "two characters of about the same size standing together")

    full_frames = {
        # 전체 프레임 — 표 4 산정에 사용한 원본 콘택트 시트
        "block3_before_full": "full_frames/b3_before_full.png",
        "block3_after_full": "full_frames/b3_after_full.png",
        "block6_before_full": "full_frames/b6_before_full.png",
        "block6_after_full": "full_frames/b6_after_full.png",
    }
    print("\n[CLIP 텍스트-이미지 유사도]")
    for name, path in full_frames.items():
        v = embed_image(model, preprocess, path)
        s_large = F.cosine_similarity(v, t_large).item()
        s_similar = F.cosine_similarity(v, t_similar).item()
        print(f"  {name}: sim(large-diff)={s_large:.4f}  sim(similar-size)={s_similar:.4f}  diff={s_large - s_similar:+.4f}")


if __name__ == "__main__":
    model, preprocess, tokenizer = load_clip()
    run_image_reference_similarity(model, preprocess)
    run_text_relation_similarity(model, preprocess, tokenizer)

    print("""
[SSIM — 별도 ffmpeg 명령으로 산정, 참고용]
  ffmpeg -i full_frames/b3_before_full.png -i full_frames/b3_after_full.png -lavfi ssim -f null -
  ffmpeg -i full_frames/b6_before_full.png -i full_frames/b6_after_full.png -lavfi ssim -f null -
""")
