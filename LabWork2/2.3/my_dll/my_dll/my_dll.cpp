#include "stdafx.h"
#include "my_dll.h"

char* FuncName() {
	char func[8] = { 'y','=','2','*','x','+','5',0 };
	return func;
}

double TheFunc(double x) {
	return 2 * x + 5;
}