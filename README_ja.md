![Security Audit](https://img.shields.io/badge/Security_Audit-Passed_Level_4-brightgreen)
<p align="center">
  <img src="build/icon.png" width="128" height="128" style="border-radius: 28px; box-shadow: 0 8px 24px rgba(0,0,0,0.25);" alt="Ableton AI Assistant Logo" />
</p>

<h1 align="center">Ableton AI Assistant V1.0.0</h1>

<p align="center">
  <b>Cognitive AI Mixing Engineer & MCP Real-Time Audio Assistant</b><br/>
  <i>認知型AIミキシングエンジニア & MCPリアルタイムオーディオアシスタント</i>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Build-Passing-brightgreen?style=for-the-badge" alt="Build" />
  <img src="https://img.shields.io/badge/Version-1.0.0-blue?style=for-the-badge" alt="Version" />
  <img src="https://img.shields.io/badge/Status-Enterprise_Ready-success?style=for-the-badge" alt="Status" />
  <img src="https://img.shields.io/badge/License-CC_BY--NC--SA_4.0-red?style=for-the-badge" alt="License" />
</p>

🌐 **日本語:** [🇬🇧 English](README.md) | [🇪🇸 Español](README_es.md) | [🇩🇪 Deutsch](README_de.md) | [🇷🇺 Русский](README_ru.md) | **🇯🇵 日本語** | [🇺🇦 Українська](README_uk.md) | [🇨🇳 中文](README_zh.md)

---

## 🎯 ビジョン (概要)

高度なオーディオミキシングは、しばしば分析のボトルネックになります。機械が周波数マスキングを計算するための外科的な精度を持っているのに、なぜ手動でノブを動かさなければならないのでしょうか？このツールは革新的な認知エンジニアです。Model Context Protocol (MCP) とTCPアーキテクチャを通じてリアルタイムで接続し、Claude AIはコンソールの状態を「聴き」、マスタリングの決定を実行します。

> [!NOTE]
> **produktes-code** と **Jesús Ferrer (CHUS BZN)** によって開発されました。

---

## 📸 インターフェイス (Ergonomics)

![Desktop Interface](docs/screenshot-UI.png)

---

## ⚙️ パラメーターのマスタークラス (機能)

- **適応型アルゴリズム圧縮 (Glue Compressor)**: AIは、セッションのBPMに基づいて、遅いアタック時間と超高速なリリースを動的に設定します。
- **マスキングと位相のクリア (EQ Eight)**: 120Hz未満のSide (S)カットを注入し、サブベースをモノラルに固定します。
- **LLMフレームワーク (MCP)**: AIはトラック状態のJSONデータを数学的に推論し、実行順序を返します。
- **非同期アーキテクチャ**: メインスレッドはUIを60fpsでレンダリングし、バックグラウンドで処理を行います。

---

## 🛡️ シールドアーキテクチャ (セキュリティ)

• **アンチフラッド (レート制限)**: 異常なTCP要求スパイクを制限します。
• **JSONペイロードの検証**: 悪意のあるOSコードの挿入を防ぎます。
• **RAM制限 (2 GB Limit)**: モデルの重い応答をブロックしてOOM攻撃を防ぎます。

---

## 🚀 技術的なデプロイ とCI/CDインストール

クロスプラットフォームの安定性を保証するため、**GitHub Actionsを介した自動CI/CD**を採用しています。
ソースコードは、クラウド内のWindows、macOS、Linux環境向けにネイティブコンパイルされています。

### 🛠️ インストーラーのダウンロード
このリポジトリの **[Releases](https://github.com/produktes-code/ableton-ai-assistant/releases)** セクションに移動して、OS用のバイナリをダウンロードします：
- **Windows**: `Ableton.AI.Assistant.Setup.1.0.0.exe`
- **macOS**: `Ableton.AI.Assistant-1.0.0.dmg`
- **Linux**: `Ableton.AI.Assistant-1.0.0.deb` / `Ableton.AI.Assistant-1.0.0.AppImage`

### 🍎 macOSユーザー (Gatekeeper)
**アプリを右クリックして「開く」**を選択してください。

### 🪟 Windowsユーザー (SmartScreen)
**「詳細情報」**をクリックし、**「実行」**をクリックしてください。

### 🐧 Linuxユーザー (AppImage & Debian)
- **AppImage**: 実行権限を付与します：
  `chmod +x Ableton.AI.Assistant-1.0.0.AppImage` 
- **Debianパッケージ (`.deb`)**: ターミナルからインストール：
  `sudo dpkg -i Ableton.AI.Assistant-1.0.0.deb`

---

## 🔌 信号フローとセットアップ

• **Remote Script (Python)**: `AntigravityCore` フォルダをAbleton LiveのRemote Scriptsパスにドラッグします。
• **低遅延TCPソケット**: Pythonスクリプトはポート `9001` を開きます。
• **LLMトークン**: Claude APIキーはローカルで暗号化されます。

---

## 📚 ドキュメントとマニュアル

高度な手順については、公式マニュアルをダウンロードしてください：

📥 **[USER_MANUAL.pdf (PDF - 7 Languages)](https://github.com/produktes-code/ableton-ai-assistant/releases/download/v1.0.0/USER_MANUAL.pdf)**

---

## ⚖️ エンジニアリング宣言とライセンス

produktes-codeとJesus Ferrer (CHUS BZN) によって開発されました。CC BY-NC-SA 4.0。CORPORATE STANDARD。

## Auditoría de Seguridad
Este repositorio superó satisfactoriamente una auditoría de Nivel 4 (análisis estático, remediación de dependencias y linting de seguridad) con fecha **2026-07-27**.
