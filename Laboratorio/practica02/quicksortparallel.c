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

int * merge(int * arreglo, int medio, int size)
{
  int * ordenado = malloc(size * sizeof(int));
  int i = 0;
  int j = medio+1;
  int contador = 0;
  while(i <= medio && j < size)
    if(arreglo[i] <= arreglo[j])
      ordenado[contador++] = arreglo[i++];
    else
      ordenado[contador++] = arreglo[j++];
  while(i < medio)
    ordenado[contador++] = arreglo[i++];
  while(j < size)
    ordenado[contador++] = arreglo[j++];
  return ordenado;
}

int * quickParallel(int * arreglo,int size)
{
  int medio = 1+(size-1)/2;
#pragma omp parallel sections 
  {
    #pragma omp section
    quicksort(arreglo,0,medio); 
    #pragma omp section
    quicksort(arreglo,medio+1,size);
  }
  imprimeArreglo(arreglo,size);
  printf("---------------");
  return merge(arreglo, medio, size);
  
}

int main(){
  int size;
  scanf("%d",&size);
  int * arreglo = malloc(size * sizeof(int));
  for(int i = 0; i < size; i++)
    scanf("%d",&arreglo[i]);
  arreglo = quickParallel(arreglo,size);
  imprimeArreglo(arreglo,size);
  free(arreglo);

  return 0;
}
