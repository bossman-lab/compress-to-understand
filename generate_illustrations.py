#!/usr/bin/env python3
"""Generate book-frame SVG diagrams for 《学透》"""
import os

OUT = "/root/Projects/compress-to-understand/illustrations"
os.makedirs(OUT, exist_ok=True)

# ===========================
# F-01: 全书学习系统架构图
# ===========================
f01 = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 900 680" font-family="'Noto Sans SC', 'Microsoft YaHei', sans-serif">
  <defs>
    <linearGradient id="bg" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#f8fafc"/>
      <stop offset="100%" stop-color="#f1f5f9"/>
    </linearGradient>
    <linearGradient id="v1" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#6366f1"/><stop offset="100%" stop-color="#818cf8"/>
    </linearGradient>
    <linearGradient id="v2" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#0891b2"/><stop offset="100%" stop-color="#22d3ee"/>
    </linearGradient>
    <linearGradient id="v3" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#059669"/><stop offset="100%" stop-color="#34d399"/>
    </linearGradient>
    <linearGradient id="v4" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#d97706"/><stop offset="100%" stop-color="#fbbf24"/>
    </linearGradient>
    <linearGradient id="v5" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#dc2626"/><stop offset="100%" stop-color="#f87171"/>
    </linearGradient>
    <filter id="shadow">
      <feDropShadow dx="0" dy="2" stdDeviation="3" flood-opacity="0.1"/>
    </filter>
  </defs>
  <rect width="900" height="680" fill="url(#bg)" rx="12"/>

  <!-- Title -->
  <text x="450" y="40" text-anchor="middle" font-size="18" font-weight="bold" fill="#1e293b">《学透：高阶学习者的压缩操作系统》全书架构</text>

  <!-- ===== V1: 为什么 ===== -->
  <rect x="40" y="60" width="820" height="100" rx="8" fill="#eef2ff" stroke="#6366f1" stroke-width="1.5" filter="url(#shadow)"/>
  <rect x="40" y="60" width="180" height="100" rx="8" fill="url(#v1)"/>
  <text x="130" y="100" text-anchor="middle" fill="white" font-size="22" font-weight="bold">第一卷</text>
  <text x="130" y="125" text-anchor="middle" fill="white" font-size="13">为什么</text>
  <text x="130" y="145" text-anchor="middle" fill="#e0e7ff" font-size="10">压缩即理解</text>
  <text x="260" y="92" fill="#1e293b" font-size="13" font-weight="bold">ch01 理解的假象 → ch02 压缩即理解 → ch03 学习法即压缩配置</text>
  <text x="260" y="115" fill="#475569" font-size="11">核心问题：为什么学了很多却用不出来？</text>
  <text x="260" y="135" fill="#475569" font-size="11">核心答案：理解 = 找到最短生成规则 &nbsp;&nbsp;|&nbsp;&nbsp; 预测测试 = 检验真理解的唯一标准</text>

  <!-- Arrow V1→V2 -->
  <polygon points="450,160 440,170 460,170" fill="#6366f1"/>
  <line x1="450" y1="160" x2="450" y2="170" stroke="#6366f1" stroke-width="2"/>

  <!-- ===== V2: 怎么学 ===== -->
  <rect x="40" y="180" width="820" height="100" rx="8" fill="#ecfeff" stroke="#0891b2" stroke-width="1.5" filter="url(#shadow)"/>
  <rect x="40" y="180" width="180" height="100" rx="8" fill="url(#v2)"/>
  <text x="130" y="220" text-anchor="middle" fill="white" font-size="22" font-weight="bold">第二卷</text>
  <text x="130" y="245" text-anchor="middle" fill="white" font-size="13">怎么学</text>
  <text x="130" y="265" text-anchor="middle" fill="#cffafe" font-size="10">经典方法压缩论</text>
  <text x="260" y="212" fill="#1e293b" font-size="13" font-weight="bold">ch04 记忆层 → ch05 认知层 → ch06 知识构建 → ch07 实践反馈</text>
  <text x="260" y="235" fill="#475569" font-size="11">用压缩论统一解释：Anki/SQ3R/Bloom/Dreyfus/Zettelkasten/Kolb/刻意练习</text>
  <text x="260" y="255" fill="#475569" font-size="11">每个方法 = 一种压缩配置 &nbsp;&nbsp;|&nbsp;&nbsp; 每个方法的盲区 = 压缩边界</text>

  <!-- Arrow V2→V3 -->
  <polygon points="450,280 440,290 460,290" fill="#0891b2"/>
  <line x1="450" y1="280" x2="450" y2="290" stroke="#0891b2" stroke-width="2"/>

  <!-- ===== V3: 操作系统 ===== -->
  <rect x="40" y="300" width="820" height="120" rx="8" fill="#ecfdf5" stroke="#059669" stroke-width="1.5" filter="url(#shadow)"/>
  <rect x="40" y="300" width="180" height="120" rx="8" fill="url(#v3)"/>
  <text x="130" y="345" text-anchor="middle" fill="white" font-size="22" font-weight="bold">第三卷</text>
  <text x="130" y="370" text-anchor="middle" fill="white" font-size="13">操作系统</text>
  <text x="130" y="390" text-anchor="middle" fill="#d1fae5" font-size="10">完整学习管线</text>
  <text x="260" y="325" fill="#1e293b" font-size="13" font-weight="bold">ch08 HLT筛选 → ch09 差异驱动 → ch10 精通五层 → ch11 Agent时代</text>
  <text x="260" y="350" fill="#475569" font-size="11">输入 → 筛选(值不值得学) → 编码(差异映射) → 质检(五层流水线) → 辅助(AI代理)</text>
  <text x="260" y="375" fill="#475569" font-size="11">HLT: 半衰期×杠杆×转移性 &nbsp;&nbsp;|&nbsp;&nbsp; 精通五层: L1跑通→L2拆解→L3调参→L4边界→L5封装</text>
  <text x="260" y="400" fill="#059669" font-size="10">本书独创：HLT评分 | 精通五层 | 差异驱动学习法</text>

  <!-- Arrow V3→V4 -->
  <polygon points="450,420 440,430 460,430" fill="#059669"/>
  <line x1="450" y1="420" x2="450" y2="430" stroke="#059669" stroke-width="2"/>

  <!-- ===== V4: 实战 ===== -->
  <rect x="40" y="440" width="820" height="95" rx="8" fill="#fffbeb" stroke="#d97706" stroke-width="1.5" filter="url(#shadow)"/>
  <rect x="40" y="440" width="180" height="95" rx="8" fill="url(#v4)"/>
  <text x="130" y="478" text-anchor="middle" fill="white" font-size="22" font-weight="bold">第四卷</text>
  <text x="130" y="503" text-anchor="middle" fill="white" font-size="13">实战</text>
  <text x="130" y="523" text-anchor="middle" fill="#fef3c7" font-size="10">真实场景演练</text>
  <text x="260" y="472" fill="#1e293b" font-size="13" font-weight="bold">ch12 学编程语言 → ch13 学硬科学 → ch14 构建个人学习系统</text>
  <text x="260" y="495" fill="#475569" font-size="11">Python→Rust: 精通五层全流程 &nbsp;&nbsp;|&nbsp;&nbsp; 信息论: 差异驱动攻克数学</text>
  <text x="260" y="518" fill="#d97706" font-size="10">输出：可运行的个人学习操作系统文档</text>

  <!-- Arrow V4→V5 -->
  <polygon points="450,535 440,545 460,545" fill="#d97706"/>
  <line x1="450" y1="535" x2="450" y2="545" stroke="#d97706" stroke-width="2"/>

  <!-- ===== V5: 边界 ===== -->
  <rect x="40" y="555" width="820" height="70" rx="8" fill="#fef2f2" stroke="#dc2626" stroke-width="1.5" filter="url(#shadow)"/>
  <rect x="40" y="555" width="180" height="70" rx="8" fill="url(#v5)"/>
  <text x="130" y="588" text-anchor="middle" fill="white" font-size="22" font-weight="bold">第五卷</text>
  <text x="130" y="613" text-anchor="middle" fill="white" font-size="13">边界</text>
  <text x="260" y="585" fill="#1e293b" font-size="13" font-weight="bold">ch15 当压缩框架失效时</text>
  <text x="260" y="610" fill="#475569" font-size="11">四个边界：基元不可压缩 / 数据不足 / 扭曲激励 / 经验不可传递</text>

  <!-- Footer -->
  <text x="450" y="668" text-anchor="middle" fill="#94a3b8" font-size="10">序幕（问题引入）→ 五卷递进 → 终章（学习是终身的模型迭代）</text>
