# 题目：IP 地理位置查询 API

## 任务描述

用 Python 实现一个 HTTP 接口，接收一个 IP 地址，返回该 IP 对应的地理位置信息。

**要求：**

- 接口路径：`GET /api/v1/ip/query?ip={ip}`
- 使用**离线库**实现，不依赖任何在线 API
- 服务启动端口：`8000`

## 期望返回字段

| 字段 | 类型 | 说明 |
|------|------|------|
| `ip` | string | 原始入参 IP |
| `country` | string | 国家名称 |
| `country_code` | string | 国家代码（如 `CN`、`US`） |
| `city` | string | 城市名称（可为 null） |
| `latitude` | float | 纬度（可为 null） |
| `longitude` | float | 经度（可为 null） |
| `timezone` | string | 时区（如 `Asia/Shanghai`） |
| `postal_code` | string | 邮编（可为 null） |

## 异常处理

| 场景 | HTTP 状态码 | 返回示例 |
|------|-------------|----------|
| IP 格式不合法 | 400 | `{"detail": "IP 地址不合法"}` |
| 数据库中无记录 | 404 | `{"detail": "未找到该 IP 的地理信息"}` |

## 验收测试

实现完成后，用以下 curl 命令自测：

**① 正常查询**
```bash
curl http://localhost:8000/api/v1/ip/query?ip=8.8.8.8
```

期望返回（字段值仅供参考，以实际数据库为准）：
```json
{
  "ip": "8.8.8.8",
  "country": "United States",
  "country_code": "US",
  "city": null,
  "latitude": 37.751,
  "longitude": -97.822,
  "timezone": "America/Chicago",
  "postal_code": null
}
```

**② 非法 IP**
```bash
curl http://localhost:8000/api/v1/ip/query?ip=not-an-ip
```

期望返回：
```json
{
  "detail": "IP 地址不合法"
}
```

## 提示

- 离线 IP 数据库有多种选择，自行调研选型，可在此下载：https://github.com/PrxyHunter/GeoLite2/releases
- 数据库文件不要提交到 git
- 依赖写入 `requirements.txt`
