//lista linear implementada com continuidade fisica com descritor

#include <stdio.h>
#include <stdlib.h>
#include <conio.h>
#include <string.h>
int MAX = 10;
int i;

typedef struct SPpessoa { 
    int idade;
    char nome[40]; 
}pessoa;
pessoa *lista; /// VETOR

typedef struct SDescritor {
 int inicio;                /// inicio do vetor
 int fim;                   ///fim do vetor
 int ini_lista;             ///inicio do lista
 int fim_lista;             /// fim da lista
 int num_ele;               /// numero de elementos
 } Descritor; 
 Descritor *DL;

//Operação

void inicializa (Descritor *DL){
    DL->fim = MAX;
    DL->inicio = 0;
    DL->num_ele =0;
    DL->ini_lista = DL->inicio;
    DL->fim_lista = 0;
    return;
}


void insere_final (pessoa *lista, Descritor *DL, pessoa p){
    if(((DL->fim) - (DL->fim_lista)) >= 1){                 ///Verifica se tem espaço
        if(DL->num_ele == 0){
        	lista[DL->fim_lista] = p;
        	DL->num_ele +=1;
        	return;	
		}
		DL->fim_lista +=1;
        DL->num_ele +=1;
		lista[DL->fim_lista]= p;

        return;
    }

    if(DL->ini_lista - DL->inicio >= 1){             ///Verifica se tem espaço
        for(i=DL->ini_lista;i <=DL->fim_lista; i++)
            lista[i -1]= lista[i];
        lista[DL->fim_lista]= p;
        DL->ini_lista -= 1;
        DL->num_ele +=1;
        return;
    }
    else{
        printf("lista Cheia \n");
        getchar();
        system("cls");
        return;
    }
}

    
void insere_inicio (pessoa *lista, Descritor *DL, pessoa p){
	if(DL->num_ele==0){
		lista[DL->ini_lista]=p;
		DL->num_ele +=1;
		return;
	}
    if(DL->ini_lista - DL->inicio >= 1){          ///Verifica se tem espaço
        lista[DL->ini_lista-1]= p;
        DL->ini_lista  -= 1;
        DL->num_ele +=1;
        return;
    }
    if(DL->fim - DL->fim_lista >= 1){             ///Verifica se tem espaço
        for(i=DL->fim_lista; i>=DL->ini_lista; i--){
            lista[i+1]= lista[i];
        }
        lista[DL->ini_lista]= p; 
        DL->fim_lista +=1;   
        DL->num_ele +=1;
        return;
    }
    else{
        printf("lista Cheia");
		getchar();
		system("cls");        
        return;
    }
        
}
void insere_meio (pessoa *lista, Descritor *DL, int posicao, pessoa p){
	if(DL->num_ele==0){
		lista[DL->ini_lista]=p;
		DL->num_ele +=1;
		return;
	}
    if(DL->fim- DL->fim_lista >= 1){                 ///Verifica se tem espaço
        for(i = DL->fim_lista; i >= (DL->ini_lista + posicao); i--){
            lista[i+1]= lista[i];
        }
        lista[DL->ini_lista + posicao]= p;
        DL->num_ele +=1;
        DL->fim_lista +=1;
        return;
    }
    if(DL->ini_lista - DL->inicio >= 1){              ///Verifica se tem espaço
        for(i=DL->ini_lista; i <= (DL->ini_lista + posicao); i++){
            lista[i -1]= lista[i];
        }
        lista[DL->ini_lista + posicao] = p;
        DL->num_ele +=1;
        DL->ini_lista -=1;
        return;
    }
    else{
            printf("lista Cheia \n");
            getchar();
			system("cls");  
            return ;
    }
}

void remove_nodo ( pessoa *lista, Descritor *DL, int posicao){
    for(i=(DL->ini_lista)+ posicao-1; i <=(DL->fim_lista); i++){
        lista[i]= lista[i + 1];
    }
    DL->fim_lista -=1;
    DL->num_ele -=1;
}

