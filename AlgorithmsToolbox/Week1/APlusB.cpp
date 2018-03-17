#include <iostream>

int main(){
  int a = 0;
  int b = 0;
  int sum = 0;
//  std::cin >> a;
//  std::cin >> b;
	std::cin >> a >> b; 

	if(a >=0 && b<=9)
	{
  	sum = a + b;
  	std::cout << sum << std::endl;
	}

	else
		std::cout << "error in inputs" << std::endl;

  return 0;
}
