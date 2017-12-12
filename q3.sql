
-- I tried these two queries, but I could only get the answer half right

SELECT setval('category_id_seq', (select max(id) from category));
WITH RECURSIVE last_run AS (
SELECT parent_id as parent_id, to_char(id, '999') as id_list, name as name_list FROM category WHERE id = 11
  UNION ALL
SELECT c.parent_id as parent_id,
to_char(category.id, '999') || ', ' || to_char(c.id, '999') as id_list,
category.name || ', ' || c.name as name_list
 FROM category AS c 
INNER JOIN category ON
        c.id = category.parent_id  
)
SELECT id_list, name_list FROM last_run
ORDER BY id_list;

-- I also tried this, but it's also not quite right

WITH RECURSIVE last_run(parent_id, id_list, name_list) AS (
SELECT parent_id, ARRAY[id], name
FROM category
UNION ALL
SELECT c.parent_id, id_list || c.id, name_list || ', ' || c.name
FROM category AS c, last_run AS r
WHERE c.id = r.parent_id
)
SELECT id_list, name_list FROM last_run
ORDER BY id_list;
