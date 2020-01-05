### To retrieve data use query.py


### To convert graph data to tree data run dfs.py for your csv file
 
 
 ### For pq gram distance one can use this code:
 
 res1 = mine_patterns(result, 3, 1, 1)
 
 res2 = mine_patterns(result2, 1, 3, 0)
 
 print(pq_gram_distance(res1, res2))
 

 ### For time testing one can run this code: 

 python -m timeit 'from index import mine_patterns' 'mine_patterns(2, 10, 0)'
 

 ###For memory allocation one can use this code:
 
 h = hpy()
 
 h.setrelheap()
 
 a = mine_patterns(20, 1, 0)
 
 x = h.heap()
 
 print(x)


 ### For profiling one  can run the following code:
 
  python -m cProfile -o output.pstats index.py 
  
  gprof2dot -f pstats output.pstats | dot -Tpng -o output.png


