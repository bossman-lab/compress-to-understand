#!/usr/bin/env python3
"""Generate child-friendly SVG illustrations for the children's version of 学透"""
import os

OUT = "/root/Projects/compress-to-understand/children-version/illustrations"
os.makedirs(OUT, exist_ok=True)

# 序幕：骑自行车
prologue = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 600 350" font-family="'Noto Sans SC', sans-serif">
  <rect width="600" height="350" fill="#fefce8" rx="16"/>
  <text x="300" y="35" text-anchor="middle" font-size="18" font-weight="bold" fill="#854d0e">小明和小花的比赛</text>
  <!-- Left bike -->
  <g transform="translate(120,200)">
    <circle cx="0" cy="0" r="30" fill="#e2e8f0" stroke="#64748b" stroke-width="2"/>
    <circle cx="60" cy="0" r="30" fill="#e2e8f0" stroke="#64748b" stroke-width="2"/>
    <line x1="0" y1="0" x2="30" y2="-50" stroke="#64748b" stroke-width="3"/>
    <line x1="60" y1="0" x2="30" y2="-50" stroke="#64748b" stroke-width="3"/>
    <line x1="30" y1="-50" x2="0" y2="-90" stroke="#64748b" stroke-width="3"/>
    <line x1="30" y1="-50" x2="60" y2="-90" stroke="#64748b" stroke-width="3"/>
    <line x1="0" y1="-90" x2="60" y2="-90" stroke="#64748b" stroke-width="3"/>
    <circle cx="30" cy="-50" r="8" fill="#e2e8f0" stroke="#64748b" stroke-width="2"/>
  </g>
  <!-- Xiao Ming head -->
  <circle cx="150" cy="130" r="20" fill="#fcd34d"/>
  <circle cx="145" cy="126" r="2" fill="#1e293b"/>
  <circle cx="155" cy="126" r="2" fill="#1e293b"/>
  <path d="M145 136 Q150 142 155 136" fill="#a21caf" stroke="#a21caf" stroke-width="1"/>
  <!-- Book -->
  <rect x="130" y="145" width="40" height="28" rx="3" fill="#fef3c7" stroke="#d97706" stroke-width="1"/>
  <text x="150" y="162" text-anchor="middle" font-size="6" fill="#d97706">说明书</text>
  <line x1="130" y1="150" x2="170" y2="150" stroke="#d97706" stroke-width="0.5"/>
  <line x1="130" y1="155" x2="170" y2="155" stroke="#d97706" stroke-width="0.5"/>
  <line x1="130" y1="160" x2="170" y2="160" stroke="#d97706" stroke-width="0.5"/>
  <line x1="130" y1="165" x2="170" y2="165" stroke="#d97706" stroke-width="0.5"/>
  <text x="150" y="145" text-anchor="middle" font-size="9" fill="#1e293b">小明</text>
  <!-- Right bike (moving) -->
  <g transform="translate(380,200)">
    <circle cx="0" cy="0" r="30" fill="#bfdbfe" stroke="#3b82f6" stroke-width="2"/>
    <circle cx="60" cy="0" r="30" fill="#bfdbfe" stroke="#3b82f6" stroke-width="2"/>
    <line x1="0" y1="0" x2="30" y2="-50" stroke="#3b82f6" stroke-width="3"/>
    <line x1="60" y1="0" x2="30" y2="-50" stroke="#3b82f6" stroke-width="3"/>
    <line x1="30" y1="-50" x2="10" y2="-85" stroke="#3b82f6" stroke-width="3"/>
    <line x1="30" y1="-50" x2="55" y2="-85" stroke="#3b82f6" stroke-width="3"/>
    <line x1="10" y1="-85" x2="55" y2="-85" stroke="#3b82f6" stroke-width="3"/>
    <circle cx="30" cy="-50" r="8" fill="#bfdbfe" stroke="#3b82f6" stroke-width="2"/>
  </g>
  <circle cx="410" cy="130" r="20" fill="#fde047"/>
  <circle cx="405" cy="126" r="2" fill="#1e293b"/>
  <circle cx="415" cy="126" r="2" fill="#1e293b"/>
  <path d="M405 136 Q410 140 415 136" fill="#e11d48" stroke="#e11d48" stroke-width="1"/>
  <text x="410" y="145" text-anchor="middle" font-size="9" fill="#1e293b">小花</text>
  <!-- Speed lines -->
  <line x1="350" y1="195" x2="320" y2="195" stroke="#3b82f6" stroke-width="1"/>
  <line x1="355" y1="205" x2="310" y2="205" stroke="#3b82f6" stroke-width="1"/>
  <line x1="350" y1="215" x2="325" y2="215" stroke="#3b82f6" stroke-width="1"/>
  <!-- Finish line -->
  <line x1="520" y1="140" x2="520" y2="250" stroke="#dc2626" stroke-width="3" stroke-dasharray="8,4"/>
  <text x="540" y="160" fill="#dc2626" font-size="10">终点</text>
  <text x="300" y="320" text-anchor="middle" font-size="12" fill="#854d0e">小明背说明书，小花直接骑——结果呢？</text>
