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

🌐 **他の言語で読む:** [🇬🇧 English](README.md) | [🇪🇸 Español](README_es.md) | [🇩🇪 Deutsch](README_de.md) | [🇷🇺 Русский](README_ru.md) | **🇯🇵 日本語** | [🇺🇦 Українська](README_uk.md) | [🇨🇳 中文](README_zh.md)

---

## 🎯 ビジョン（はじめに）

ミキシングは分析のボトルネックです。DAWのパラダイムに疑問を投げかけることで、このツールを開発しました。機械がマスキングを計算できるのに、なぜノブを手動で動かす必要があるのでしょうか。このAIは、MCPを介してAbletonのステータスを読み取り、マスタリングの決定を実行する認知エンジニアとして機能します。

> [!NOTE]
> Developed by **produktes-code** and **Jesús Ferrer (CHUS BZN)** to establish professional standards in commercial engineering.

---

## 📸 Interface / Ergonomics

![Desktop Interface](docs/screenshot-UI.png)


---

## ⚙️ パラメーターマスタークラス（機能）

- **アダプティブコンプレッション**：スローアタックとファストリリース（BPMに基づく）を動的に設定し、コンプレッサーをトラックの一定のペースで呼吸させます。
- **位相分解能 (EQ Eight)**：120Hz未満のSide (S) カットにより、ベースがMonoに固定され、位相の打ち消し合いが回避されます。
- **MCPプロトコル**：AIはJSONを介してトラックのステータスを読み取り、数学的な決定を実行します。
- **TCPコア**：生のTCPソケットがMIDIレイテンシなしでAbletonを制御します。
- **True Peak / LUFSマネージャー**：ストリーミングプラットフォームへの完璧な配信のためにリミッターを設定します。

---

## 🛡️ シールドアーキテクチャ（セキュリティ）

防御装甲：

• アンチフラッド：リクエストのスパイクを制限します。
• マジックバイト：16進ヘッダーの検証。
• RAM制限（2 GB）：OOM攻撃を防ぎます。

---

## 🚀 技術展開（インストール）

ゼロフリクションアーキテクチャにより、DSPとPythonがアプリケーションコアに直接コンパイルされます。

### 🍎 macOSユーザー（Gatekeeper）
有料証明書がないため、Gatekeeperはファイルを隔離します。ローカルでの正当なバイパス方法は、**アプリを右クリック -> 開く** です。

### 🪟 Windowsユーザー（SmartScreen）
`.exe`を実行すると、Windows Defenderが青い警告を表示する場合があります。**「詳細情報」**をクリックしてから、**「実行」**をクリックしてください。

---

## 📚 ドキュメントとマニュアル

公式マニュアルをダウンロードしてください：

📥 **[USER_MANUAL.pdf (PDF - 7 Languages)](docs/USER_MANUAL.pdf)**


---

## ⚖️ エンジニアリングマニフェスト、クレジット、ライセンス

produktes-codeとJesus Ferrer（CHUS BZN）によって開発されました。 CC BY-NC-SA 4.0。 企業標準。


