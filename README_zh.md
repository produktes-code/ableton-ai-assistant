![Security Audit](https://img.shields.io/badge/Security_Audit-Passed_Level_4-brightgreen)
<p align="center">
  <img src="build/icon.png" width="128" height="128" style="border-radius: 28px; box-shadow: 0 8px 24px rgba(0,0,0,0.25);" alt="Ableton AI Assistant Logo" />
</p>

<h1 align="center">Ableton AI Assistant V1.0.0</h1>

<p align="center">
  <b>Cognitive AI Mixing Engineer & MCP Real-Time Audio Assistant</b><br/>
  <i>认知AI混音工程师 & MCP实时音频助手</i>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Build-Passing-brightgreen?style=for-the-badge" alt="Build" />
  <img src="https://img.shields.io/badge/Version-1.0.0-blue?style=for-the-badge" alt="Version" />
  <img src="https://img.shields.io/badge/Status-Enterprise_Ready-success?style=for-the-badge" alt="Status" />
  <img src="https://img.shields.io/badge/License-CC_BY--NC--SA_4.0-red?style=for-the-badge" alt="License" />
</p>

🌐 **阅读:** [🇬🇧 English](README.md) | [🇪🇸 Español](README_es.md) | [🇩🇪 Deutsch](README_de.md) | [🇷🇺 Русский](README_ru.md) | [🇯🇵 日本語](README_ja.md) | [🇺🇦 Українська](README_uk.md) | **🇨🇳 中文**

---

## 🎯 愿景 (简介)

高级音频混音通常是一个分析瓶颈。我们开发了 Ableton AI Assistant，并对 DAW 范式提出了质疑：当机器具有计算频率掩蔽的外科手术般的精度时，为什么我们必须手动移动旋钮？这个工具是一个革命性的认知工程师。通过模型上下文协议 (MCP) 和 TCP 架构进行实时连接，Claude AI 可以“监听”控制台的状态并执行母带处理决策。

> [!NOTE]
> 由 **produktes-code** 和 **Jesús Ferrer (CHUS BZN)** 开发。

---

## 📸 接口 (Ergonomics)

![Desktop Interface](docs/screenshot-UI.png)

---

## ⚙️ 参数大师班 (功能)

- **自适应算法压缩 (Glue Compressor)**: AI 根据 BPM 动态设置慢速起音和超快速释放。
- **相位与掩蔽清除 (EQ Eight)**: 注入低于 120Hz 的 Side (S) 削减。
- **LLM 框架 (MCP)**: AI 从数学上推理轨道状态的 JSON 数据并返回执行顺序。
- **异步**: 60fps UI，没有冻结。

---

## 🛡️ 屏蔽架构 (安全性)

• **防洪 (速率限制)**: 限制异常 TCP 请求。
• **JSON 负载验证**: 防止恶意操作系统代码注入。
• **RAM 限制 (2 GB Limit)**: 防止 OOM 攻击。

---

## 🚀 技术部署 与 CI/CD 安装

为了保证跨平台稳定性，我们使用 **通过 GitHub Actions 进行自动化 CI/CD**。
源代码在云中为 Windows、macOS 和 Linux 环境编译。

### 🛠️ 下载安装程序
导航到此存储库的 **[Releases](https://github.com/produktes-code/ableton-ai-assistant/releases)** 部分以获取您的操作系统：
- **Windows**: `Ableton.AI.Assistant.Setup.1.0.0.exe`
- **macOS**: `Ableton.AI.Assistant-1.0.0.dmg`
- **Linux**: `Ableton.AI.Assistant-1.0.0.deb` / `Ableton.AI.Assistant-1.0.0.AppImage`

### 🍎 macOS 用户 (Gatekeeper)
**右键单击该应用程序 -> 打开**。

### 🪟 Windows 用户 (SmartScreen)
单击 **“更多信息”**，然后单击 **“仍要运行”**。

### 🐧 Linux 用户 (AppImage & Debian)
- **AppImage**: 赋予执行权限：
  `chmod +x Ableton.AI.Assistant-1.0.0.AppImage`
- **Debian Package (`.deb`)**: 通过终端安装：
  `sudo dpkg -i Ableton.AI.Assistant-1.0.0.deb`

---

## 🔌 信号流与设置

• **Remote Script (Python)**: 将 `AntigravityCore` 文件夹拖到 Ableton Live 的 Remote Scripts 路径中。
• **低延迟 TCP 套接字**: Python 脚本打开端口 `9001`。
• **LLM 令牌**: 您的 Claude API 密钥在本地加密。

---

## 📚 下载用户手册 (PDF)

有关高级说明，请下载官方手册：

📥 **[USER_MANUAL.pdf (PDF - 7 Languages)](https://github.com/produktes-code/ableton-ai-assistant/releases/download/v1.0.0/USER_MANUAL.pdf)**

---

## ⚖️ 工程宣言与许可证

由 produktes-code 和 Jesus Ferrer (CHUS BZN) 创建。CC BY-NC-SA 4.0。CORPORATE STANDARD。

## Auditoría de Seguridad
Este repositorio superó satisfactoriamente una auditoría de Nivel 4 (análisis estático, remediación de dependencias y linting de seguridad) con fecha **2026-07-27**.
