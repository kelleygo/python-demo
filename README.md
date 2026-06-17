# Python API 实战练习

用 Python 实现各类 API 功能的实战项目，每个功能模块放在独立文件夹中，文件夹名即功能名。

## 项目结构

```
python-demo/
├── ip/          # IP 地理位置查询
│   ├── README.md
│   ├── app.py
│   └── requirements.txt
└── ...          # 后续功能模块
```

## 模块列表

| 文件夹 | 功能 | 接口 |
| ------ | ---- | ---- |
| [ip](./ip/README.md) | IP 地理位置查询（离线） | `POST /api/v1/ip/query` |

## 约定

- 每个模块有独立的 `README.md` 说明需求和用法
- 每个模块有独立的 `requirements.txt` 管理依赖
- 使用 FastAPI 作为统一 Web 框架
- 不提交 `.venv`、离线数据库（`.mmdb`）等大文件

## 环境准备

项目使用 [uv](https://docs.astral.sh/uv/) 管理环境。

```bash
# 安装依赖（自动创建 .venv）
uv pip install -r <模块>/requirements.txt

# 启动服务示例（以 ip 模块为例）
uv run uvicorn ip.app:app --reload --port 8000
```