</svg>'''

with open(f"{OUT}/F01-full-architecture.svg", "w") as f:
    f.write(f01)
print(f"✅ F01: 全书架构图 ({len(f01)} chars)")

# ===========================
# F-02: 压缩管道全景图
# ===========================
f02 = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 520" font-family="'Noto Sans SC', 'Microsoft YaHei', sans-serif">
  <defs>
    <linearGradient id="bg2" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#f8fafc"/><stop offset="100%" stop-color="#f1f5f9"/>
    </linearGradient>
    <linearGradient id="step1" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#6366f1"/><stop offset="100%" stop-color="#818cf8"/>
    </linearGradient>
    <linearGradient id="step2" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#0891b2"/><stop offset="100%" stop-color="#22d3ee"/>
    </linearGradient>
    <linearGradient id="step3" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#059669"/><stop offset="100%" stop-color="#34d399"/>
    </linearGradient>
    <linearGradient id="step4" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#d97706"/><stop offset="100%" stop-color="#fbbf24"/>
    </linearGradient>
    <linearGradient id="step5" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#dc2626"/><stop offset="100%" stop-color="#f87171"/>
    </linearGradient>
    <filter id="shadow2">
      <feDropShadow dx="0" dy="2" stdDeviation="3" flood-opacity="0.1"/>
    </filter>
    <marker id="arrow" markerWidth="8" markerHeight="6" refX="8" refY="3" orient="auto">
      <polygon points="0 0, 8 3, 0 6" fill="#94a3b8"/>
    </marker>
    <marker id="arrow-green" markerWidth="8" markerHeight="6" refX="8" refY="3" orient="auto">
      <polygon points="0 0, 8 3, 0 6" fill="#059669"/>
    </marker>
  </defs>
  <rect width="1000" height="520" fill="url(#bg2)" rx="12"/>

  <text x="500" y="35" text-anchor="middle" font-size="18" font-weight="bold" fill="#1e293b">压缩管道全景图：从原始信息到可运行模型</text>

  <!-- Step 1: 输入 -->
  <rect x="40" y="70" width="140" height="90" rx="8" fill="url(#step1)" filter="url(#shadow2)"/>
  <text x="110" y="105" text-anchor="middle" fill="white" font-size="16" font-weight="bold">输入</text>
  <text x="110" y="125" text-anchor="middle" fill="#e0e7ff" font-size="9">原始现象</text>
  <text x="110" y="140" text-anchor="middle" fill="#e0e7ff" font-size="9">教材/论文</text>
  <text x="110" y="155" text-anchor="middle" fill="#e0e7ff" font-size="9">代码/项目</text>

  <!-- Arrow 1→2 -->
  <line x1="180" y1="115" x2="215" y2="115" stroke="#94a3b8" stroke-width="2" marker-end="url(#arrow)"/>

  <!-- Step 2: HLT筛选 -->
  <rect x="225" y="70" width="140" height="90" rx="8" fill="url(#step2)" filter="url(#shadow2)"/>
  <text x="295" y="100" text-anchor="middle" fill="white" font-size="14" font-weight="bold">HLT筛选</text>
  <text x="295" y="118" text-anchor="middle" fill="#cffafe" font-size="9">值不值得学？</text>
  <text x="295" y="133" text-anchor="middle" fill="#cffafe" font-size="9">H=半衰期</text>
  <text x="295" y="148" text-anchor="middle" fill="#cffafe" font-size="9">L=杠杆 | T=转移性</text>

  <!-- Arrow 2→3 -->
  <line x1="365" y1="115" x2="400" y2="115" stroke="#94a3b8" stroke-width="2" marker-end="url(#arrow)"/>

  <!-- Step 3: 差异编码 -->
  <rect x="410" y="70" width="140" height="90" rx="8" fill="url(#step3)" filter="url(#shadow2)"/>
  <text x="480" y="100" text-anchor="middle" fill="white" font-size="14" font-weight="bold">差异映射</text>
  <text x="480" y="118" text-anchor="middle" fill="#d1fae5" font-size="9">基线建立</text>
  <text x="480" y="133" text-anchor="middle" fill="#d1fae5" font-size="9">Delta编码</text>
  <text x="480" y="148" text-anchor="middle" fill="#d1fae5" font-size="9">只存差异</text>

  <!-- Arrow 3→4 -->
  <line x1="550" y1="115" x2="585" y2="115" stroke="#94a3b8" stroke-width="2" marker-end="url(#arrow)"/>

  <!-- Step 4: 精通五层质检 -->
  <rect x="595" y="50" width="160" height="130" rx="8" fill="url(#step4)" filter="url(#shadow2)"/>
  <text x="675" y="78" text-anchor="middle" fill="white" font-size="14" font-weight="bold">精通五层</text>
  <text x="675" y="98" text-anchor="middle" fill="#fef3c7" font-size="9">质检流水线</text>
  <text x="675" y="118" text-anchor="middle" fill="#fef3c7" font-size="9">L1跑通 → L2拆解</text>
  <text x="675" y="133" text-anchor="middle" fill="#fef3c7" font-size="9">L3调参 → L4边界</text>
  <text x="675" y="148" text-anchor="middle" fill="#fef3c7" font-size="9">L5封装</text>

  <!-- Arrow 4→5 -->
  <line x1="755" y1="115" x2="790" y2="115" stroke="#94a3b8" stroke-width="2" marker-end="url(#arrow)"/>

  <!-- Step 5: 输出 -->
  <rect x="800" y="70" width="160" height="90" rx="8" fill="url(#step5)" filter="url(#shadow2)"/>
  <text x="880" y="105" text-anchor="middle" fill="white" font-size="16" font-weight="bold">可运行模型</text>
  <text x="880" y="125" text-anchor="middle" fill="#fecaca" font-size="9">能预测 / 能判断</text>
  <text x="880" y="140" text-anchor="middle" fill="#fecaca" font-size="9">能改参数</text>
  <text x="880" y="155" text-anchor="middle" fill="#fecaca" font-size="9">能教别人</text>

  <!-- Feedback loop -->
  <path d="M 880 160 L 880 200 L 480 200 L 480 160" fill="none" stroke="#059669" stroke-width="1.5" stroke-dasharray="5,3" marker-end="url(#arrow-green)"/>
  <text x="680" y="195" text-anchor="middle" fill="#059669" font-size="10">反馈循环：质检不合格 → 重新压缩</text>

  <!-- ===== 质检标准 ===== -->
  <rect x="40" y="210" width="920" height="1" fill="#e2e8f0"/>
  <text x="500" y="240" text-anchor="middle" font-size="14" font-weight="bold" fill="#1e293b">精通五层质检标准</text>

  <!-- L1-L5 boxes -->
  <rect x="40" y="260" width="160" height="80" rx="6" fill="#f8fafc" stroke="#94a3b8" stroke-width="1"/>
  <text x="120" y="285" text-anchor="middle" font-size="13" font-weight="bold" fill="#6366f1">L1 跑通</text>
  <text x="120" y="303" text-anchor="middle" fill="#64748b" font-size="9">能运行/复述</text>
  <text x="120" y="318" text-anchor="middle" fill="#64748b" font-size="9">照做不出错</text>

  <rect x="220" y="260" width="160" height="80" rx="6" fill="#f8fafc" stroke="#94a3b8" stroke-width="1"/>
  <text x="300" y="285" text-anchor="middle" font-size="13" font-weight="bold" fill="#0891b2">L2 拆解</text>
  <text x="300" y="303" text-anchor="middle" fill="#64748b" font-size="9">能分解结构</text>
  <text x="300" y="318" text-anchor="middle" fill="#64748b" font-size="9">能解释为什么</text>

  <rect x="400" y="260" width="160" height="80" rx="6" fill="#f8fafc" stroke="#94a3b8" stroke-width="1"/>
  <text x="480" y="285" text-anchor="middle" font-size="13" font-weight="bold" fill="#059669">L3 调参</text>
  <text x="480" y="303" text-anchor="middle" fill="#64748b" font-size="9">能改参数预测</text>
  <text x="480" y="318" text-anchor="middle" fill="#64748b" font-size="9">因果模型建立</text>

  <rect x="580" y="260" width="160" height="80" rx="6" fill="#f8fafc" stroke="#94a3b8" stroke-width="1"/>
  <text x="660" y="285" text-anchor="middle" font-size="13" font-weight="bold" fill="#d97706">L4 边界</text>
  <text x="660" y="303" text-anchor="middle" fill="#64748b" font-size="9">知道失效场景</text>
  <text x="660" y="318" text-anchor="middle" fill="#64748b" font-size="9">知道局限</text>

  <rect x="760" y="260" width="160" height="80" rx="6" fill="#f8fafc" stroke="#94a3b8" stroke-width="1"/>
  <text x="840" y="285" text-anchor="middle" font-size="13" font-weight="bold" fill="#dc2626">L5 封装</text>
  <text x="840" y="303" text-anchor="middle" fill="#64748b" font-size="9">能教别人</text>
  <text x="840" y="318" text-anchor="middle" fill="#64748b" font-size="9">能迁移复用</text>

  <!-- Arrow progression between levels -->
  <text x="200" y="300" text-anchor="middle" fill="#94a3b8" font-size="12">→</text>
  <text x="380" y="300" text-anchor="middle" fill="#94a3b8" font-size="12">→</text>
  <text x="560" y="300" text-anchor="middle" fill="#94a3b8" font-size="12">→</text>
  <text x="740" y="300" text-anchor="middle" fill="#94a3b8" font-size="12">→</text>

  <!-- Quality check -->
  <rect x="40" y="360" width="920" height="1" fill="#e2e8f0"/>

  <text x="500" y="385" text-anchor="middle" font-size="13" font-weight="bold" fill="#1e293b">辅助系统</text>

  <rect x="60" y="400" width="200" height="65" rx="6" fill="#eef2ff" stroke="#6366f1" stroke-width="1"/>
  <text x="160" y="425" text-anchor="middle" font-size="12" font-weight="bold" fill="#6366f1">记忆固化</text>
  <text x="160" y="445" text-anchor="middle" fill="#4338ca" font-size="10">Anki 间隔重复</text>

  <rect x="290" y="400" width="200" height="65" rx="6" fill="#ecfeff" stroke="#0891b2" stroke-width="1"/>
  <text x="390" y="425" text-anchor="middle" font-size="12" font-weight="bold" fill="#0891b2">知识组织</text>
  <text x="390" y="445" text-anchor="middle" fill="#0e7490" font-size="10">Zettelkasten / 导图</text>

  <rect x="520" y="400" width="200" height="65" rx="6" fill="#ecfdf5" stroke="#059669" stroke-width="1"/>
  <text x="620" y="425" text-anchor="middle" font-size="12" font-weight="bold" fill="#059669">AI代理</text>
  <text x="620" y="445" text-anchor="middle" fill="#047857" font-size="10">Codex / Claude / Copilot</text>

  <rect x="750" y="400" width="200" height="65" rx="6" fill="#fffbeb" stroke="#d97706" stroke-width="1"/>
  <text x="850" y="425" text-anchor="middle" font-size="12" font-weight="bold" fill="#d97706">日志复盘</text>
  <text x="850" y="445" text-anchor="middle" fill="#b45309" font-size="10">差异日志 / 预测记录</text>

  <text x="500" y="510" text-anchor="middle" fill="#94a3b8" font-size="9">《学透》| 压缩即理解 | 学习不是记忆，是压缩</text>
</svg>'''

