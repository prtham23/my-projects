#include<stdio.h>

int palindrome(char,int);

int main()
{
    char str1[100];
    int i;
    printf("enter the string:\n");
    scanf("%s",&str1);
   int n=sizeof(str1)/sizeof(str1[0]);
    // palindrome(str1,n);
    int flag;
    for(i=0;i<n;i++)
    {
        printf("%s\n",str1[i]);
        if(str1[i]!=str1[n-i-1])
        {
            
            flag=1;
            

        }
        else
        {
           flag=0;
        }
    }
    
    printf("%d",flag);
    
    if(flag)
    {
        printf("not palindrome");

    }
    else
    {
        printf("palindrome");
    }
    return 0;

}

// int palindrome(char str,int n)
// {int *i,*j;
//    for(i=0;i<n;i++)
//       i=j;

//     { if(str[j]==str[n])
    
    

//     }
// }