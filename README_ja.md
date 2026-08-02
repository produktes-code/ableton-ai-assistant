![Security Audit](https://img.shields.io/badge/Security_Audit-Passed_Level_4-brightgreen)
![Build](https://img.shields.io/badge/Build-Passing-brightgreen?style=for-the-badge)
![Version](https://img.shields.io/badge/Version-1.0.0-blue?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Enterprise_Ready-success?style=for-the-badge)
![License](https://img.shields.io/badge/License-CC_BY--NC--SA_4.0-red?style=for-the-badge)

![Ableton AI Assistant Logo](build/icon.png)

# Ableton AI Assistant V1.0.0

##### 認知型AIミキシングエンジニア & MCPリアルタイムオーディオアシスタント / Cognitive AI Mixing Engineer & MCP Real-Time Audio Assistant

🌐 **日本語:** [🇬🇧 English](README.md) | [🇪🇸 Español](README_es.md) | [🇩🇪 Deutsch](README_de.md) | [🇷🇺 Русский](README_ru.md) | **🇯🇵 日本語** | [🇺🇦 Українська](README_uk.md) | [🇨🇳 中文](README_zh.md)

---

## 📖 ユーザーマニュアル (PDF) のダウンロード
高度な手順については、公式マニュアルをダウンロードしてください：
📥 **[USER_MANUAL.pdf (V1.0.0) をダウンロード](https://github.com/produktes-code/ableton-ai-assistant/releases/download/v1.0.0/USER_MANUAL.pdf)**

---

## 🎯 1. ビジョン (概要)

高度なオーディオミキシングは、しばしば分析のボトルネックになります。機械が周波数マスキングを計算するための外科的な精度を持っているのに、なぜ手動でノブを動かさなければならないのでしょうか？このツールは革新的な認知エンジニアです。Model Context Protocol (MCP) とTCPアーキテクチャを通じてリアルタイムで接続し、Claude AIはコンソールの状態を「聴き」、マスタリングの決定を実行します。

> [!NOTE]
> **produktes-code** と **Jesús Ferrer (CHUS BZN)** によって開発されました。

## 🚀 2. 技術的なデプロイ (インストール)

クロスプラットフォームの安定性を保証するため、**GitHub Actionsを介した自動CI/CD**を採用しています。
ソースコードは、クラウド内のWindows、macOS、Linux環境向けにコンパイルされています。

#### ダウンロードとインストール
1. このリポジトリの **[Releases](https://github.com/produktes-code/ableton-ai-assistant/releases)** セクションに移動します。
2. オペレーティングシステム用の最新ビルドをダウンロードします：
   - `Ableton.AI.Assistant.Setup.1.0.0.exe` (Windows)
   - `Ableton.AI.Assistant-1.0.0.dmg` (macOS)
   - `Ableton.AI.Assistant-1.0.0.AppImage` (Linux Portable)
   - `Ableton.AI.Assistant-1.0.0.deb` (Linux Ubuntu)

### 🍎 macOSユーザー (Gatekeeper)
有料のApple開発者証明書がないため、Gatekeeperはバイナリをブロックします。正当なバイパス方法は、**アプリを右クリックして「開く」**を選択することです。

### 🪟 Windowsユーザー (SmartScreen)
Windows Defenderが青い警告画面を表示する場合があります。**「詳細情報」**をクリックし、**「実行」**をクリックします。

## 🔌 3. 信号フローとセットアップ

• **Remote Script (Python):** `AntigravityCore` フォルダをAbleton LiveのRemote Scriptsパスにドラッグする必要があります。
• **低遅延TCPソケット:** Pythonスクリプトはサイレントにポート `9001` を開きます。ElectronデスクトップアプリケーションはIPCを介してこのポートに接続します。
• **LLMトークン:** Claude APIキーはローカルで暗号化されます。

## 💻 4. 操作哲学 (ユーザーガイド)

プロデューサー向けのインターフェース設計。ダークモードの原則。
• **メインキャンバス (Dashboard):** プロジェクトの「健康状態」を即座に表示します。
• **ネイティブな触覚コントロール:** スライダーはTCPポートにミリ秒単位でバインドされています。
• **非同期性:** メインスレッドはUIを60fpsでレンダリングします。

## ⚙️ 5. パラメーターのマスタークラス (機能)

- **適応型アルゴリズム圧縮 (Glue Compressor):** AIは、セッションのBPMに基づいて、遅いアタック時間と超高速なリリースを動的に設定します。
- **マスキングと位相のクリア (EQ Eight):** 120Hz未満のSide (S)カットを注入し、サブベースをモノラルに固定します。
- **LLMフレームワーク (MCP):** AIはトラック状態のJSONデータを数学的に推論し、実行順序を返します。

## 🌍 6. グローバルマルチモーダル統合

7言語（ES、EN、DE、UK、RU、ZH、JA）の100% Unicodeサポートとホットリロード。

## 🛡️ 7. シールドアーキテクチャ (セキュリティ)

• **アンチフラッド (レート制限):** 異常なTCP要求スパイクを制限します。
• **JSONペイロードの検証:** 悪意のあるOSコードの挿入を防ぎます。
• **RAM制限 (2 GB Limit):** OOM攻撃を防ぎます。

## 📝 8. デバッグログ (FAQ)

Q: **macOS Gatekeeperがアプリをブロックする。**
A: 右クリック -> 開く。

Q: **TCPデッドロック / Ableton Liveからの応答がない。**
A: A) ローカルポート `9001` がファイアウォールでブロックされている。B) `AntigravityCore` スクリプトが割り当てられていない。

## ⚖️ 9. エンジニアリング宣言とライセンス

produktes-codeとJesus Ferrer (CHUS BZN) によって開発されました。CC BY-NC-SA 4.0。CORPORATE STANDARD。