</svg>'''

with open(f"{OUT}/00-prologue.svg", "w") as f:
    f.write(prologue)
print(f"✅ 序幕: 骑自行车 ({len(prologue)} chars)")

# 第1章：大脑里的模型
ch01 = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 600 300" font-family="'Noto Sans SC', sans-serif">
  <rect width="600" height="300" fill="#f0f9ff" rx="16"/>
  <text x="300" y="35" text-anchor="middle" font-size="18" font-weight="bold" fill="#0369a1">学东西不是背，是会变！</text>
  <!-- Left: 死记硬背 -->
  <rect x="30" y="70" width="250" height="200" rx="12" fill="#fef2f2" stroke="#dc2626" stroke-width="2"/>
  <text x="155" y="100" text-anchor="middle" font-size="14" font-weight="bold" fill="#dc2626">死记硬背</text>
  <rect x="50" y="115" width="90" height="130" rx="6" fill="#fecaca" stroke="#dc2626" stroke-width="1"/>
  <text x="95" y="135" text-anchor="middle" font-size="10" fill="#7f1d1d">背诵内容</text>
  <text x="95" y="155" text-anchor="middle" font-size="9" fill="#7f1d1d">踏板在车架两侧</text>
  <text x="95" y="170" text-anchor="middle" font-size="9" fill="#7f1d1d">刹车在右边</text>
  <text x="95" y="185" text-anchor="middle" font-size="9" fill="#7f1d1d">坐垫高度...</text>
  <text x="95" y="220" text-anchor="middle" font-size="10" fill="#dc2626">💀 换个车就不会</text>
  <!-- Right: 会变的模型 -->
  <rect x="320" y="70" width="250" height="200" rx="12" fill="#ecfdf5" stroke="#059669" stroke-width="2"/>
  <text x="445" y="100" text-anchor="middle" font-size="14" font-weight="bold" fill="#059669">会变的模型</text>
  <circle cx="445" cy="150" r="40" fill="#d1fae5" stroke="#059669" stroke-width="2"/>
  <text x="445" y="145" text-anchor="middle" font-size="11" fill="#065f46">平衡</text>
  <text x="445" y="162" text-anchor="middle" font-size="11" fill="#065f46">+ 转向</text>
  <text x="445" y="179" text-anchor="middle" font-size="11" fill="#065f46">+ 刹车</text>
  <text x="445" y="230" text-anchor="middle" font-size="10" fill="#059669">🎉 换一辆车也会骑</text>
  <!-- Arrow -->
  <text x="295" y="170" text-anchor="middle" font-size="24" fill="#94a3b8">→</text>
  <text x="300" y="285" text-anchor="middle" font-size="12" font-weight="bold" fill="#0369a1">记住答案 ≠ 学会。会变 = 学会！</text>
</svg>'''

