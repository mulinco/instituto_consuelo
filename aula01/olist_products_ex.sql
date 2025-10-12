
SELECT 
    product_id,
    product_category_name,
    product_photos_qty
FROM 
    olist_produtos
WHERE 
    product_photos_qty <= 1
LIMIT 10;