![Security Audit](https://img.shields.io/badge/Security_Audit-Passed_Level_4-brightgreen)
![Build](https://img.shields.io/badge/Build-Passing-brightgreen?style=for-the-badge)
![Version](https://img.shields.io/badge/Version-1.0.0-blue?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Enterprise_Ready-success?style=for-the-badge)
![License](https://img.shields.io/badge/License-CC_BY--NC--SA_4.0-red?style=for-the-badge)

![Ableton AI Assistant Logo](build/icon.png)

# Ableton AI Assistant V1.0.0

##### 认知AI混音工程师 & MCP实时音频助手 / Cognitive AI Mixing Engineer & MCP Real-Time Audio Assistant

🌐 **阅读:** [🇬🇧 English](README.md) | [🇪🇸 Español](README_es.md) | [🇩🇪 Deutsch](README_de.md) | [🇷🇺 Русский](README_ru.md) | [🇯🇵 日本語](README_ja.md) | [🇺🇦 Українська](README_uk.md) | **🇨🇳 中文**

---

## 🎯 1. 愿景 (简介)

高级音频混音通常是一个分析瓶颈。制作人的大脑在试图解决毫米级相位冲突时会进入听觉疲劳，从而失去全局创作视角。我们开发了 Ableton AI Assistant，并对 DAW 范式提出了质疑：当机器具有计算频率掩蔽的外科手术般的精度时，为什么我们必须手动移动旋钮？这个工具是一个革命性的认知工程师。通过模型上下文协议 (MCP) 和 TCP 架构进行实时连接，Claude AI 可以“监听”控制台的状态并执行母带处理决策。

> [!NOTE]
> 由 **produktes-code** 和 **Jesús Ferrer (CHUS BZN)** 开发。

## 🚀 2. 技术部署 (安装)

为了保证跨平台稳定性，我们使用 **通过 GitHub Actions 进行自动化 CI/CD**。

#### 下载和安装
1. 导航到此存储库的 **Releases** 部分。
2. 下载适用于您操作系统的最新版本：
   - `antigravity-app.Setup.1.0.0.exe` (Windows)
   - `antigravity-app-1.0.0.dmg` (macOS)

### 🍎 macOS 用户 (Gatekeeper)
**右键单击该应用程序 -> 打开**。

### 🪟 Windows 用户 (SmartScreen)
单击 **“更多信息”**，然后单击 **“仍要运行”**。

## 🔌 3. 信号流与设置

• **Remote Script (Python):** 将 `AntigravityCore` 文件夹拖到 Ableton Live 的 Remote Scripts 路径中。
• **低延迟 TCP 套接字:** Python 脚本打开端口 `9001`。Electron 桌面应用程序通过 IPC 连接到此端口。
• **LLM 令牌:** 您的 Claude API 密钥在本地加密。

## 💻 4. 操作理念

制作人的界面设计。暗模式原则。
• **主画布 (Dashboard):** 诊断面板。
• **原生触觉控制:** 滑块毫秒级绑定到 TCP 端口。
• **异步:** 60fps UI，没有冻结。

## ⚙️ 5. 参数大师班 (功能)

- **自适应算法压缩 (Glue Compressor):** AI 根据 BPM 动态设置慢速起音和超快速释放。
- **相位与掩蔽清除 (EQ Eight):** 注入低于 120Hz 的 Side (S) 削减。
- **LLM 框架 (MCP):** AI 从数学上推理轨道状态的 JSON 数据并返回执行顺序。

## 🌍 6. 全球多模态集成

100% Unicode 支持和 7 种语言的热重载。

## 🛡️ 7. 屏蔽架构 (安全性)

• **防洪 (速率限制):** 限制异常 TCP 请求。
• **JSON 负载验证:** 防止恶意操作系统代码注入。
• **RAM 限制 (2 GB Limit):** 防止 OOM 攻击。

## 📝 8. 调试日志 (FAQ)

Q: **macOS Gatekeeper 阻止该应用程序。**
A: 右键单击 -> 打开。

Q: **TCP 死锁 / 无响应。**
A: A) 本地端口 `9001` 被防火墙阻止。B) 未分配 `AntigravityCore` 脚本。

## ⚖️ 9. 工程宣言与许可证

由 produktes-code 和 Jesus Ferrer (CHUS BZN) 创建。CC BY-NC-SA 4.0。CORPORATE STANDARD。