with open(f"{OUT}/01-not-memorize-transform.svg", "w") as f:
    f.write(ch01)
print(f"✅ ch01: 不是背是会变 ({len(ch01)} chars)")

# 第2章：三根手指
ch02 = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 600 400" font-family="'Noto Sans SC', sans-serif">
  <rect width="600" height="400" fill="#faf5ff" rx="16"/>
  <text x="300" y="35" text-anchor="middle" font-size="18" font-weight="bold" fill="#6b21a8">学前三问</text>
  <!-- Hand -->
  <g transform="translate(100,60)">
    <ellipse cx="200" cy="200" rx="80" ry="100" fill="#fcd34d"/>
    <!-- 5 fingers spread -->
    <rect x="185" y="30" width="30" height="120" rx="15" fill="#fcd34d" stroke="#d97706" stroke-width="2"/>
    <rect x="150" y="50" width="28" height="110" rx="14" fill="#fde047" stroke="#d97706" stroke-width="2"/>
    <rect x="220" y="50" width="28" height="110" rx="14" fill="#fde047" stroke="#d97706" stroke-width="2"/>
    <rect x="125" y="80" width="25" height="90" rx="12" fill="#fef9c3" stroke="#d97706" stroke-width="2"/>
    <rect x="245" y="80" width="25" height="90" rx="12" fill="#fef9c3" stroke="#d97706" stroke-width="2"/>
  </g>
  <!-- Thumb question -->
  <rect x="110" y="80" width="120" height="50" rx="8" fill="#fef3c7" stroke="#d97706" stroke-width="1.5"/>
  <text x="170" y="100" text-anchor="middle" font-size="9" font-weight="bold" fill="#854d0e">大拇指 👍</text>
  <text x="170" y="118" text-anchor="middle" font-size="8" fill="#854d0e">以后还用得上吗？</text>
  <!-- Index question -->
  <rect x="360" y="70" width="120" height="50" rx="8" fill="#dbeafe" stroke="#2563eb" stroke-width="1.5"/>
  <text x="420" y="90" text-anchor="middle" font-size="9" font-weight="bold" fill="#1e40af">食指 👆</text>
  <text x="420" y="108" text-anchor="middle" font-size="8" fill="#1e40af">我能做什么？</text>
  <!-- Palm question -->
  <rect x="350" y="200" width="130" height="50" rx="8" fill="#dcfce7" stroke="#16a34a" stroke-width="1.5"/>
  <text x="415" y="220" text-anchor="middle" font-size="9" font-weight="bold" fill="#166534">手掌 🖐️</text>
  <text x="415" y="238" text-anchor="middle" font-size="8" fill="#166534">还能用在哪？</text>
  <text x="300" y="370" text-anchor="middle" font-size="12" font-weight="bold" fill="#6b21a8">学前三问：学啥？为啥？还能用在哪？</text>
