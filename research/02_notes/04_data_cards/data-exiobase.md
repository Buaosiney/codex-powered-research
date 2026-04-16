# EXIOBASE

## 数据源基本信息

- 名称：EXIOBASE 3
- 官方来源：https://exiobase.eu/
- 获取链接：https://www.exiobase.eu/ ; https://zenodo.org/records/15689391
- 获取日期：2026-04-16

## 覆盖范围

- 空间范围：
  - 44 个国家
  - 5 个 Rest of World 区域

- 时间范围：
  - 官方介绍显示 EXIOBASE 3 的原始时间序列覆盖 `1995-2011`
  - 官网说明后续 monetary 版本更新已迁移到 Zenodo，并有 nowcast/update 版本

- 行业/产品范围：
  - 163 industries
  - 200 products

## 主要变量

- 中间投入或供给使用表
- 最终需求
- 行业产出
- 环境扩展账户
- 就业、资源、排放等卫星账户

## 数据结构

- 文件类型：
  - MR-SUT
  - MR-IOT
  - monetary version
  - hybrid version

- 主要特点：
  - 高部门细分
  - 环境扩展丰富
  - 适合做消费端足迹、贸易隐含环境影响和结构分解分析

## 口径与限制

- 统计口径：
  - 属于全球环境扩展多区域投入产出数据库
  - 与 SEEA 兼容性较强

- 已知限制：
  - 数据体量较大，学习曲线较陡
  - 不同版本和 update 的适用范围需要单独核验
  - 对固定资本形成和资本内生化研究，原始结构仍可能需要额外辅助数据

- 使用注意事项：
  - 下载前需要确认使用版本、年份和 license
  - 使用时必须明确是 SUT 还是 IOT
  - 环境扩展变量非常多，入门阶段应先选最核心变量

## 获取与处理

- 原始文件位置：
  - 建议放到 `research/04_data/raw/exiobase/`

- 读取脚本位置：
  - 建议放到 `research/03_methods/input_output/scripts/`

- 清洗结果位置：
  - 建议放到 `research/04_data/interim/exiobase/`

## 适用问题

- 适合回答什么问题：
  - 消费、贸易、投资相关的隐含资源与排放分析
  - 环境扩展 MRIO 足迹研究
  - 产业链传导与全球价值链环境责任分析
  - 与资本形成、基础设施投资相关的上游环境影响识别

- 不适合直接回答什么问题：
  - 长期动态政策情景模拟
  - 行为反馈和技术替代的显式动态过程

## 当前状态

- [ ] 已下载
- [x] 已初读官网说明
- [ ] 已写读取脚本
- [ ] 已进入项目

## 当前判断

- 对你最重要的意义：
  - 这是后续做环境扩展 MRIO 和资本相关研究的高价值主力数据库候选
  - 不建议把它作为第一天上手的数据，但应尽早建立认知入口

- 推荐角色：
  - 中期核心数据库

## 参考来源

- EXIOBASE 官网：https://exiobase.eu/
- EXIOBASE about page：https://www.exiobase.eu/index.php/about-exiobase
- Stadler, K. et al. (2018). EXIOBASE 3: Developing a Time Series of Detailed Environmentally Extended Multi-Regional Input-Output Tables. Journal of Industrial Ecology. DOI: https://doi.org/10.1111/jiec.12715

