#define SIZE 10000000
#include "quicksort.c"
#include <omp.h>
#include <time.h>
#include <stdlib.h>
#include <stdio.h>
void llenaArreglo(int * arreglo, int size)
{
  srand(time(NULL));
  for(int i = 0; i < size; i++)
    {
      int r = rand();
      arreglo[i] = r;
    }
}
int isSorted(int *arreglo , int size)
{
  int last = arreglo[0];
  for(int i = 1; i < size; i++)
    if(last > arreglo[i]){
      printf("Fallo aqui:%i %i",i,arreglo[i]);
      return 0;
    }
  return 1;
}
void imprimeArreglo(int* arreglo, int size)
{
  for(int i = 0; i < size; i++)
    printf("%i\n",arreglo[i]);
  return;
}

int * merge(int * arreglo, int medio)
{
  int * ordenado = malloc(SIZE * sizeof(int));
  int i = 0;
  int j = medio+1;
  int contador = 0;
  while(i <= medio && j < SIZE)
    if(arreglo[i] <= arreglo[j])
      ordenado[contador++] = arreglo[i++];
    else
      ordenado[contador++] = arreglo[j++];
  while(i < medio)
    ordenado[contador++] = arreglo[i++];
  while(j < SIZE)
    ordenado[contador++] = arreglo[j++];
  return ordenado;
}

int * quickParallel(int * arreglo)
{
  int medio = SIZE/2;
#pragma omp parallel sections 
  {
    #pragma omp section
    quicksort(arreglo,0,medio); 
    #pragma omp section
    quicksort(arreglo,medio+1,SIZE);
  }
  return merge(arreglo, medio);
  
}

int main(){
  int* arreglo = malloc(SIZE * sizeof(int));
  llenaArreglo(arreglo, SIZE);  
  clock_t t = clock();
  arreglo = quickParallel(arreglo);
  t = clock() - t;

  double time = ((double)t)/CLOCKS_PER_SEC;
  printf("%f seconds sorting with parallelism\n",time);
  if(isSorted(arreglo,SIZE) == 1)
    printf("Success\n");
  else
    printf("FAIL\n");
  free(arreglo);
  return 0;
}