with open(f"{OUT}/F02-compression-pipeline.svg", "w") as f:
    f.write(f02)
print(f"✅ F02: 压缩管道图 ({len(f02)} chars)")

# ===========================
# F-03: 坐标图
# ===========================
f03 = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 700 650" font-family="'Noto Sans SC', 'Microsoft YaHei', sans-serif">
  <rect width="700" height="650" fill="#f8fafc" rx="12"/>
  <text x="350" y="35" text-anchor="middle" font-size="18" font-weight="bold" fill="#1e293b">经典学习法压缩论坐标图</text>

  <!-- Axes -->
  <line x1="80" y1="570" x2="660" y2="570" stroke="#475569" stroke-width="2"/>
  <line x1="80" y1="80" x2="80" y2="570" stroke="#475569" stroke-width="2"/>

  <!-- X axis label -->
  <text x="370" y="605" text-anchor="middle" font-size="14" fill="#64748b">操作复杂度 →</text>
  <text x="370" y="625" text-anchor="middle" font-size="11" fill="#94a3b8">(简单操作 → 深度操作)</text>
  <text x="120" y="585" fill="#94a3b8" font-size="9">简单</text>
  <text x="620" y="585" fill="#94a3b8" font-size="9">复杂</text>

  <!-- Y axis label -->
  <!-- Rotated text not well supported in basic SVG, using simple positioning -->
  <text x="20" y="340" text-anchor="middle" font-size="14" fill="#64748b" transform="rotate(-90, 20, 340)">压缩深度</text>

  <text x="50" y="120" fill="#94a3b8" font-size="9">深层</text>
  <text x="50" y="560" fill="#94a3b8" font-size="9">表层</text>

  <!-- Grid lines (horizontal) -->
  <line x1="80" y1="200" x2="660" y2="200" stroke="#e2e8f0" stroke-width="0.5"/>
  <line x1="80" y1="320" x2="660" y2="320" stroke="#e2e8f0" stroke-width="0.5"/>
  <line x1="80" y1="440" x2="660" y2="440" stroke="#e2e8f0" stroke-width="0.5"/>

  <!-- Methods positioned manually -->
  <!-- Bottom left: simple, shallow -->
  <circle cx="160" cy="500" r="18" fill="#e0e7ff" stroke="#6366f1" stroke-width="1.5"/>
  <text x="160" y="505" text-anchor="middle" fill="#4338ca" font-size="7">Anki</text>

  <circle cx="140" cy="450" r="16" fill="#e0e7ff" stroke="#6366f1" stroke-width="1.5"/>
  <text x="140" y="455" text-anchor="middle" fill="#4338ca" font-size="6">笔记</text>

  <circle cx="220" cy="460" r="16" fill="#e0e7ff" stroke="#6366f1" stroke-width="1.5"/>
  <text x="220" y="465" text-anchor="middle" fill="#4338ca" font-size="6">SQ3R</text>

  <!-- Mid-left -->
  <circle cx="280" cy="380" r="18" fill="#fed7aa" stroke="#f97316" stroke-width="1.5"/>
  <text x="280" y="385" text-anchor="middle" fill="#9a3412" font-size="7">导图</text>

  <circle cx="330" cy="340" r="18" fill="#a7f3d0" stroke="#059669" stroke-width="1.5"/>
  <text x="330" y="345" text-anchor="middle" fill="#065f46" font-size="6">Kolb</text>

  <!-- Center -->
  <circle cx="400" cy="280" r="20" fill="#fecaca" stroke="#ef4444" stroke-width="1.5"/>
  <text x="400" y="285" text-anchor="middle" fill="#991b1b" font-size="7">Zettel</text>

  <circle cx="350" cy="250" r="18" fill="#bfdbfe" stroke="#3b82f6" stroke-width="1.5"/>
  <text x="350" y="255" text-anchor="middle" fill="#1e40af" font-size="7">Bloom</text>

  <!-- Mid-right: complex, deeper -->
  <circle cx="470" cy="210" r="20" fill="#fef3c7" stroke="#d97706" stroke-width="1.5"/>
  <text x="470" y="215" text-anchor="middle" fill="#92400e" font-size="7">刻意</text>
  <text x="470" y="228" text-anchor="middle" fill="#92400e" font-size="6">练习</text>

  <!-- Top right: most complex, deepest -->
  <circle cx="530" cy="150" r="22" fill="#e9d5ff" stroke="#8b5cf6" stroke-width="2"/>
  <text x="530" y="155" text-anchor="middle" fill="#5b21b6" font-size="7">精通</text>
  <text x="530" y="168" text-anchor="middle" fill="#5b21b6" font-size="7">五层</text>

  <circle cx="580" cy="180" r="20" fill="#e9d5ff" stroke="#8b5cf6" stroke-width="1.5"/>
  <text x="580" y="185" text-anchor="middle" fill="#5b21b6" font-size="7">差异</text>
  <text x="580" y="198" text-anchor="middle" fill="#5b21b6" font-size="6">驱动</text>

  <circle cx="490" cy="140" r="18" fill="#e9d5ff" stroke="#8b5cf6" stroke-width="1.5"/>
  <text x="490" y="145" text-anchor="middle" fill="#5b21b6" font-size="7">HLT</text>

  <circle cx="430" cy="160" r="18" fill="#e9d5ff" stroke="#8b5cf6" stroke-width="1.5"/>
  <text x="430" y="165" text-anchor="middle" fill="#5b21b6" font-size="7">Agent</text>

  <!-- Dreyfus -> special: wide vertical -->
  <ellipse cx="250" cy="240" rx="35" ry="60" fill="none" stroke="#94a3b8" stroke-width="1" stroke-dasharray="4,3"/>
  <text x="250" y="230" text-anchor="middle" fill="#64748b" font-size="7">Dreyfus</text>
  <text x="250" y="260" text-anchor="middle" fill="#64748b" font-size="6">新手→专家</text>

  <!-- Legend -->
  <rect x="40" y="610" width="620" height="30" rx="6" fill="#f1f5f9"/>
  <circle cx="80" cy="625" r="6" fill="#e0e7ff" stroke="#6366f1" stroke-width="1"/>
  <text x="92" y="629" fill="#475569" font-size="9">记忆/笔记类</text>
  <circle cx="220" cy="625" r="6" fill="#fed7aa" stroke="#f97316" stroke-width="1"/>
  <text x="232" y="629" fill="#475569" font-size="9">组织类</text>
  <circle cx="340" cy="625" r="6" fill="#e9d5ff" stroke="#8b5cf6" stroke-width="1"/>
  <text x="352" y="629" fill="#475569" font-size="9">元框架（本书独创）</text>
  <circle cx="530" cy="625" r="6" fill="#fecaca" stroke="#ef4444" stroke-width="1"/>
  <text x="542" y="629" fill="#475569" font-size="9">高级构建类</text>