</svg>'''

with open(f"{OUT}/02-three-questions.svg", "w") as f:
    f.write(ch02)
print(f"✅ ch02: 学前三问 ({len(ch02)} chars)")

# 第3章：分蛋糕
ch03 = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 600 320" font-family="'Noto Sans SC', sans-serif">
  <rect width="600" height="320" fill="#fff7ed" rx="16"/>
  <text x="300" y="35" text-anchor="middle" font-size="18" font-weight="bold" fill="#c2410c">你早就会了一半！</text>
  <!-- Cake -->
  <ellipse cx="200" cy="170" rx="80" ry="30" fill="#fb923c"/>
  <rect x="120" y="120" width="160" height="50" rx="5" fill="#fdba74"/>
  <ellipse cx="200" cy="120" rx="80" ry="20" fill="#fed7aa"/>
  <!-- Candle -->
  <rect x="195" y="90" width="10" height="30" fill="#f87171"/>
  <circle cx="200" cy="88" r="5" fill="#fbbf24"/>
  <!-- Cake division lines -->
  <line x1="200" y1="120" x2="160" y2="170" stroke="#c2410c" stroke-width="2" stroke-dasharray="4,3"/>
  <line x1="200" y1="120" x2="240" y2="170" stroke="#c2410c" stroke-width="2" stroke-dasharray="4,3"/>
  <text x="175" y="168" text-anchor="middle" font-size="10" fill="#c2410c">¼</text>
  <text x="225" y="168" text-anchor="middle" font-size="10" fill="#c2410c">¼</text>
  <text x="200" y="168" text-anchor="middle" font-size="10" fill="#c2410c">½</text>
  <!-- Arrow -->
  <text x="300" y="160" text-anchor="middle" font-size="24" fill="#94a3b8">→</text>
  <!-- Fraction on paper -->
  <rect x="340" y="100" width="150" height="100" rx="8" fill="white" stroke="#c2410c" stroke-width="2"/>
  <text x="415" y="135" text-anchor="middle" font-size="24" fill="#c2410c">1/4</text>
  <text x="415" y="165" text-anchor="middle" font-size="10" fill="#9a3412">"分蛋糕嘛，</text>
  <text x="415" y="180" text-anchor="middle" font-size="10" fill="#9a3412">我早就会了！"</text>
  <text x="300" y="290" text-anchor="middle" font-size="12" font-weight="bold" fill="#c2410c">每个新东西，你都早就会了一半！</text>
</svg>'''

with open(f"{OUT}/03-already-know-half.svg", "w") as f:
    f.write(ch03)
print(f"✅ ch03: 早就会了一半 ({len(ch03)} chars)")

