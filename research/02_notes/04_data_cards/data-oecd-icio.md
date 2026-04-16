# OECD ICIO

## 数据源基本信息

- 名称：OECD Inter-Country Input-Output Tables
- 官方来源：https://www.oecd.org/sti/ind/inter-country-input-output-tables.htm
- 获取链接：https://www.oecd.org/sti/ind/inter-country-input-output-tables.htm
- 获取日期：2026-04-16

## 覆盖范围

- 空间范围：
  - regular ICIO：80 个经济体 + rest of the world
  - extended ICIO：80 个国家，并对中国和墨西哥做更细分处理

- 时间范围：
  - 当前官网显示 2025 edition 覆盖 `1995-2022`

- 行业范围：
  - 按 OECD ICIO 活动分类组织

## 主要变量

- 国家间中间品流
- 最终需求
- 贸易增加值相关计算基础
- 全球价值链分析相关指标基础

## 数据结构

- 发布形式：
  - regular ICIO
  - extended ICIO
  - readme
  - annex
  - CSV / R data

- 主要特点：
  - 官方口径
  - 国际可比性较强
  - 与 TiVA 和 GVC 分析联系紧密

## 口径与限制

- 统计口径：
  - OECD 构建的国际投入产出基础设施
  - 强调生产、消费、投资与国际贸易之间的联系

- 已知限制：
  - 部门细度通常低于 EXIOBASE 一类数据库
  - 环境扩展信息需要结合 OECD 其他指标或外部账户使用

- 使用注意事项：
  - 适合先理解国家间投入产出与价值链逻辑
  - 如果目标是精细环境扩展分析，需要检查环境账户的可衔接性

## 获取与处理

- 原始文件位置：
  - 建议放到 `research/04_data/raw/oecd_icio/`

- 读取脚本位置：
  - 建议放到 `research/03_methods/input_output/scripts/`

- 清洗结果位置：
  - 建议放到 `research/04_data/interim/oecd_icio/`

## 适用问题

- 适合回答什么问题：
  - 全球价值链与贸易增加值问题
  - 国家间产业链依赖和结构传导
  - 投资、消费和贸易在国际生产网络中的位置分析

- 不适合直接回答什么问题：
  - 高细度部门环境扩展足迹问题
  - 复杂资本内生化问题

## 当前状态

- [ ] 已下载
- [x] 已初读官网说明
- [ ] 已写读取脚本
- [ ] 已进入项目

## 当前判断

- 对你最重要的意义：
  - 这是官方且较稳健的国际投入产出入口，适合建立全球价值链和国际比较视角
  - 对“消费、贸易、投资活动的全球资源环境影响”这个导师方向有直接支撑价值

- 推荐角色：
  - 官方国际比较数据库

## 参考来源

- OECD ICIO 页面：https://www.oecd.org/sti/ind/inter-country-input-output-tables.htm
- Yamano, N. et al. (2023). Development of the OECD Inter Country Input-Output Database 2023. OECD Science, Technology and Industry Working Papers. DOI: https://doi.org/10.1787/5a5d0665-en

