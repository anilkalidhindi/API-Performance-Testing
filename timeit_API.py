import timeit

timeit_API = rdd.map(lambda x: timeit.timeit('requests.post(%r,%r).json()' % (url,x), setup='import requests', number=1))
timeit_API.cache()

print 'timeit_API_min %s' % timeit_API.min()
print 'timeit_API_max %s' % timeit_API.max()
print 'timeit_API_mean %s' % timeit_API.mean()
print 'timeit_API_variance %s' % timeit_API.variance()
print 'timeit_API_stdev %s' % timeit_API.stdev()
print '\n'