# Five animals combined SVG
animals = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 600 480" font-family="'Noto Sans SC', sans-serif">
  <rect width="600" height="480" fill="#f8fafc" rx="16"/>
  <text x="300" y="35" text-anchor="middle" font-size="18" font-weight="bold" fill="#1e293b">五层通关法</text>
  
  <!-- L1 Monkey -->
  <rect x="20" y="60" width="260" height="70" rx="10" fill="#ecfdf5" stroke="#059669" stroke-width="2"/>
  <circle cx="58" cy="95" r="25" fill="#fb923c"/>
  <circle cx="48" cy="90" r="4" fill="#1e293b"/>
  <circle cx="68" cy="90" r="4" fill="#1e293b"/>
  <path d="M52 100 Q58 108 64 100" stroke="#1e293b" stroke-width="2" fill="none"/>
  <ellipse cx="73" cy="82" rx="10" ry="6" fill="#fdba74"/>
  <text x="60" y="62" text-anchor="middle" font-size="12" font-weight="bold" fill="#059669">第一关 🐒 跟屁虫</text>
  <text x="120" y="95" fill="#065f46" font-size="10">照着做，不犯错</text>
  <text x="120" y="115" fill="#047857" font-size="9">跟着老师做一遍</text>

  <!-- L2 Owl -->
  <rect x="320" y="60" width="260" height="70" rx="10" fill="#fefce8" stroke="#ca8a04" stroke-width="2"/>
  <circle cx="358" cy="95" r="25" fill="#a78bfa"/>
  <circle cx="348" cy="90" r="5" fill="white"/>
  <circle cx="348" cy="90" r="3" fill="#1e293b"/>
  <circle cx="368" cy="90" r="5" fill="white"/>
  <circle cx="368" cy="90" r="3" fill="#1e293b"/>
  <polygon points="358,75 348,82 368,82" fill="#f59e0b"/>
  <text x="360" y="62" text-anchor="middle" font-size="12" font-weight="bold" fill="#ca8a04">第二关 🦉 小侦探</text>
  <text x="420" y="95" fill="#854d0e" font-size="10">拆开看，找零件</text>
  <text x="420" y="115" fill="#a16207" font-size="9">把它分成几个部分</text>

  <!-- L3 Cat -->
  <rect x="20" y="150" width="260" height="70" rx="10" fill="#f0f9ff" stroke="#0284c7" stroke-width="2"/>
  <circle cx="58" cy="185" r="25" fill="#fcd34d"/>
  <polygon points="42,168 48,180 36,180" fill="#fcd34d"/>
  <polygon points="74,168 68,180 80,180" fill="#fcd34d"/>
  <circle cx="48" cy="182" r="3" fill="#1e293b"/>
  <circle cx="68" cy="182" r="3" fill="#1e293b"/>
  <ellipse cx="58" cy="192" rx="6" ry="3" fill="#f472b6"/>
  <text x="60" y="152" text-anchor="middle" font-size="12" font-weight="bold" fill="#0284c7">第三关 🐱 小玩家</text>
  <text x="120" y="185" fill="#0f766e" font-size="10">改一改，猜一猜</text>
  <text x="120" y="205" fill="#0f766e" font-size="9">改个条件，先说结果再验证</text>

  <!-- L4 Wolf -->
  <rect x="320" y="150" width="260" height="70" rx="10" fill="#fef2f2" stroke="#dc2626" stroke-width="2"/>
  <circle cx="358" cy="185" r="25" fill="#94a3b8"/>
  <ellipse cx="348" cy="178" rx="6" ry="4" fill="#e2e8f0"/>
  <ellipse cx="368" cy="178" rx="6" ry="4" fill="#e2e8f0"/>
  <circle cx="348" cy="178" r="2" fill="#dc2626"/>
  <circle cx="368" cy="178" r="2" fill="#dc2626"/>
  <ellipse cx="358" cy="192" rx="8" ry="5" fill="#dc2626"/>
  <polygon points="350,192 345,200 355,195" fill="white"/>
  <polygon points="366,192 375,200 362,195" fill="white"/>
  <text x="360" y="152" text-anchor="middle" font-size="12" font-weight="bold" fill="#dc2626">第四关 🐺 破坏王</text>
  <text x="420" y="185" fill="#991b1b" font-size="10">故意搞坏它</text>
  <text x="420" y="205" fill="#991b1b" font-size="9">知道什么时候会失败</text>

  <!-- L5 Dolphin -->
  <rect x="170" y="240" width="260" height="70" rx="10" fill="#ecfeff" stroke="#0891b2" stroke-width="2"/>
  <path d="M270 275 Q300 245 340 275 Q300 310 270 275" fill="#06b6d4"/>
  <circle cx="275" cy="270" r="3" fill="#1e293b"/>
  <path d="M270 275 L260 268" stroke="#06b6d4" stroke-width="3"/>
  <text x="300" y="247" text-anchor="middle" font-size="12" font-weight="bold" fill="#0891b2">第五关 🐬 小老师</text>
  <text x="350" y="275" fill="#155e75" font-size="10">讲给别人听</text>
  <text x="350" y="295" fill="#155e75" font-size="9">能教别人才叫真学会了</text>

  <!-- Arrow progression -->
  <text x="295" y="100" text-anchor="middle" fill="#94a3b8" font-size="16">→</text>
  <text x="295" y="190" text-anchor="middle" fill="#94a3b8" font-size="16">→</text>
  <text x="295" y="280" text-anchor="middle" fill="#94a3b8" font-size="16">→</text>
  
  <text x="300" y="355" text-anchor="middle" font-size="12" font-weight="bold" fill="#1e293b">五关全部通过 = 学透了！</text>
  
  <!-- Level badge -->
  <rect x="200" y="375" width="200" height="50" rx="25" fill="#facc15" stroke="#ca8a04" stroke-width="2"/>
  <text x="300" y="400" text-anchor="middle" font-size="14" font-weight="bold" fill="#854d0e">🏆 学透认证 🏆</text>
  <text x="300" y="420" text-anchor="middle" font-size="9" fill="#854d0e">跟 → 看 → 玩 → 破 → 教</text>

  <text x="300" y="470" text-anchor="middle" fill="#94a3b8" font-size="10">五层通关：跟 → 看 → 玩 → 破 → 教</text>
