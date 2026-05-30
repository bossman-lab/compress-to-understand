# Codex: 生成第五章「认知层级的压缩——Bloom和Dreyfus」

## 指令

你是一个中文科技畅销书作家。请根据以下大纲撰写第五章。

## 输出

写入文件：`/root/Projects/compress-to-understand/chapters/ch05-cognitive-layers.md`

## 写作风格

- 中文流畅，分析性强，不要学术论文风
- 核心任务是：证明Bloom和Dreyfus是"描述性"的，我们的精通五层是"操作性"的
- 目标字数：6,000字

## 章节大纲

### 开篇（~600字）

场景：你在学校学过Bloom Taxonomy——六个层级，从知道到创造。但你当时用它做了什么？你可能在教案上写"目标：学生能分析..."，但没人给你一个方法验证学生到底有没有达到"分析"层级。

引出核心论点：Bloom和Dreyfus是理解层级的描述性框架，它们告诉你"更好的理解长什么样"，但不告诉你"怎样才能达到更好的理解"。我们的精通五层补上了这个缺口。

### Bloom's Taxonomy（2001修订版）（~2,500字）

**六级简述：** Remember→Understand→Apply→Analyze→Evaluate→Create。
**压缩论映射：** 每一级对应一种压缩操作：
- Remember = 存档
- Understand = 初次压缩（能用自己的话复述）
- Apply = 压缩模型在已知场景中的泛化
- Analyze = 拆解压缩结构
- Evaluate = 判断压缩质量
- Create = 用压缩模型生成未见实例

**与精通五层的完整映射表（核心内容）：**

| Bloom层级 | 我们的精通五层对应 | 差异说明 |
|-----------|-------------------|---------|
| Remember | 跳过（假设读者不是初学者） | 我们的框架不做记忆检验 |
| Understand | Level 1-2（跑通+拆解） | Bloom的Understand模糊，我们的Level 1-2有明确检验标准 |
| Apply | Level 3（参数实验） | Bloom只说"能用"，我们要求"能改参数预测" |
| Analyze | Level 4（边界探索） | 制造失败就是分析极限 |
| Evaluate | Level 5（一句话封装） | 判断压缩质量 |
| Create | Level 6扩展（生成未见） | 我们的框架有余量去扩展 |

**Blooms的盲区：** 描述性、非操作化、线性假设。你不可能在各层级之间线性爬升——你可能在Apply层对90%的内容正确、在Evaluate层只对10%的内容正确。Bloom没有处理这种不均匀性。

### Dreyfus Model（Novice→Expert）（~2,000字）

**五级简述：** Novice→Advanced Beginner→Competent→Proficient→Expert。
**压缩论解释：** Dreyfus模型是知识压缩的自然演化史：
- Novice：靠规则表（原始规则集，未压缩）
- Competent：靠分层决策（层次化压缩）
- Expert：靠直觉（压缩到不用显式解压缩）

**Dreyfus的价值：** 承认Expert不需要用"教小孩"的方式输出。费曼学习法要求你把Expert级别的直觉解压缩为小孩级别的语言——这在某些场景是反效率的。
**Dreyfus的盲区：** 同样只是描述性的说"Expert就是这样的"，没有给操作路径。我们的Level 3-4（参数实验+边界探索）提供了从Competent爬到Proficient的具体工具。

### 与精通五层的综合对比（~900字）

三个框架放在一起：

- Bloom：告诉你理解有哪些层次（名称）
- Dreyfus：告诉你理解的自然演化路径（历史）
- 精通五层：告诉你如何质检验证每一层（操作）

哪一个对学习者更有用？都用了才是完整的。用Bloom/Dreyfus理解"我在哪层"，用精通五层执行"怎么到下一层"。
