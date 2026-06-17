# 题目：二维码生成 API

## 任务描述

用 Python 实现一个 HTTP 接口，接收文本内容，生成对应的二维码图片并以 Base64 格式返回。

**要求：**

- 接口路径：`POST /api/v1/qrcode/generate`
- 使用**离线库**实现，不依赖任何在线服务
- 服务启动端口：`8000`

## 入参

| 字段 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `content` | string | ✅ | 二维码内容（URL、文本等） |
| `size` | integer | ❌ | 图片尺寸（像素），默认 200，范围 100~1000 |
| `format` | string | ❌ | 图片格式，支持 `png` / `jpeg`，默认 `png` |

**请求示例：**

```json
{
  "content": "https://github.com",
  "size": 200,
  "format": "png"
}
```

## 期望返回字段

| 字段 | 类型 | 说明 |
|------|------|------|
| `content` | string | 原始入参内容 |
| `format` | string | 图片格式 |
| `image_base64` | string | 二维码图片的 Base64 编码字符串 |

**返回示例：**

```json
{
  "content": "https://github.com",
  "format": "png",
  "image_base64": "iVBORw0KGgoAAAANSUhEUgAA..."
}
```

## 异常处理

| 场景 | HTTP 状态码 | 返回示例 |
|------|-------------|----------|
| `content` 为空 | 400 | `{"detail": "content 不能为空"}` |
| `size` 超出范围 | 400 | `{"detail": "size 范围为 100~1000"}` |
| `format` 不支持 | 400 | `{"detail": "format 仅支持 png 或 jpeg"}` |

## 验收测试

实现完成后，用以下 curl 命令自测：

**① 正常生成（默认参数）**
```bash
curl -X POST http://localhost:8000/api/v1/qrcode/generate \
  -H "Content-Type: application/json" \
  -d '{"content": "https://github.com"}'
```

期望返回：
```json
{
  "content": "https://github.com",
  "format": "png",
  "image_base64": "iVBORw0KGgoAAAANSUhEUgAA..."
}
```

**② 指定尺寸和格式**
```bash
curl -X POST http://localhost:8000/api/v1/qrcode/generate \
  -H "Content-Type: application/json" \
  -d '{"content": "hello world", "size": 300, "format": "jpeg"}'
```

**③ content 为空**
```bash
curl -X POST http://localhost:8000/api/v1/qrcode/generate \
  -H "Content-Type: application/json" \
  -d '{"content": ""}'
```

期望返回：
```json
{
  "detail": "content 不能为空"
}
```

**④ size 超出范围**
```bash
curl -X POST http://localhost:8000/api/v1/qrcode/generate \
  -H "Content-Type: application/json" \
  -d '{"content": "test", "size": 9999}'
```

期望返回：
```json
{
  "detail": "size 范围为 100~1000"
}
```

## 提示

- 推荐使用 `qrcode` 库生成二维码，`Pillow` 库处理图片
- 图片生成到**内存**即可，不需要写入磁盘
- Base64 编码可使用 Python 内置 `base64` 模块
- 依赖写入 `requirements.txt`