</svg>'''

with open(f"{OUT}/04-five-animals.svg", "w") as f:
    f.write(animals)
print(f"✅ ch04-08: 五层动物 ({len(animals)} chars)")

# 第9章：改改猜猜
ch09 = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 600 320" font-family="'Noto Sans SC', sans-serif">
  <rect width="600" height="320" fill="#fffbeb" rx="16"/>
  <text x="300" y="35" text-anchor="middle" font-size="18" font-weight="bold" fill="#92400e">改一改，猜得对</text>
  
  <!-- Before -->
  <rect x="30" y="60" width="250" height="200" rx="12" fill="#fef3c7" stroke="#d97706" stroke-width="2"/>
  <text x="155" y="90" text-anchor="middle" font-size="14" font-weight="bold" fill="#92400e">觉得自己学会了</text>
  <text x="155" y="130" text-anchor="middle" font-size="24" fill="#1e293b">3 + 5 = 8</text>
  <text x="155" y="160" text-anchor="middle" font-size="10" fill="#92400e">嗯，我会了。</text>
  <text x="155" y="180" text-anchor="middle" font-size="10" fill="#92400e">✓ 能背出来</text>
  <text x="155" y="200" text-anchor="middle" font-size="10" fill="#92400e">✓ 作业全对</text>
  <text x="155" y="230" text-anchor="middle" font-size="10" fill="#f59e0b">但是...</text>
  
  <!-- Arrow -->
  <text x="295" y="160" text-anchor="middle" font-size="24" fill="#94a3b8">→</text>

  <!-- After -->
  <rect x="320" y="60" width="250" height="200" rx="12" fill="#dcfce7" stroke="#16a34a" stroke-width="2"/>
  <text x="445" y="90" text-anchor="middle" font-size="14" font-weight="bold" fill="#166534">改一改，试试</text>
  <text x="445" y="125" text-anchor="middle" font-size="10" fill="#166534">把 5 改成 0：3 + 0 = ？</text>
  <text x="445" y="145" text-anchor="middle" font-size="10" fill="#166534">→ 先猜…… 3！✓</text>
  <text x="445" y="170" text-anchor="middle" font-size="10" fill="#166534">把 + 改成 -：3 - 5 = ？</text>
  <text x="445" y="190" text-anchor="middle" font-size="10" fill="#166534">→ 先猜……嗯？</text>
  <text x="445" y="215" text-anchor="middle" font-size="10" fill="#166534">把 5 改成 100：3 + 100 = ？</text>
  <text x="445" y="235" text-anchor="middle" font-size="10" fill="#166534">→ 先猜……103！✓</text>
  <text x="445" y="260" text-anchor="middle" font-size="10" font-weight="bold" fill="#059669">猜对了才是真懂了！</text>

  <text x="300" y="305" text-anchor="middle" font-size="12" font-weight="bold" fill="#92400e">改一改，猜得对——你学透了吗？</text>
</svg>'''

with open(f"{OUT}/09-change-and-guess.svg", "w") as f:
    f.write(ch09)
print(f"✅ ch09: 改改猜猜 ({len(ch09)} chars)")

