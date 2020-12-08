## Softmax
- input: An array of real numbers
- output: An array of probabilities summing to `1`
```python
In [2]: x = np.array([1,2,7,3,2])

In [3]: np.exp(x)
Out[3]:
array([   2.71828183,    7.3890561 , 1096.63315843,   20.08553692,
          7.3890561 ])

In [4]: np.exp(x).sum()
Out[4]: 1134.2150893779665

In [5]: np.exp(x) / np.exp(x).sum()
Out[5]: array([0.00239662, 0.00651469, 0.96686525, 0.01770875, 0.00651469])
```
