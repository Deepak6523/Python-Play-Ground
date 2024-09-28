#include <iostream>
using namespace std;

class cal{
    public:
    // float a,b;
    void add(float a,float b){
        
        cout << "The addition is " << a+b << endl; 
    }
    void sub(float a,float b){
        cout << "The subtraction is " << a-b << endl;
    }
    void mul(float a,float b){
        cout << "The product is " << a*b << endl;
    }
    void div(float a,float b){
        cout << "The divition is " << a/b << endl;
    }
    void avg(float a,float b){
        cout << "The mean is " << ((a+b)/2) << endl;
    }
};
int main()
{
    cal s1;
    float a,b;
    string opt;
    cout << "Enter the first number ";
    cin >> a;
    cout << "Enter the second number ";
    cin >> b;
    cout << "Choose the operation" << endl;
    cin >> opt;
    if(opt=="+"){
        s1.add(a,b);
    }
    else if(opt=="-"){
        s1.sub(a,b);
    }
    else if(opt=="*"){
        s1.mul(a,b);
    }
    else if(opt=="/"){
        s1.div(a,b);
    }
    else if(opt=="a"){
        s1.avg(a,b);
    }
}
