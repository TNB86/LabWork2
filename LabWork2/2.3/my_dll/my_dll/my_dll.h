#pragma once

#ifdef MY_DLL_EXPORTS
#define MY_DLL_API __declspec(dllexport)
#else
#define MY_DLL_API __declspec(dllimport)
#endif 

extern "C" MY_DLL_API char* FuncName();

extern "C" MY_DLL_API double TheFunc(double x);