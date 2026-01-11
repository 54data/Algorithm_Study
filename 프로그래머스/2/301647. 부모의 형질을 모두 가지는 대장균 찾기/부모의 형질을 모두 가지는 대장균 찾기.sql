SELECT
  t1.id,
  t1.genotype,
  t2.genotype AS parent_genotype
FROM ecoli_data t1
JOIN ecoli_data t2
  ON t1.parent_id = t2.id
WHERE (t1.genotype & t2.genotype) = t2.genotype
ORDER BY t1.id;