# 第10章：跳房子
ch10 = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 600 400" font-family="'Noto Sans SC', sans-serif">
  <rect width="600" height="400" fill="#f0fdf4" rx="16"/>
  <text x="300" y="35" text-anchor="middle" font-size="18" font-weight="bold" fill="#166534">大冒险：学会跳房子</text>
  
  <!-- Hopscotch grid -->
  <rect x="50" y="80" width="60" height="60" rx="4" fill="#fef3c7" stroke="#d97706" stroke-width="2"/>
  <text x="80" y="115" text-anchor="middle" font-size="14" fill="#d97706">1</text>
  <rect x="50" y="150" width="60" height="60" rx="4" fill="#fef3c7" stroke="#d97706" stroke-width="2"/>
  <text x="80" y="185" text-anchor="middle" font-size="14" fill="#d97706">2</text>
  <rect x="130" y="150" width="60" height="60" rx="4" fill="#fef3c7" stroke="#d97706" stroke-width="2"/>
  <text x="160" y="185" text-anchor="middle" font-size="14" fill="#d97706">3</text>
  <rect x="50" y="220" width="60" height="60" rx="4" fill="#fef3c7" stroke="#d97706" stroke-width="2"/>
  <text x="80" y="255" text-anchor="middle" font-size="14" fill="#d97706">4</text>
  <rect x="130" y="220" width="60" height="60" rx="4" fill="#fef3c7" stroke="#d97706" stroke-width="2"/>
  <text x="160" y="255" text-anchor="middle" font-size="14" fill="#d97706">5</text>
  
  <!-- Stone -->
  <circle cx="80" cy="100" r="8" fill="#94a3b8"/>
  
  <!-- Footprints -->
  <ellipse cx="80" cy="270" rx="12" ry="6" fill="#d1fae5" stroke="#059669" stroke-width="1"/>
  <text x="60" y="295" font-size="8" fill="#059669">🦶</text>
  
  <!-- Five levels checklist -->
  <rect x="250" y="70" width="320" height="310" rx="10" fill="white" stroke="#059669" stroke-width="2"/>
  <text x="410" y="95" text-anchor="middle" font-size="13" font-weight="bold" fill="#166534">五层闯关</text>
  
  <rect x="270" y="110" width="280" height="40" rx="6" fill="#ecfdf5" stroke="#059669" stroke-width="1"/>
  <text x="410" y="130" text-anchor="middle" font-size="10" fill="#065f46">🐒 跟屁虫：看别人跳，跟着跳一次</text>
  <text x="410" y="143" text-anchor="middle" font-size="9" fill="#059669">⏺ 完成！</text>
  
  <rect x="270" y="160" width="280" height="40" rx="6" fill="#fefce8" stroke="#ca8a04" stroke-width="1"/>
  <text x="410" y="180" text-anchor="middle" font-size="10" fill="#854d0e">🦉 小侦探：分几步？</text>
  <text x="410" y="193" text-anchor="middle" font-size="9" fill="#ca8a04">⏺ 完成！</text>
  
  <rect x="270" y="210" width="280" height="40" rx="6" fill="#f0f9ff" stroke="#0284c7" stroke-width="1"/>
  <text x="410" y="230" text-anchor="middle" font-size="10" fill="#0f766e">🐱 小玩家：格子画大会怎样？</text>
  <text x="410" y="243" text-anchor="middle" font-size="9" fill="#0284c7">⏺ 完成！</text>
  
  <rect x="270" y="260" width="280" height="40" rx="6" fill="#fef2f2" stroke="#dc2626" stroke-width="1"/>
  <text x="410" y="280" text-anchor="middle" font-size="10" fill="#991b1b">🐺 破坏王：滑的时候不好玩</text>
  <text x="410" y="293" text-anchor="middle" font-size="9" fill="#dc2626">⏺ 完成！</text>
  
  <rect x="270" y="310" width="280" height="50" rx="6" fill="#ecfeff" stroke="#0891b2" stroke-width="1"/>
  <text x="410" y="330" text-anchor="middle" font-size="10" fill="#155e75">🐬 小老师：教朋友跳</text>
  <text x="410" y="348" text-anchor="middle" font-size="9" fill="#0891b2">⏺ 完成！🎉</text>
  
  <text x="300" y="385" text-anchor="middle" font-size="12" font-weight="bold" fill="#166534">五关通过 = 学透了！什么都能这样学！</text>
