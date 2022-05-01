SELECT YEAR(CREATED_AT)                             AS YEAR,
       MONTH(CREATED_AT)                            AS MONTH,
       IF(COUNT(CATEGORY) > 0, SUM(CATEGORY), 0)    AS CANCEL_COUNT,
       IF(SUM(CATEGORY) > 0, (SUM(ABS(AMOUNT))), 0) AS AMOUNT
  FROM CARD_USAGES
 GROUP BY YEAR(CREATED_AT), MONTH(CREATED_AT), CATEGORY
 ORDER BY YEAR(CREATED_AT) DESC,MONTH(CREATED_AT) DESC;