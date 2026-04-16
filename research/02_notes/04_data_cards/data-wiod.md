# WIOD

## 数据源基本信息

- 名称：World Input-Output Database
- 官方来源：https://www.rug.nl/ggdc/valuechain/wiod/
- 获取链接：https://www.rug.nl/ggdc/valuechain/wiod/wiod-2016-release
- 获取日期：2026-04-16

## 覆盖范围

- 空间范围：
  - 43 个国家
  - 1 个 Rest of the World

- 时间范围：
  - WIOD 2016 release 覆盖 `2000-2014`
  - 网站同时保留 2013 release 入口

- 行业范围：
  - 56 sectors
  - 分类与 ISIC Rev. 4 一致

## 主要变量

- 世界投入产出表
- 部门产出和中间投入
- 社会经济账户
- 与 WIOD 兼容的环境账户入口

## 数据结构

- 发布格式：
  - Stata
  - R
  - Excel

- 主要特点：
  - 文档成熟
  - 学术界使用广泛
  - 对入门学习相对友好

## 口径与限制

- 统计口径：
  - 遵循 2008 SNA
  - 更强调可用性与长期学术积累

- 已知限制：
  - 相较 EXIOBASE，部门细度和环境扩展维度有限
  - 时间覆盖已不算最新

- 使用注意事项：
  - 很适合作为学习 MRIO 和复现经典文献的训练数据
  - 如果后续要做更细致环境分析，通常需要切换或补充到 EXIOBASE 等数据库

## 获取与处理

- 原始文件位置：
  - 建议放到 `research/04_data/raw/wiod/`

- 读取脚本位置：
  - 建议放到 `research/03_methods/input_output/scripts/`

- 清洗结果位置：
  - 建议放到 `research/04_data/interim/wiod/`

## 适用问题

- 适合回答什么问题：
  - MRIO 学习和入门复现
  - 全球价值链和贸易结构基础分析
  - 方法教学和小型训练项目

- 不适合直接回答什么问题：
  - 最新年份国际结构分析
  - 高细度环境扩展研究

## 当前状态

- [ ] 已下载
- [x] 已初读官网说明
- [ ] 已写读取脚本
- [ ] 已进入项目

## 当前判断

- 对你最重要的意义：
  - 是非常适合入门和训练 MRIO 直觉的经典数据库
  - 可以作为你正式进入 EXIOBASE 或资本内生化前的教学型训练数据

- 推荐角色：
  - 入门训练数据库

## 参考来源

- WIOD 首页：https://www.rug.nl/ggdc/valuechain/wiod/
- WIOD 2016 release：https://www.rug.nl/ggdc/valuechain/wiod/wiod-2016-release
- Timmer, M. P. et al. (2015). An Illustrated User Guide to the World Input-Output Database: the Case of Global Automotive Production. Review of International Economics, 23, 575-605.

