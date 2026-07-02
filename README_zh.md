<p align="center">
  <img src="build/icon.png" width="128" height="128" style="border-radius: 28px; box-shadow: 0 8px 24px rgba(0,0,0,0.25);" alt="Ableton AI Assistant Logo" />
</p>

<h1 align="center">Ableton AI Assistant V1.0.0</h1>

<p align="center">
  <b>Cognitive AI Mixing Engineer & MCP Real-Time Audio Assistant</b><br/>
  <i>Ingeniero de Mezcla Cognitivo IA y Asistente de Audio en Tiempo Real MCP</i>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Build-Passing-brightgreen?style=for-the-badge" alt="Build" />
  <img src="https://img.shields.io/badge/Version-1.0.0-blue?style=for-the-badge" alt="Version" />
  <img src="https://img.shields.io/badge/Status-Enterprise_Ready-success?style=for-the-badge" alt="Status" />
  <img src="https://img.shields.io/badge/License-CC_BY--NC--SA_4.0-red?style=for-the-badge" alt="License" />
</p>

🌐 **其他语言阅读:** [🇬🇧 English](README.md) | [🇪🇸 Español](README_es.md) | [🇩🇪 Deutsch](README_de.md) | [🇷🇺 Русский](README_ru.md) | [🇯🇵 日本語](README_ja.md) | [🇺🇦 Українська](README_uk.md) | **🇨🇳 中文**

---

## 🎯 愿景 (介绍)

混音是一个分析瓶颈。我们通过质疑 DAW 范式来开发此工具：当机器可以计算掩蔽时，为什么还要手动转动旋钮？此 AI 充当认知工程师，通过 MCP 读取 Ableton 的状态并执行母带处理决策。

> [!NOTE]
> Developed by **produktes-code** and **Jesús Ferrer (CHUS BZN)** to establish professional standards in commercial engineering.

---

## 📸 Interface / Ergonomics

![Desktop Interface](docs/screenshot-UI.png)


---

## ⚙️ 参数大师班 (功能)

- **自适应压缩**：动态设置慢速起音和快速释放（基于 BPM），让压缩器随着轨道节奏呼吸。
- **相位解析 (EQ Eight)**：120Hz 以下的 Side (S) 切割将低音固定在 Mono 中，以避免相位抵消。
- **MCP 协议**：AI 通过 JSON 读取轨道状态并执行数学决策。
- **TCP 核心**：原始 TCP 套接字无延迟地控制 Ableton。
- **True Peak / LUFS 管理器**：设置限制器以完美交付给流媒体平台。

---

## 🛡️ 屏蔽架构 (安全)

防御装甲：

• 反洪泛：限制请求峰值。
• 魔法字节：十六进制标头验证。
• RAM 限制 (2 GB)：防止 OOM 攻击。

---

## 🚀 技术部署 (安装)

零摩擦架构：

• macOS：Gatekeeper 将隔离二进制文件。工程师解决方案：“右键单击 -> 打开”。
• Windows：自动 PATH 配置。

---

## 📚 文档和手册

请下载我们的官方手册：

📥 **[USER_MANUAL.pdf (PDF - 7 Languages)](docs/USER_MANUAL.pdf)**


---

## ⚖️ 工程宣言，鸣谢与许可

由 produktes-code 和 Jesus Ferrer (CHUS BZN) 开发。CC BY-NC-SA 4.0。企业标准。



⚠️ macOS Users Notice: When opening the application for the first time, macOS may show a security warning. Solution: right-click on the application and select "Open", then click "Open" in the dialog. If it was already blocked, go to System Preferences > Privacy & Security and click "Open Anyway".