</svg>'''

with open(f"{OUT}/10-hopscotch-adventure.svg", "w") as f:
    f.write(ch10)
print(f"✅ ch10: 跳房子 ({len(ch10)} chars)")

# 尾声：地球
epilogue = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 600 350" font-family="'Noto Sans SC', sans-serif">
  <rect width="600" height="350" fill="#0f172a" rx="16"/>
  <!-- Stars -->
  <circle cx="50" cy="40" r="2" fill="white" opacity="0.8"/>
  <circle cx="150" cy="70" r="1" fill="white" opacity="0.6"/>
  <circle cx="400" cy="30" r="2" fill="white" opacity="0.8"/>
  <circle cx="550" cy="60" r="1.5" fill="white" opacity="0.7"/>
  <circle cx="80" cy="120" r="1" fill="white" opacity="0.5"/>
  <circle cx="520" cy="100" r="2" fill="white" opacity="0.8"/>
  <circle cx="300" cy="20" r="1" fill="white" opacity="0.6"/>
  <circle cx="580" cy="150" r="1" fill="white" opacity="0.5"/>
  <circle cx="30" cy="200" r="1.5" fill="white" opacity="0.7"/>
  <!-- Earth -->
  <circle cx="300" cy="200" r="100" fill="#1e40af"/>
  <path d="M220 160 Q260 140 300 150 Q340 160 370 145 Q390 140 400 160" fill="#22c55e" opacity="0.8"/>
  <path d="M340 200 Q360 220 380 210 Q390 205 395 220" fill="#22c55e" opacity="0.8"/>
  <path d="M200 220 Q230 230 250 215 Q260 210 250 230 Q240 250 220 250 Q200 250 200 220" fill="#22c55e" opacity="0.8"/>
  <path d="M300 270 Q320 280 340 260 Q350 250 360 270" fill="#22c55e" opacity="0.7"/>
  <!-- Book floating -->
  <g transform="translate(300,190)">
    <rect x="-25" y="-15" width="50" height="35" rx="3" fill="#fbbf24" stroke="#d97706" stroke-width="1"/>
    <line x1="-20" y1="-8" x2="20" y2="-8" stroke="#d97706" stroke-width="0.5"/>
    <line x1="-20" y1="-2" x2="20" y2="-2" stroke="#d97706" stroke-width="0.5"/>
    <line x1="-20" y1="4" x2="20" y2="4" stroke="#d97706" stroke-width="0.5"/>
    <text x="0" y="12" text-anchor="middle" font-size="6" fill="#92400e">学透</text>
  </g>
  <!-- Light rays -->
  <line x1="300" y1="100" x2="200" y2="40" stroke="#fbbf24" stroke-width="1" opacity="0.3"/>
  <line x1="300" y1="100" x2="400" y2="40" stroke="#fbbf24" stroke-width="1" opacity="0.3"/>
  <line x1="300" y1="100" x2="100" y2="80" stroke="#fbbf24" stroke-width="1" opacity="0.2"/>
  <line x1="300" y1="100" x2="500" y2="80" stroke="#fbbf24" stroke-width="1" opacity="0.2"/>
  <line x1="300" y1="100" x2="150" y2="140" stroke="#fbbf24" stroke-width="1" opacity="0.2"/>
  <line x1="300" y1="100" x2="450" y2="140" stroke="#fbbf24" stroke-width="1" opacity="0.2"/>

  <text x="300" y="320" text-anchor="middle" font-size="14" font-weight="bold" fill="#fbbf24">学透 = 会变</text>
  <text x="300" y="338" text-anchor="middle" font-size="10" fill="#94a3b8">LEARN ≠ MEMORIZE. LEARN = TRANSFORM.</text>
</svg>'''

with open(f"{OUT}/11-epilogue-global.svg", "w") as f:
    f.write(epilogue)
print(f"✅ 尾声: 地球 ({len(epilogue)} chars)")

print(f"\n全部生成! 共 7 张SVG → {OUT}")
