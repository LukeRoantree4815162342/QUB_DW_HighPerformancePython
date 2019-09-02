#include "Rectangle.h"

namespace shapes{ 

    // Default constructor
    Rectangle::Rectangle () {}

    // Overloaded constructor
    Rectangle::Rectangle (int x0, int y0, int x1, int y1) {
        this->x0 = x0;
        this->y0 = y0;
        this->x1 = x1;
        this->y1 = y1;
    }

    // Destructor
    Rectangle::~Rectangle () {}

    // Return the area of the rectangle
    int Rectangle::getArea () {
        return (this->x1 - this->x0) * (this->y1 - this->y0);
    }
};