</svg>'''

with open(f"{OUT}/F03-method-coordinates.svg", "w") as f:
    f.write(f03)
print(f"✅ F03: 学习法坐标图 ({len(f03)} chars)")

# ===========================
# F-04: 理解三层模型
# ===========================
f04 = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 350" font-family="'Noto Sans SC', 'Microsoft YaHei', sans-serif">
  <defs>
    <linearGradient id="l1g" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0%" stop-color="#f1f5f9"/><stop offset="100%" stop-color="#e2e8f0"/>
    </linearGradient>
    <linearGradient id="l2g" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0%" stop-color="#e0e7ff"/><stop offset="100%" stop-color="#c7d2fe"/>
    </linearGradient>
    <linearGradient id="l3g" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0%" stop-color="#d1fae5"/><stop offset="100%" stop-color="#a7f3d0"/>
    </linearGradient>
  </defs>
  <rect width="800" height="350" fill="#f8fafc" rx="12"/>
  <text x="400" y="35" text-anchor="middle" font-size="18" font-weight="bold" fill="#1e293b">理解的三层模型</text>

  <!-- L1 -->
  <rect x="60" y="70" width="680" height="65" rx="8" fill="url(#l1g)" stroke="#cbd5e1" stroke-width="1.5"/>
  <rect x="60" y="70" width="110" height="65" rx="8" fill="#94a3b8"/>
  <text x="115" y="105" text-anchor="middle" fill="white" font-size="16" font-weight="bold">L1</text>
  <text x="115" y="123" text-anchor="middle" fill="#f1f5f9" font-size="9">能复述</text>
  <text x="200" y="98" fill="#475569" font-size="13">✅</text>
  <text x="220" y="98" fill="#1e293b" font-size="13" font-weight="bold">存档模式</text>
  <text x="220" y="118" fill="#64748b" font-size="11">能复述内容，能照做不出错。但没有改变认知结构。</text>
  <text x="590" y="105" text-anchor="end" fill="#94a3b8" font-size="10">类比：zip文件</text>

  <!-- Arrow L1→L2 -->
  <polygon points="400,135 392,145 408,145" fill="#6366f1"/>
  <line x1="400" y1="135" x2="400" y2="145" stroke="#6366f1" stroke-width="2"/>

  <!-- L2 -->
  <rect x="60" y="150" width="680" height="65" rx="8" fill="url(#l2g)" stroke="#818cf8" stroke-width="1.5"/>
  <rect x="60" y="150" width="110" height="65" rx="8" fill="#6366f1"/>
  <text x="115" y="185" text-anchor="middle" fill="white" font-size="16" font-weight="bold">L2</text>
  <text x="115" y="203" text-anchor="middle" fill="#e0e7ff" font-size="9">能解释</text>
  <text x="200" y="178" fill="#6366f1" font-size="13">✅✅</text>
  <text x="220" y="178" fill="#1e293b" font-size="13" font-weight="bold">有损压缩模式</text>
  <text x="220" y="198" fill="#475569" font-size="11">能用自己话解释、能举例、能比喻。但面对变化参数可能卡住。</text>
  <text x="590" y="185" text-anchor="end" fill="#818cf8" font-size="10">类比：MP3 文件</text>

  <!-- Arrow L2→L3 -->
  <polygon points="400,215 392,225 408,225" fill="#059669"/>
  <line x1="400" y1="215" x2="400" y2="225" stroke="#059669" stroke-width="2"/>

  <!-- L3 -->
  <rect x="60" y="230" width="680" height="65" rx="8" fill="url(#l3g)" stroke="#059669" stroke-width="1.5"/>
  <rect x="60" y="230" width="110" height="65" rx="8" fill="#059669"/>
  <text x="115" y="265" text-anchor="middle" fill="white" font-size="16" font-weight="bold">L3</text>
  <text x="115" y="283" text-anchor="middle" fill="#d1fae5" font-size="9">能预测</text>
  <text x="200" y="258" fill="#059669" font-size="13">✅✅✅</text>
  <text x="220" y="258" fill="#1e293b" font-size="13" font-weight="bold">可运行模型模式</text>
  <text x="220" y="278" fill="#475569" font-size="11">改一个参数，能预测结果。换个问题域，能迁移使用。</text>
  <text x="590" y="265" text-anchor="end" fill="#059669" font-size="10">类比：可执行文件</text>

  <text x="400" y="338" text-anchor="middle" fill="#94a3b8" font-size="10">核心检验方式：改一个参数，你能准确预测结果吗？</text>
</svg>'''

with open(f"{OUT}/F04-understanding-three-levels.svg", "w") as f:
    f.write(f04)
print(f"✅ F04: 理解三层模型 ({len(f04)} chars)")

print(f"\n全部生成完毕！输出目录: {OUT}")
print("共 4 个 SVG 文件")
