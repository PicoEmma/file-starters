#ifndef __C_STARTER_H
#define __C_STARTER_H

#include "Example.h"

namespace Foo {

class Bar {
protected:
  int value;
  
public:
  Bar(int value) : value(value) {}  // todo I don't remember if initializer list works in header file...
  
  int getValue();
  void setValue(int const & v);
}  // close class Bar

};  // close namespace Foo

#endif  // __C_STARTER_H
