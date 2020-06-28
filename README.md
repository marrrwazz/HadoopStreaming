# HadoopStreaming
Example of SQL query performed with Hadoop Streaming

SELECT EFirst, ELast, COUNT(*)
FROM Employee, Customer
WHERE EFirst = CFirst AND ELast = CLast
GROUP BY EFirst, ELast;
