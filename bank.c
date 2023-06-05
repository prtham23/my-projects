#include<stdio.h>
#include<string.h>
#include<stdlib.h>

int main()
{
    typedef struct 
    {
        int account;
        char type;
        char name[50];
    }bankk;
    bankk bank[130];

    // bank[100] = {100,'S',"Abhijit"};
    // bank[101] = {101,'S',"Abhi"};
    // bank[102] = {102,'S',"sahil"};/
    bank[100].account=100;
    bank[100].type='S';
    strcpy(bank[100].name,"Abhijit");

    bank[101].account=101;
    bank[101].type='S';
    strcpy(bank[101].name,"Abhi");

    bank[102].account=102;
    bank[102].type='S';
    strcpy(bank[102].name,"Sahil");
    
    bank[103].account=103;
    bank[103].type='S';
    strcpy(bank[103].name,"mayappa");

    bank[104].account=104;
    bank[104].type='S';
    strcpy(bank[104].name,"parth");

    bank[105].account=105;
    bank[105].type='S';
    strcpy(bank[105].name,"prathamesh");



    printf("-----------------------------\n");
    printf("Welcome to Bank\n");
    printf("-----------------------------\n");
    int j;
    printf("Enter costomer account number: \n");
    scanf("%d",&j);

   printf("\n Account No. : %d\n Account Type : %c \n Costomer Name : %s",bank[j].account,bank[j].type,bank[j].name);




    // printf("%d %c %s",bank[100].account,bank[100].type,bank[100].name);
    return 0;

}
