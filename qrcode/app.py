import base64
import io

import qrcode
from fastapi import FastAPI, HTTPException
from PIL import Image
from pydantic import BaseModel

app = FastAPI(title="二维码生成")

SUPPORTED_FORMATS = {"png", "jpeg"}


class QRCodeRequest(BaseModel):
    content: str
    size: int = 200
    format: str = "png"


class QRCodeResponse(BaseModel):
    content: str
    format: str
    image_base64: str


@app.post("/api/v1/qrcode/generate", response_model=QRCodeResponse)
def generate_qrcode(body: QRCodeRequest):
    if not body.content.strip():
        raise HTTPException(status_code=400, detail="content 不能为空")

    if not (100 <= body.size <= 1000):
        raise HTTPException(status_code=400, detail="size 范围为 100~1000")

    fmt = body.format.lower()
    if fmt not in SUPPORTED_FORMATS:
        raise HTTPException(status_code=400, detail="format 仅支持 png 或 jpeg")

    qr = qrcode.QRCode(border=1)
    qr.add_data(body.content)
    qr.make(fit=True)

    img: Image.Image = qr.make_image(fill_color="black", back_color="white").convert("RGB")
    img = img.resize((body.size, body.size), Image.LANCZOS)

    buffer = io.BytesIO()
    img.save(buffer, format=fmt.upper())
    encoded = base64.b64encode(buffer.getvalue()).decode("utf-8")

    return QRCodeResponse(content=body.content, format=fmt, image_base64=encoded)
