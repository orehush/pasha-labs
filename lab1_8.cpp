#include <iostream>
#include <string.h>

using namespace std;

class Product {
    private:
        string name;
        int count;
        float price;

    public:
        Product() {
            cout << "This is constructor without parameters\n";
            name = "Unknown product";
            count = 1;
            price = 0;
        }

        Product(string pname, int pcount, float pprice) {
            cout << "This is constructor with parameters\n";
            name = pname;
            count = pcount;
            price = pprice;
        }

        Product(const Product &obj) {
            cout << "This is copy constructor\n";
            name = obj.name;
            count = 0;
            price = obj.price;
        }

        ~Product() {
            cout << "This is decounstructor\n";
        }

        void print() {
            cout << "This is product: " << name << "\n";
            cout << "Available count is: " << count << "\n";
            cout << "Price by 1 item: " << price << "\n";
            cout << "----------\n";
        }

        void set(string pname, int pcount, float pprice) {
            name = pname;
            count = pcount;
            price = pprice;
        }
};

void (Product::*fptr) () = &Product::print;

int main() {
    Product p1("Apple", 10, 1.5);
    p1.print();

    Product p2;
    p2.print();
    p2.set("Banana", 20, 5.5);
    p2.print(); 

    Product p3 = p1;
    p3.print();

    Product *p = &p2;
    p->print();

    cout << "Hello World!" << '\n';
    return 0;
}