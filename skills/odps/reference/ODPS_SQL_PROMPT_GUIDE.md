# ODPS SQL Generation Guide

本文档旨在指导 AI 助手生成高质量、符合阿里云 MaxCompute (ODPS) 规范的 SQL 语句。

## 核心原则

当用户请求生成或转换 SQL 时，请遵循以下规则：

### 1. 分区处理 (Partition Handling)

**这是最重要的规则**。ODPS 表通常是分区的，全表扫描极其低效且常被禁止。

*   **最新分区**：默认使用 `MAX_PT('table_name')` 函数来获取最新分区。
    *   示例：`WHERE ds = MAX_PT('lazada_ods.s_gm_seller_tag_data_th')`
    *   说明：`MAX_PT` 是此 Skill 环境中常用的宏或自定义函数，用于动态获取最大分区值。
*   **明确分区**：如果用户指定了日期，请使用明确的分区过滤。
    *   示例：`WHERE pt = '20231001'`

### 2. 语法映射 (MySQL vs ODPS)

| 功能 | MySQL | ODPS SQL |
| :--- | :--- | :--- |
| **当前时间** | `NOW()` | `GETDATE()` |
| **日期加减** | `DATE_ADD(date, INTERVAL n DAY)` | `DATEADD(date, n, 'dd')` |
| **字符串截取** | `SUBSTRING(str, 1, 5)` | `SUBSTR(str, 1, 5)` (索引从1开始) |
| **字符串拼接** | `CONCAT()` | `CONCAT()` (注意 NULL 处理) |
| **聚合拼接** | `GROUP_CONCAT()` | `WM_CONCAT(separator, col)` |
| **类型转换** | 隐式转换 | 必须显式 `CAST(val AS TYPE)` |
| **JSON处理** | `JSON_EXTRACT` | `GET_JSON_OBJECT` |

### 3. 性能优化 (Performance Optimization)

*   **MAPJOIN**: 小表关联大表时，必须使用 MAPJOIN Hint。
    ```sql
    SELECT /*+ MAPJOIN(b) */ a.id, b.name 
    FROM large_table a JOIN small_table b ON a.key = b.key
    ```
*   **LIMIT**: 探索性查询（SELECT *）必须加上 `LIMIT n`。
*   **列裁剪**: 避免 `SELECT *`，尽量只查询需要的列。

### 4. 数据类型

*   `VARCHAR` -> `STRING`
*   `INT` -> `BIGINT` (推荐默认使用 BIGINT)
*   `DATETIME` / `TIMESTAMP` -> `DATETIME`

## Prompt 示例

当用户问：“查询昨天销售额最高的前 10 个商品”

**推荐生成的 SQL**：

```sql
SELECT 
    product_id,
    SUM(gmv) as total_gmv
FROM 
    sales_detail
WHERE 
    ds = MAX_PT('sales_detail')  -- 使用 MAX_PT 获取最新分区
GROUP BY 
    product_id
ORDER BY 
    total_gmv DESC
LIMIT 10;
```

## 错误检查清单

生成 SQL 后，请自检：
- [ ] 是否添加了分区过滤条件（`ds = ...` 或 `pt = ...`）？
- [ ] 是否使用了 `MAX_PT` 处理默认的最新分区需求？
- [ ] 是否将 MySQL 特有函数（如 `NOW()`）转换为了 ODPS 函数（`GETDATE()`）？
- [ ] 是否对小表 JOIN 使用了 `MAPJOIN`？
- [ ] 是否加上了 `LIMIT` 限制返回行数？
