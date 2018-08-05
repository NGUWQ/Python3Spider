__author__ = 'WQ'
# *_*coding:utf-8 *_*
import pyquery
html='''
<div class="wrap">
<div id="container">
<ul class="list">
<li class="item-0">first item</li>
<li class="item-1"><a href="link2.html">second item</a></li>
<li class="item-0 active"><a href="link3.html"><span class="bold">third item<span></a></li>
<li class="item-1 active"><a href="link4.html">fourth item</a></li>
<li class="item-0"><a href="link5.html">fifth item</a></li>
</ul>
</div>
</div>
'''
doc=pyquery.PyQuery(html)
#li=doc('li:first-child')
l0=doc('li a:first-child')
#print(li)
print(l0)