void consulta ( pessoa *lista, Descritor *DL, int posicao){
	
    if((posicao >= 0) && (posicao <=(DL->fim_lista - DL->ini_lista))){
        printf("Pessoa : %s \n",lista[posicao + DL->ini_lista].nome);
        printf("Idade: %i \n \n", lista[posicao + DL->ini_lista].idade);
        return;
    }
    else{
        printf("Error");

        return ;
    }
}
void imprime_lista(pessoa *lista, Descritor *DL){
    for(i=(DL->ini_lista); i<=(DL->fim_lista); i++){
    	printf("Pessoa : %s \n", lista[i].nome);
        printf("Idade: %i \n \n", lista[i].idade);
    }
    return;
}
void destroi( pessoa *lista){
    free(lista);
}
void libera_lista(pessoa * lista, Descritor *DL){
	for( i=(DL->ini_lista);i<=(DL->fim_lista);i++){
        strcpy(lista[i].nome , "Vazio");
        lista[i].idade=0;
    }
    DL->ini_lista=0;
    DL->fim_lista=0;
    DL->num_ele=0;
}
void busca_idade(pessoa *lista, Descritor *DL, int idade){
	int helpa =0;
    for(i=DL->ini_lista; i<=DL->fim_lista;i++){
        if(lista[i].idade==idade){
        	printf("Pessoa : %s \n",lista[i].nome);
        	printf("Idade: %i \n \n", lista[i].idade);
			helpa +=1;
        }
    }
    if(helpa>0){
    	return;
	}
    printf("Erro - Dado nao encontrado");
    return;
}


pessoa pega_pessoa(){
    pessoa aux;
    printf("Digite um nome: \n");
    scanf("%s",&aux.nome);
    printf("Digite uma idade: \n");
    scanf("%i", &aux.idade);
    system("cls");
    return aux;
}

int main(){
	int valor, k,w;
	int z=1;
	pessoa test;
	lista = malloc(sizeof(pessoa)*MAX);
	DL = malloc(sizeof(Descritor));
	inicializa(DL);
 
	while(z==1){
		printf ("1 - Imprime lista \n");
		printf ("2 - Adicionar ao final \n");
		printf ("3 - Adicionar ao inicio \n");
		printf ("4 - Adicionar na posicao N \n");
		printf ("5 - Consultar posicao \n");
		printf ("6 - Busca por tipo de dado (IDADE) \n");
		printf ("7 - Remove um nodo \n");
		printf ("8 - Libera lista \n");
		printf ("9 - Sair \n \n");
		scanf("%i", &valor);
		system("cls");
		
		switch (valor){
			
			case 1 :
				printf("Imprime lista \n \n");
				imprime_lista(lista, DL);
	        	getchar();
			break;
	 
			case 2 :
				printf ("Adiciona ao final \n \n");
				test = pega_pessoa();
				insere_final( lista,  DL, test);
	     	break;
	 
	     	case 3 :
	        	printf ("Adiciona ao inicio \n \n");
	        	test = pega_pessoa();
				insere_inicio( lista,  DL, test);
	     	break;
	 
	     	case 4 :
	        	printf ("Adiciona na posicao N \n \n");
	        	printf ("Qual a posicao N? \n");
	        	scanf("%i", &k);
	        	test = pega_pessoa();
				insere_meio( lista,  DL, (k-1), test);
	     	break;
	 
	     	case 5 :
	        	printf ("Consulta posicao \n \n");
	        	printf ("Qual a posicao N? \n");
	        	scanf("%i", &k);
	        	consulta( lista, DL, (k-1));
	        	getchar();
	     	break;
	 
	     	case 6 :
	     		printf("Busca por tipo de dado (IDADE) \n \n");
	     		printf ("Qual a idade? \n");
	        	scanf("%i", &k);
				busca_idade(lista, DL, k);
	        	getchar();

	     	break;
	 
	     	case 7 :
	        	printf ("Remover um nodo \n \n");
	        	printf ("Qual a posicao do nodo? \n");
	        	scanf("%i", &k);
	        	remove_nodo(lista, DL, k);
	    	break;
	     	
	     	case 8 :
	        	printf ("Liberar Lista \n \n");
	        	libera_lista(lista, DL);
	        	getchar();
	     	break;
		 
	     	case 9 :
	        	printf ("SAIR");
	        	z = 2;
	        
	    	break; 
	     
	    	default :
	    		
				printf("Opcao invalida");
				getchar();
		}
		getchar();
		system("cls");
	  
	}
    return 0;

}
