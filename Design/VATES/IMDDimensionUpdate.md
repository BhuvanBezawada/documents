#IMDDimension Update#

##Motivation##

The IMDWorkspace format in Mantid provides a flexible way to store n-dimensional data of any type. The format is not limited to work either with a fixed number, or dimensions, or a particular set of units for any of the dimensions.

Increasingly we need to know more information about the dimensions when algorithm, visualisation and other processing code needs to look for, and act on specific dimensions. The primary use case for this is to find the Q dimensions.

Up until now, we have had no way to do this, and have had to resort to regex matching the dimension names and ids in order to find our Q dimensions in the workspace. For example [here](https://github.com/mantidproject/mantid/blob/master/Code/Mantid/Framework/API/src/PeakTransformHKL.cpp#L9:L18). This is fragile, but the information to otherwise identify these dimensions is missing. Likewise, we have no good way of extracting the scaling off these dimensions. Once it gets written as a string. We would again need some kind of regex to rextract it. This is done, for example, [here](https://github.com/mantidproject/mantid/blob/master/Code/Mantid/Framework/MDAlgorithms/src/MDWSTransform.cpp#L357:L390), and used to create dimensions [by calling this](#https://github.com/mantidproject/mantid/blob/master/Code/Mantid/Framework/MDAlgorithms/src/MDEventWSWrapper.cpp#L25:L46). you will notice the lack of other information fed into the MDHistoDimension because the MDhistoDimension currently has no proper placeholder for the unit type.

We currently have a visualisation request to lock the aspect ratios in the SliceViewer only for the Q dimensions, and this would be a good opportunity to tackle the issue properly as part of this work, and retrospectively fix the areas of the code base that string based matching to determine these fields.

##Definitions##

| Term        | Meaning          |
| ------------- |:-------------:|
| IMDWorkspace      | Interface for the multidimensional Mantid Workspace |
| IMDDimension      | Interface for a dimension of an IMDWorkspace |
| SliceViewer      | Multidimensional 2D slicing tool in Mantid |
| r.l.u       | Reciprocal lattice units |

##Solution 1##

This solution is based around introducing a complete set of missing types, which are fundamental to recording and interchanging between different representation.


####IMDDimension####

```cpp
class IMDDimension {

  ...
  public:
    MDQuantity getMDQuantity() const; // Add new accessor

};

```

####MDQuantity####

New abstract type. Replaces Mantid::Kernel::SpecialCoordinateSystem
```cpp
class MDQuantity {
  public:
    UnitLabel getUnitLabel() const = 0; // Concrete implementations will forward
    MDUnit getMDUnit() const = 0;
};

class QLab : public MDQuantity{
  ...
};

class QSample : public MDQuantity{
  ...
};

class HKL : public MDQuantity{
  ...
};

class General : public MDQuantity{
  ...
};


```

####MDUnit####

The reason to separate MDUnit from MDQuantity is to support the concept of conversion better. While QLab can be converted to QSample and HKL, according to the Busing-Levy model, it is not possible to represent QLab or QSample in anything other than inverse Angstroms. HKL quantities can be represented in either inverse Angstroms or reciprocal lattice units. We would then later be able to add algorithms that support these conversions. We currently have to perform these conversions in a bespoke fashion in numerous places particularly in the Crystal module of Mantid.

HKL (r.l.u) and HKL (A^-1) would be modelled with the same MDQuantity, but with different MDUnits. We would of course overload operator== to ensure that instances of these were treated as non-equal.

```cpp
class MDUnit {
  public:
    std::string getMDUnitId(); 
    UnitLabel getUnitLabel() const = 0;
    bool canConvertTo(&MDUnit other) const = 0;
    MDUnit convertTo(const std::string mdUnitID) const = 0; 
};

class RLU : public MDUnit {
  ...
};

class InverseAngstroms : public MDUnit {
  ...
};

class LabelMDUnit : public MDUnit {
  ...
};
```

###Development Steps###
* Introduce the new types and subtypes. Ensure equality is implemented properly.
* Handle persistance 
* Replace Mantid::Kernel::SpecialCoordateSystem with MDQuantity
* Add getters/setters to IMDDimension and subtypes

Refactoring all existing code to better use these types would be a further step.




