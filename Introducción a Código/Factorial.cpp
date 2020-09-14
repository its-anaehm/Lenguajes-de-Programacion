
#include <iostream>
using namespace std;
int Factorial(int);

int main(){
    int n;
    cout<<"Introduzca el número al cual le desea calcular su factorial: "<<endl;
    cin>>n;
    cout<<"El factorial de "<<n<<" es "<<Factorial(n)<<endl;
}

int Factorial(int n){
    if (n==0 || n==1){
        return 1;
    }else{
        return n*Factorial(n-1);
    }
}