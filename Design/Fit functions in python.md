# Working with fit functions in python

Although fitting functions have some of the functionality exposed to python the use of it is very limited and functions are constructed via strings. Values of the optimised parameters get extracted from `TableWorkspace`s output from the Fit algorithm. Both function construction and extraction of the results are cumbersome and error prone. This document describes a design of a python fitting API aiming to overcome these problems. The main idea of the solution proposed here is to create and manipulate a C++ [`IFunction`](https://github.com/mantidproject/mantid/blob/master/Framework/API/inc/MantidAPI/IFunction.h) object from python directly via a thin wrapper python class `FitFunctionWrapper`.

## Function construction

For each concrete function type (Gaussian, Lorentzian, etc) there should exist a corresponding python function with the same name automatically generated in a way similar to the algorithm functions. A function object is then constructed by calling such a function (constructor) and is an instance of `FitFunctionWrapper`. For example
```
  g = Gaussian()
```
A call without passing in any initialisation arguments should create a function with default parameters and attributes.
Initial values of parameters and attributes can be given via keyword arguments, for example
```
  p = Polynomial(attributes={'n': 3}, parameters={'A0': 1, 'A1': 2, 'A3': 3, 'A4': 4})
```
Parameter and attribute names can also be used as the keys:
```
  g = Gaussian(Height=1, Sigma=0.1)
  
  p = Polynomial(n=3, A0=1, A1=2, A3=3, A4=4)
```
The implementation must check each keyword argument if it's a parameter or an attribute by calling `IFunction::hasAttribute(name)`. All passed attributes must be set before setting parameters. There is need to be a provision for setting attributes in a particular order in case it is essential for a fitting function. This can be done for example by passing a list of name/value pairs (tuples or lists) to the `attributes` keyword argument.

### Construction of composite functions

Composite functions can be created in a similar way, by callig a constructor. It should be able to accept the same types of arguments as a simple function but also it must have the `functions` keyword argument that takes a list of member functions. For example:
```
  c = CompositeFunction(functions=[Gaussian(PeakCentre=1), Gaussian(PeakCentre=2)])
```
Another way of setting member functions is via positional arguments of the condtructor:
```
  c = CompositeFunction(Gaussian(PeakCentre=1), Gaussian(PeakCentre=2))
```
`FitFunctionWrapper` class will override the `__add__()` method to allow construction of composite functions from a sum of member functions:
```
  c = LinearBackground() + Gaussian(PeakCentre=1) + Gaussian(PeakCentre=2)
```
`ProductFunction` can be constructed from a product of member functions:
```
  p = ExpDecay() * UserFunction(Formula='sin(w*x)', w=1)
```

### Multi-domain functions

A [`MultiDomainFunction`](https://github.com/mantidproject/mantid/blob/master/Framework/API/inc/MantidAPI/MultiDomainFunction.h) needs a custom constructor which sets domain indices to its members.

## Updating functions

### Getting and setting parameters and attributes

`FitFunctionWrapper` will implement `__getitem__(self, name)` and `__setitem__(self, name, value)` methods to access parameters and attributes in a dictionary-like style (`name` is a string):
```
  sigma = gaussian['Sigma']
  
  comp_func['f1.A0'] = 0.5
```

Parameters of members of composite functions can be accessed via their wrapper objects. For example:
```
  bk = LinearBackground()
  peak = Lorentzian()
  spectrum = bk + peak
  ...
  bk['A0'] = 1
  peak['FWHM'] = 0.123
  assert spectrum['f0.A0'] == 1
  assert spectrum['f1.FWHM'] == 0.123
```
*Question: what to do if a function becomes a member of two or more composite functions?*
  1. *Ignore and let the user be responsible for it*
  2. *Set a flag on `FtFunctionWrapper` and prevent subsequent attempts to add it*

### Managing members of composite functions

`FitFunctionWrapper` will implement `__getitem__(self, i)` and `__setitem__(self, i, value)` methods to access members of a composite function in a list-like style (`i` is an `int`):
```
  spectrum = LinearBackground() + Gaussian(PeakCentre=1) + Gaussian(PeakCentre=2)
  peak1 = spectrum[1]
  peak1['Sigma'] = 0.123
  spectrum[2] = Lorentzian(PeakCentre=2)
```

`FitFunctionWrapper` will override `__iadd__(self, func)` and `__delitem__(self, i)` (`i` is an `int`, `func` is a `FitFunctionWrapper`) to implement adding and deleting members via `+=` and `del` operators:
```
  spectrum += Lorentzian(PeakCentre=3)
  del spectrum[0]
```

Implement `__len__(self)` to return the number of member functions.
```
  n_peaks = len(spectrum)
```
