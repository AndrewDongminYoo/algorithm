SELECT COUNT(*) AS CNT
  FROM PAYMENTS A
       RIGHT OUTER JOIN PURCHASES B
         ON A.USER_ID = B.USER_ID
 WHERE A.USER_ID IS NULL;
